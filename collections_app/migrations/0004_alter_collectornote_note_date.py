# Generated by Django 5.1.4 on 2025-01-14 02:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0003_collectornote_note_date_collectornote_note_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectornote',
            name='note_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
