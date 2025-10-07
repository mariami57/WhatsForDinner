"""
URL configuration for WhatsForDinner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include, re_path


MAILJET_VERIFICATION_FILENAME = 'e2988da24db20aee7b06774e8d791edd.txt'

def mailjet_verification(request, filename):
    if filename == MAILJET_VERIFICATION_FILENAME:
        return HttpResponse("", content_type="text/plain")
    return HttpResponse(status=404)
urlpatterns = [
    re_path(rf'^{MAILJET_VERIFICATION_FILENAME}$', mailjet_verification),
    path('', include('common.urls')),
    path('admin/', admin.site.urls),
    path('recipes/', include('recipes.urls')),
    path('accounts/', include('accounts.urls')),
    path('subscriber/', include('subscriber.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
