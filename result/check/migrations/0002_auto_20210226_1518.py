# Generated by Django 3.1.7 on 2021-02-26 14:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='exam',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(70, message='must not be more than 70')]),
        ),
        migrations.AlterField(
            model_name='score',
            name='first_test',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(15, message='must not be more than 15')]),
        ),
        migrations.AlterField(
            model_name='score',
            name='second_test',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(15, message='must not be more than 15')]),
        ),
        migrations.AlterField(
            model_name='score',
            name='subject',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Economics', 'Economics'), ('Government', 'Government'), ('French', 'French'), ('Animal Husbandry', 'Animal Husbandry'), ('Financial Accounting', 'Financial Accounting'), ('CRS', 'CRS'), ('Agricultural Science', 'Agricultural Science'), ('RNV', 'RNV'), ('IGBO', 'IGBO'), ('Civic', 'Civic'), ('Marketing', 'Marketing'), ('Lit in English', 'Lit in English'), ('Basic Science', 'Basic Science'), ('Basic Technology', 'Basic Technology'), ('ICT', 'ICT'), ('Home Economics', 'Home Economics'), ('PHE', 'PHE'), ('History', 'History'), ('Creative Arts', 'Creative Arts'), ('Business Studies', 'Business Studies')], default='English', max_length=50, null=True),
        ),
    ]
