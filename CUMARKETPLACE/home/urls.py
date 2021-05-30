from django.contrib import admin
from django.urls import path,include
 
from django.contrib.auth import views as auth_views

from home import views


urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.loginuser, name="login"),
    path('signup', views.signupuser, name="signup"),
    path('logout', views.logoutuser, name="logout"),
    path('emailsent', views.emailsent, name="emailsent"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('contactus', views.contactus, name="contactus~"),
    
    # password reset part
    path("reset_password", auth_views.PasswordResetView.as_view(template_name="forgotpassword.html"), name="reset_password"),
    path("reset_password_sent", auth_views.PasswordResetDoneView.as_view(template_name="emailsent1.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name="changepassword.html"), name="password_reset_confirm"),
    path("reset_password_complete", auth_views.PasswordResetCompleteView.as_view(template_name="passwordchanged.html"), name="password_reset_complete"), 
    # path('forgotpassword', views.forgotpassword, name="forgotpassword"),

    #Product Related..
    path('product_reg', views.product_reg, name="product_reg"),
    path('product_sell', views.product_sell, name="product_sell"),
    path('product_confirmation/<str:primarykey>', views.product_conf, name="product_confirmation"),
]