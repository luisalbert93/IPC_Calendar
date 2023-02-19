from django.urls import path

from . import views

app_name = "calendarapp"

urlpatterns = [
    path("calendar/", views.CalendarViewNew.as_view(), name="calendar"),
    path("event/new/", views.create_event, name="event_new"),
    path("all-event-list/", views.AllEventsListView.as_view(), name="all_events"),
    # path("event/<int:id>/remove/", views.remove_event, name="event_remove")
    path("event/remove/", views.remove_event, name="event_remove")
]