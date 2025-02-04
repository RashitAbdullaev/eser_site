
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.i18n import set_language

urlpatterns = [

    path('admin/', admin.site.urls),
    path(r'i18n/', include('django.conf.urls.i18n')),
    path('', include('eserSite.urls')),
]
# ]+i18n_patterns(

#     path("i18n/", include("django.conf.urls.i18n")),
#
#     prefix_default_language=False
# )


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)