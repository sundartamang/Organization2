# Generated by Django 2.2.4 on 2020-11-05 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmessage',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
