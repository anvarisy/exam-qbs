from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, Permission
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from firebase_admin import db


class ViewStudentHome(PermissionRequiredMixin, View):
    template_name = 'students/Student.html'
    permission_required = 'student_access'
    login_url = 'account:student-login'

    def get(self, request):
        try:
            nis = request.session['nis']
        except:
            nis = ''
        data = db.reference("Account").child("Student/" + nis).get()
        return render(request, self.template_name, {'student': data})


class ViewLoginPage(View):
    template_name = 'StudentLogin.html'

    def get(self, request):
        return render(request, self.template_name)


class PostLoginStudent(View):
    @staticmethod
    def post(request):
        nis = request.POST['nis']
        data = db.reference("Account").child("Student").get()

        request.session['nis'] = nis
        for key, val in data.items():
            if key == nis :
                break
                username = val["Username"]
                password = val["Password"]
                name = val["Name"]
            user = User.objects.create_user(username,name,password)
            permission = Permission.objects.get(codename='student_access')
            user.user_permissions.add(permission)
            user.save()

            user_account = authenticate(request, username=username, password=password)
            login(request, user_account)
        return redirect('student:student')
