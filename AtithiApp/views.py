
from django.views.generic import TemplateView
from . forms import *
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def userLogin(request):
    next = request.GET.get('next')
    form = UserLogin(request.POST or None)

    if request.user.is_authenticated:
        return redirect('AtithiApp:dashboard')

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/AtithiApp/dashboard')

    context = {
        'form': form,
    }
    return render(request, "AtithiApp/login.html",context)


def logoutRequest(request):
    logout(request)
    return redirect("AtithiApp:login")


@method_decorator(login_required, name='dispatch')
class DashboardPage(TemplateView):
    template_name = "AtithiApp/dashboard.html"

    def get(self, request):
        currentUser = request.user

        args = {'currentUser':currentUser}
        return render(request,self.template_name,args)

    def post(self,request):
        currentUser = request.user
        print(request.POST)
        args = {'currentUser': currentUser}
        return render(request, self.template_name, args)


@login_required()
def checkIn(request):
    form = CheckInForm(request=request)
    if request.method == 'POST':
        form = CheckInForm(request.POST,request=request)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AtithiApp:dashboard')
        else:
            print(form.errors)
    context = {
        "form": form,
        "currentUser": request.user,
    }
    return render(request, "AtithiApp/checkin.html", context)


@method_decorator(login_required, name='dispatch')
class InHouse(TemplateView):
    template_name = "AtithiApp/inhouse.html"

    def get(self, request):
        guestList = Guest.objects.all()
        currentUser = request.user

        args = {
            'currentUser': currentUser,
            'guestList': guestList,
        }
        return render(request,self.template_name,args)


@method_decorator(login_required, name='dispatch')
class Admin(TemplateView):
    template_name = "AtithiApp/admin.html"

    def get(self, request):
        currentUser = request.user

        args = {'currentUser':currentUser}
        return render(request,self.template_name,args)

    def post(self,request):
        currentUser = request.user
        print(request.POST)
        args = {'currentUser': currentUser}
        return render(request, self.template_name, args)


@method_decorator(login_required, name='dispatch')
class Departure(TemplateView):
    template_name = "AtithiApp/departures.html"

    def get(self, request):
        currentUser = request.user

        args = {'currentUser':currentUser}
        return render(request,self.template_name,args)

    def post(self,request):
        currentUser = request.user
        print(request.POST)
        args = {'currentUser': currentUser}
        return render(request, self.template_name, args)


@method_decorator(login_required, name='dispatch')
class PastStay(TemplateView):
    template_name = "AtithiApp/paststay.html"

    def get(self, request):
        currentUser = request.user

        args = {'currentUser':currentUser}
        return render(request,self.template_name,args)


@method_decorator(login_required, name='dispatch')
class Search(TemplateView):
    template_name = "AtithiApp/search.html"

    def get(self, request):
        currentUser = request.user
        dl = request.GET['dl']

        guest = Guest.objects.filter(driverLicense__icontains=dl).first()

        args = {
            'currentUser':currentUser,
            'guest': guest,
        }
        return render(request,self.template_name,args)

    def post(self,request):
        currentUser = request.user
        print(request.POST)
        args = {'currentUser': currentUser}
        return render(request, self.template_name, args)


@method_decorator(login_required, name='dispatch')
class SelectDates(TemplateView):
    template_name = "AtithiApp/selectDates.html"

    def get(self, request):
        current_user = request.user
        dl = request.GET['dl']
        personal_form = CheckInForm(request=request)
        guest = Guest.objects.filter(driverLicense__icontains=dl).first()

        args = {
            'personalForm': personal_form,
            'currentUser': current_user,
            'guest': guest,
        }
        return render(request,self.template_name,args)

    def post(self, request):
        current_user = request.user
        print(request.POST)
        args = {'currentUser': current_user}
        return render(request, self.template_name, args)