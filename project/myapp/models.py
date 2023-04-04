from django.db import models

# Create your models here.

#1. user_login - id, uname, passwd, u_type
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return self.uname

#2. user_details - id, user_id, fname, laname, dob, gender, addr, pin, email, contact, status
class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=25)
    age = models.IntegerField()
    addr = models.CharField(max_length=500)
    pin = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=35)
    c_email = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    sem = models.CharField(max_length=150)

    def __str__(self):
        return self.fname

#3. seller_details - id, user_id, name, about, addr, pin, email, contact, status
class seller_details(models.Model):
    #id
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=500)
    addr = models.CharField(max_length=500)
    pin = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    c_email = models.CharField(max_length=150)
    contact = models.CharField(max_length=15)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user_id}'

#4. category_master - id, category_name
class category_master(models.Model):
    #id
    category_name = models.CharField(max_length=50)

#5. sub_category_master - id, category_id, sub_category_name
class sub_category_master(models.Model):
    #id
    category_id = models.IntegerField()
    sub_category_name = models.CharField(max_length=50)

#6. product_master - id, product_name, seller_id, sub_category_id, description, pic, price, stock, dt, tm, keywords, status
class product_master(models.Model):
    #id
    product_name = models.CharField(max_length=50)
    seller_id = models.IntegerField()
    sub_category_id = models.IntegerField()
    description = models.CharField(max_length=500)
    pic = models.CharField(max_length=500)
    price = models.FloatField()
    stock = models.IntegerField()
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    keywords = models.CharField(max_length=500)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.seller_id}, {self.id}'

#7. product_pics - id, product_id, pics
class product_pics(models.Model):
    # id
    product_id = models.IntegerField()
    pics = models.CharField(max_length=500)

#8. shopping_cart - id, user_id, product_id, qty, dt, tm, status
class shopping_cart(models.Model):
    # id
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    qty = models.IntegerField()
    price = models.FloatField()
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=10)

#9. bill_master - id, user_id, bill_no, bill_addr, total_amt, dt, tm
class bill_master(models.Model):
    #id
    user_id = models.IntegerField()
    bill_no = models.CharField(max_length=50)
    bill_addr = models.CharField(max_length=500)
    total_amt = models.FloatField()
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)

#10. payment_master - id, user_id, bill_id, amt, card_no, cvv, dt, tm, status
class payment_master(models.Model):
    # id
    user_id = models.IntegerField()
    bill_id =models.IntegerField()
    amt = models.FloatField()
    card_no = models.CharField(max_length=50)
    cvv = models.CharField(max_length=10)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=10)

#11. bill_details - id, bill_id, product_id, qty, amt
class bill_details(models.Model):
    # id
    bill_id = models.IntegerField()
    product_id = models.IntegerField()
    qty = models.IntegerField()
    amt = models.FloatField()

#12. product_rating - id, user_id, feedback, rating, dt, tm
class product_review(models.Model):
    product_master_id = models.IntegerField()
    user_id = models.IntegerField()
    rating = models.IntegerField()
    review = models.CharField(max_length=500)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)


class p_return(models.Model):
    product_id = models.IntegerField()
    user_id = models.IntegerField()
    amt = models.FloatField()
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
