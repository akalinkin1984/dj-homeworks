# Generated by Django 5.0.6 on 2024-07-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_measurement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='image',
            field=models.ImageField(null=True, upload_to='measurement/image/1.jpg'),
        ),
    ]
