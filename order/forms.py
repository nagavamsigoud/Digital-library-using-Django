from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    DIVISION_CHOICES = (("Kabankalan City", "Kabankalan City"), ("Bacolod City", "Bacolod City"),
        ("Himamaylan City", "Himamaylan City"), ("Binalbagan", "Binalbagan"), ("Hinigaran", "Hinigaran"))
    DISTRICT_CHOICES = tuple((f"Brgy.{n}", f"Brgy.{n}") for n in range(1, 6))
    division = forms.ChoiceField(choices=DIVISION_CHOICES)
    district = forms.ChoiceField(choices=DISTRICT_CHOICES)
    payment_method = forms.ChoiceField(choices=(("Cash on delivery", "Cash on delivery"),), initial="Cash on delivery")
    class Meta:
        model = Order
        fields = ["name", "email", "phone", "address", "division", "district", "zip_code", "payment_method"]
