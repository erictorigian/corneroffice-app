# Generated by Django 4.0 on 2022-01-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_teacher_guest_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='sponsor',
            field=models.IntegerField(default=1, verbose_name='Teacher Sponsor'),
            preserve_default=False,
        ),
    ]
