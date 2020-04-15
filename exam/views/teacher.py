import string
import random

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from firebase_admin import db


class ViewTeacherHome(View):
    template_name = 'teachers/TeacherHome.html'

    def get(self, request):
        return render(request, self.template_name)


class ViewStudentRegister(View):
    template_name = 'teachers/StudentRegister.html'

    def get(self, request):
        return render(request, self.template_name)


class PostStudentRegister(View):

    @staticmethod
    def post(request):
        nis = request.POST['nis']
        fullname = request.POST['fullname']
        username = randomString(10)
        password = randomString(10)
        key_task = randomString(10)
        data = {"Name": fullname, "Username": username, "Password": password, "Task": {
            key_task: {
                "Subject": "#",
                "Result": "#",
                "Question": "#",
                "Answer": "#"
            }
        }}
        ref = db.reference("Account").child("Student/"+nis)
        ref.set(data)
        messages.add_message(request, messages.INFO, 'Request complete')
        return redirect('teacher:student-register')


class ViewStudentList(View):
    template_name = 'teachers/StudentTask.html'

    def get(self, request):
        data = db.reference("Subject").get()
        return render(request, self.template_name, {'subjects': data})


class PostStudentDelete(View):
    def post(self, request):
        nis = request.POST['nis']
        db.reference("Account").child("Student/"+nis).delete()
        return HttpResponse("Ok")


class ViewSubject(View):
    template_name = 'teachers/Subject.html'

    def get(self, request):
        data = db.reference("Subject").get()
        return render(request, self.template_name, {'subjects': data})


class PostSubject(View):
    @staticmethod
    def post(request):
        subject = request.POST['subject']
        teacher = request.POST['teacher']
        question = request.FILES['question']
        fs = FileSystemStorage()
        filename = fs.save(question.name, question)
        url = fs.url(filename)
        data = {"Subject": subject, "Teacher": teacher, "URL": url}
        db.reference("Subject").push(data)
        return redirect('teacher:subject-register')


class PostDeleteSubject(View):
    @staticmethod
    def post(request):
        key = request.POST['Key']
        db.reference("Subject").child(key).delete()
        return HttpResponse("Ok")


class PostUpdateTask(View):
    @staticmethod
    def post(request):
        nis = request.POST['nis']
        question = request.POST['question']
        subject = request.POST['subject']
        ref = db.reference("Account").child("Student/"+nis+"/Task")
        data = {'Subject': subject, 'Question': question, 'Answer': '#', 'Result': '#'}
        ref.push(data)
        return HttpResponse("Ok")


class PostDeleteTask(View):
    @staticmethod
    def post(request):
        nis = request.POST['nis']
        keytask = request.POST['keytask']
        print(keytask)
        db.reference("Account").child("Student/"+nis+"/Task/"+keytask).delete()
        return HttpResponse("Ok")


class LoadJsonStudent(View):
    @staticmethod
    def get(request):
        data = db.reference("Account").child("Student").get()
        return JsonResponse(data)


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
