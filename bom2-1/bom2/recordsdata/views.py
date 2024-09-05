
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from .models import (
    FrontConveyorData, RearConveyorData, TemperingData, WashingData, PreheatingData, ConveyorData, FurnaceData, FrontdoorData
)

from .forms import (
    EquipmentDataForm, 
    AddDataForm,
    FrontConveyorForm,
    RearConveyorForm, 
    TemperingForm, 
    WashingForm, 
    PreheatingForm, 
    ConveyorForm, 
    FurnaceForm, 
    FrontdoorForm
)
from django.http import JsonResponse
from django.shortcuts import render
from .models import FurnaceData, RearConveyorData
import json

def get_equipment_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        bom = data.get('bom')
        model = data.get('model')
        
        # Query the database based on BOM and model
        equipment_data = TemperingData.objects.filter(bom=bom, model=model)
        
        # Prepare data for response
        data_to_display = list(equipment_data.values())
        
        # Generate HTML content to be inserted
        html = render_to_string('equipment_data.html', {'data_to_display': data_to_display})
        
        return JsonResponse({'html': html})
    return JsonResponse({'error': 'Invalid request'}, status=400)

# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .forms import (
    TemperingForm, WashingForm, PreheatingForm, ConveyorForm,
    FurnaceForm, FrontdoorForm, RearConveyorForm, FrontConveyorForm
)
from .models import EquipmentData

def equipment_form_view(request, equipment_type):
    form_class = {
        'tempering': TemperingForm,
        'washing': WashingForm,
        'preheating': PreheatingForm,
        'conveyor': ConveyorForm,
        'furnace': FurnaceForm,
        'front_door': FrontdoorForm,
        'rearconveyor': RearConveyorForm,
        'frontconveyor': FrontConveyorForm
    }.get(equipment_type.lower())

    if not form_class:
        return HttpResponseNotFound("Equipment type not found")

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = form_class()

    return render(request, 'equipment_form.html', {
        'form': form,
        'form_title': f'{equipment_type.replace("_", " ").capitalize()} Equipment Data Form',
    })
    
def add_data_view(request):
    if request.method == 'POST':
        form = EquipmentDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Ensure 'success_page' is a valid URL name
    else:
        form = EquipmentDataForm()

    return render(request, 'add_data.html', {'form': form})

def home(request):
    equipment_choices = [
        ('washing_80', 'Washing Equipment 80'),
        ('washing_100', 'Washing Equipment 100'),
        ('washing_120', 'Washing Equipment 120'),
        ('furnace_80', 'Furnace Equipment 80'),
        ('furnace_100', 'Furnace Equipment 100'),
        ('furnace_120', 'Furnace Equipment 120'),
        ('tempering_80', 'Tempering Equipment 80'),
        ('tempering_100', 'Tempering Equipment 100'),
        ('tempering_120', 'Tempering Equipment 120'),
        ('conveyor_80', 'Conveyor Equipment 80'),
        ('conveyor_100', 'Conveyor Equipment 100'),
        ('conveyor_120', 'Conveyor Equipment 120'),
        ('front_door_80', 'Front Door Equipment 80'),
        ('front_door_100', 'Front Door Equipment 100'),
        ('front_door_120', 'Front Door Equipment 120'),
        ('rear_door_80', 'Rear Door Equipment 80'),
        ('rear_door_100', 'Rear Door Equipment 100'),
        ('rear_door_120', 'Rear Door Equipment 120'),
        ('double_door_80', 'Double Door Equipment 80'),
        ('double_door_100', 'Double Door Equipment 100'),
        ('double_door_120', 'Double Door Equipment 120'),
    ]

    model_choices = [
        ('model_a', 'Model A'),
        ('model_b', 'Model B'),
        ('model_c', 'Model C'),
    ]

    data_to_display = []

    if request.method == 'POST':
        bom = request.POST.get('bom')
        model = request.POST.get('model')
        if bom and model:
            data_to_display = EquipmentData.objects.filter(bom=bom, model=model)

    context = {
        'equipment_choices': equipment_choices,
        'model_choices': model_choices,
        'data_to_display': data_to_display,
    }

    return render(request, 'home.html', context)  # Ensure the render statement is executed


def success_view(request):
    return render(request, 'success.html')

def add_data(request):
    if request.method == 'POST':
        form = AddDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Ensure 'home' is a valid URL name
    else:
        form = AddDataForm()
    
    return render(request, 'add_data.html', {'form': form})

