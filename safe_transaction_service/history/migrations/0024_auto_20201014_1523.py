# Generated by Django 3.0.10 on 2020-10-14 15:23

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0023_auto_20200924_0841"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="ethereumevent",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["arguments"], name="history_eth_argumen_ba76e0_gin"
            ),
        ),
    ]
