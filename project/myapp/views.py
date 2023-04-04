from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login

def index(request):
    return render(request, './myapp/index.html')


def about(request):
    return render(request, './myapp/about.html')


def contact(request):
    return render(request, './myapp/contact.html')

##########################################################################################
######################################## ADMIN ###########################################
def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/admin_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        return render(request, './myapp/admin_login.html')


def admin_home(request):

    return render(request,'./myapp/admin_home.html')


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)


def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)

from . models import seller_details
def admin_seller_details_add(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        about = request.POST.get('about')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        c_email = request.POST.get('c_email')
        contact = request.POST.get('contact')
        status = "new"

        uname = email
        password = '1234'
        ul = user_login(uname=uname, passwd=password, u_type='seller')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = seller_details(user_id=user_id, name=name, about=about, addr=addr, pin=pin, contact=contact, email=email,
                            c_email=c_email,status=status)
        ud.save()

        print(user_id)
        context = {'msg': 'Seller Added'}
        return render(request, 'myapp/admin_seller_details_add.html',context)

    else:
        return render(request, 'myapp/admin_seller_details_add.html')

def admin_seller_details_view(request):
    sd = seller_details.objects.all()
    context = {'seller_list': sd}
    return render(request, './myapp/admin_seller_details_view.html', context)




def admin_seller_details_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    cg = seller_details.objects.get(user_id=int(id))
    ud = user_login.objects.get(id=int(cg.user_id))
    ud.delete()
    cg.delete()
    msg = 'Seller Removed'

    s_l = seller_details.objects.all()
    context = {'seller_list': s_l, 'msg':msg}
    return render(request, './myapp/admin_seller_details_view.html', context)


from . models import category_master
def admin_category_add(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        dg = category_master(category_name = category_name)
        dg.save()
        context = {'msg':'New Category Added'}
        return render(request, './myapp/admin_category_add.html',context)
    else:
        return render(request, './myapp/admin_category_add.html')

def admin_category_view(request):
    ev_l = category_master.objects.all()
    context = {'category_list':ev_l}
    return render(request, './myapp/admin_category_view.html',context)

def admin_category_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    cg = category_master.objects.get(id=int(id))
    cg.delete()
    msg = 'Event Removed'

    ev_l = category_master.objects.all()
    context = {'category_list': ev_l, 'msg':msg}
    return render(request, './myapp/admin_category_view.html', context)

def admin_category_edit(request):
    if request.method == 'POST':
        e_id = request.POST.get('e_id')
        category_name = request.POST.get('category_name')
        dp = category_master.objects.get(id=int(e_id))
        dp.category_name = category_name
        dp.save()

        msg = 'Category Record Updated'
        ev_l = category_master.objects.all()
        context = {'event_list': ev_l, 'msg': msg}
        return render(request, './myapp/admin_category_view.html', context)
    else:
        id = request.GET.get('id')
        ev = category_master.objects.get(id=int(id))
        context = {'category_name': ev.category_name, 'e_id': ev.id}
        return render(request, './myapp/admin_category_edit.html',context)


from . models import sub_category_master
def admin_sub_category_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    category_id = int(request.GET.get('category_id'))
    dd_l = sub_category_master.objects.filter(category_id=category_id)
    context = {'sub_cat_list':dd_l,'category_id': category_id}
    return render(request, './myapp/admin_sub_category_view.html',context)

def admin_sub_category_add(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    if request.method == 'POST':
        category_id = int(request.POST.get('category_id'))
        sub_category_name = request.POST.get('sub_category_name')


        dd = sub_category_master(category_id=category_id, sub_category_name=sub_category_name)
        dd.save()
        context = {'category_id':category_id,'msg': 'Record Added'}
        return render(request, './myapp/admin_sub_category_add.html', context)
    else:
        category_id = int(request.GET.get('category_id'))
        context = {'category_id': category_id, 'msg': ''}
        return render(request, './myapp/admin_sub_category_add.html', context)

def admin_sub_category_edit(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        category_id = int(request.POST.get('category_id'))
        sub_category_name = request.POST.get('sub_category_name')

        dd = sub_category_master.objects.get(id=int(s_id))

        dd.category_id = category_id
        dd.sub_category_name = sub_category_name
        dd.save()
        msg = 'Record Updated'
        dd_l = sub_category_master.objects.all()
        context = {'sub_cat_list': dd_l, 'msg': msg,'category_id': category_id}
        return render(request, './myapp/admin_sub_category_edit.html', context)
    else:
        id = request.GET.get('id')
        category_id = int(request.GET.get('category_id'))
        dd = sub_category_master.objects.get(id=int(id))
        context = {'sub_category_name':dd.sub_category_name,
                   's_id':dd.id,'category_id': category_id}
        return render(request, './myapp/admin_sub_category_edit.html',context)

def admin_sub_category_delete(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    id = request.GET.get('id')
    print('id = '+id)
    category_id = int(request.GET.get('category_id'))
    dd = sub_category_master.objects.get(id=int(id))
    dd.delete()
    msg = 'Record Deleted'
    dd_l = sub_category_master.objects.filter(category_id=category_id)
    context = {'sub_cat_list': dd_l,'msg':msg,'category_id': category_id}
    return render(request, './myapp/admin_sub_category_view.html',context)

def admin_user_details_view(request):
    u_l = user_details.objects.all()
    context = {'user_list' : u_l}
    return render(request, './myapp/admin_user_details_view.html',context)

def admin_product_master_view(request):
    seller_id = request.GET.get('user_id')

    pm_l = product_master.objects.filter(seller_id=int(seller_id))

    scm_l = sub_category_master.objects.all()

    context = {'product_list': pm_l, 'subcategory_list': scm_l, 'msg': ''}
    return render(request, 'myapp/admin_product_master_view.html', context)

def admin_product_pic_view(request):
    product_id = request.GET.get('product_id')
    pp_l = product_pics.objects.filter(product_id=product_id)
    context = {'pic_list': pp_l, 'product_id': product_id, 'msg': ''}
    return render(request, 'myapp/admin_product_pic_view.html', context)

def admin_product_allreview_view(request):
    product_master_id = request.GET.get('product_master_id')
    pr_l = product_review.objects.filter(product_master_id=product_master_id)
    umd = user_details.objects.all()
    context = {'review_list': pr_l,'user_list': umd, 'product_master_id': product_master_id, 'msg': ''}
    return render(request, 'myapp/admin_product_allreview_view.html', context)

###################################################################################
############################### SELLER #######################################

def seller_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='seller')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/seller_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/seller_login.html',context)
    else:
        return render(request, 'myapp/seller_login.html')

def seller_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/seller_home.html',context)
    #send_mail("heoo", "hai", '**@gmail.com')


def seller_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/seller_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/seller_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/seller_changepassword.html', context)
    else:
        return render(request, './myapp/seller_changepassword.html')



def seller_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return seller_login_check(request)
    else:
        return seller_login_check(request)


from .models import product_master
from django.core.files.storage import FileSystemStorage
from datetime import datetime
def seller_product_master_add(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        pic = fs.save(uploaded_file.name, uploaded_file)

        product_name = request.POST.get('product_name')
        seller_id = request.session['user_id']
        sub_category_id = int(request.POST.get('sub_category_id'))
        description = request.POST.get('description')
        price = float(request.POST.get('price'))
        stock = int(request.POST.get('stock'))
        keywords = request.POST.get('keywords')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')

        status='new'

        pm = product_master(product_name=product_name, seller_id=int(seller_id),
                            sub_category_id=sub_category_id, description=description, pic=pic,
                            price=price, stock=stock, dt=dt,tm=tm, keywords=keywords, status=status)
        pm.save()

        scm_l = sub_category_master.objects.all()
        context = {'subcategory_list':scm_l,'msg':'Record added'}
        return render(request, 'myapp/seller_product_master_add.html',context)

    else:
        scm_l = sub_category_master.objects.all()
        context = {'subcategory_list':scm_l,'msg':''}
        return render(request, 'myapp/seller_product_master_add.html',context)

def seller_product_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    pm = product_master.objects.get(id=int(id))
    pm.delete()

    seller_id = request.session['user_id']

    pm_l = product_master.objects.filter(seller_id=int(seller_id))

    scm_l = sub_category_master.objects.all()

    context ={'product_list':pm_l,'subcategory_list': scm_l,'msg':'Record deleted'}
    return render(request,'myapp/seller_product_master_view.html',context)

def seller_product_master_view(request):
    seller_id = request.session['user_id']

    pm_l = product_master.objects.filter(seller_id=int(seller_id))

    scm_l = sub_category_master.objects.all()

    context = {'product_list': pm_l, 'subcategory_list': scm_l, 'msg': ''}
    return render(request, 'myapp/seller_product_master_view.html', context)

def seller_product_master_stock_edit(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return seller_login_check(request)

    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        stock = int(request.POST.get('stock'))
        price = int(request.POST.get('price'))
        dd = product_master.objects.get(id=int(s_id))
        dd.stock = stock
        dd.price = price
        dd.save()
        msg = 'Record Updated'
        seller_id = request.session['user_id']
        pm_l = product_master.objects.filter(seller_id=int(seller_id))

        scm_l = sub_category_master.objects.all()

        context = {'product_list': pm_l, 'subcategory_list': scm_l, 'msg': ''}
        return render(request, 'myapp/seller_product_master_view.html', context)
    else:
        id = request.GET.get('id')
        dd = product_master.objects.get(id=int(id))
        context = {'stock': dd.stock, 'price': dd.price, 's_id': dd.id}
        return render(request, './myapp/seller_product_master_stock_edit.html',context)


from .models import product_pics
def seller_product_pic_add(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        pics = fs.save(uploaded_file.name, uploaded_file)

        pp = product_pics(product_id=int(product_id),pics=pics)
        pp.save()

        context = {'msg':'Picture added','product_id':product_id}
        return render(request, 'myapp/seller_product_pic_add.html',context)

    else:
        product_id = request.GET.get('product_id')
        context = {'msg':'','product_id':product_id}
        return render(request, 'myapp/seller_product_pic_add.html',context)

def seller_product_pic_delete(request):
    id = request.GET.get('id')
    product_id = request.GET.get('product_id')
    print("id="+id)
    pp = product_pics.objects.get(id=int(id))
    pp.delete()

    pp_l = product_pics.objects.filter(product_id=int(product_id))
    context ={'pic_list':pp_l,'product_id': product_id,'msg':'Picture deleted'}
    return render(request,'myapp/seller_product_pic_view.html',context)

def seller_product_pic_view(request):
    product_id = request.GET.get('product_id')
    pp_l = product_pics.objects.filter(product_id=product_id)
    context = {'pic_list': pp_l, 'product_id': product_id, 'msg': ''}
    return render(request, 'myapp/seller_product_pic_view.html', context)

def seller_bill_view(request):
    user_id = request.session['user_id']
    suc_l = bill_master.objects.all()
    bill_list = []
    for suc in suc_l:
        pr_l = bill_details.objects.filter(bill_id=int(suc.id))
        for pr in pr_l:
            p_l = product_master.objects.filter(id=pr.product_id, seller_id=int(user_id))
            if len(p_l) >= 1:
                bill_list.append(suc)
                break
    ud_l = user_details.objects.all()
    context = {'transaction_list': suc_l, 'msg': '', 'user_list': ud_l}
    return render(request, './myapp/seller_bill_view.html', context)

def seller_bill_details_view(request):
    user_id = request.session['user_id']
    bill_id = request.GET.get('bill_id')
    pr_l = bill_details.objects.filter(bill_id=int(bill_id))
    bill_list = []
    for pr in pr_l:
        p_l = product_master.objects.filter(id=pr.product_id,seller_id=int(user_id))
        if len(p_l) >=1:
            bill_list.append(pr)
    pm_l = product_master.objects.all()
    context = {'details_list': pr_l, 'product_list': pm_l, 'msg': ''}
    return render(request, 'myapp/seller_bill_details_view.html', context)

def seller_product_allreview_view(request):
    product_master_id = request.GET.get('product_master_id')
    pr_l = product_review.objects.filter(product_master_id=product_master_id)
    umd = user_details.objects.all()
    context = {'review_list': pr_l,'user_list': umd, 'product_master_id': product_master_id, 'msg': ''}
    return render(request, 'myapp/seller_product_allreview_view.html', context)
###########################################################################################
################################ USER #################################################
from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/user_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/user_login.html',context)
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        age = request.POST.get('age')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        sem = request.POST.get('sem')
        department = request.POST.get('department')
        c_email = request.POST.get('c_email')



        uname=c_email
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='user0')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, age=age,addr=addr, pin=pin, contact=contact, email=email,department=department,sem=sem,c_email=c_email )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/user_login.html',context)

    else:
        return render(request, 'myapp/user_details_add.html')

def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/user_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/user_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/user_changepassword.html', context)
    else:
        return render(request, './myapp/user_changepassword.html')



def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)

def user_product_master_view(request):

    pm_l = product_master.objects.all()

    scm_l = sub_category_master.objects.all()
    sc_l = seller_details.objects.all()

    context = {'product_list': pm_l, 'subcategory_list': scm_l, 'msg': '', 'seller_list':sc_l}
    return render(request, 'myapp/user_product_master_view.html', context)


from django.db.models import Q
def user_product_search(request):
    if request.method == 'POST':
        app_name = request.POST.get('app_name')
        sub_category_id = int(request.POST.get('sub_category_id'))
        print('sub_category_id ', sub_category_id)
        if sub_category_id == 0:
            pm_l = product_master.objects.filter(Q(product_name__contains=app_name) | Q(keywords__contains=app_name))
        else:
            p = product_master.objects.filter(sub_category_id=sub_category_id)
            pm_l = p.filter(Q(product_name__contains=app_name) | Q(keywords__contains=app_name))


        scm_l = sub_category_master.objects.all()
        sc_l = seller_details.objects.all()

        context = {'product_list': pm_l, 'subcategory_list': scm_l, 'msg': '', 'seller_list': sc_l}
        return render(request, 'myapp/user_product_master_view.html', context)
    else:
        scm_l = sub_category_master.objects.all()
        context = {'subcategory_list': scm_l}
        return render(request, 'myapp/user_product_search.html', context)


def user_product_pic_view(request):
    product_id = request.GET.get('product_id')
    pp_l = product_pics.objects.filter(product_id=product_id)
    context = {'pic_list': pp_l, 'product_id': product_id, 'msg': ''}
    return render(request, 'myapp/user_product_pic_view.html', context)

from .models import shopping_cart
def user_shopping_cart_add(request):
    product_id = request.GET.get('product_id')
    user_id = request.session['user_id']
    qty = 1
    dt = datetime.today().strftime('%Y-%m-%d')
    tm = datetime.today().strftime('%H:%M:%S')
    status = 'ok'
    prd = product_master.objects.get(id=int(product_id))
    if prd.stock == 0:
        context = {'msg': 'Sorry, No stock'}
        return render(request, 'myapp/user_product_search.html', context)

    pr_l = shopping_cart.objects.filter(product_id=product_id,user_id=user_id)
    if len(pr_l) == 0:
        pr = shopping_cart(product_id=int(product_id), user_id=int(user_id), qty=int(qty),
                           price=float(prd.price),dt=dt, tm=tm, status=status)
        stock = prd.stock-1
        prd.stock = stock
        prd.save()
        pr.save()
    else:
        pr = shopping_cart.objects.get(product_id=product_id,user_id=user_id)
        qty = pr.qty
        pr.qty = qty+1
        pr.price=float(prd.price*pr.qty)
        pr.save()
        stock = prd.stock - 1
        prd.stock = stock
        prd.save()
        pr.save()




    context = {'msg':'Added to cart'}
    return render(request, 'myapp/user_product_search.html',context)


def user_shopping_cart_delete(request):
    id = request.GET.get('id')

    print("id="+id)
    pp = shopping_cart.objects.get(id=int(id))
    pr = product_master.objects.get(id=int(pp.product_id))
    if pp.qty >1:
        qty = pp.qty
        pp.qty = qty - 1
        pp.price = float(pr.price * pp.qty)
        pp.save()
    elif pp.qty == 0:
        pp.delete()
    else:
        pp.delete()

    user_id = request.session['user_id']
    pr_l = shopping_cart.objects.filter(user_id=int(user_id))
    pm_l = product_master.objects.all()
    context = {'cart_list': pr_l, 'product_list': pm_l, 'msg': 'Deleted'}
    return render(request, 'myapp/user_shopping_cart_view.html', context)

def user_shopping_cart_view(request):
    user_id = request.session['user_id']
    pr_l = shopping_cart.objects.filter(user_id=int(user_id))
    pm_l = product_master.objects.all()
    context = {'cart_list': pr_l, 'product_list': pm_l, 'msg': ''}
    return render(request, 'myapp/user_shopping_cart_view.html', context)


from .models import bill_master,bill_details, payment_master
def user_payment_add(request):
    if request.method == 'POST':

        amt = request.POST.get('amt')
        card_no = request.POST.get('card_no')
        cvv = request.POST.get('cvv')

        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'ok'
        qty=1
        user_id = request.session['user_id']

        pm_l = product_master.objects.all()
        user = user_details.objects.get(user_id= int(user_id))

        bm = bill_master(user_id=int(user_id), bill_no='bno', bill_addr=user.addr,
                         total_amt=float(amt), dt=dt, tm=tm)
        bm.save()

        bill_id = bill_master.objects.all().aggregate(Max('id'))['id__max']

        pm = payment_master(bill_id=bill_id, user_id=int(user_id), amt=float(amt),
                            card_no=card_no, cvv=cvv, dt=dt, tm=tm, status='ok')
        pm.save()
        pr_l = shopping_cart.objects.filter(user_id=int(user_id))
        for pr in pr_l:
            pm = product_master.objects.get(id=pr.product_id)
            if pm.stock >=1:
                #amt += pm.price
                pm.stock = pm.stock-pr.qty
                pm.save()
                bd = bill_details(bill_id=bill_id, product_id=pm.id, qty=pr.qty, amt=pr.price)
                bd.save()
                sc = shopping_cart.objects.get(id=pr.id)
                sc.delete()

        sc_l = shopping_cart.objects.filter(user_id=int(user_id))
        context = {'cart_list': sc_l, 'product_list': pm_l, 'msg': 'Payment successfully done'}
        return render(request, 'myapp/user_shopping_cart_view.html', context)

    else:
        user_id = request.session['user_id']
        pr_l = shopping_cart.objects.filter(user_id=int(user_id))
        cart_list = []
        pm_l = product_master.objects.all()
        amt = 0.0
        for pr in pr_l:
            pm = product_master.objects.get(id=pr.product_id)
            if pm.stock >=1:
                # amt += pm.price
                cart_list.append(pr)
        for pr in pr_l:
            amt += pr.price
        context = { 'cart_list': cart_list, 'product_list': pm_l, 'msg': '','amt':amt}
        return render(request, './myapp/user_payment_add.html', context)

def user_payment_view(request):
    user_id = request.session['user_id']
    suc_l = payment_master.objects.filter(user_id=int(user_id))
    ud_l = user_details.objects.all()
    context = {'transaction_list': suc_l, 'msg': '', 'user_list': ud_l}
    return render(request, './myapp/user_payment_view.html', context)

def user_bill_view(request):
    user_id = request.session['user_id']
    suc_l = bill_master.objects.filter(user_id=int(user_id))
    ud_l = user_details.objects.all()
    context = {'transaction_list': suc_l, 'msg': '', 'user_list': ud_l}
    return render(request, './myapp/user_bill_view.html', context)

def user_bill_details_view(request):
    user_id = request.session['user_id']
    bill_id = request.GET.get('bill_id')
    pr_l = bill_details.objects.filter(bill_id=int(bill_id))
    pm_l = product_master.objects.all()
    context = {'details_list': pr_l, 'product_list': pm_l, 'msg': '','bill_id':bill_id}
    return render(request, 'myapp/user_bill_details_view.html', context)

from .models import product_review
def user_product_review_add(request):
    if request.method == 'POST':
        product_master_id = request.POST.get('product_master_id')
        user_id = request.session['user_id']
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'ok'
        pr = product_review(product_master_id=int(product_master_id),user_id=int(user_id),rating=int(rating),review=review,
                            dt=dt,tm=tm,status=status)
        pr.save()

        context = {'msg':'Review added','product_master_id':product_master_id}
        return render(request, 'myapp/user_product_review_add.html',context)

    else:
        product_master_id = request.GET.get('product_master_id')
        context = {'msg':'','product_master_id':product_master_id}
        return render(request, 'myapp/user_product_review_add.html',context)

def user_product_review_delete(request):
    id = request.GET.get('id')
    product_master_id = request.GET.get('product_master_id')
    print("id="+id)
    pp = product_review.objects.get(id=int(id))
    pp.delete()

    user_id = request.session['user_id']
    product_master_id = request.GET.get('product_master_id')
    pr_l = product_review.objects.filter(product_master_id=product_master_id, user_id=int(user_id))
    context = {'review_list': pr_l, 'product_master_id': product_master_id, 'msg': 'Review deleted'}
    return render(request, 'myapp/user_product_review_view.html', context)

def user_product_review_view(request):
    user_id=request.session['user_id']
    product_master_id = request.GET.get('product_master_id')
    pr_l = product_review.objects.filter(product_master_id=product_master_id,user_id=int(user_id))
    context = {'review_list': pr_l, 'product_master_id': product_master_id, 'msg': ''}
    return render(request, 'myapp/user_product_review_view.html', context)

def user_product_allreview_view(request):
    product_master_id = request.GET.get('product_master_id')
    pr_l = product_review.objects.filter(product_master_id=product_master_id)
    umd = user_details.objects.all()
    context = {'review_list': pr_l,'user_list': umd, 'product_master_id': product_master_id, 'msg': ''}
    return render(request, 'myapp/user_product_allreview_view.html', context)



###########################################################################################
from . models import p_return
def user_return_add(request):
    id = request.GET.get('id')
    product_id = request.GET.get('product_id')
    user_id = request.session['user_id']
    bill_id = request.GET.get('bill_id')
    b = bill_details.objects.get(id=int(id))

    dt = datetime.today().strftime('%Y-%m-%d')
    tm = datetime.today().strftime('%H:%M:%S')

    pr = p_return(product_id=product_id, user_id=user_id, amt = float(b.amt),dt=dt,tm=tm,status='requested')
    pr.save()

    pr_l = bill_details.objects.filter(bill_id=int(bill_id))
    pm_l = product_master.objects.all()
    context = {'details_list': pr_l, 'product_list': pm_l, 'msg': 'return requested','bill_id':bill_id}
    return render(request, 'myapp/user_bill_details_view.html', context)



def user_return_view(request):
    user_id = request.session['user_id']
    print(user_id)
    r_l = p_return.objects.filter(user_id=user_id)
    p_l = product_master.objects.all()
    context = {'r_l':r_l, 'p_l':p_l}
    return render(request, 'myapp/user_return_view.html', context)

def seller_return_request_view(request):
    seller_id = request.session['user_id']
    p_l = product_master.objects.filter(seller_id=seller_id)
    r_l = []
    for p in p_l:

        rl = p_return.objects.get(product_id=p.id)
        r_l.append(rl)

    print(r_l)
    ul = user_details.objects.all()
    context = {'r_l':r_l, 'p_l':p_l, 'u_l':ul}
    return render(request, 'myapp/seller_return_request_view.html', context)

def seller_return_request_update(request):
    id = request.GET.get('id')
    pr = p_return.objects.get(id=int(id))
    pr.status = 'Return Approved'
    pr.save()
    seller_id = request.session['user_id']
    p_l = product_master.objects.filter(seller_id=seller_id)
    r_l = []
    for p in p_l:
        rl = p_return.objects.get(product_id=p.id)
        r_l.append(rl)

    print(r_l)
    ul = user_details.objects.all()
    context = {'r_l':r_l, 'p_l':p_l, 'u_l':ul}
    return render(request, 'myapp/seller_return_request_view.html', context)

def  seller_details_add(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        about = request.POST.get('about')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('passwd')
        c_email = request.POST.get('c_email')
        status = "new"

        uname = c_email

        ul = user_login(uname=uname, passwd=password, u_type='seller0')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = seller_details(user_id=user_id, name=name, about=about, addr=addr, pin=pin, contact=contact, email=email,c_email=c_email,
                            status=status)
        ud.save()

        print(user_id)
        context = {'msg': 'Seller Added'}
        return render(request, 'myapp/seller_login.html',context)

    else:
        return render(request, 'myapp/seller_details_add.html')

#######################################################
def seller_category_add(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        dg = category_master(category_name = category_name)
        dg.save()
        context = {'msg':'New Category Added'}
        return render(request, './myapp/seller_category_add.html',context)
    else:
        return render(request, './myapp/seller_category_add.html')

def seller_category_view(request):
    ev_l = category_master.objects.all()
    context = {'category_list':ev_l}
    return render(request, './myapp/seller_category_view.html',context)

def seller_category_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    cg = category_master.objects.get(id=int(id))
    cg.delete()
    msg = 'Event Removed'

    ev_l = category_master.objects.all()
    context = {'category_list': ev_l, 'msg':msg}
    return render(request, './myapp/seller_category_view.html', context)

def seller_category_edit(request):
    if request.method == 'POST':
        e_id = request.POST.get('e_id')
        category_name = request.POST.get('category_name')
        dp = category_master.objects.get(id=int(e_id))
        dp.category_name = category_name
        dp.save()

        msg = 'Category Record Updated'
        ev_l = category_master.objects.all()
        context = {'event_list': ev_l, 'msg': msg}
        return render(request, './myapp/seller_category_view.html', context)
    else:
        id = request.GET.get('id')
        ev = category_master.objects.get(id=int(id))
        context = {'category_name': ev.category_name, 'e_id': ev.id}
        return render(request, './myapp/seller_category_edit.html',context)


from . models import sub_category_master
def seller_sub_category_view(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    category_id = int(request.GET.get('category_id'))
    dd_l = sub_category_master.objects.filter(category_id=category_id)
    context = {'sub_cat_list':dd_l,'category_id': category_id}
    return render(request, './myapp/seller_sub_category_view.html',context)

def seller_sub_category_add(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    if request.method == 'POST':
        category_id = int(request.POST.get('category_id'))
        sub_category_name = request.POST.get('sub_category_name')


        dd = sub_category_master(category_id=category_id, sub_category_name=sub_category_name)
        dd.save()
        context = {'category_id':category_id,'msg': 'Record Added'}
        return render(request, './myapp/seller_sub_category_add.html', context)
    else:
        category_id = int(request.GET.get('category_id'))
        context = {'category_id': category_id, 'msg': ''}
        return render(request, './myapp/seller_sub_category_add.html', context)

def seller_sub_category_edit(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        category_id = int(request.POST.get('category_id'))
        sub_category_name = request.POST.get('sub_category_name')

        dd = sub_category_master.objects.get(id=int(s_id))

        dd.category_id = category_id
        dd.sub_category_name = sub_category_name
        dd.save()
        msg = 'Record Updated'
        dd_l = sub_category_master.objects.all()
        context = {'sub_cat_list': dd_l, 'msg': msg,'category_id': category_id}
        return render(request, './myapp/seller_sub_category_edit.html', context)
    else:
        id = request.GET.get('id')
        category_id = int(request.GET.get('category_id'))
        dd = sub_category_master.objects.get(id=int(id))
        context = {'sub_category_name':dd.sub_category_name,
                   's_id':dd.id,'category_id': category_id}
        return render(request, './myapp/seller_sub_category_edit.html',context)

def seller_sub_category_delete(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    id = request.GET.get('id')
    print('id = '+id)
    category_id = int(request.GET.get('category_id'))
    dd = sub_category_master.objects.get(id=int(id))
    dd.delete()
    msg = 'Record Deleted'
    dd_l = sub_category_master.objects.filter(category_id=category_id)
    context = {'sub_cat_list': dd_l,'msg':msg,'category_id': category_id}
    return render(request, './myapp/seller_sub_category_view.html',context)
#######################################################

def print_bill(request):
    user_id = request.session['user_id']
    bill_id = request.GET.get('bill_id')
    b_m = bill_master.objects.get(id=int(bill_id))
    pr_l = bill_details.objects.filter(bill_id=int(bill_id))
    ud = user_details.objects.get(user_id=int(user_id))
    pm_l = product_master.objects.all()
    context = {'details_list': pr_l, 'product_list': pm_l, 'msg': '','bill_id':bill_id,
               'bm':b_m,'ud':ud}
    return render(request, 'myapp/print_bill.html', context)




def admin_bill_view(request):
    user_id = request.GET.get('user_id')
    suc_l = bill_master.objects.filter(user_id__contains = user_id)
    bill_list = []
    for suc in suc_l:
        pr_l = bill_details.objects.filter(bill_id=int(suc.id))
        for pr in pr_l:
            p_l = product_master.objects.filter(id=pr.product_id, seller_id=int(user_id))
            if len(p_l) >= 1:
                bill_list.append(suc)
                break
    ud_l = user_details.objects.all()
    context = {'transaction_list': suc_l, 'msg': '', 'user_list': ud_l}
    return render(request, './myapp/admin_bill_view.html', context)


def admin_bill_details_view(request):
    user_id = request.session['user_id']
    bill_id = request.GET.get('bill_id')
    pr_l = bill_details.objects.filter(bill_id=int(bill_id))
    bill_list = []
    for pr in pr_l:
        p_l = product_master.objects.filter(id=pr.product_id)#,seller_id=int(user_id)
        if len(p_l) >=1:
            bill_list.append(pr)
    pm_l = product_master.objects.all()

    suc_l = payment_master.objects.filter(bill_id=int(bill_id))
    ud_l = user_details.objects.all()


    context = {'details_list': pr_l, 'product_list': pm_l, 'msg': '','transaction_list': suc_l}
    return render(request, 'myapp/admin_bill_details_view.html', context)

def admin_pending_registrations_view(request):
    seller_list = user_login.objects.filter(u_type='seller0')
    selr_list = []
    for sl in seller_list:
        sd = seller_details.objects.get(user_id=sl.id)
        selr_list.append(sd)

    user_list = user_login.objects.filter(u_type='user0')
    usr_list = []
    for ul in user_list:
        ud = user_details.objects.get(user_id=ul.id)
        usr_list.append(ud)

    context = {'seller_list':selr_list,'user_list':usr_list}
    return render(request, 'myapp/admin_pending_registrations_view.html', context)


from django.http import HttpResponse
def admin_pending_registrations_approve(request):
    id = request.GET.get('id')

    apl = user_login.objects.get(id=id)
    mail = apl.uname

    if mail[:1] == 'u':
        if apl.u_type=='seller0':
            apl.u_type='seller'
            apl.save()
        else:
            apl.u_type = 'user'
            apl.save()

    if apl.u_type == 'user':
        msg = 'Registration Approved'
    else:
        msg = 'Registration Rejected'

    seller_list = user_login.objects.filter(u_type='seller0')
    selr_list = []
    for sl in seller_list:
        sd = seller_details.objects.get(user_id=sl.id)
        selr_list.append(sd)

    user_list = user_login.objects.filter(u_type='user0')
    usr_list = []
    for ul in user_list:
        ud = user_details.objects.get(user_id=ul.id)
        usr_list.append(ud)

    context = {'seller_list': selr_list, 'user_list': usr_list, 'msg': msg}
    return render(request, 'myapp/admin_pending_registrations_view.html', context)