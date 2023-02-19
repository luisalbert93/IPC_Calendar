from django.views.generic import ListView
from calendarapp.models import Event

class AllEventsListView(ListView):
    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_all_events(user=self.request.user)
