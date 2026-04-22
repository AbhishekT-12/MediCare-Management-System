from django.urls import path
from learnapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.registration,name='register'),
    path('login/',views.user_login,name='login'),
    path('home',views.home,name='home'),
    path('labtechreg/', views.labtechreg, name='labtechreg'),
    path('logout',views.user_logout,name="logout"),
    path('profile',views.profile,name='profile'),
    path('update',views.update,name='update')
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)