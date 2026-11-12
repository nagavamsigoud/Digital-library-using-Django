from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review

class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["name", "email", "username", "password1", "password2"]
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ReviewForm(forms.ModelForm):
    review_star = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), initial=1)
    review_text = forms.CharField(widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Write your review"}), max_length=2000)
    class Meta:
        model = Review
        fields = ["review_star", "review_text"]
