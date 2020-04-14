from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from firebase_admin import db
from ..firebase import init


class ViewStudentObligation(View):
    template_name = 'teacher/ObligationPage.html'
    
    def get(self, request):
        return render(request, self.template_name)


class JsonStudent(View):
    @staticmethod
    def get(request):
        data = db.reference("Account").child("Student").get()
        return JsonResponse(data)


class ViewObligationEdit(View):
    template_name='teacher/ObligationEdit.html'

    def get(self, request):
        id = request.GET["id"]
        data = db.reference("Account").child("Student/"+id+"/Result").get()
        subject = db.reference("Subject").get()
        return render(request, self.template_name, {'data': data, 'subject': subject})


class PostDeleteObligation(View):
    @staticmethod
    def post(request):
        keyI = request.POST['KeyI']
        keyII = request.POST['KeyII']
        db.reference("Account").child("Student/"+keyI+"/Result/"+keyII).delete()
        return HttpResponse("Ok")


class PostAddObligation(View):
    @staticmethod
    def post(request):
        keyI = request.POST['KeyI']
        subject = request.POST['Subject']
        grade = request.POST['Grade']
        data = {"Mapel": subject, "Hasil": "#", "Nilai": "#", "Kelas": grade}
        db.reference("Account").child("Student/"+keyI+"/Result").push(data)
        return HttpResponse("Ok")