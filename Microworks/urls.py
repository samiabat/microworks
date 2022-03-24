from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
import rest_framework
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)