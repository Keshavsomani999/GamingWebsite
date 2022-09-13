from.import views
from django.urls import path ,include

urlpatterns = [
    
    path('', views.index,name='index'),
    path('home/', views.home,name='home'),
    path('store/', views.store,name='store'),
    path('discover/', views.discover,name='discover'),
    path('tg1/', views.tg1,name='tg1'),
    path('tg2/', views.tg2),
    path('tg3/', views.tg3),
    path('tg4/', views.tg4),
    path('tg5/', views.tg5),
    path('news/', views.news,name='news'),
    path('gameproduct/<int:myid>', views.gameproduct,name='gameproduct'),
    path('adventure/', views.adventure,name='adventure'),
    path('action/', views.action,name='action'),
    path('roleplay/', views.roleplay,name='roleplay'),
    path('Sports/', views.Sports,name='Sports'),
    path('Simulation/', views.Simulation,name='Simulation'),
    path('Strategy/', views.Strategy,name='Strategy'), 
    path('search/', views.search, name='search'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('account/', views.account, name='account'),
    path('bill/', views.bill, name='bill'),
    path('status/', views.status, name='status'),
    path('handlerequest/', views.handlerequest, name="handlerequest"),

   
]

    
