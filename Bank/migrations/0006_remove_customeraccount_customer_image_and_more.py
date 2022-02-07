# Generated by Django 4.0.1 on 2022-02-06 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0005_alter_customeraccount_customer_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeraccount',
            name='customer_image',
        ),
        migrations.AddField(
            model_name='customeraccount',
            name='image',
            field=models.ImageField(default='', upload_to='Bank/images'),
        ),
    ]