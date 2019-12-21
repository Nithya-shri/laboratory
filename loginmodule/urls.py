from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('studentlogin',views.studentlogin,name="studentlogin"),
    path('studentregister',views.studentregister,name="studentregister"),
    path('staffphysics',views.staffphysics,name="staffphysics"),
    path('components',views.components,name="components"),
    path('add',views.add,name="add"),
    path('staffchemistry',views.staffchemistry,name="staffchemistry"),
    path('studentphysics',views.studentphysics,name="studentphysics"),
    path('req',views.req,name="req"),
    path('requesting',views.requesting,name="requesting"),
    path('requestdetails',views.requestdetails,name="requestdetails"),
    path('studenthomepage',views.studenthomepage,name="studenthomepage"),
    path('studentchemistry',views.studentchemistry,name="studentchemistry"),
    path('logout',views.logout,name="logout"),
    path('staffp',views.staffp,name="staffp"),
    path('staff',views.staff,name="staff")
    









]