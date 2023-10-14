# Generated by Django 4.2 on 2023-10-14 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('experince', models.IntegerField()),
                ('certificate', models.CharField(max_length=20)),
                ('salary', models.FloatField()),
                ('tranining', models.IntegerField()),
                ('male_or_female', models.BooleanField(choices=[('Male', 'Male'), ('Fmale', 'Fmale')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_job', models.CharField(max_length=20)),
                ('desriptionJob', models.CharField(max_length=200)),
                ('part_of_time', models.CharField(max_length=50)),
            ],
        ),
    ]
