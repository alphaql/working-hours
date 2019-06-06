from rest_framework import serializers

from working_hours.models import WorkingHour


class WorkingHourSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        return WorkingHour.objects.create(**validated_data)

    class Meta:
        model = WorkingHour
        fields = ('date',
                  'user',
                  'start_time',
                  'end_time',
                  'mandatory_hours',
                  'lunch_hours',
                  'festive',
                  'holiday',
                  'worked_hours',
                  'extra',
                  )


class WorkingHourWeekSerializer(serializers.Serializer):
    first_date_from_week = serializers.DateField()
    end_date_from_week = serializers.DateField()
    total_worked_hours_in_week = serializers.FloatField()
    total_extra_hours_in_week = serializers.FloatField()
    total_mandatory_hours_in_week = serializers.FloatField()
