from django.test import TestCase

from models import EquipmentData

# Create your tests here.
all_data = EquipmentData.objects.all()
print(all_data)

# Example of filtering with specific BOM and model
bom = 'washing_80'
model = 'model_a'
filtered_data = EquipmentData.objects.filter(bom=bom, model=model)
print(filtered_data)