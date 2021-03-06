# Generated by Django 3.1.7 on 2021-02-26 10:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('level', models.CharField(choices=[('JSS1', 'JSS1'), ('JSS2', 'JSS2'), ('JSS3', 'JSS3'), ('SSS1', 'SSS1'), ('SSS2', 'SSS2'), ('SSS3', 'SSS3')], default='JSS1', max_length=50)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, choices=[('Aeronautics & Astronautics', 'Aeronautics & Astronautics'), ('Anesthesia', 'Anesthesia'), ('Anthropology', 'Anthropology'), ('Applied Physics', 'Applied Physics'), ('Art or Art History', 'Art & Art History'), ('Astrophysics', 'Astrophysics'), ('Biochemistry', 'Biochemistry'), ('Bioengineering', 'Bioengineering'), ('Biology', 'Biology'), ('Business', 'Business'), ('Cardiothoracic Surgery', 'Cardiothoracic Surgery'), ('Chemical and Systems Biology', 'Chemical and Systems Biology'), ('Chemical Engineering', 'Chemical Engineering'), ('Chemistry', 'Chemistry'), ('Civil and Environmental Engineering', 'Civil and Environmental Engineering'), ('Classics', 'Classics'), ('Communication', 'Communication'), ('Comparative Literature', 'Comparative Literature'), ('Comparative Medicine', 'Comparative Medicine'), ('Computer Science', 'Computer Science'), ('Dermatology', 'Dermatology'), ('Developmental Biology', 'Developmental Biology'), ('East Asian Languages and Cultures', 'East Asian Languages and Cultures'), ('Economics', 'Economics'), ('Education', 'Education'), ('Electrical Engineering', 'Electrical Engineering'), ('English', 'English'), ('French', 'French'), ('Genetics', 'Genetics'), ('General Eduction', 'General Education'), ('Geological and Environmental Sciences', 'Geological and Environmental Sciences'), ('Geophysics', 'Geophysics'), ('Health', 'Health'), ('History', 'History'), ('Latin American Cultures', 'Latin American Cultures'), ('Law School', 'Law School'), ('Linguistics', 'Linguistics'), ('Management', 'Management'), ('Materials Science', 'Materials Science'), ('Mathematics', 'Mathematics'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Medicine', 'Medicine'), ('Microbiology and Immunology', 'Microbiology and Immunology'), ('Molecular and Cellular Physiology', 'Molecular and Cellular Physiology'), ('Music', 'Music'), ('Neurobiology', 'Neurobiology'), ('Neurology', 'Neurology'), ('Neurosurgery', 'Neurosurgery'), ('Obstetrics and Gynecology', 'Obstetrics and Gynecology'), ('Ophthalmology', 'Ophthalmology'), ('Orthopaedic Surgery', 'Orthopaedic Surgery'), ('Other', 'Other'), ('Otolaryngology', 'Otolaryngology'), ('Pathology', 'Pathology'), ('Pediatrics', 'Pediatrics'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Political Science', 'Political Science'), ('Psychiatry', 'Psychiatry'), ('Psychology', 'Psychology'), ('Radiation Oncology', 'Radiation Oncology'), ('Radiology', 'Radiology'), ('Religious Studies', 'Religious Studies'), ('Slavic Languages and Literature', 'Slavic Languages and Literature'), ('Sociology', 'Sociology'), ('Statistics', 'Statistics'), ('Surgery', 'Surgery'), ('Theater and Performance Studies', 'Theater and Performance Studies'), ('Urology', 'Urology')], default='Aeronautics & Astronautics', max_length=50)),
                ('first_test', models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(15, message='must not be more than 15')])),
                ('second_test', models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(15, message='must not be more than 15')])),
                ('exam', models.PositiveIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(70, message='must not be more than 70')])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='check.student')),
            ],
        ),
    ]
