import json

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, Permission
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from firebase_admin import db
from ..firebase import init


# Done
class ViewLoginPage(View):
    template_name = 'account/LoginPage.html'

    def get(self, request):
        return render(request, self.template_name)


# Done
class ViewRegisterPage(View):
    template_name = 'account/RegPage.html'

    def get(self, request):
        return render(request, self.template_name)


# Done
class InsertStudent(View):
    @staticmethod
    def post(request):
        name = request.POST['s-name']
        classes = request.POST['s-class']
        plp = request.POST['s-plp']
        uname = request.POST['s-uname']
        passes = request.POST['s-pass']
        data = {"Name": name, "Grade": classes, "PLP": plp, "Username": uname, "Pass": passes, "Result":{"l-1": {"Mapel": "QCB", "Hasil": "#", "Kelas": "#", "Nilai": "#"}}}
        db.reference("Account").child("Student").push(data)
        permission = Permission.objects.get(codename='student_access')
        user = User.objects.create_user(uname, "@student", passes)
        user.user_permissions.add(permission)
        user.save()
        return redirect('login')


# Done
class PostLoginStudent(View):
    @staticmethod
    def post(request):
        uname = request.POST['s-uname']
        passes = request.POST['s-pass']
        data = db.reference("Account").child("Student").get()
        for key, val in data.items():
            if val["Username"] == uname and val["Pass"] == passes:
                request.session["key-student"] = key
                user = authenticate(request, username=uname, password=passes)
        if user is not None:
            login(request, user)
            return redirect('student')
        else:
            return redirect('login')


# Done
class ViewTeacherLogin(View):
    template_name = 'account/TeacherLogin.html'

    def get(self, request):
        return render(request, self.template_name)


# Done
class PostLoginTeacher(View):
    @staticmethod
    def post(request):
        uname = request.POST['t-uname']
        passes = request.POST['t-pass']
        data = db.reference("Account").child("Teacher").get()
        for key, val in data.items():
            if val["Username"] == uname and val["Password"] == passes:
                request.session["key-teacher"] = key
                user = authenticate(request, username=uname, password=passes)
            if user is not None:
                login(request, user)
                return redirect('teacher')
            else:
                print("False")
                return redirect('teacher-login')


# Done
class ViewTeacherReg(PermissionRequiredMixin, View):
    template_name = 'account/TeacherReg.html'
    login_url = 'admin-login'
    permission_required = 'exam.admin_access'

    def get(self, request):
        return render(request, self.template_name)


# Done
class PostTeacherReg(View):
    @staticmethod
    def post(request):
        name = request.POST['t-name']
        divisi = request.POST['t-divisi']
        uname = request.POST['t-uname']
        passes = request.POST['t-pass']
        data = {"Name": name, "Division": divisi, "Username": uname, "Password": passes}
        db.reference("Account").child("Teacher").push(data)
        permission = Permission.objects.get(codename='teacher_access')
        user = User.objects.create_user(uname, "@teacher", passes)
        user.user_permissions.add(permission)
        user.save()
        return redirect('teacher-register')


# Done
class ViewAdminLogin(View):
    template_name = 'account/AdminLogin.html'

    def get(self, request):
        return render(request, self.template_name)


# Done
class PostAdminLogin(View):
    @staticmethod
    def post(request):
        uname = request.POST['a-uname']
        passes = request.POST['a-pass']
        data = db.reference("Account").child("Admin").get()
        permission_a = Permission.objects.get(codename='admin_access')
        permission_s = Permission.objects.get(codename='student_access')
        permission_t = Permission.objects.get(codename='teacher_access')
        admin_name = None
        for key, val in data.items():
            if val["Username"] == uname and val["Pass"] == passes:
                admin_name = key
                check_user = User.objects.get(username=uname)
                if check_user is not None:
                    print("already")
                else:
                    user = User.objects.create_user(uname, "@admin", passes)
                    user.user_permissions.add(permission_a, permission_s, permission_t)
                    user.save()

        if admin_name is not None:
            auth_user = authenticate([request], password=passes, username=uname)
            login(request, auth_user)
            return redirect('teacher-register')
        else:
            print("False")
            return redirect('teacher-login')


# Done
class LogoutUser(View):
    @staticmethod
    def get(request):
        logout(request)
        return redirect('home')
