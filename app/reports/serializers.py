from rest_framework import serializers
from .models import Report, ReportInfo

class ReportSerializer(serializers.ModelSerializer):
    parameter_info = serializers.StringRelatedField(many=True)

    class Meta:
        model = Report
        fields = ('id', 'user', 'report_type', 'date_added', 'parameter_info', 'ocr_data')
        # extra_kwargs = {
        #     'user': {'read_only': True}
        # }

class ReportInfoSerializer(serializers.ModelSerializer):
    # parameter = serializers.CharField()
    # value = serializers.IntegerField()
    # upper_limit = serializers.IntegerField()
    # lower_limit = serializers.IntegerField()

    class Meta:
        model = ReportInfo
        fields = ('id', 'report', 'parameter', 'value', 'upper_limit', 'lower_limit')