# Generated by Django 3.2.2 on 2021-05-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210511_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.CharField(choices=[('BR', 'Breakfast'), ('LU', 'Lunch'), ('DI', ' Dinner'), ('SN', 'Snack'), ('DR', 'Drink'), ('CM', 'Cheat Meal')], max_length=2),
        ),
    ]
