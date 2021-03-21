from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
from .choices import SUBJECTS, CLASS
from django.contrib.auth.models import User



class Student(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=50, choices=CLASS, default=CLASS[0][0])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk":self.pk})


class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, choices=SUBJECTS, default=SUBJECTS[0][0], blank=True, null=True)
    first_test = models.PositiveIntegerField(validators=[MaxValueValidator(15, message="must not be more than 15")], blank=True, null=True)
    second_test = models.PositiveIntegerField(validators=[MaxValueValidator(15, message="must not be more than 15")], blank=True, null=True)
    exam = models.PositiveIntegerField(validators=[MaxValueValidator(70, message="must not be more than 70")], blank=True, null=True)

    def __str__(self):
        return self.student.name

    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk":self.pk})

    @property
    def total(self):
        return self.first_test + self.second_test + self.exam

    @property
    def grade(self):
        if self.total in range(80, 101):
            return "A"
        elif self.total in range(60, 80):
            return "B"
        elif self.total in range(50, 60):
            return "C"
        elif self.total in range(40, 50):
            return "D"
        elif self.total in range(30, 40):
            return "E"
        elif self.total < 30:
            return "F"
        else:
            return 0


