# Generated by Django 5.0.6 on 2024-07-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_alter_bencana_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bencana",
            name="date",
            field=models.CharField(max_length=100),
        ),
    ]