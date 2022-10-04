import traceback

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from webapp.users.models import Profile, ExtendedProfile, States


def userlogin(request):
    """
    Function for handling login requests
    :param request: HTTP Request
    :return: Redirects to the profile page
    """
    if request.method == "POST":
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.get(username=email)
            if user.check_password(password):
                login(request, user)
                return redirect('webapp:users:profile')
            else:
                print("User Not Authenticated")
        except Exception as e:
            print(e)
            return render(request, 'users/login.html', {})
    else:
        return render(request, 'users/login.html', {})


def userregister(request):
    """
    Fucntion for handling Registration requests
    :param request: HTTP Request
    :return:  Redirects to the profile page
    """
    if request.method == "POST":
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_type = request.POST.get('user_type')
            user, created = User.objects.get_or_create(username=email, password=make_password(password))
            if created:
                Profile.objects.get_or_create(user=user, user_type=int(user_type))
                login(request, user)
                return redirect("webapp:users:profile")
        except Exception as e:
            return render(request, 'users/register.html', {})
    else:
        return render(request, 'users/register.html', {})


@login_required
def userdashboard(request):
    """
    Function use to render dashboard
    :param request: HTTP Request
    :return: Renders an HTML Template for Dashbaord
    """
    try:
        extended_profile = ExtendedProfile.objects.all()
        return render(request, 'users/dashboard.html', {'extended_profile':extended_profile})
    except Exception as e:
        print(e)
        traceback.print_exc()


@login_required
def extendedprofile(request):
    """
    Fucntion use to handle the User Additional information form
    :param request: HTTP Request
    :return: Renders the additional form details or redirects to the dashboard
    """
    try:
        profile = Profile.objects.get(user=request.user)
        if request.method == 'POST':
            user = request.user
            startup_name = request.POST.get("startup_name")
            tagline = request.POST.get("Tagline")
            mobile = request.POST.get("mobile")
            category = request.POST.get("category")
            segment = request.POST.get("segment")
            business_model = request.POST.get('bmodel')
            cin_number = request.POST.get('cin')
            registration_state = request.POST.get('registration_state')
            founder_name = request.POST.get('founder_name')
            founder_email = request.POST.get('founder_email')
            lastyear_revenue = request.POST.get('lastyear_revenue')
            funded_bootstrapped = request.POST.get('funded_bootstrapped')
            tech_brief = request.POST.get('tech_brief')
            rewards_recognition = request.POST.get('rewards_recognition')
            company_website = request.POST.get('company_website')
            extended_profile = ExtendedProfile.objects.create(user=user,startup_name=startup_name,tagline=tagline,
                                                              mobile=mobile,category=category,segment=segment,
                                                              business_model=business_model,cin_number=cin_number,
                                                              registration_state=States.objects.first(),founder_email=founder_email,
                                                              founder_name=founder_name,lastyear_revenue=lastyear_revenue,
                                                              funded_bootstrapped=True,tech_brief=tech_brief,
                                                              rewards_recognition=rewards_recognition,company_website="https://hgsystems.in")
            profile.extended_profile = extended_profile
            profile.save()
            return redirect('webapp:users:dashboard')
        else:
            if profile.extended_profile:
                return redirect('webapp:users:dashboard')
            else:
                return render(request, 'users/extendedprofile.html', {})
    except Exception as e:
        print(e)
        traceback.print_exc()


def logout_user(request):
    """
    Fucntion used to logout user
    :param request: HTTP Request
    :return: Redirects to the login page
    """
    logout(request)
    return redirect('webapp:users:login')
