from django import forms
from .models import EquipmentData, FrontConveyorData, RearConveyorData, TemperingData,WashingData,PreheatingData,ConveyorData,FurnaceData,FrontdoorData

# A form using `forms.Form` to allow more customized input handling
class EquipmentForm(forms.Form):
    EQUIPMENT_CHOICES = [
        ('washing_80', 'Washing Equipment 80'),
        ('washing_100', 'Washing Equipment 100'),
        ('washing_120', 'Washing Equipment 120'),
        ('furnace_80', 'Furnace Equipment 80'),
        ('furnace_100', 'Furnace Equipment 100'),
        ('furnace_120', 'Furnace Equipment 120'),
        ('tempering_80', 'Tempering Equipment 80'),
        ('tempering_100', 'Tempering Equipment 100'),
        ('tempering_120', 'Tempering Equipment 120'),
    ]

    MODEL_CHOICES = [
        ('model_a', 'Model A'),
        ('model_b', 'Model B'),
        ('model_c', 'Model C'),
    ]

    bom = forms.ChoiceField(choices=EQUIPMENT_CHOICES, required=True)
    model = forms.ChoiceField(choices=MODEL_CHOICES, required=True)
    components = forms.MultipleChoiceField(choices=[
        ('component_1', 'Component 1'),
        ('component_2', 'Component 2'),
        ('component_3', 'Component 3'),
    ], required=False)

# A form using `forms.ModelForm` for a simple model-based form

class EquipmentDataForm(forms.Form):
    # Tempering
    tempering_80 = forms.CharField(label='Tempering 80', max_length=100, required=False)
    tempering_100 = forms.CharField(label='Tempering 100', max_length=100, required=False)
    tempering_120 = forms.CharField(label='Tempering 120', max_length=100, required=False)

    # Washing
    washing_80 = forms.CharField(label='Washing 80', max_length=100, required=False)
    washing_100 = forms.CharField(label='Washing 100', max_length=100, required=False)
    washing_120 = forms.CharField(label='Washing 120', max_length=100, required=False)

    # Conveyor
    conveyor_80 = forms.CharField(label='Conveyor 80', max_length=100, required=False)
    conveyor_100 = forms.CharField(label='Conveyor 100', max_length=100, required=False)
    conveyor_120 = forms.CharField(label='Conveyor 120', max_length=100, required=False)

    # Preheating
    preheating_80 = forms.CharField(label='Preheating 80', max_length=100, required=False)
    preheating_100 = forms.CharField(label='Preheating 100', max_length=100, required=False)
    preheating_120 = forms.CharField(label='Preheating 120', max_length=100, required=False)

    # Front Door
    frontdoor_80 = forms.CharField(label='Front Door 80', max_length=100, required=False)
    frontdoor_100 = forms.CharField(label='Front Door 100', max_length=100, required=False)
    frontdoor_120 = forms.CharField(label='Front Door 120', max_length=100, required=False)

    # Tank
    tank_80 = forms.CharField(label='Tank 80', max_length=100, required=False)
    tank_100 = forms.CharField(label='Tank 100', max_length=100, required=False)
    tank_120 = forms.CharField(label='Tank 120', max_length=100, required=False)

    # Rear Conveyor
    rear_conveyor_80 = forms.CharField(label='Rear Conveyor 80', max_length=100, required=False)
    rear_conveyor_100 = forms.CharField(label='Rear Conveyor 100', max_length=100, required=False)
    rear_conveyor_120 = forms.CharField(label='Rear Conveyor 120', max_length=100, required=False)

    # Newly Making
    newly_making_80 = forms.CharField(label='Newly Making 80', max_length=100, required=False)
    newly_making_100 = forms.CharField(label='Newly Making 100', max_length=100, required=False)
    newly_making_120 = forms.CharField(label='Newly Making 120', max_length=100, required=False)

       
# Another model form example
class AddDataForm(forms.ModelForm):
    class Meta:
        model = EquipmentData
        fields = ['bom', 'components', 'model', 'specification', 'make', 'purpose', 'quality', 'price', 'total']
        widgets = {
            'components': forms.CheckboxSelectMultiple(),
            # Add other widgets if needed
        }


class TemperingForm(forms.ModelForm):
    class Meta:
        model = TemperingData
        fields = ['bom','model','specification', 'make', 'purpose', 'quality', 'price', 'total']
class WashingForm(forms.ModelForm):
    class Meta:
        model = WashingData
        fields = ['type','model','specification', 'make', 'purpose', 'quality', 'price', 'total']
class PreheatingForm(forms.ModelForm):
    class Meta:
        model = PreheatingData
        fields = ['type','model','specification', 'make', 'purpose', 'quality', 'price', 'total']
class FurnaceForm(forms.ModelForm):
    class Meta:
        model = FurnaceData
        fields = ['type','model','specification', 'make', 'purpose', 'quality', 'price', 'total']
class ConveyorForm(forms.ModelForm):
    class Meta:
        model = ConveyorData
        fields = ['type','model','specification', 'make', 'purpose', 'quality', 'price', 'total']
class FrontdoorForm(forms.ModelForm):
    class Meta:
        model = FrontdoorData
        fields = ['type','model','specification', 'make', 'purpose', 'quality', 'price', 'total']
class FrontConveyorForm(forms.ModelForm):
    class Meta:
        model = FrontConveyorData
        fields = ['type', 'model', 'specification', 'make', 'purpose', 'quality', 'price', 'total']

class RearConveyorForm(forms.ModelForm):
    class Meta:
        model = RearConveyorData
        fields = ['type', 'model', 'specification', 'make', 'purpose', 'quality', 'price', 'total']

# forms.py


class EquipmentFilterForm(forms.Form):
    BOM_CHOICES = [
        ('tempering', 'Tempering'),
        ('washing', 'Washing'),
        ('preheating', 'Preheating'),
        ('conveyor', 'Conveyor'),
        ('furnace', 'Furnace'),
        ('frontdoor', 'Front Door'),
        ('rearconveyor', 'Rear Conveyor'),
        ('frontconveyor', 'Front Conveyor'),

    ]
    
    MODEL_CHOICES = [
        ('model_a', 'Model A'),
        ('model_b', 'Model B'),
        ('model_c', 'Model C'),
    ]
    
    bom = forms.ChoiceField(choices=BOM_CHOICES, required=True)
    model = forms.ChoiceField(choices=MODEL_CHOICES, required=True)