# Generated by Django 2.1 on 2018-08-27 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ostacor', '0009_auto_20180827_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='homepage_food_locus_story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_title', models.CharField(blank=True, max_length=75, null=True)),
                ('cover_img_src', models.CharField(max_length=100)),
                ('one_liner', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='homepage_latest_story',
            name='one_liner_recipie_name',
            field=models.CharField(max_length=75),
        ),
    ]
