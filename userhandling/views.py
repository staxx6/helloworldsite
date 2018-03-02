from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction

from .models import User

from .forms import UserForm, ProfileForm

def update_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.profile.bio = "Test update"
    return redirect('')

def show_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {'user':user}
    return render(request, 'userhandling/show_user.html', context)

@transaction.atomic
def user_registration(request):
    #form = UserForm(prefix='user')
    #form_profile = ProfileForm(prefix='profile')

    #if request.user.is_authenticated():
    #    return redirect('')
    #else:
    if request.method == "POST":
        form = UserForm(request.POST)
        form_profile = ProfileForm(request.POST)

        #Not sure why here should be an "all([~.is_valid(), ~.is_valid()])"
        if form.is_valid() and form_profile.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)

            user.profile = form_profile.save(commit=False)
            user.profile.id_user = user.id
            #user.profile.bio = str(form_profile.avatar)

            user.save()
            user.profile.save()
            return redirect('/')
    else:
        form = UserForm()
        form_profile = ProfileForm( )

    context = {'form':form, 'form_profile':form_profile}
    return render(request, 'userhandling/registration.html', context)
