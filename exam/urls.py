from django.conf.urls.static import static
from django.urls import path

from z import settings
from .views.accounts import *
from .views.home import *
from .views.questions import *
from .views.teacher import *
from .views.student import *


urlpatterns =[
    path('', ViewLandingPage.as_view(), name='home'),
    path('logout', LogoutUser.as_view(), name='logout'),
    path('admin-login', ViewAdminLogin.as_view(), name='admin-login'),
    path('post-admin-login', PostAdminLogin.as_view(), name='post-admin-login'),

    path('login', ViewLoginPage.as_view(), name='login'),
    path('register', ViewRegisterPage.as_view(), name='register'),
    path('student-register', InsertStudent.as_view(), name='student-register'),
    path('student-login', PostLoginStudent.as_view(), name='student-login'),

    path('teacher-login', ViewTeacherLogin.as_view(), name='teacher-login'),
    path('post-teacher-login', PostLoginTeacher.as_view(), name='post-teacher-login'),
    path('teacher-register', ViewTeacherReg.as_view(), name='teacher-register'),
    path('post-teacher-reg', PostTeacherReg.as_view(), name='post-teacher-reg'),

    path('subject', ViewInputSubject.as_view(), name='subject'),
    path('post-subject', InputNewSubject.as_view(), name='post-subject'),
    path('delete-subject', DeleteSubject.as_view(), name='delete-subject'),

    path('teacher', ViewTeacherHome.as_view(), name='teacher'),
    path('teacher-obligation', ViewStudentObligation.as_view(), name='teacher-obligation'),
    path('obligation-edit', ViewObligationEdit.as_view(), name='obligation-edit'),
    path('obligation-delete',PostDeleteObligation.as_view(), name='obligation-delete'),
    path('obligation-add', PostAddObligation.as_view(), name='obligation-add'),
    path('student', ViewStudentHome.as_view(), name='student'),
    path('json-student', JsonStudent.as_view(), name='json-student'),
    path('post-task-student', PostUpdateTast.as_view(), name='post-task-student'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)