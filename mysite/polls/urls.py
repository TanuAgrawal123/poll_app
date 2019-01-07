from django.urls import path
from  . import views
from django.contrib.auth import views as auth_views

app_name='polls'
urlpatterns=[
path('',views.home, name='polls-home'),
 path('login/', auth_views.LoginView.as_view(template_name='polls/login.html'), name='login'),
 path('logout/', auth_views.LogoutView.as_view(template_name='polls/logout.html'), name='logout'),

path('index/',views.index, name='polls-index'),
path('<int:question_id>/results/', views.results, name='results'),
path('<int:question_id>/vote/', views.vote, name='vote'),
path('register/', views.register, name='register'),
]