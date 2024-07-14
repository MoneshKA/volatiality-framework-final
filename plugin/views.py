from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import PluginUploadForm, MemoryDumpUploadForm
from .models import PluginAnalysis, MemoryDump
import os
import zipfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            form = SignUpForm(request.POST)
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)
def landing_page(request):
    return render(request, 'landing.html')

def base(request):
    return render(request, 'base.html')
def login_user(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('landing')
        else:
            messages.warning(request, "Username or Password is incorrect !!")
            return redirect('login')
    else:
        return render(request, 'login.html')
    # return render(request,'login.html', {})
def upload_memory_dump(request):
    if request.method == 'POST':
        form = MemoryDumpUploadForm(request.POST, request.FILES)
        if form.is_valid():
            memory_dump = form.save()
            return JsonResponse({'status': 'success', 'fileId': memory_dump.id})
    else:
        form = MemoryDumpUploadForm()
    return render(request, 'upload_memory_dump.html', {'form': form})

def start_memory_analysis(request):
    if request.method == 'POST':
        file_id = request.POST.get('fileId')
        plugin_name = request.POST.get('plugin')
        memory_dump = get_object_or_404(MemoryDump, id=file_id)

        plugin_analysis = PluginAnalysis.objects.create(
            memory_dump=memory_dump,
            plugin_name=plugin_name,
            status='pending'
        )

        plugin_path = plugin_analysis.plugin_folder.path

        # Unzip the plugin folder if necessary
        if zipfile.is_zipfile(plugin_path):
            with zipfile.ZipFile(plugin_path, 'r') as zip_ref:
                extract_path = os.path.splitext(plugin_path)[0]
                zip_ref.extractall(extract_path)
                plugin_path = extract_path

        # Analyze the plugin
        analysis_result = analyze_plugin(plugin_path, memory_dump.file.path)
        plugin_analysis.analysis_result = analysis_result
        plugin_analysis.status = 'completed'
        plugin_analysis.save()

        return JsonResponse({'status': 'analysis_started', 'analysisId': plugin_analysis.id})

def analyze_plugin(plugin_path, memory_dump_path):
    # Dummy function to simulate analysis
    return f"Analysis of plugin at {plugin_path} with memory dump at {memory_dump_path}"

def get_analysis_status(request, analysis_id):
    plugin_analysis = get_object_or_404(PluginAnalysis, id=analysis_id)
    return JsonResponse({'status': plugin_analysis.status})

def get_analysis_results(request, analysis_id):
    plugin_analysis = get_object_or_404(PluginAnalysis, id=analysis_id)
    return JsonResponse({'status': 'success', 'results': plugin_analysis.analysis_result})

def list_historical_analyses(request):
    analyses = PluginAnalysis.objects.all()
    analysis_list = [{
        'analysisId': analysis.id,
        'date': analysis.created_at,
        'plugin': analysis.plugin_name,
    } for analysis in analyses]
    return JsonResponse({'analyses': analysis_list})

def upload_plugin(request):
    if request.method == 'POST':
        form = PluginUploadForm(request.POST, request.FILES)
        if form.is_valid():
            plugin_analysis = form.save()
            plugin_path = plugin_analysis.plugin_folder.path

            # Unzip the plugin folder if necessary
            if zipfile.is_zipfile(plugin_path):
                with zipfile.ZipFile(plugin_path, 'r') as zip_ref:
                    extract_path = os.path.splitext(plugin_path)[0]
                    zip_ref.extractall(extract_path)
                    plugin_path = extract_path

            # Analyze the plugin
            analysis_result = analyze_plugin(plugin_path)
            plugin_analysis.analysis_result = analysis_result
            plugin_analysis.status = 'completed'
            plugin_analysis.save()

            return redirect('plugin_analysis_result', pk=plugin_analysis.pk)
    else:
        form = PluginUploadForm()
    return render(request, 'upload.html', {'form': form})

# plugin/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, CustomLoginForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('landing')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('protected')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def protected_view(request):
    return render(request, 'protected.html')

def logout_view(request):
    logout(request)
    return redirect('login')
