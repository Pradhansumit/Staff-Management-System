from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    # authentication links
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('success/', views.success, name='success'),

    # dashboard links
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # timer ajax function
    path('timer/', views.timer, name='timer'),
    path('start/', views.timerStart, name="startTimer"),
    path('stop/', views.timerStop, name="stopTimer"),
    path('createtimesheet/', views.timeSheetUpdate, name="timeSheetUpdate"),

    # admin dashboard actions
    path('admin-search/', views.adminSearch, name='admin-search'),
]
