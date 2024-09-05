from django import forms
from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class EquipmentData(models.Model):
    # Choices for equipment BOM
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
        ('conveyor_80', 'Conveyor Equipment 80'),
        ('conveyor_100', 'Conveyor Equipment 100'),
        ('conveyor_120', 'Conveyor Equipment 120'),
    ]
    
    # Choices for models
    MODEL_CHOICES = [
        ('model_a', 'Model A'),
        ('model_b', 'Model B'),
        ('model_c', 'Model C'),
    ]

    # Fields for the model
    bom = models.CharField(max_length=20, choices=EQUIPMENT_CHOICES, verbose_name='Equipment BOM')
    model = models.CharField(max_length=20, choices=MODEL_CHOICES, verbose_name='Model')
    components = models.JSONField(verbose_name='Components')  # Storing a list of selected components
    specification = models.TextField(verbose_name='Specification')
    make = models.CharField(max_length=100, verbose_name='Make')
    purpose = models.CharField(max_length=100, verbose_name='Purpose')
    quality = models.CharField(max_length=100, verbose_name='Quality')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total')

    def __str__(self):
        return f'{self.bom} - {self.model}'
class EquipmentDataForm(forms.ModelForm):
    class Meta:
        model = EquipmentData
        fields = '__all__'  # or list the fields you want to include

class TemperingData(models.Model):
    TYPE_CHOICES = [
        ('tempering_80', 'Tempering Equipment 80'),
        ('tempering_100', 'Tempering Equipment 100'),
        ('tempering_120', 'Tempering Equipment 120'),
    ]
    MODEL_CHOICES = [
        ('model_a', 'Model A'),
        ('model_b', 'Model B'),
        ('model_c', 'Model C'),
    ]

    bom = models.CharField(max_length=100, choices=TYPE_CHOICES)
    model=models.CharField(max_length=100, choices=MODEL_CHOICES)
    specification = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as necessary

    def __str__(self):
        return f"Tempering {self.bom}"
    
# models.py
class WashingData(models.Model):
    TYPE_CHOICES = [
        ('80', '80'),
        ('100', '100'),
        ('120', '120'),
    ]
    MODEL_CHOICES = [
        ('model_a', 'Model A'),
        ('model_b', 'Model B'),
        ('model_c', 'Model C'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    model = models.CharField(max_length=10, choices=MODEL_CHOICES)
    specification = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Washing {self.type}"
# models.py
class PreheatingData(models.Model):
    TYPE_CHOICES = [
        ('80', '80'),
        ('100', '100'),
        ('120', '120'),
    ]
    MODEL_CHOICES = [
        ('model_a', 'Model A'),
        ('model_b', 'Model B'),
        ('model_c', 'Model C'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    model = models.CharField(max_length=10, choices=MODEL_CHOICES)
    specification = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Preheating {self.type}"
# models.py
class ConveyorData(models.Model):
    TYPE_CHOICES = [
        ('80', '80'),
        ('100', '100'),
        ('120', '120'),
    ]
    MODEL_CHOICES = [
        ('model_a', 'Model A'),
        ('model_b', 'Model B'),
        ('model_c', 'Model C'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    model = models.CharField(max_length=10, choices=MODEL_CHOICES)
    specification = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Conveyor {self.type}"
# models.py
class FurnaceData(models.Model):
    TYPE_CHOICES = [
        ('80', '80'),
        ('100', '100'),
        ('120', '120'),
    ]
    MODEL_CHOICES = [
        ('model_a', 'Model A'),
        ('model_b', 'Model B'),
        ('model_c', 'Model C'),
    ]

    type= models.CharField(max_length=10, choices=TYPE_CHOICES)
    model = models.CharField(max_length=10, choices=MODEL_CHOICES)
    specification = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Furnace {self.type}"
class FrontdoorData(models.Model):
    TYPE_CHOICES = [
        ('80', '80'),
        ('100', '100'),
        ('120', '120'),
    ]
    MODEL_CHOICES = [
        ('model_a', 'Model A'),
        ('model_b', 'Model B'),
        ('model_c', 'Model C'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    model = models.CharField(max_length=10, choices=MODEL_CHOICES)
    specification = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Frontdoor {self.type}"
class FrontConveyorData(models.Model):
    TYPE_CHOICES = [
        ('80', '80'),
        ('100', '100'),
        ('120', '120'),
    ]
    MODEL_CHOICES = [
        ('model_a', 'Model A'),
        ('model_b', 'Model B'),
        ('model_c', 'Model C'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    model = models.CharField(max_length=10, choices=MODEL_CHOICES)
    specification = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Frontconveyor {self.type}"
class RearConveyorData(models.Model):
    TYPE_CHOICES = [
        ('80', '80'),
        ('100', '100'),
        ('120', '120'),
    ]
    MODEL_CHOICES = [
        ('model_a', 'Model A'),
        ('model_b', 'Model B'),
        ('model_c', 'Model C'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    model = models.CharField(max_length=10, choices=MODEL_CHOICES)
    specification = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
       return f"Rear Conveyor {self.type}"