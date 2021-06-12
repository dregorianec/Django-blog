from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page),
    path('post/<int:post_id>', views.post_page),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)