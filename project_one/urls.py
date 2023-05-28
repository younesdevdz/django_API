
from django.contrib import admin
from django.urls import path , include
from django_app_one import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("breakdown" , views.viewsets_Breakdown)
router.register("reporting" , views.viewsets_reporting)


urlpatterns = [
    path('admin/', admin.site.urls),

    # methode1
    path('django/jsonresponsenomodel/' , views.no_rest),

    # methode2 
    path('django/jsonresponsefromemodel/' , views.no_rest_module),

    # methode3.1
    path('rest/fbvlist/' , views.FBV_List),

    # methode3.2
    path('rest/fbvlist/<int:id>' , views.FBV_ID),

    # methode4

    path('rest/cbv/' , views.CBV_List.as_view()),

    path('rest/cbv/<int:id>' , views.CBV_ID.as_view()),

    path('rest/mixins/' , views.Mixin_List .as_view()),

    path('rest/mixins/<int:pk>' , views.mixins_id.as_view()),

    path('rest/generics/' , views.generics_list.as_view()),

    path('rest/generics/<int:pk>' , views.generics_pk.as_view()),

    path('rest/viewsets/' , include(router.urls)),
    
    path('fbv/findbreakdown/' , views.find_breakdown),
]
