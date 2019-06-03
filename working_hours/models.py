# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from users.models import User


class WorkingHour   (models.Model):
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
