from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

# Görüntüleme fonksiyonları

def Index(request):
    # Tüm ürünleri ve kategorileri veritabanından al
    products = Product.objects.all()
    categories = Categories.objects.all()
    
    query=request.GET.get('q')
    if query:
       products=products.filter(
            Q(title__icontains=query)|
            Q(product_detail__icontains=query)|
            Q(category__title__icontains=query)
        ).distinct
    
    
    context = {
        "products": products,
        "categories": categories,
    }
    
    return render(request, 'index.html', context)


def Category(request, id):
    # Kategori kimliğine göre ürünleri filtrele
    products = Product.objects.filter(category=id)
    categories = Categories.objects.all()
    
    context = {
        "products": products,
        "categories": categories,
    }
    
    return render(request, 'category.html', context)

def Detail(request, id):
    # Ürün detaylarını ve ürüne ait yorumları al
    product = Product.objects.get(id=id)
    categories = Categories.objects.all()
    comments = Comment.objects.filter(product_comment=product)
    
    if request.method == 'POST':
        # Ürüne yorum kaydet
        comment_text = request.POST['comments']
        comm = Comment(comments=comment_text, product_comment=product)
        comm.save()
        
        return redirect('/detail/' + id + '/')
    
    context = {
        "product": product,
        "categories": categories,
        "comments": comments
    }
    
    return render(request, 'detail.html', context)

# Kullanıcı işlemleri fonksiyonları

def Register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        job = request.POST['job']
        
        if password == confirm_password:
            if User.objects.filter(username=firstname).exists():
                context = {
                    "information": "Bu kullanıcı adı zaten alınmış. Lütfen başka bir tane deneyin."
                }
                return render(request, 'register.html', context)
          
            if User.objects.filter(email=email).exists():
                context = {
                    "information": "Bu e-posta adresi zaten kayıtlı. Lütfen başka bir tane deneyin."
                }
                return render(request, 'register.html', context)
            
            user = User.objects.create_user(username=firstname, last_name=lastname, email=email, password=password, job=job)
            user.save()
            
            return redirect('register')
        
        else:
            context = {
                "information": "İki parola birbiriyle uyuşmuyor. Lütfen tekrar deneyin."
            }
            return render(request, 'register.html', context)

    return render(request, 'register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('Anasayfa')
        else:
            context = {
                "information": "Geçersiz kullanıcı adı veya parola girdiniz."
            }
            return render(request, 'login.html', context)

    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('giris')

def Profil(request):
    categories = Categories.objects.all()

    if request.method == "POST" and "product" in request.POST:
        title = request.POST['product_name']
        product_detail = request.POST['product_title']
        product_price = request.POST['product_price']
        product_img = request.FILES['product_img']
        category_id = request.POST['category']

        category = Categories.objects.get(id=category_id)

        product = Product(title=title, product_detail=product_detail, product_price=product_price, product_img=product_img, category=category)
        product.save()

        return redirect('Index')
    
    context = {
        "categories": categories
    }
    return render(request, 'profil.html', context)

def ürünEkle(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    sepet = Sepet.objects.create(user=user, Product=product, adet=1, allprice=product.product_price)
    sepet.save()
    return redirect('sepet')




def Shopping(request):
    sepet =Sepet.objects.filter(user=request.user)
    
    context={
        "sepet":sepet
    }
    
    return render(request,'shop.html', context)