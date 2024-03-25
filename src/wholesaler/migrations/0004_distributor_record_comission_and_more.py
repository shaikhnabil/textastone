# Generated by Django 5.0.2 on 2024-03-20 17:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wholesaler', '0003_alter_saree_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributor_record',
            name='comission',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(500)]),
        ),
        migrations.AlterField(
            model_name='saree',
            name='sample_image',
            field=models.ImageField(blank=True, upload_to='saree_images/'),
        ),
    ]