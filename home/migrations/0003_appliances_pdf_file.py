# Generated by Django 4.2.8 on 2024-02-04 13:20

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_remove_appliances_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="appliances",
            name="pdf_file",
            field=models.FileField(
                blank=True, null=True, upload_to=home.models.file_path
            ),
        ),
    ]
