# Generated by Django 5.0.4 on 2024-05-04 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0003_alter_userportfolio_liquidamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userportfolio',
            name='totalPortfolioAmount',
            field=models.FloatField(default=25000),
        ),
    ]
