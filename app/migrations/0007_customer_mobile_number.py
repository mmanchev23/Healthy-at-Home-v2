# Generated by Django 3.2.6 on 2021-08-05 20:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210805_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='mobile_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
