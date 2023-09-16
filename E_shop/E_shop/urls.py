from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/', views.Master, name='master'),
    path('', views.Index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    #ADD TO CART URLS
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    #contact page url
    path('contact_us/', views.contact_page, name='contact_page'),
    
    #checkout page
    path('checkout/',views.Checkout, name='checkout'),
    #order page
    path('order/', views.Your_Order, name='Order'),
    #product page
    path('product/', views.Product_Page, name='product'),
    #product details page
    path('product/<str:id>', views.Product_Detail, name='product_detail'),
    #search
    path('search/', views.Search, name='search'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
