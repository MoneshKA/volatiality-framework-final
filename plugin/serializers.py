from rest_framework import serializers
from .models import MemoryDump, PluginAnalysis

class MemoryDumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryDump
        fields = ['id', 'file', 'uploaded_at']

class PluginAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = PluginAnalysis
        fields = ['id',  'plugin_name', 'analysis_result', 'status', 'started_at', 'completed_at']
