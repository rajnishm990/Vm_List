# Generated by Django 4.2.8 on 2024-02-04 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_appliances_pdf_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="appliances",
            name="description",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
