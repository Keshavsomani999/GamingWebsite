# Generated by Django 4.0.4 on 2022-09-05 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_orders_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='download_link',
            field=models.URLField(default=1, max_length=50000),
            preserve_default=False,
        ),
    ]
