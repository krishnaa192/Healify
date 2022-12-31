# Generated by Django 3.2.12 on 2022-12-29 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=40)),
                ('dept_code', models.CharField(max_length=40)),
                ('headofdept', models.CharField(max_length=50)),
                ('dept_desc', models.TextField()),
                ('dept_specialization', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=40)),
                ('package_code', models.CharField(max_length=40)),
                ('price', models.CharField(max_length=10)),
                ('package_desc', models.TextField()),
                ('duration', models.CharField(max_length=45)),
            ],
        ),
        migrations.AlterField(
            model_name='booking_appointments',
            name='Name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='booking_appointments',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking_appointments',
            name='description',
            field=models.TextField(default='Describe your problem'),
        ),
    ]