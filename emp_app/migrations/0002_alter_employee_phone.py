# Generated by Django 4.0.5 on 2022-08-24 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]
