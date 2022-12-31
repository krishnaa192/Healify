# Generated by Django 3.2.12 on 2022-12-29 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Health', '0002_auto_20221229_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='have_query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=30)),
                ('phone_no', models.CharField(max_length=10)),
                ('short_desc', models.TextField()),
                ('related_dept', models.CharField(default='All_dept', max_length=66)),
            ],
        ),
    ]