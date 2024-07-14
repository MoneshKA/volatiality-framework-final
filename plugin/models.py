# from django.db import models

# # Create your models here.


# class MemoryDump(models.Model):
#     file = models.FileField(upload_to='memory_dumps/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.file.name

# # class PluginAnalysis(models.Model):
# #     memory_dump = models.ForeignKey(MemoryDump, on_delete=models.CASCADE)
# #     plugin_name = models.CharField(max_length=100)
# #     analysis_result = models.TextField(blank=True, null=True)
# #     status = models.CharField(max_length=50, default='in_progress')
# #     started_at = models.DateTimeField(auto_now_add=True)
# #     completed_at = models.DateTimeField(blank=True, null=True)

# #     def __str__(self):
# #         return f"{self.plugin_name} - {self.memory_dump.file.name}"





# class PluginAnalysis(models.Model):
#     plugin_name = models.CharField(max_length=255, default='default_plugin_name')  # Add this line if plugin_name is required
#     plugin_folder = models.FileField(upload_to='plugins/')
#     analysis_result = models.TextField(blank=True, null=True)
#     status = models.CharField(max_length=20, default='pending')
#     created_at = models.DateTimeField(auto_now_add=True)
#     completed_at = models.DateTimeField(blank=True, null=True)
    
#     def __str__(self):
#         return self.plugin_folder.name





from django.db import models

class MemoryDump(models.Model):
    file = models.FileField(upload_to='memory_dumps/')
    created_at = models.DateTimeField(auto_now_add=True)


class PluginAnalysis(models.Model):
    memory_dump = models.ForeignKey(MemoryDump, on_delete=models.CASCADE, related_name='analyses',null=True)
    plugin_name = models.CharField(max_length=255, blank=True, null=True)
    plugin_folder = models.FileField(upload_to='plugins/')
    analysis_result = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.plugin_name} - {self.plugin_folder.name}"