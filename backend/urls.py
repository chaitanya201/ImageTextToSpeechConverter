from django.urls import path

from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('home/', include('backend.urls')),

    path('home/', home),
    path('showText/', showText, name= "text"),
]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
print("in second urls")