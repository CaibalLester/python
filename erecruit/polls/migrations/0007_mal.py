# Generated by Django 4.2.7 on 2023-12-13 22:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=500)),
                ('age', models.PositiveSmallIntegerField(default='default_value', null=True)),
                ('birthdate', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
    ]
