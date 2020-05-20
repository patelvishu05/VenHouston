from django.urls import path
from . import views

app_name = 'AtithiApp'
urlpatterns = [
    path('login/',views.userLogin, name='login'),
    path('dashboard/',views.DashboardPage.as_view(), name='dashboard'),
    path('departures/',views.Departure.as_view(), name='departures'),
    path('paststay/', views.PastStay.as_view(), name='paststay'),
    path('search/', views.Search.as_view(), name='search'),
    path('selectDates/', views.SelectDates.as_view(), name='selectDates'),
    path('inhouse/',views.InHouse.as_view(), name='inhouse'),
    path('admin/',views.Admin.as_view(), name='admin'),
    path('logout/',views.logoutRequest, name='logout'),
    path('checkin/',views.checkIn,name='checkin'),
]