# Generated by Django 3.1.6 on 2021-06-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0039_auto_20210615_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdomain',
            name='http_status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]