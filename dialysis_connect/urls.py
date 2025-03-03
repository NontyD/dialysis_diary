from django.conf import settings  
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf.urls import handler404, handler500, handler403
from .views import custom_404, custom_500, custom_403
from django.shortcuts import render


def custom_404(request, exception):
    return render(request, "404.html", status=404)


def custom_500(request):
    return render(request, "500.html", status=500)


def custom_403(request):
    return render(request, "403.html", status=403)


handler404 = 'dialysis_connect.views.custom_404'
handler500 = 'dialysis_connect.views.custom_500'
handler403 = 'dialysis_connect.views.custom_403'


urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('community/', include('community.urls')),
    path('records/', include('records.urls')),
    path('calendar/', include('calendar_app.urls')),
    path("uploads/", include("uploads.urls", namespace="uploads")),
    path('logout/', LogoutView.as_view(next_page='landing_page'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
