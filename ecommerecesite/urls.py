from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("cart/", include('cart.urls', namespace='cart')),
    path("orders/", include("orders.urls")),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls')), 
    path('', include('products.urls')),
     

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
