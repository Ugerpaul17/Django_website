from django.conf.urls import include, url
from django.contrib import admin
from my_personal_app import urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'paul_website.views.home', name='home'),
     url(r'', include('my_personal_app.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
