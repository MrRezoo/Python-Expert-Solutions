# Generated by Django 3.2.4 on 2021-06-09 10:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=14, validators=[
                    django.core.validators.RegexValidator(code='invalid_phone_number',
                                                          message='Phone number format is not valid',
                                                          regex='^(0|\\+98|0098)9[0-9]{9}$')])),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
    ]
