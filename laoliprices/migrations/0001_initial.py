# Generated by Django 2.2.4 on 2019-08-25 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPrices',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_title', models.CharField(max_length=200)),
                ('product_spec', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('unit', models.CharField(blank=True, max_length=20, null=True)),
                ('unit_price', models.IntegerField(default=0)),
                ('total_price', models.IntegerField(blank=True, default=0, null=True)),
                ('remarks', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
