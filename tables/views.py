from django.shortcuts import render
from django.views.generic.list import ListView

from django.utils import timezone

from .models import Table

class TableListView(ListView):
    model = Table
    #paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
