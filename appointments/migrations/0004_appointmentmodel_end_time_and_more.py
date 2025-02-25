# Generated by Django 5.1.6 on 2025-02-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_remove_appointmentmodel_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointmentmodel',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
