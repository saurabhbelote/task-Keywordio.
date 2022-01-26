from django.contrib import admin
from django.urls import path
from books.views import BooksList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',BooksList.as_view(), name = 'Books' ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.index_title = "Books library"
admin.site.site_header = "Books library"
admin.site.site_title = "Books library"