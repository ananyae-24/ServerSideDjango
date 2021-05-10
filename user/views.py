from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from user.form import UserRegisterForm, UserUpdateform, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if(request.method == "GET"):
        form = UserRegisterForm()
    elif request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            return redirect("blog-home")
    return render(request, "user/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateform(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f"Your profile is updated")
            redirect("profile")
    else:

        u_form = UserUpdateform(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, "user/profile.html", {"u_form": u_form, "p_form": p_form})
