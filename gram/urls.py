from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^$',views.welcome,name = 'welcome'),
    re_path(r'^accounts/profile/$',views.profile,name = 'profile'),
    re_path(r'^comments$',views.comment,name = 'comment'),
    re_path(r'^posts$',views.post,name = 'post'),
    re_path(r'^search/profile$', views.search, name='profiles'),
    re_path(r'^edit_profile$', views.edit_profile, name='edit'),
    re_path(r'^logout', views.logout, name='logout'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)