from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import contactPage
from .views import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='home_page'),
    path('contact/', contactPage, name='contact_page'),
    path('property/', include('property.urls')),
    path('user/', include('users.urls')),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='squarefeet/home.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
