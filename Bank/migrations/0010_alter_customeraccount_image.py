# Generated by Django 4.0.2 on 2022-02-08 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0009_alter_customeraccount_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraccount',
            name='image',
            field=models.ImageField(default='Image003.png', upload_to='media/'),
        ),
    ]