from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data_preprocessing/', include('data_preprocessing.urls')),
    path('model_training/', include('model_training.urls')),
    path('rag_system/', include('rag_system.urls')),
    path('llm_integration/', include('llm_integration.urls')),
]
