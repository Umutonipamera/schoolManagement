# Generated by Django 3.2.6 on 2021-09-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='images/')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('3', 'Prefer not to say')], max_length=8)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('nationality', models.CharField(choices=[('1', 'Rwandan'), ('2', 'Kenyan'), ('3', 'Ugandan'), ('4', 'SouthSudanes'), ('5', 'Sudanes')], max_length=15)),
                ('national_Id', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254, null=True)),
                ('joining_date', models.DateField(null=True)),
                ('resume', models.FileField(null=True, upload_to='documents/')),
                ('contract', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('course_name', models.CharField(max_length=25)),
                ('salary', models.PositiveBigIntegerField(blank=True, null=True)),
                ('job_title', models.CharField(max_length=25)),
                ('company', models.CharField(max_length=30)),
            ],
        ),
    ]
