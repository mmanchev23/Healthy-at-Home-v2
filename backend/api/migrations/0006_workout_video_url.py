# Generated by Django 3.2.3 on 2021-05-25 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210518_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='video_url',
            field=models.CharField(default='https://www.youtube.com/embed/oAPCPjnU1wA', max_length=200),
        ),
    ]
