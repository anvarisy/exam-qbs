from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.views import View
from firebase_admin import db


class PostUpdateTast(PermissionRequiredMixin, View):
    permission_required = 'exam.student_access'
    login_url = 'login'

    @staticmethod
    def post(request):
        key = request.POST['key']
        answer = request.FILES['answer']
        key_student = request.session['key-student']
        fs = FileSystemStorage()
        filename = fs.save(answer.name, answer)
        url = fs.url(filename)
        link = db.reference("Account").child("Student/"+key_student+"/Result/"+key)
        link.update({'Hasil': url})
        return redirect('student')
