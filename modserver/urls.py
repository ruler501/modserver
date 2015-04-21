from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'modserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('snippets.urls')),
]
