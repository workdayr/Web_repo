from rest_framework import serializers
from Web_repo.models.stats import *

class UserRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRecord
        fields = '__all__'

class NotificationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationLog
        fields = '__all__'
        
class RedirectAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedirectAnalytics
        fields = '__all__'
