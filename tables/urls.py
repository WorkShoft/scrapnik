from django.urls import path

from .views import TableListView

urlpatterns = [
    path('', TableListView.as_view(), name='table-list'),
]
