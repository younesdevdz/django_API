
from django.contrib import admin
from django.urls import path , include
from django_app_one import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("Product" , views.viewsets_Product)


urlpatterns = [
    path('admin/', admin.site.urls),

    # methode1


    path('rest/viewsets/' , include(router.urls)),
    
    
]
