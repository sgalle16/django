from django.urls import path
from .views import NewsView

app_name = "news"

urlpatterns = [
    path('', NewsView.as_view(), name="news"),
]
