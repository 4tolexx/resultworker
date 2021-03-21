from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from .models import Student, Score
from .forms import StudentForm
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F, Sum, Avg



class HomePageView(TemplateView):
    template_name = 'check/home.html'


@login_required
def add_student(request):
    student = Student()
    student_form  = StudentForm(instance=student)
    StudentFormset = inlineformset_factory(
                                            Student,
                                            Score, 
                                            fields=("subject", "first_test", "second_test", "exam"),
                                            max_num=3,
                                            extra=3,
                                            can_delete=True,
                                            help_texts={
                                                        "first_test":"test scores should not be more than 15", 
                                                        "second_test":"test scores should not be more than 15",
                                                        "exam":"exam score should not be more than 70"
                                                        }
                                            )

    if request.method == "POST":
        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            created_student = student_form.save(commit=False)
            created_student.author = request.user
            formset = StudentFormset(request.POST, instance=created_student)

            if formset.is_valid():
                created_student.save()
                formset.save()

                messages.success(request, "Student details successfully added")
                return HttpResponseRedirect(created_student.get_absolute_url())
    else:
        student_form = StudentForm(instance=student)
        formset = StudentFormset()

    return render(request, "check/student_creation_form.html", {"formset":formset, "student_form":student_form})



@login_required
def edit_student(request, id):
    student = Student.objects.get(pk=id)
    StudentFormset = inlineformset_factory(
                                            Student,
                                            Score, 
                                            fields=("subject", "first_test", "second_test", "exam"),
                                            max_num=3,
                                            extra=3,
                                            can_delete=True
                                         )

    if request.method == "POST":
        student_form = StudentForm(request.POST, instance=student)

        if student_form.is_valid():
            student_edit = student_form.save(commit=False)
            student_edit.author = request.user
            formset = StudentFormset(request.POST, instance=student)

            if formset.is_valid():
                student_edit.save()
                formset.save()

                return HttpResponseRedirect(student_edit.get_absolute_url())

    else:
        student_form = StudentForm(instance=student)
        formset = StudentFormset(instance=student)

    return render(request, "check/student_creation_form.html", {"student_form":student_form, "formset":formset})


class StudentDetailView(DetailView):
    model = Student
    template_name = "check/student_detail.html"
    context_object_name = "student"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["student_scores"] = Score.objects.filter(student__id=self.kwargs.get("pk"))
        context["total"] = Score.objects.filter(student__id=self.kwargs.get("pk")).annotate(sum_test=F("first_test") + F("second_test") + F("exam")).aggregate(total=Sum("sum_test"))
        context["average"] = Score.objects.filter(student__id=self.kwargs.get("pk")).annotate(sum_test=F("first_test") + F("second_test") + F("exam")).aggregate(average=Avg("sum_test"))
        return context



class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "check/student_list.html"
    context_object_name = "students"

    def get_queryset(self):
        return Student.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["student_scores"] = Score.objects.filter(student__id=self.kwargs.get("pk"))
        context["total"] = Score.objects.filter(student__id=self.kwargs.get("pk")).annotate(sum_test=F("first_test") + F("second_test") + F("exam")).aggregate(total=Sum("sum_test"))
        context["average"] = Score.objects.filter(student__id=self.kwargs.get("pk")).annotate(sum_test=F("first_test") + F("second_test") + F("exam")).aggregate(average=Avg("sum_test"))
        return context

