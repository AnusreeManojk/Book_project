from django.urls import path
from . import views

urlpatterns = [
    path('create-book', views.createBook, name='create_book'),
    path('author/', views.Create_Author, name='author'),
    path('',views.listBook, name='list_book'),
    path('detailsview/<int:book_id>/', views.detailsView, name='details'),
    path('updateview/<int:book_id>/', views.updateView, name='update'),
    path('deleteview/<int:book_id>/', views.deleteView, name='delete'),
    path('index/', views.index),
    path('search', views.Search_Book, name='search'),
    path('register/',views.Register_user, name='register'),
    path('login/',views.loginUser, name='login'),
    path('logout/',views.logOut,name='logout'),
    path('home/',views.homePage,name='home')


]
