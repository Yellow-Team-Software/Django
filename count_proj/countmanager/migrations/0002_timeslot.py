# Generated by Django 3.0.3 on 2020-02-20 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.IntegerField(default=0)),
                ('duration', models.IntegerField(default=0)),
            ],
        ),
    ]