# Generated by Django 3.0.2 on 2020-01-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calvintbl',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
