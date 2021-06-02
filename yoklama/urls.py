from django.urls import path

from yoklama import views
from yoklama.views import YoklamaView

urlpatterns = [
    path('yoklama/', YoklamaView.as_view(), name='yoklama'),
]
