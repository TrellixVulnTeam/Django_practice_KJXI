# Generated by Django 2.1 on 2018-08-17 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ostacor', '0006_homepage_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage_about',
            name='about_icons',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
