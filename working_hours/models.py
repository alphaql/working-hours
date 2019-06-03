# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from users.models import User


class WorkingHour(models.Model):
    date = models.DateField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(blank=False, null=False)
    end_time = models.DateTimeField(blank=False, null=False)
    mandatory_hours = models.PositiveIntegerField(default=8, null=False)
    lunch_hours = models.FloatField(default=1)
    holiday = models.BooleanField(default=False)
    festive = models.BooleanField(default=False)

    class Meta:
        unique_together = [['user', 'date']]

    @property
    def worked_hours(self):
        res = round(((self.end_time -
                      self.start_time).total_seconds()) / 3600,
                    2) - self.lunch_hours
        return res

    @property
    def extra(self):
        res = self.worked_hours - self.mandatory_hours
        return round(res, 2)

    @property
    def week_number(self):
        return int(self.date.isocalendar()[1])

    @staticmethod
    def total_worked_hours_in_week(week):
        days_in_week = WorkingHour.objects.filter(date__week=week)

        sum = 0

        for one_day in days_in_week:
            sum += one_day.worked_hours

        return sum

    @staticmethod
    def total_mandatory_hours_in_week(week):
        days_in_week = WorkingHour.objects.filter(date__week=week)

        sum = 0

        for one_day in days_in_week:
            sum += one_day.mandatory_hours

        return sum

    @staticmethod
    def total_extra_hours_in_week(week):
        days_in_week = WorkingHour.objects.filter(date__week=week)

        sum = 0

        for one_day in days_in_week:
            sum += one_day.extra

        return sum

    def __repr__(self):
        return '{user}: {date} {start_time} - {end_time}'.format(
            user=self.user,
            date=self.date,
            start_time=self.start_time,
            end_time=self.end_time,
        )

    def __str__(self):
        return '{user}: {date} {start_time} - {end_time}'.format(
            user=self.user,
            date=self.date,
            start_time=self.start_time,
            end_time=self.end_time,
        )
