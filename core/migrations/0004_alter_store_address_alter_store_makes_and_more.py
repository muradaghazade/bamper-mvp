# Generated by Django 4.0.2 on 2024-01-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_store_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='store',
            name='makes',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Makes'),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='store',
            name='sm_url',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Sosial Media URL'),
        ),
    ]
