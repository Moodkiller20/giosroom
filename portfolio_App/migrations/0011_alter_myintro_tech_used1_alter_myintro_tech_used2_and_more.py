# Generated by Django 4.1.6 on 2023-02-12 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_App', '0010_myintro_tech_used6'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myintro',
            name='tech_used1',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='myintro',
            name='tech_used2',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='myintro',
            name='tech_used3',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='myintro',
            name='tech_used4',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='myintro',
            name='tech_used5',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='myintro',
            name='tech_used6',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
