# Generated by Django 2.2.8 on 2020-05-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driverLicense', models.CharField(max_length=255)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('address1', models.CharField(max_length=50)),
                ('phoneNumber', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('dob', models.DateField()),
                ('checkin', models.DateField(default='2020-05-20')),
                ('checkout', models.DateField(default='2020-05-20')),
                ('adults', models.IntegerField(null=True)),
                ('children', models.IntegerField(null=True)),
                ('paymentAmount', models.IntegerField(null=True)),
                ('petFee', models.IntegerField(default=0)),
                ('roomNumber', models.IntegerField(null=True)),
            ],
        ),
    ]
