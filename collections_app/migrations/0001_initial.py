# Generated by Django 5.1.4 on 2025-01-13 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollectorNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'collector_notes',
            },
        ),
        migrations.CreateModel(
            name='CustomerTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.IntegerField()),
                ('transaction_date', models.DateField()),
                ('monthly_amount_due', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
