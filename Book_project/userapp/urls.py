from django.urls import path
from . import views

urlpatterns = [
    # path('author/', views.Create_Author, name='author'),
    path('',views.listBook, name='user_book'),
    path('detailsview/<int:book_id>/', views.detailsView, name='user_details'),

    # path('search/book', views.Search_Book, name='user_search'),
    # path('search/author/', views.Search_Author, name='user_search_author'),
    path('search-user/', views.Search_Book, name='usersearch'),
    path('add_to_cart/<int:book_id>/',views.add_to_cart, name='addtocart'),
    path('view_cart/',views.view_cart,name='viewcart'),
    path('increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove-from-cart/<int:item_id>/',views.remove_from_cart,name='remove_cart'),
    path('create-checkout-session/',views.create_checkout_session,name='create-checkout-session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]
