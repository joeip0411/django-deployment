from django.shortcuts import render

from registration_app.forms import NewUserForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            form = NewUserForm()
            messages.success(request, 'Registration successful !')
        else:
            print('Error form Invalid')
    return render(request,'registration_app/users.html', {'form':form})
