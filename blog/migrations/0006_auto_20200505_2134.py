# Generated by Django 3.0.4 on 2020-05-05 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200505_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
