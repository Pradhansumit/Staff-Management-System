# Generated by Django 4.2.4 on 2023-08-24 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starttime',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stoptime',
            name='stop_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]