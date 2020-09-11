from django.contrib import admin
from django.urls import path
from EEE import views

urlpatterns=[

      path('',views.home,name='home'),

    # #path("EEE_A/",views.EEE_A,name="EEE_A")
      path("index/",views.index,name="index"),
      path('gallery/', views.gallery, name='gallery'),
      #path('login/', views.login, name='login'),
      path("home/",views.home,name="home"),
      path("about/",views.about,name="about"),
      path('edit/<int:id>',views.edit,name='edit'),
      path('delete/<int:id>', views.delete, name='delete'),
      path('fregister/',views.facultyregister,name='facultyregister'),
      path('update/<int:num>',views.facultyedit,name='facultyedit'),
      path('display/', views.faculty_data, name='faculty_data'),
      path('fdelete/<int:num>', views.fdelete, name='fdelete'),
      path('',views.home,name="home"),
      path('register/',views.register,name="register"),
      path('signin/',views.signin,name="signin"),
      
      
      path('home/', views.home,name='home'),
      path('about/', views.about, name='testing'),
     
    #path('login/', views.login, name='login'),
      path('student/register/', views.register, name='register'),
      path('student/display/', views.student_details, name='student_details'),
      path('userprofile/',views.userprofile,name="userprofile"),
      path('changepassword/',views.changepassword,name='changepassword'),
      path('signout/',views.signout,name="signout"),
      
      path('editprofile/',views.editprofile,name="editprofile"),
    


]



