"""
URL configuration for settings project.

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
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.i18n import set_language

urlpatterns = [
    path("i18n/setlang/", set_language, name="set_language"),  # 👈 это нужно Jazzmin

    path('api/users/', include('users.urls')),
    path('api/products/', include('products.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/dealers/', include('dealers.urls')),
    path('api/info/', include('info.urls')),
    path('api/forms/', include('forms.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
)
