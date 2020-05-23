from django.urls import path,include
from . import views
#from rest_framework.routers import DefaultRouter   //for view sets

#router = DefaultRouter()
#router.register('article',AtricleViewSet, basename='article')

urlpatterns = [
    #Functional Based API View
    #path('api/', views.article_list), 
    #path('api1/<int:pk>/', views.artticle_detail),
   
    #Class Based API View
    path('api/', views.ArticleAPIView.as_view()),
    path('api1/<int:id>/',views.ArticleDetail.as_view()),

    #generiv views and mixins
    path('api/api/<int:id>/', views.GenericAPIView.as_view()), 

    #viewset
    #path('viewset/',include(routers.urls))




]
