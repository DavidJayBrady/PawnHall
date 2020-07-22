from django.shortcuts import render
from django.views.generic.edit import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserProfileForm

# Create your views here.

class Register(View):

    def get(self, request):
        context = {"profile_form": UserProfileForm()}
        return render(request, "registration/register.html", context=context)

    def post(self, request):
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            user = profile_form.save() # Creates a user

            login(request, user)
            return redirect(reverse("list-all-pawns"))
        else:
            context = {"profile_form": profile_form}
            return render(request, "registration/register.html", context=context)


class UpdateProfile(LoginRequiredMixin, View):

    def get(self, request):
        context = {"profile_form": UserProfileForm() }
        return render(request, "registration/update_profile.html", context=context)

    def post(self, request):
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect(reverse("list-all-pawns"))
        else:
            context = {"profile_form": profile_form}
            return render(request, "registration/update_profile.html", context=context)