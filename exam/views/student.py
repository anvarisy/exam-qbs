from django.shortcuts import render
from django.views import View
from firebase_admin import db


class ViewStudentHome(View):
    template_name = 'students/Student.html'

    def get(self, request):
        nis = request.sessions['nis']
        data = db.reference("Account").child("Student/"+nis).get()
        return render(request, self.template_name, {'student': data})