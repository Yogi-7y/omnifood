# Generated by Django 2.2.4 on 2019-08-04 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20190803_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(upload_to='restaurant_logo/'),
        ),
    ]
