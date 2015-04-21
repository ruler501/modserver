from django.conf.urls import url, include
from mods import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'mods', views.ModViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^users/register', views.CreateUserView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
