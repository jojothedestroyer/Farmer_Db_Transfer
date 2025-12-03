from import_export import resources
from .models import fullform
from .models import Dried_Moisture_Analysis_A 
from .models import Dried_Moisture_Analysis_B 
from .models import Floated_Moisture_Analysis_A 
from .models import Floated_Moisture_Analysis_B 
from .models import Quality_Control 

class fullformResources(resources.ModelResource):
	class Meta:
		model = fullform
		

class Dried_Form_A_Resources(resources.ModelResource):
	class Meta:
		model = Dried_Moisture_Analysis_A


class Dried_Form_B_Resources(resources.ModelResource):
	class Meta:
		model = Dried_Moisture_Analysis_B


class Floated_Form_A_Resources(resources.ModelResource):
	class Meta:
		model = Floated_Moisture_Analysis_A




class Floated_Form_B_Resources(resources.ModelResource):
	class Meta:
		model = Floated_Moisture_Analysis_B



class Quality_Control_Resources(resources.ModelResource):
	class Meta:
		model = Quality_Control