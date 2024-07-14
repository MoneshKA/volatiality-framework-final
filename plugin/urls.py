# # # from django.urls import path, include
# # # from rest_framework.routers import DefaultRouter
# # # from .views import MemoryDumpViewSet, PluginAnalysisViewSet

# # # router = DefaultRouter()
# # # router.register(r'memory-dump', MemoryDumpViewSet, basename='memory-dump')
# # # router.register(r'analysis', PluginAnalysisViewSet, basename='analysis')

# # # urlpatterns = [
# # #     path('api/', include(router.urls)),
# # # ]
# # from django.urls import path, include
# # from rest_framework.routers import DefaultRouter
# # from .views import MemoryDumpViewSet, PluginAnalysisViewSet, landing_page

# # router = DefaultRouter()
# # router.register(r'memory-dump', MemoryDumpViewSet, basename='memory-dump')
# # router.register(r'analysis', PluginAnalysisViewSet, basename='analysis')

# # urlpatterns = [
# #     path('', landing_page, name='landing_page'),
# #     path('api/', include(router.urls)),
# # ]
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import MemoryDumpViewSet, PluginAnalysisViewSet, upload_plugin, plugin_analysis_result, landing_page

# router = DefaultRouter()
# router.register(r'memory-dump', MemoryDumpViewSet, basename='memory-dump')
# router.register(r'analysis', PluginAnalysisViewSet, basename='analysis')

# urlpatterns = [
#     path('', landing_page, name='landing_page'),
#     path('upload/', upload_plugin, name='upload_plugin'),
#     path('result/<int:pk>/', plugin_analysis_result, name='plugin_analysis_result'),
#     path('api/', include(router.urls)),
# ]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.landing_page, name='landing_page'),
#     path('upload/', views.upload_plugin, name='upload_plugin'),
#     path('result/<int:pk>/', views.plugin_analysis_result, name='plugin_analysis_result'),
# ]
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('protected/', views.protected_view, name='protected'),
    path('register/', views.register_user, name='register'),
    path('login',views.login_user,name="login"),
    path('landing', views.landing_page, name='landing'),
    path('home',views.base,name='home'),
    path('upload_memory_dump/', views.upload_memory_dump, name='upload_memory_dump'),
    path('start_analysis/', views.start_memory_analysis, name='start_memory_analysis'),
    path('analysis/<int:analysis_id>/status/', views.get_analysis_status, name='get_analysis_status'),
    path('analysis/<int:analysis_id>/results/', views.get_analysis_results, name='get_analysis_results'),
    path('analyses/', views.list_historical_analyses, name='list_historical_analyses'),
    path('upload/', views.upload_plugin, name='upload_plugin'),
    # path('result/<int:pk>/', views.plugin_analysis_result, name='plugin_analysis_result'),
]
