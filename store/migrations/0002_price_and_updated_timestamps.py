from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [("store", "0001_initial")]
    operations = [
        migrations.AlterField(model_name="book", name="price", field=models.DecimalField(decimal_places=2, max_digits=10)),
        migrations.AlterField(model_name="category", name="updated_at", field=models.DateTimeField(auto_now=True)),
        migrations.AlterField(model_name="writer", name="updated_at", field=models.DateTimeField(auto_now=True)),
    ]
