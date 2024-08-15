
from django.contrib import admin
from django.urls import path
from auth_app import views

# config for css
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inscription, name="inscription"),
    path('connexion/', views.connexion, name="connexion"),
    path('acceuil/', views.acceuil, name="acceuil"),
    path('deconnexion/', views.deconnexion, name="deconnexion"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    


