from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from firebase_admin import db

from ..firebase import init


class ViewInputSubject(View):
    template_name = 'questions/SubjectPage.html'

    def get(self, request):
        data = db.reference('Subject').get()
        return render(request, self.template_name, {'data': data})


class InputNewSubject(View):
    @staticmethod
    def post(request):
        subject = request.POST["subject"]
        grade = request.POST["grade"]
        teacher = request.POST["teacher"]
        question = request.FILES["question"]

        fs = FileSystemStorage()
        filename = fs.save(question.name, question)
        url = fs.url(filename)
        data = {"Subject": subject, "Grade": grade, "Teacher": teacher, "Question": url}
        db.reference("Subject").push(data)
        return redirect('subject')


class DeleteSubject(View):
    @staticmethod
    def post(request):
        key = request.POST["Key"]
        db.reference("Subject").child(key).delete()
        return HttpResponse('OK')

