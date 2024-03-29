# Generated by Django 4.0.2 on 2024-01-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_order_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Name')),
                ('email', models.CharField(blank=True, max_length=150, null=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=150, null=True, verbose_name='Phone')),
                ('message', models.CharField(blank=True, max_length=150, null=True, verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
