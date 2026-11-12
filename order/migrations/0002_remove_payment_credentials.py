from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [("order", "0001_initial")]
    operations = [
        migrations.RemoveField(model_name="order", name="account_no"),
        migrations.RemoveField(model_name="order", name="transaction_id"),
        migrations.AlterField(model_name="order", name="payable", field=models.DecimalField(decimal_places=2, max_digits=10)),
        migrations.AlterField(model_name="order", name="payment_method", field=models.CharField(default="Cash on delivery", max_length=30)),
        migrations.AlterField(model_name="orderitem", name="order", field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="items", to="order.order")),
    ]
