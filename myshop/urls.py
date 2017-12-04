from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^account/', include('account.urls')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^payment/', include('payment.urls', namespace='payment')),
    url(r'^', include('shop.urls', namespace='shop')),
    url('social-auth/',include('social.apps.django_app.urls', namespace='social')),
    #url(r'^account/', include('account.urls', namespace='account')),
    #url(r'^oauth/', include('social_django.urls', namespace='social')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)