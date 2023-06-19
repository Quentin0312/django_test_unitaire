# Generated by Django 4.2.2 on 2023-06-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testUnitaire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('price', models.FloatField()),
            ],
        ),
    ]
