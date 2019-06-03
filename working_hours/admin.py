from django.contrib import admin
from working_hours.models import WorkingHour

class WHAdmin(admin.ModelAdmin):
    list_display = ('username',
                    'week_day',
                    'start_time',
                    'end_time',
                    'holiday',
                    'festive',
                    'mandatory_hours',
                    'lunch_hours',
                    'worked_hours',
                    'extra',
                    )
    ordering = ('date',)

    def username(self, obj):
        return obj.user.username.upper()

    def worked_hours(self, obj):
        res = round(((obj.end_time -
                      obj.start_time).total_seconds()) / 3600,
                    2) - obj.lunch_hours
        return res

    def week_day(self, obj):
        return obj.start_time.strftime("%A")

    def extra(self, obj):
        res = self.worked_hours(obj) - obj.mandatory_hours
        return round(res, 2)


admin.site.register(WorkingHour, WHAdmin)
