# Generated by Django 5.0 on 2024-01-04 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fraud_detection_app', '0004_alter_transaction_namedest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='isFraud',
            field=models.BooleanField(),
        ),
    ]
