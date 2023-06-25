from django.contrib import admin
from django.urls import path
from appKozmetik .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name="Anasayfa"),
    path('kategori/<id>/', Category, name='kategori'),
    path('detay/<id>/',Detail,name='detay'),
    path('kaydol/',Register,name='kaydol'),
    path('giris/',Login,name='giris'),
    path('cikis/',Logout,name='çıkış'),
    path('profil/',Profil,name='profil'),
    path('ürünEkle/<product_id>/',ürünEkle,name='ürünEkle'),
    path('sepet/',Shopping,name='sepet')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


