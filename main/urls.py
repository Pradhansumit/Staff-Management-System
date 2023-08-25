from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    # authentication links
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('success/', views.success, name='success'),

    path('timer/', views.timer, name='timer'),

    # timer ajax function
    path('start/', views.timerStart, name="startTimer"),
    path('stop/', views.timerStop, name="stopTimer"),
    path('createtimesheet/', views.timeSheetUpdate, name="timeSheetUpdate"),
]
