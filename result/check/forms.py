from django.forms import ModelForm
from .models import Student, Score
from django.utils.translation import gettext_lazy as _


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["name", "level",]

        help_texts = {
            "name": _("enter student's full name"),
            "level": _("select student's class")
        }

