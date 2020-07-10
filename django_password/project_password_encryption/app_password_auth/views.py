from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomUserForm, UserForm
# Create your views here.

def index(request):
    return render(request,'app_password_auth/index.html')


def register(request):
    registered = False
    if request.method == 'POST':
        fu = UserForm(data = request.POST)
        fcu = CustomUserForm(data = request.POST)


        if fu.is_valid() and fcu.is_valid():
            user = fu.save()
            user.set_password(user.password)
            user.save()

            profile = fcu.save(commit=False)

            """
            profile is an instance of fcu.
            fcu is an instance of CustomUserForm.
            CustomUserForm is configured to the model of EndUserProfileInfo.
            EndUserProfileInfo class has end_user = models.OneToOneField(User, on_delete = models.CASCADE)
            """
            profile.user = user

            if 'end_user_dp' in request.FILES:

                """
                request.FILES is USED FOR ALL UPLOADED FILES LIKE .CSV .TXT .JPEG .PNG etc.
                """
                profile.end_user_dp = request.FILES['end_user_dp']

            profile.save()
            registered = True
        else:
            print(fu.errors, fcu.errors)
    else:
        fu = UserForm()
        fcu = CustomUserForm()

    return render(request, 'app_password_auth/registration_page.html', {'user_form':fu, 'user_profile_form':fcu, 'registered':registered})
