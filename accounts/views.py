from django.shortcuts import render
from .models import User

def users_list(request):
    users = User.objects.all()
    return render(request, 'accounts/users.html', {'users': users})
