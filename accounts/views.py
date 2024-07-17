from django.http import HttpResponse
from django.shortcuts import redirect, render

from accounts.forms import UserForm
from accounts.models import User

def registerUser(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            # password=form.cleaned_data['password']
            # user=form.save(commit=False)
            # user.set_password(password)
            # user.role=User.CUSTOMER
            # user.save()

            # create a user user_create method
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role=User.CUSTOMER
            user.save()
            return redirect('registerUser')
        else:
            print('invalid from error')
            print(form.errors)
    else:
        form=UserForm()
    context={
        'form':form,
    }
    return render(request, 'accounts/registerUser.html', context)
