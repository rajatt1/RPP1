# Generated by Django 4.2.1 on 2023-06-08 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='referenceM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('volume', models.CharField(max_length=255)),
                ('Doi', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('page', models.CharField(max_length=255)),
            ],
        ),
    ]
