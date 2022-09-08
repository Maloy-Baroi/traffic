# Generated by Django 4.0.4 on 2022-08-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PenaltyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_section', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('penalty_imposed_on_1st_time', models.CharField(max_length=50)),
                ('penalty_imposed_on_2nd_time', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
