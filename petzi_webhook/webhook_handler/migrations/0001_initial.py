# Generated by Django 4.2.7 on 2023-11-08 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('eventId', models.IntegerField()),
                ('event', models.CharField(max_length=100)),
                ('buyer_first_name', models.CharField(max_length=50)),
                ('buyer_last_name', models.CharField(max_length=50)),
                ('buyer_postcode', models.CharField(max_length=10)),
            ],
        ),
    ]