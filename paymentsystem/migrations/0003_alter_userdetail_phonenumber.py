# Generated by Django 4.1.5 on 2023-02-17 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentsystem', '0002_remove_userdetail_dayofbirth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='phonenumber',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]