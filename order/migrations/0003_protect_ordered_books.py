from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [("order", "0002_remove_payment_credentials")]
    operations = [
        migrations.AlterField(model_name="orderitem", name="book", field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="store.book")),
    ]
