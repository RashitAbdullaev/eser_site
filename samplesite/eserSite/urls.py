from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
app_name = 'eserSite'
urlpatterns = [
    path('', ListSite.as_view(), name="main_page"),
    path('england', LanguagePage.as_view(), name="england_page"),
    path('germany', LanguagePage.as_view(), name="germany_page"),
    path('chine', LanguagePage.as_view(), name="chine_page"),
    path('russia', LanguagePage.as_view(), name="russia_page"),
    path('komp', LanguagePage.as_view(), name="komp_page"),
    path('math', LanguagePage.as_view(), name="math_page"),
    path('vacancies', LanguagePage.as_view(), name="vacancies"),
    path('teacherInfo', TeacherInfo.as_view(), name="teacher_page"),
    path('bidCreate', BidCreate.as_view(), name="bidCreate"),
    path('videoList', VideoList.as_view(), name="videoList"),
    path('VideoSingle/<int:pk>', VideoSingle.as_view(), name="VideoSingle"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


