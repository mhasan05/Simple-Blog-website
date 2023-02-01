from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
class DashboardView(View):
    def get(self, request):
        user = User.objects.all()
        data = {
            'user': user
        }
        return render(request, 'dashboard/dashboard.html',data)
