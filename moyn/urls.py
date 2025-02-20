"""
URL configuration for moyn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from moyn_user.views import MoynUserViewSet
from communities.views import CommunityViewSet, PostViewSet, CommentViewSet, ReactionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'communities', CommunityViewSet)
router.register(r'posts', PostViewSet)
router.register(r'users', MoynUserViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'reactions', ReactionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