def fetch_equipment_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            bom = data.get('bom')
            model = data.get('model')

            # Fetch data from the database based on BOM and model
            equipment_data = EquipmentData.objects.filter(bom=bom, model=model)

            context = {
                'data_to_display': equipment_data,
            }

            html = render_to_string('equipment_data.html', context)
            return JsonResponse({'html': html})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)


def filter_data(request):
    equipment_choices = [
        ('tempering_80', 'Tempering Equipment 80'),
        ('tempering_100', 'Tempering Equipment 100'),
        ('tempering_120', 'Tempering Equipment 120'),
        ('washing_80', 'Washing Equipment 80'),
        ('washing_100', 'Washing Equipment 100'),
        ('washing_120', 'Washing Equipment 120'),
        ('preheating_80', 'Preheating Equipment 80'),
        ('preheating_100', 'Preheating Equipment 100'),
        ('preheating_120', 'Preheating Equipment 120'),
        ('conveyor_80', 'Conveyor Equipment 80'),
        ('conveyor_100', 'Conveyor Equipment 100'),
        ('conveyor_120', 'Conveyor Equipment 120'),
        ('furnace_80', 'Furnace Equipment 80'),
        ('furnace_100', 'Furnace Equipment 100'),
        ('furnace_120', 'Furnace Equipment 120'),
        ('front_door_80', 'Front Door Equipment 80'),
        ('front_door_100', 'Front Door Equipment 100'),
        ('front_door_120', 'Front Door Equipment 120'),
    ]

    model_choices = [
        ('model_a', 'Model A'),
        ('model_b', 'Model B'),
        ('model_c', 'Model C'),
    ]

  
    if request.method == 'POST':
        selected_bom = request.POST.get('bom')
        selected_model = request.POST.get('model')
        
        if selected_bom and selected_model:
            # Extract model type from BOM
            model_name = selected_bom.split('_')[0]
            model_class = {
                'tempering': TemperingData,
                'washing': WashingData,
                'preheating': PreheatingData,
                'conveyor': ConveyorData,
                'furnace': FurnaceData,
                'front_door': FrontdoorData,
                'rearconveyor': RearConveyorData,
                'frontconveyor': FrontConveyorData,
            }.get(model_name)

            if model_class:
                filtered_data = model_class.objects.filter(type=selected_bom.split('_')[1], model=selected_model)
            else:
                filtered_data = []
        else:
            filtered_data = []
    else:
        filtered_data = []

    return render(request, 'equipment_form.html', {
        'equipment_choices': equipment_choices,
        'model_choices': model_choices,
        'filtered_data': filtered_data
    })

def get_furnace_data(request):
    if request.method == 'GET':
        furnace_type = request.GET.get('type', None)

        if furnace_type:
            if furnace_type not in dict(FurnaceData.TYPE_CHOICES).keys():
                return JsonResponse({'error': 'Invalid type value'}, status=400)
            
            furnace_entries = FurnaceData.objects.filter(type=furnace_type)
        else:
            #furnace_entries = FurnaceData.objects.all()
            furnace_entries = FurnaceData.objects.filter(type=furnace_type)
        data = list(furnace_entries.values())
        return JsonResponse(data, safe=False)
    
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
def get_front_conveyor_data(request):
    if request.method == 'GET':
        front_conveyor_data = request.GET.get('type', None)

        if front_conveyor_data:
            if front_conveyor_data not in dict(FurnaceData.TYPE_CHOICES).keys():
                return JsonResponse({'error': 'Invalid type value'}, status=400)
            
            front_conveyor_entries = FrontConveyorData.objects.filter(type=front_conveyor_data)
        else:
            #furnace_entries = FurnaceData.objects.all()
            front_conveyor_entries = FrontConveyorData.objects.filter(type=front_conveyor_data)
        data = list(front_conveyor_entries.values())
        return JsonResponse(data, safe=False)
    
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
def get_rear_conveyor_data(request):
    if request.method == 'GET':
        rear_conveyor_data = request.GET.get('type', None)

        if rear_conveyor_data:
            if rear_conveyor_data not in dict(RearConveyorData.TYPE_CHOICES).keys():
                return JsonResponse({'error': 'Invalid type value'}, status=400)
            
            rear_conveyor_entries =RearConveyorData.objects.filter(type=rear_conveyor_data)
        else:
            #furnace_entries = FurnaceData.objects.all()
            rear_conveyor_entries = RearConveyorData.objects.filter(type=rear_conveyor_data)
        data = list(rear_conveyor_entries.values())
        return JsonResponse(data, safe=False)
    
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)