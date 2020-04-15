from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View


class ViewHomePage(View):
    template_name = 'Home.html'

    def get(self, request):
        return render(request, self.template_name)


class LogoutAccount(View):
    @staticmethod
    def get(request):
        logout(request)
        return redirect('home')
