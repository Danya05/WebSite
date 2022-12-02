from django.urls import path
from . import views

urlpatterns = [
    path('', views.parser_home, name="parser_home"),
    path('create', views.create, name="create"),
    path('<int:pk>', views.CoinsDetailView.as_view(), name='coins-detail'),
    path('<int:pk>/update', views.CoinsUpdateView.as_view(), name='coins-update'),
    path('<int:pk>/delete', views.CoinsDeleteView.as_view(), name='coins-delete'),
    path('<int:pk>/parse', views.CoinsUpdateView.as_view(), name='coins-parse')
]
