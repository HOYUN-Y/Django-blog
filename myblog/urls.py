"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from blog import views 


handler404 = 'myblog.views.hander_404_views'

def home(request):
    """홈 페이지 렌더링"""
    return render(request, 'home.html')  # ✅ `templates/home.html` 렌더링

urlpatterns = [
    path('',views.landing_view, name='landing'),

    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),#사용자가 CKeditor로 이미지럴 업로드할 때 사용할 URL처리 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#handler404 = 'erpsite.views.custom_page_not_found_view'