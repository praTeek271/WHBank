# Generated by Django 4.0.1 on 2022-02-06 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraccount',
            name='customer_image',
            field=models.ImageField(default='', upload_to='customer_img'),
        ),
    ]
