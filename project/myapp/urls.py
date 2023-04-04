"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),


    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_seller_details_view', views.admin_seller_details_view, name='admin_seller_details_view'),
    path('admin_seller_details_add', views.admin_seller_details_add, name='admin_seller_details_add'),
    path('admin_seller_details_delete', views.admin_seller_details_delete, name='admin_seller_details_delete'),

    path('admin_category_delete', views.admin_category_delete, name='admin_category_delete'),
    path('admin_category_add', views.admin_category_add, name='admin_category_add'),
    path('admin_category_view', views.admin_category_view, name='admin_category_view'),
    path('admin_category_edit', views.admin_category_edit, name='admin_category_edit'),

    path('admin_sub_category_delete', views.admin_sub_category_delete, name='admin_sub_category_delete'),
    path('admin_sub_category_add', views.admin_sub_category_add, name='admin_sub_category_add'),
    path('admin_sub_category_view', views.admin_sub_category_view, name='admin_sub_category_view'),
    path('admin_sub_category_edit', views.admin_sub_category_edit, name='admin_sub_category_edit'),

    path('admin_user_details_view', views.admin_user_details_view, name='admin_user_details_view'),

    path('admin_product_master_view', views.admin_product_master_view, name='admin_product_master_view'),

    path('admin_product_pic_view', views.admin_product_pic_view, name='admin_product_pic_view'),

    path('admin_product_allreview_view', views.admin_product_allreview_view, name='admin_product_allreview_view'),

    path('seller_login', views.seller_login_check, name='seller_login'),
    path('seller_logout', views.seller_logout, name='seller_logout'),
    path('seller_home', views.seller_home, name='seller_home'),
    path('seller_changepassword', views.seller_changepassword, name='seller_changepassword'),

    path('seller_product_master_add', views.seller_product_master_add, name='seller_product_master_add'),
    path('seller_product_master_delete', views.seller_product_master_delete, name='seller_product_master_delete'),
    path('seller_product_master_view', views.seller_product_master_view, name='seller_product_master_view'),
    path('seller_product_master_stock_edit', views.seller_product_master_stock_edit, name='seller_product_master_stock_edit'),

    path('seller_product_pic_add', views.seller_product_pic_add, name='seller_product_pic_add'),
    path('seller_product_pic_delete', views.seller_product_pic_delete, name='seller_product_pic_delete'),
    path('seller_product_pic_view', views.seller_product_pic_view, name='seller_product_pic_view'),

    path('seller_bill_view', views.seller_bill_view, name='seller_bill_view'),
    path('seller_bill_details_view', views.seller_bill_details_view, name='seller_bill_details_view'),

    path('seller_product_allreview_view', views.seller_product_allreview_view, name='seller_product_allreview_view'),

    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),

    path('user_product_master_view', views.user_product_master_view, name='user_product_master_view'),

    path('user_product_pic_view', views.user_product_pic_view, name='user_product_pic_view'),

    path('user_product_search', views.user_product_search, name='user_product_search'),

    path('user_shopping_cart_add', views.user_shopping_cart_add, name='user_shopping_cart_add'),
    path('user_shopping_cart_delete', views.user_shopping_cart_delete, name='user_shopping_cart_delete'),
    path('user_shopping_cart_view', views.user_shopping_cart_view, name='user_shopping_cart_view'),

    path('user_payment_add', views.user_payment_add, name="user_payment_add"),
    path('user_payment_view', views.user_payment_view, name='user_payment_view'),

    path('user_bill_view', views.user_bill_view, name='user_bill_view'),
    path('user_bill_details_view', views.user_bill_details_view, name='user_bill_details_view'),

    path('user_product_review_add', views.user_product_review_add, name='user_product_review_add'),
    path('user_product_review_delete', views.user_product_review_delete, name='user_product_review_delete'),
    path('user_product_review_view', views.user_product_review_view, name='user_product_review_view'),
    path('user_product_allreview_view', views.user_product_allreview_view, name='user_product_allreview_view'),

    path('user_return_add', views.user_return_add, name='user_return_add'),
    path('user_return_view', views.user_return_view, name='user_return_view'),
    path('seller_return_request_view', views.seller_return_request_view, name='seller_return_request_view'),

    path('seller_return_request_update', views.seller_return_request_update, name='seller_return_request_update'),

    path('seller_details_add', views.seller_details_add, name='seller_details_add'),

    path('seller_category_delete', views.seller_category_delete, name='seller_category_delete'),
    path('seller_category_add', views.seller_category_add, name='seller_category_add'),
    path('seller_category_view', views.seller_category_view, name='seller_category_view'),
    path('seller_category_edit', views.seller_category_edit, name='seller_category_edit'),

    path('seller_sub_category_delete', views.seller_sub_category_delete, name='seller_sub_category_delete'),
    path('seller_sub_category_add', views.seller_sub_category_add, name='seller_sub_category_add'),
    path('seller_sub_category_view', views.seller_sub_category_view, name='seller_sub_category_view'),
    path('seller_sub_category_edit', views.seller_sub_category_edit, name='seller_sub_category_edit'),

    path('print_bill', views.print_bill, name='print_bill'),

    path('admin_bill_view', views.admin_bill_view, name='admin_bill_view'),
    path('admin_bill_details_view', views.admin_bill_details_view, name='admin_bill_details_view'),

    path('admin_pending_registrations_view', views.admin_pending_registrations_view, name='admin_pending_registrations_view'),
    path('admin_pending_registrations_approve', views.admin_pending_registrations_approve,
         name='admin_pending_registrations_approve'),



]
