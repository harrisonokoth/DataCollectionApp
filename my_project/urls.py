from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from data_preprocessing import views  # Import the view from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Map root URL to home view
    path('data_preprocessing/', include('data_preprocessing.urls')),
    path('model_training/', include('model_training.urls')),
    path('rag_system/', include('rag_system.urls')),
    path('llm_integration/', include('llm_integration.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
