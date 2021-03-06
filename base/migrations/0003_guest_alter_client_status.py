# Generated by Django 4.0 on 2022-01-01 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_clients_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('topic', models.TextField()),
                ('show_date', models.DateField()),
                ('source', models.CharField(max_length=200)),
                ('comments', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('active', 'ACTIVE'), ('quoted', 'QUOTED'), ('prospect', 'PROSPECT')], default='prospect', max_length=10),
        ),
    ]
