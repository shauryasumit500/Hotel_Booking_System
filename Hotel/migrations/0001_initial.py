# Generated by Django 3.1.5 on 2021-01-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hotel_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('room_no', models.IntegerField()),
            ],
        ),
    ]
