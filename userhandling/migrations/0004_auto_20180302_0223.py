# Generated by Django 2.0.2 on 2018-03-02 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userhandling', '0003_auto_20180302_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='sup', max_length=500),
            preserve_default=False,
        ),
    ]
