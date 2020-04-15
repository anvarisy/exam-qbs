from django.conf.urls.static import static
from django.urls import path, include

from x import settings
from .views.home import *
from .views.teacher import *
from .views.student import *

urlpatterns = [
    path('', ViewHomePage.as_view(), name='home'),


    path('teacher/', include(([
        path('', ViewTeacherHome.as_view(), name='teacher'),
        path('student-register', ViewStudentRegister.as_view(), name='student-register'),
        path('post-student-register', PostStudentRegister.as_view(), name='post-student-register'),
        path('student-list', ViewStudentList.as_view(), name='student-list'),
        path('load-json-student', LoadJsonStudent.as_view(), name='load-json-student'),
        path('post-delete-student', PostStudentDelete.as_view(), name='post-delete-student'),
        path('subject-register', ViewSubject.as_view(), name='subject-register'),
        path('post-subject-register', PostSubject.as_view(), name='post-subject-register'),
        path('post-subject-delete', PostDeleteSubject.as_view(), name='post-subject-delete'),
        path('post-task-update', PostUpdateTask.as_view(), name='post-task-update'),
        path('post-task-delete', PostDeleteTask.as_view(), name='post-task-delete')

    ], 'exam'), namespace='teacher')),

    path('student/', include(([
        path('', ViewStudentHome.as_view(), name='student'),
    ], 'exam'), namespace='student')),

    path('account/', include(([
        path('logout', LogoutAccount.as_view(), name='logout'),
        path('student-login', ViewLoginPage.as_view(), name='student-login'),
        path('post-student-login', PostLoginStudent.as_view(), name='post-student-login')
    ], 'exam'), namespace='account'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
