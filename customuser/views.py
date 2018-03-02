from django.shortcuts import render, redirect

from .forms import RegistrationForm

def registration_user(request):
    form = UserForm(prefix='usr')
    form_customuser = CustomForm(prefix='custom_usr')

    if request.user.is_authenticated():
        return redirect('')
    else:
        if request.method == "POST":
            form = UserForm(request.POST, prefix="usr")
            form_customuser = RegistrationForm(request.POST, prefix="custom_usr")

            #Not sure why here should be an "all([~.is_valid(), ~.is_valid()])"
            if form_user.is_valid() and form_customuser.is_valid():
                user = form.save(commit=False)
                user.customuser = form_customuser.save()
                user.save()
                return redirect('')
        else:
            form = UserForm(prefix='usr')
            form_customuser = RegistrationForm(prefix='custom_usr')

        context = {'form':form, 'form_customuser':form_customuser}
        return render(request, 'customuser/registration.html', context)
