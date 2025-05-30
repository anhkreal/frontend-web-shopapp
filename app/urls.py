from django.urls import path
from . import views

urlpatterns = [
    path('customer-home/', views.customer_home, name='customer-home'),
    path('dish-detail/', views.dish_detail, name='dish-detail'),
    path('restaurant-view-details/', views.restaurant_view_details, name='restaurant-view-details'),
    path('cart/', views.cart, name='cart'),
    path('shipping-order/', views.shipping_order, name='shipping-order'),
    path('order-history/', views.order_history, name='order-history'),
    path('spending-statistics/', views.spending_statistics, name='spending-statistics'),
    path('change-password/', views.change_password, name='change-password'),
    path('login/', views.login, name='login'),
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('customer-info/', views.customer_info, name='customer-info'),
    path('restaurant-owner-home/', views.restaurant_owner_home, name='restaurant-owner-home'),
    path('restaurant-pending-order/', views.restaurant_pending_order, name='restaurant-pending-order'),
    path('restaurant-shipping-order/', views.restaurant_shipping_order, name='restaurant-shipping-order'),
    path('restaurant-order-history/', views.restaurant_order_history, name='restaurant-order-history'),
    path('revenue-statistics/', views.revenue_statistics, name='revenue-statistics'),
    path('logout/', views.logout, name='logout'),
    path('restaurant-info/', views.restaurant_info, name='restaurant-info'),
    path('restaurant-owner-info/', views.restaurant_owner_info, name='restaurant-owner-info'),
    path('restaurant-owner-change-password/', views.restaurant_owner_change_password, name='restaurant-owner-change-password'),
    path('api/add-dish/', views.api_add_dish, name='api-add-dish'),
    path('api/update-dish/', views.api_update_dish, name='api-update-dish'),
    path('api/delete-dish/', views.api_delete_dish, name='api-delete-dish'),
    path('api/dish-reviews/', views.api_dish_reviews, name='api-dish-reviews'),

]
