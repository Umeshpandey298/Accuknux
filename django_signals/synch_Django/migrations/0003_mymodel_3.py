# Generated by Django 5.0.3 on 2024-09-11 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synch_Django', '0002_mymodel_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
