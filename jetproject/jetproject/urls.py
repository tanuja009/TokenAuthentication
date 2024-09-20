from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from django.contrib import admin
from django.urls import path,include
from jwtapp import views
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('studentapi',views.MyModelViewSet,basename="studentapi")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='gettoken'),
    path('verifytoken/',TokenVerifyView.as_view(),name='gettoken'),
     path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),  
]

urlpatterns += router.urls
