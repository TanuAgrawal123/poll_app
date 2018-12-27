from django.urls import path
from  . import views
app_name='polls'
urlpatterns=[
path('',views.index, name='index'),
path('<int:pk>/', views.index, name='detail'),
path('<int:pk>/results/', views.results, name='results'),
path('<int:question_id>/vote/', views.vote, name='vote'),
]