from rest_framework import (
    viewsets,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v0.serializers.working_hours import (
    WorkingHourSerializer,
    WorkingHourWeekSerializer,
)
from working_hours.models import WorkingHour


class WorkingHoursViewSet(viewsets.ModelViewSet):
    http_method_names = ['options', 'patch', 'put', 'get', 'post']
    resource_name = 'working_hours'
    serializer_class = WorkingHourSerializer
    permission_classes = (IsAuthenticated,)
    queryset = WorkingHour.objects.all().order_by("-date")


class WorkingHoursWeekViewSet(viewsets.ModelViewSet):
    http_method_names = ['options', 'get', ]
    resource_name = 'working_hours_week'
    serializer_class = WorkingHourWeekSerializer
    permission_classes = (IsAuthenticated,)
    week = None

    def list(self, request, *args, **kwargs):
        total_worked_hours_in_week = round(
            WorkingHour.total_worked_hours_in_week(kwargs["week"],
                                                   kwargs["year"],
                                                   kwargs["username"],
                                                   ))
        total_extra_hours_in_week = round(
            WorkingHour.total_extra_hours_in_week(
                kwargs["week"],
                kwargs["year"],
                kwargs["username"]), 2)
        total_mandatory_hours_in_week = round(
            WorkingHour.total_mandatory_hours_in_week(
                kwargs["week"],
                kwargs["year"],
                kwargs["username"]), 2)
        first_date_from_week = WorkingHour.first_date_from_week(
            kwargs['week'],
            kwargs["year"])
        end_date_from_week = WorkingHour.end_date_from_week(
            kwargs['week'],
            kwargs["year"])

        data = {
            'first_date_from_week': first_date_from_week,
            'end_date_from_week': end_date_from_week,
            'total_worked_hours_in_week': total_worked_hours_in_week,
            'total_extra_hours_in_week': total_extra_hours_in_week,
            'total_mandatory_hours_in_week': total_mandatory_hours_in_week,
        }

        serializer = WorkingHourWeekSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)
