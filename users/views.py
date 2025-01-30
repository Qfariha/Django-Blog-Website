from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def logout_view(request):
    logout(request)  # This will log out the user
    return redirect('login')  # Redirect the user to the login page


def register(request):
    if request.method=='POST':
        form= UserRegisterForm(request.POST) # when providing username and pass
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form= UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required #It is a decorator which adds funtionalities here it is working a condition to view profile
def profile(request):
    if request.method=='POST': #'POST' request=form submission
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')
    
    else: #If the request is not a form submission, the form fields are pre-filled with the user's existing data.
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
        
    context={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html',context)