# Generated by Django 2.1.11 on 2019-08-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.CharField(max_length=100)),
                ('econtact', models.CharField(max_length=15)),
                ('unique_id', models.IntegerField(max_length=10)),
            ],
        ),
    ]
