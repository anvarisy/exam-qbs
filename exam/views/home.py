from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from firebase_admin import db
from ..firebase import init


class ViewLandingPage(View):
    template_name = 'home/HomePage.html'

    def get(self, request):
        return render(request, self.template_name, {'auth': request.user.is_authenticated})


class ViewTeacherHome(PermissionRequiredMixin, View):
    template_name = 'home/HomeTeacher.html'
    login_url = 'teacher-login'
    permission_required = 'exam.teacher_access'

    def get(self, request):
        return render(request, self.template_name)


class ViewStudentHome(PermissionRequiredMixin, View):
    template_name = 'home/StudentHome.html'
    login_url = 'login'
    permission_required = 'exam.student_access'

    def get(self, request):
        data = db.reference("Subject").get()
        key = request.session["key-student"]
        task = db.reference("Account").child("Student/"+key+"/Result").get()
        return render(request, self.template_name, {'data': data, 'task': task})
