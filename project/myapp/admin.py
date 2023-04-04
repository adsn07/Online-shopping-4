from django.contrib import admin

# Register your models here.
# user_login, user_details, seller_details, category_master, sub_category_master
# product_master, product_pics, shopping_cart, bill_master, payment_master
# bill_details, product_rating

from .models import user_login, user_details
from .models import seller_details, category_master, sub_category_master
from .models import product_master, product_pics, shopping_cart, bill_master, payment_master
from .models import bill_details, product_review, p_return

admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(bill_details)
admin.site.register(product_review)
admin.site.register(seller_details)
admin.site.register(category_master)
admin.site.register(sub_category_master)
admin.site.register(product_master)
admin.site.register(product_pics)
admin.site.register(shopping_cart)
admin.site.register(bill_master)
admin.site.register(payment_master)
admin.site.register(p_return)