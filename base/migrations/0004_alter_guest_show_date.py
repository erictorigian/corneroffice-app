# Generated by Django 4.0 on 2022-01-01 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_guest_alter_client_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='show_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
