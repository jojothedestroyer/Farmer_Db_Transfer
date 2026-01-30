from django.shortcuts import render
import calendar
from tablib import Dataset
from calendar import HTMLCalendar 
from datetime import datetime

from rest_framework import status
import json

from django.http import HttpResponseRedirect
from .resources import fullformResources
from .resources import Dried_Form_A_Resources
from .resources import Dried_Form_B_Resources
from .resources import Floated_Form_A_Resources
from .resources import Floated_Form_B_Resources
from .resources import Quality_Control_Resources
from django.forms import modelformset_factory
from django.shortcuts import render, redirect


import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponse
# from .forms import Full_Form

from .forms import Dried_Form_A 
from .forms import Dried_Form_B 
from .forms import Floated_Form_A 
from .forms import Floated_Form_B 
from .forms import Quality_Form 
from .models import land_info
from .forms import land_info_Form

from .models import Dried_Moisture_Analysis_A 
from .models import Dried_Moisture_Analysis_B 
from .models import Floated_Moisture_Analysis_A 
from .models import Floated_Moisture_Analysis_B 
from .models import Quality_Control 




# from .forms import User_info_Form 
# from .forms import Land_tenurship_Form 
# from .forms import tree_Form 
# from .forms import farm_Form 
# from .forms import state_Form 
# from .forms import symmary_Form 







from .models import Worker_Info 

from .models import Farmer_Info 
from .models import land_info 
from .models import Land_Tenur 
from .models import Nutmeg_Trees 
from .models import Nutmeg_Variety 
from .models import Other_Crops 
from .models import Coconut_Trees 
from .models import Citrus_Mango_Trees 
from .models import Other_Spices_Trees 
from .models import Other_Seasoning_Trees 
from .models import Other_Crops_Cultivated 

from .models import Condition 
from .models import Nutmeg_Land 

from .models import Nutmeg_Frequency 
from .models import Potential_Risks 
from .models import Policy 
from .models import Road_Access 
from .models import Food_Safety_and_Quality 
from .models import Farm_Water_Source 
from .models import Farm_House 
from .models import inspector_symmary 







from .forms import Farmer_Info_Form
from .forms import land_info_Form
from .forms import Land_Tenur_Form
from .forms import Nutmeg_Trees_Form
from .forms import Nutmeg_Variety_Form
from .forms import Other_Crops_Form
from .forms import Coconut_Trees_Form
from .forms import Citrus_Mango_Trees_Form
from .forms import Other_Spices_Trees_Form
from .forms import Other_Seasoning_Trees_Form
from .forms import Other_Crops_Cultivated_Form
from .models import Cracking_Extraction_Summary
from .forms import Cracking_Extraction_Summary_Form

from .forms import Condition_Form
from .forms import Nutmeg_Land_Form
from .forms import Nutmeg_Frequency_Form
from .forms import Potential_Risks_Form
from .forms import Policy_Form
from .forms import Road_Access_Form
from .forms import Food_Safety_and_Quality_Form
from .forms import Farm_Water_Source_Form
from .forms import Farm_House_Form
from .forms import inspector_symmary_Form





from .forms import Labour_support_Form
from .forms import Training_support_Form

from .models import visit 


from .forms import visit_Form 



from .models import In_House_Drying 
from .models import Dispatch_Of_Dried_Nutmeg 
from .models import Dispatch_Of_Green_Nutmeg 
from .models import Cracking_Summary 
from .models import Floation_Summary 
from .models import Package_Ciontrol 




from .forms import In_House_Drying_Form 
from .forms import Dispatch_Of_Dried_Nutmeg_Form 
from .forms import Dispatch_Of_Green_Nutmeg_Form 
from .forms import Cracking_Summary_Form 
from .forms import Floation_Summary_Form 
from .forms import Package_Ciontrol_Form 


from .forms import LoginForm
from .forms import SectionForm

from .models import Editors 

from .models import Labour_support 
from .models import Training_support 

from .serializers import Cracking_Extraction_Summary_Serializer


# from .serializers import Dried_Moisture_Analysis_A_Serializer 
# from .serializers import Dried_Moisture_Analysis_B_Serializer 
# from .serializers import Floated_Moisture_Analysis_A_Serializer 
# from .serializers import Floated_Moisture_Analysis_B_Serializer 
# from .serializers import Quality_Control_Serializer 
# from .serializers import Worker_Info_Serializer 
# from .serializers import Farmer_Info_Serializer 

from rest_framework import generics
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
# from chartjs.views.lines import BaseLineChartView
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import Dried_Moisture_Analysis_A_Serializer
from .serializers import Dried_Moisture_Analysis_B_Serializer 
from .serializers import Floated_Moisture_Analysis_A_Serializer 
from .serializers import Floated_Moisture_Analysis_B_Serializer 
from .serializers import Quality_Control_Serializer 

from .serializers import Worker_Info_Serializer 
from .serializers import Farmer_Info_Serializer 
from .serializers import land_info_Serializer 
from .serializers import Land_Tenur_Serializer 
from .serializers import Nutmeg_Trees_Serializer 
from .serializers import Nutmeg_Variety_Serializer 
from .serializers import Other_Crops_Serializer 
from .serializers import Coconut_Trees_Serializer 
from .serializers import Citrus_Mango_Trees_Serializer 
from .serializers import Other_Spices_Trees_Serializer 
from .serializers import Other_Seasoning_Trees_Serializer 
from .serializers import Other_Crops_Cultivated_Serializer 
from .serializers import Condition_Serializer 
from .serializers import Nutmeg_Land_Serializer 
from .serializers import Nutmeg_Frequency_Serializer 
from .serializers import Potential_Risks_Serializer 
from .serializers import Policy_Serializer 
from .serializers import Road_Access_Serializer 
from .serializers import Food_Safety_and_Quality_Serializer 
from .serializers import Farm_Water_Source_Serializer 
from .serializers import Farm_House_Serializer
from .serializers import inspector_symmary_Serializer 












from .serializers import visit_Serializer 
from .serializers import In_House_Drying_Serializer 
from .serializers import Dispatch_Of_Dried_Nutmeg_Serializer 
from .serializers import Dispatch_Of_Green_Nutmeg_Serializer 
from .serializers import Cracking_Summary_Serializer 
from .serializers import Floation_Summary_Serializer 
from .serializers import Package_Ciontrol_Serializer 
from .serializers import Editors_Serializer 
from .serializers import Labour_support_Serializer 
from .serializers import Training_support_Serializer 

from .serializers import Policy_Serializer 

from .serializers import Sanitation_A_Serializer 
from .serializers import Sanitation_B_Serializer 
from .serializers import Sanitation_C_Serializer 
from django.forms.models import model_to_dict
from .models import Sanitation_A 
from .models import Sanitation_B 
from .models import Sanitation_C 

from .models import Cracking_Schedule 
from .models import Assorting_Log 
from .models import Extractor_Log
from .models import Fumigation_Log

from .forms import Cracking_Schedule_Form 
from .forms import Assorting_Log_Form  
from .forms import Extractor_Log_Form 
from .forms import Fumigation_Log_Form 




from .serializers import Cracking_Schedule_Serializer 
from .serializers import Assorting_Log_Serializer 
from .serializers import Extractor_Log_Serializer 
from .serializers import Fumigation_Log_Serializer 


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import Shelves_Serializer 
from .forms import Shelves_Form 
from .models import Shelves
from .models import M_Shelves
from .models import W_Shelves

from .models import W_Shelves_Dried
from .models import M_Shelves_Dried


from .forms import  Dispatch_Of_Dried_Nutmeg_Rec_Form
from .forms import  Dispatch_Of_Green_Nutmeg_Rec_Form


from .serializers import M_Shelves_Dried_Serializer 
from .serializers import W_Shelves_Dried_Serializer 







from .serializers import M_Shelves_Serializer 
from .serializers import W_Shelves_Serializer 








from .models import Vehicle_Inspection
from .models import Final_Weight_Inspection
from .models import Final_Weight_Inspection_fields




from .serializers import Vehicle_Inspection_Serializer 
from .serializers import Final_Weight_Inspection_Serializer 
from .serializers import Final_Weight_Inspection_fields_Serializer 




from .forms import Vehicle_Inspection_Form
from .forms import Final_Weight_Inspection_Form 
from .forms import Final_Weight_Inspection_fields_Form 



from .models import Dispatch_Of_Dried_Nutmeg_Rec
from .models import Dispatch_Of_Green_Nutmeg_Rec


from .serializers import Dispatch_Of_Dried_Nutmeg_Rec_Serializer 
from .serializers import Dispatch_Of_Green_Nutmeg_Rec_Serializer 




from .serializers import Mace_Purchase_Serializer 
from .serializers import Mace_Dispatched_Serializer 






from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *


from .models import Mace_Dispatched
from .models import Mace_Purchase



from .forms import Mace_Dispatched_Form
from .forms import Mace_Purchase_Form









from .forms import Vehicle_Inspection_Form
from .forms import Final_Weight_Inspection_Form 
from .forms import Final_Weight_Inspection_fields_Form 
from .models import Mace_Dispatched_Rec

from .forms import Mace_Dispatched_Rec_Form 

from .serializers import Mace_Dispatched_Rec_Serializer 


from .models import Day_Of_Loading
from .models import TruckEntry
from .models import Container_Inspection_Log

from .forms import Day_Of_Loading_Form
from .forms import TruckEntry_Form
from .forms import Container_Inspection_Log_Form

from .serializers import Day_Of_Loading_Serializer 
from .serializers import TruckEntry_Serializer 
from .serializers import Container_Inspection_Log_Serializer 




def Pending_Container_Inspection_Log(request):
	submitted = False

	form = Container_Inspection_Log_Form()

	return render(request,'gcna/Pending_Container_Inspection_Log.html',{'form':form,  'submitted':submitted})


def add_Container_Inspection_Log(request):
	submitted = False

	form = Container_Inspection_Log_Form()

	return render(request,'gcna/add_Container_Inspection_Log.html',{'form':form,  'submitted':submitted})




def view_Day_Of_Loading(request):
	submitted = False

	form = Day_Of_Loading_Form()

	return render(request,'gcna/view_Day_Of_Loading.html',{'form':form,  'submitted':submitted})


def view_Container_Inspection_Log(request):
	submitted = False

	form = Container_Inspection_Log_Form()

	return render(request,'gcna/view_Container_Inspection_Log.html',{'form':form,  'submitted':submitted})




class  Container_Inspection_Log_View(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Container_Inspection_Log.objects.all()
    serializer_class =  Container_Inspection_Log_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class  Container_Inspection_Log_CreateView(generics.ListCreateAPIView):
    queryset =  Container_Inspection_Log.objects.all()
    serializer_class =  Container_Inspection_Log_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


















class  Day_Of_Loading_View(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Day_Of_Loading.objects.all()
    serializer_class =  Day_Of_Loading_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class  Day_Of_Loading_CreateView(generics.ListCreateAPIView):
    queryset =  Day_Of_Loading.objects.all()
    serializer_class =  Day_Of_Loading_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
























class  TruckEntry_View(generics.RetrieveUpdateDestroyAPIView):
    queryset =  TruckEntry.objects.all()
    serializer_class =  TruckEntry_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class  TruckEntry_CreateView(generics.ListCreateAPIView):
    queryset =  TruckEntry.objects.all()
    serializer_class =  TruckEntry_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)



























def add_Dispatch_Of_Dried_Nutmeg_Rec(request):
	submitted = False

	form = Dispatch_Of_Dried_Nutmeg_Rec_Form()

	return render(request,'gcna/Dispatch_Of_Dried_Nutmeg_Rec.html',{'form':form,  'submitted':submitted})


def add_Dispatch_Of_Green_Nutmeg_Rec(request):
	submitted = False

	form = Dispatch_Of_Green_Nutmeg_Rec_Form()

	return render(request,'gcna/Dispatch_Of_Green_Nutmeg_Rec.html',{'form':form,  'submitted':submitted})




def view_Dispatch_Of_Dried_Nutmeg_Rec(request):
	submitted = False

	form = Dispatch_Of_Dried_Nutmeg_Rec_Form()

	return render(request,'gcna/view_Dispatch_Of_Dried_Nutmeg_Rec.html',{'form':form,  'submitted':submitted})


def view_Dispatch_Of_Green_Nutmeg_Rec(request):
	submitted = False

	form = Dispatch_Of_Green_Nutmeg_Rec_Form()

	return render(request,'gcna/view_Dispatch_Of_Green_Nutmeg_Rec.html',{'form':form,  'submitted':submitted})







def add_Mace_Dispatched(request):
	submitted = False

	form = Mace_Dispatched_Form()
	form_popups = Vehicle_Inspection_Form()

	return render(request,'gcna/Mace_Dispatched.html',{'form':form,'form_popups':form_popups,  'submitted':submitted})


def add_Mace_Purchase(request):
	submitted = False

	form = Mace_Purchase_Form()

	return render(request,'gcna/Mace_Purchase.html',{'form':form,  'submitted':submitted})

def find_Traceability_Origin(request):


	return render(request,'gcna/find_Traceability_origin.html')




def view_Mace_Dispatched(request):
	submitted = False

	form = Mace_Dispatched_Form()

	return render(request,'gcna/view_Mace_Dispatched.html',{'form':form,  'submitted':submitted})


def view_Mace_Purchase(request):
	submitted = False

	form = Mace_Purchase_Form()

	return render(request,'gcna/view_Mace_Purchase.html',{'form':form,  'submitted':submitted})






from .models import Mace_Dispatched_Rec













def add_Mace_Dispatched_Rec(request):
	submitted = False

	form = Mace_Dispatched_Rec_Form()

	return render(request,'gcna/Mace_Dispatched_Rec.html',{'form':form,  'submitted':submitted})





def view_Mace_Dispatched_Rec(request):
	submitted = False

	form = Mace_Dispatched_Rec_Form()

	return render(request,'gcna/view_Mace_Dispatched_Rec.html',{'form':form,  'submitted':submitted})












def add_Final_Weigtht_Inspection(request):
	submitted = False

	form = Final_Weight_Inspection_Form()

	return render(request,'gcna/add_weight_inspection.html',{'form':form,  'submitted':submitted})






def add_Vehicle_Inspection(request):
	submitted = False

	form = Vehicle_Inspection_Form()

	return render(request,'gcna/add_vehicle_inspection.html',{'form':form,  'submitted':submitted})














def view_Final_Weigtht_Inspection(request):
	submitted = False

	form = Final_Weight_Inspection_Form()

	return render(request,'gcna/view_weight_inspection.html',{'form':form,  'submitted':submitted})






def view_Vehicle_Inspection(request):
	submitted = False

	form = Vehicle_Inspection_Form()

	return render(request,'gcna/view_vehicle_inspection.html',{'form':form,  'submitted':submitted})











# def Logs_add_data1(request):
# 	submitted = False

# 	form = Final_Weight_Inspection_fields_Form()

# 	return render(request,'gcna/add_Logs1.html',{'form':form,  'submitted':submitted})










#asdasdsadsadasdassadsadasdsadsad









class  Cracking_Extraction_Summary_View(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Cracking_Extraction_Summary.objects.all()
    serializer_class =  Cracking_Extraction_Summary_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class  Cracking_Extraction_Summary_CreateView(generics.ListCreateAPIView):
    queryset =  Cracking_Extraction_Summary.objects.all()
    serializer_class =  Cracking_Extraction_Summary_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
















#adasfasfasfasadfdsfdsfdsfdsfdsfdsf






from .models import Dispatch_Of_Dried_Nutmeg_Rec
from .models import Dispatch_Of_Green_Nutmeg_Rec


from .models import Mace_Dispatched_Rec




























class Mace_Dispatched_Rec_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mace_Dispatched_Rec.objects.all()
    serializer_class = Mace_Dispatched_Rec_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Mace_Dispatched_Rec_CreateView(generics.ListCreateAPIView):
    queryset = Mace_Dispatched_Rec.objects.all()
    serializer_class = Mace_Dispatched_Rec_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


























class Mace_Purchase_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mace_Purchase.objects.all()
    serializer_class = Mace_Purchase_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Mace_Purchase_CreateView(generics.ListCreateAPIView):
    queryset = Mace_Purchase.objects.all()
    serializer_class = Mace_Purchase_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
































class Mace_Dispatched_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mace_Dispatched.objects.all()
    serializer_class = Mace_Dispatched_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Mace_Dispatched_CreateView(generics.ListCreateAPIView):
    queryset = Mace_Dispatched.objects.all()
    serializer_class = Mace_Dispatched_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


























































class Dispatch_Of_Dried_Nutmeg_Rec_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dispatch_Of_Dried_Nutmeg_Rec.objects.all()
    serializer_class = Dispatch_Of_Dried_Nutmeg_Rec_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Dispatch_Of_Dried_Nutmeg_Rec_CreateView(generics.ListCreateAPIView):
    queryset = Dispatch_Of_Dried_Nutmeg_Rec.objects.all()
    serializer_class = Dispatch_Of_Dried_Nutmeg_Rec_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


















class Dispatch_Of_Green_Nutmeg_Rec_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dispatch_Of_Green_Nutmeg_Rec.objects.all()
    serializer_class = Dispatch_Of_Green_Nutmeg_Rec_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Dispatch_Of_Green_Nutmeg_Rec_CreateView(generics.ListCreateAPIView):
    queryset = Dispatch_Of_Green_Nutmeg_Rec.objects.all()
    serializer_class = Dispatch_Of_Green_Nutmeg_Rec_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

























#sync CHECK
@csrf_exempt
def check_and_add(request):
    if request.method == 'POST':
        try:
            post_data = json.loads(request.body)
            model_name = post_data.get('model')
            data = post_data.get('data')

            # Determine the appropriate Django model based on the model name
            if model_name == 'Worker':
                model = Worker_Info
            elif model_name == 'Farmer':
                model = Farmer_Info
            elif model_name == 'DriedA':
                model = Dried_Moisture_Analysis_A
            elif model_name == 'DriedB':
                model = Dried_Moisture_Analysis_B
            elif model_name == 'FloatA':
                model = Floated_Moisture_Analysis_A
            elif model_name == 'FloatB':
                model = Floated_Moisture_Analysis_B
            elif model_name == 'Quaility':
                model = Quality_Control
            elif model_name == 'visit':
                model = visit
            elif model_name == 'In-House-Drying':
                model = In_House_Drying
            elif model_name == 'Dispatch-Of-Dried_Nutmeg':
                model = Dispatch_Of_Dried_Nutmeg
            elif model_name == 'Dispatch-Of-Green':
                model = Dispatch_Of_Green_Nutmeg
            elif model_name == 'Cracking-Summary':
                model = Cracking_Summary
            elif model_name == 'Floation-Summary':
                model = Floation_Summary
            elif model_name == 'Package-Ciontrol':
                model = Package_Ciontrol
            elif model_name == 'Editors':
                model = Editors
            elif model_name == 'Labour_support':
                model = Labour_support
            elif model_name == 'Training_support':
                model = Training_support
            elif model_name == 'land_info':
                model = land_info
            elif model_name == 'Land_Tenur':
                model = Land_Tenur
            elif model_name == 'Nutmeg_Trees':
                model = Nutmeg_Trees
            elif model_name == 'Nutmeg_Variety':
                model = Nutmeg_Variety
            elif model_name == 'Other_Crops':
                model = Other_Crops
            elif model_name == 'Coconut_Trees':
                model = Coconut_Trees
            elif model_name == 'Citrus_Mango_Trees':
                model = Citrus_Mango_Trees
            elif model_name == 'Other_Spices_Trees':
                model = Other_Spices_Trees
            elif model_name == 'Other_Seasoning_Trees':
                model = Other_Seasoning_Trees
            elif model_name == 'Other_Crops_Cultivated':
                model = Other_Crops_Cultivated
            elif model_name == 'Condition':
                model = Condition
            elif model_name == 'Nutmeg_Land':
                model = Nutmeg_Land
            elif model_name == 'Nutmeg_Frequency':
                model = Nutmeg_Frequency
            elif model_name == 'Potential_Risks':
                model = Potential_Risks
            elif model_name == 'Road_Access':
                model = Road_Access
            elif model_name == 'Food_Safety_and_Quality':
                model = Food_Safety_and_Quality
            elif model_name == 'Farm_Water_Source':
                model = Farm_Water_Source
            elif model_name == 'Farm_House':
                model = Farm_House
            elif model_name == 'inspector_symmary':
                model = inspector_symmary
            elif model_name == 'Policy':
                model = Policy
            elif model_name == 'Sanitation_A':
                model = Sanitation_A
            elif model_name == 'Sanitation_B':
                model = Sanitation_B
            elif model_name == 'Sanitation_C':
                model = Sanitation_C
				

            elif model_name == 'Cracking_Schedule':
                model = Cracking_Schedule
            elif model_name == 'Assorting_Log':
                model = Assorting_Log
            elif model_name == 'Extractor_Log':
                model = Extractor_Log
            elif model_name == 'Fumigation_Log':
                model = Fumigation_Log
            elif model_name == 'Shelves':
                model = Shelves
				
            elif model_name == 'W_Shelves':
                model = W_Shelves
				
            elif model_name == 'M_Shelves':
                model = M_Shelves



            elif model_name == 'W_Shelves_Dried':
                model = W_Shelves_Dried
				
            elif model_name == 'M_Shelves_Dried':
                model = M_Shelves_Dried
				

            elif model_name == 'Vehicle_Inspection':
                model = Vehicle_Inspection


            elif model_name == 'Dispatch_Of_Green_Nutmeg_Rec':
                model = Dispatch_Of_Green_Nutmeg_Rec




            elif model_name == 'Dispatch_Of_Dried_Nutmeg_Rec':
                model = Dispatch_Of_Dried_Nutmeg_Rec







            elif model_name == 'Mace_Dispatched':
                model = Mace_Dispatched




            elif model_name == 'Mace_Purchase':
                model = Mace_Purchase


            elif model_name == 'Day_Of_Loading':
                model = Day_Of_Loading

            elif model_name == 'TruckEntry':
                model = TruckEntry

            elif model_name == 'Container_Inspection_Log':
                model = Container_Inspection_Log






            elif model_name == 'Final_Weight_Inspection':
                model = Final_Weight_Inspection
				
            elif model_name == 'Final_Weight_Inspection_fields':
                model = Final_Weight_Inspection_fields
				
            elif model_name == 'Cracking_Extraction_Summary ':
                model = Cracking_Extraction_Summary

            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid model name'})

            # Check if the entry already exists
            id_to_check = data.get('id')
            if model.objects.filter(id=id_to_check).exists():
                # Update the existing entry in the Django database
                instance = model.objects.get(id=id_to_check)
                for key, value in data.items():
                    setattr(instance, key, value)
                instance.save()
                return JsonResponse({'status': 'updated'})
            else:
                # Create a new entry in the Django database
                model.objects.create(**data)
                return JsonResponse({'status': 'created'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})







@csrf_exempt
def check_and_add2(request):
    if request.method == 'POST':
        try:
            post_data = json.loads(request.body)
            model_name = post_data.get('model')
            data = post_data.get('data')

            # Determine the appropriate Django model based on the model name
            model = None
            if model_name == 'In-House-Drying':  # Assuming this is the model for your current form
                model = In_House_Drying
            else:
                # Handle other models here based on your application's logic
                pass

            if model:
                # Check if the entry already exists
                id_to_check = data.get('id')
                if id_to_check is not None:
                    if model.objects.filter(id=id_to_check).exists():
                        # Update the existing entry in the Django database
                        instance = model.objects.get(id=id_to_check)
                        for key, value in data.items():
                            setattr(instance, key, value)
                        instance.save()
                        return JsonResponse({'status': 'updated'})
                
                # Create a new entry in the Django database
                new_instance = model.objects.create(**data)
                return JsonResponse({'status': 'created', 'id': new_instance.id})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid model name'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})







def Logs_add_data1(request):
	submitted = False

	form1 = Cracking_Schedule_Form()

	return render(request,'gcna/add_Logs1.html',{'form1':form1,  'submitted':submitted})







def Logs_add_data2(request):
	submitted = False

	form2 = Assorting_Log_Form()

	return render(request,'gcna/add_Logs2.html',{'form2':form2, 'submitted':submitted})











def Logs_add_data3(request):
	submitted = False

	form3 = Extractor_Log_Form()
	
	return render(request,'gcna/add_Logs3.html',{'form3':form3, 'submitted':submitted})











def Logs_add_data4(request):
	submitted = False


	form4 = Fumigation_Log_Form()
	
	return render(request,'gcna/add_Logs4.html',{'form4':form4,  'submitted':submitted})









































class Vehicle_Inspection_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle_Inspection.objects.all()
    serializer_class = Vehicle_Inspection_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Vehicle_Inspection_CreateView(generics.ListCreateAPIView):
    queryset = Vehicle_Inspection.objects.all()
    serializer_class = Vehicle_Inspection_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)















































class Final_Weight_Inspection_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Final_Weight_Inspection.objects.all()
    serializer_class = Final_Weight_Inspection_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Final_Weight_Inspection_CreateView(generics.ListCreateAPIView):
    queryset = Final_Weight_Inspection.objects.all()
    serializer_class = Final_Weight_Inspection_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)









































class Final_Weight_Inspection_fields_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Final_Weight_Inspection_fields.objects.all()
    serializer_class = Final_Weight_Inspection_fields_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Final_Weight_Inspection_fields_CreateView(generics.ListCreateAPIView):
    queryset = Final_Weight_Inspection_fields.objects.all()
    serializer_class = Final_Weight_Inspection_fields_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
















































class Shelves_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shelves.objects.all()
    serializer_class = Shelves_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Shelves_CreateView(generics.ListCreateAPIView):
    queryset = Shelves.objects.all()
    serializer_class = Shelves_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)








































class M_Shelves_Dried_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = M_Shelves_Dried.objects.all()
    serializer_class = M_Shelves_Dried_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class M_Shelves_Dried_CreateView(generics.ListCreateAPIView):
    queryset = M_Shelves_Dried.objects.all()
    serializer_class = M_Shelves_Dried_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)















class W_Shelves_Dried_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = W_Shelves_Dried.objects.all()
    serializer_class = W_Shelves_Dried_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class W_Shelves_Dried_CreateView(generics.ListCreateAPIView):
    queryset = W_Shelves_Dried.objects.all()
    serializer_class = W_Shelves_Dried_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
























































class M_Shelves_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = M_Shelves.objects.all()
    serializer_class = M_Shelves_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class M_Shelves_CreateView(generics.ListCreateAPIView):
    queryset = M_Shelves.objects.all()
    serializer_class = M_Shelves_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)















class W_Shelves_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = W_Shelves.objects.all()
    serializer_class = W_Shelves_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class W_Shelves_CreateView(generics.ListCreateAPIView):
    queryset = W_Shelves.objects.all()
    serializer_class = W_Shelves_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)









class Cracking_Schedule_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cracking_Schedule.objects.all()
    serializer_class = Cracking_Schedule_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Cracking_Schedule_CreateView(generics.ListCreateAPIView):
    queryset = Cracking_Schedule.objects.all()
    serializer_class = Cracking_Schedule_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)










class Assorting_Log_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assorting_Log.objects.all()
    serializer_class = Assorting_Log_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Assorting_Log_CreateView(generics.ListCreateAPIView):
    queryset = Assorting_Log.objects.all()
    serializer_class = Assorting_Log_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)










class Extractor_Log_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Extractor_Log.objects.all()
    serializer_class = Extractor_Log_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Extractor_Log_CreateView(generics.ListCreateAPIView):
    queryset = Extractor_Log.objects.all()
    serializer_class = Extractor_Log_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)










class Fumigation_Log_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fumigation_Log.objects.all()
    serializer_class = Fumigation_Log_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Fumigation_Log_CreateView(generics.ListCreateAPIView):
    queryset = Fumigation_Log.objects.all()
    serializer_class = Fumigation_Log_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)






















































# @csrf_exempt
# def check_and_add(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         id_to_check = data.get('id')
#         if In_House_Drying.objects.filter(id=id_to_check).exists():
#             # Update the existing entry in Django database
#             instance = In_House_Drying.objects.get(id=id_to_check)
#             for key, value in data.items():
#                 setattr(instance, key, value)
#             instance.save()
#             return JsonResponse({'status': 'updated'})
#         else:
#             # Create a new entry in Django database
#             In_House_Drying.objects.create(**data)
#             return JsonResponse({'status': 'created'})
#     return JsonResponse({'status': 'error'})

# def check_and_add(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         id_to_check = data.get('id')
#         if not Dried_Moisture_Analysis_A.objects.filter(id=id_to_check).exists():
#             # Create the entry in Django database
#             Dried_Moisture_Analysis_A.objects.create(**data)
#             return JsonResponse({'status': 'success'})
#         else:
#             return JsonResponse({'status': 'exists'})
#     return JsonResponse({'status': 'error'})







class Sanitation_A_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sanitation_A.objects.all()
    serializer_class = Sanitation_A_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Sanitation_A_CreateView(generics.ListCreateAPIView):
    queryset = Sanitation_A.objects.all()
    serializer_class = Sanitation_A_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)












class Sanitation_B_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sanitation_B.objects.all()
    serializer_class = Sanitation_B_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Sanitation_B_CreateView(generics.ListCreateAPIView):
    queryset = Sanitation_B.objects.all()
    serializer_class = Sanitation_B_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)












class Sanitation_C_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sanitation_C.objects.all()
    serializer_class = Sanitation_C_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Sanitation_C_CreateView(generics.ListCreateAPIView):
    queryset = Sanitation_C.objects.all()
    serializer_class = Sanitation_A_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

















class PolicyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Policy.objects.all()
    serializer_class = Policy_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Policy_CreateView(generics.ListCreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = Policy_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)




















class Dried_Moisture_Analysis_A_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dried_Moisture_Analysis_A.objects.all()
    serializer_class = Dried_Moisture_Analysis_A_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)




class Dried_Moisture_Analysis_A_CreateView(generics.ListCreateAPIView):
    queryset = Dried_Moisture_Analysis_A.objects.all()
    serializer_class = Dried_Moisture_Analysis_A_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)





















class Dried_Moisture_Analysis_B_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dried_Moisture_Analysis_B.objects.all()
    serializer_class = Dried_Moisture_Analysis_B_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)

class Dried_Moisture_Analysis_B_CreateView(generics.ListCreateAPIView):
    queryset = Dried_Moisture_Analysis_B.objects.all()
    serializer_class = Dried_Moisture_Analysis_B_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)














class Floated_Moisture_Analysis_A_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Floated_Moisture_Analysis_A.objects.all()
    serializer_class = Floated_Moisture_Analysis_A_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Floated_Moisture_Analysis_A_CreateView(generics.ListCreateAPIView):
    queryset = Floated_Moisture_Analysis_A.objects.all()
    serializer_class = Floated_Moisture_Analysis_A_Serializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)






















class Floated_Moisture_Analysis_B_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Floated_Moisture_Analysis_B.objects.all()
    serializer_class = Floated_Moisture_Analysis_B_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)


class Floated_Moisture_Analysis_B_CreateView(generics.ListCreateAPIView):
    queryset = Floated_Moisture_Analysis_B.objects.all()
    serializer_class = Floated_Moisture_Analysis_B_Serializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)






















class Quality_Control_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quality_Control.objects.all()
    serializer_class = Quality_Control_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)


class Quality_Control_CreateView(generics.ListCreateAPIView):
    queryset = Quality_Control.objects.all()
    serializer_class = Quality_Control_Serializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)





















class Worker_Info_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker_Info.objects.all()
    serializer_class = Worker_Info_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)




class Worker_Info_CreateView(generics.ListCreateAPIView):
    queryset = Worker_Info.objects.all()
    serializer_class = Worker_Info_Serializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)














class Farmer_Info_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Farmer_Info.objects.all()
    serializer_class = Farmer_Info_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)





class Farmer_Info_CreateView(generics.ListCreateAPIView):
    queryset = Farmer_Info.objects.all()
    serializer_class = Farmer_Info_Serializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)






from rest_framework import status
from rest_framework import generics
from .models import visit
from .serializers import visit_Serializer
import json
import logging
from django.http import HttpResponseForbidden

# Add this at the beginning of your views.py
logger = logging.getLogger(__name__)



class VisitView(generics.RetrieveUpdateDestroyAPIView):
    queryset = visit.objects.all()
    serializer_class = visit_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)
        
class visit_CreateView(generics.ListCreateAPIView):
    queryset = visit.objects.all()
    serializer_class = visit_Serializer
		
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)




















class In_House_Drying_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = In_House_Drying.objects.all()
    serializer_class = In_House_Drying_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)






class In_House_Drying_CreateView(generics.ListCreateAPIView):
    queryset = In_House_Drying.objects.all()
    serializer_class = In_House_Drying_Serializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    
    











class Dispatch_Of_Dried_Nutmeg_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dispatch_Of_Dried_Nutmeg.objects.all()
    serializer_class = Dispatch_Of_Dried_Nutmeg_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)






class Dispatch_Of_Dried_Nutmeg_CreateView(generics.ListCreateAPIView):
    queryset = Dispatch_Of_Dried_Nutmeg.objects.all()
    serializer_class = Dispatch_Of_Dried_Nutmeg_Serializer
    
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    
    
    
    


















class Dispatch_Of_Green_Nutmeg_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dispatch_Of_Green_Nutmeg.objects.all()
    serializer_class = Dispatch_Of_Green_Nutmeg_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)






class Dispatch_Of_Green_Nutmeg_CreateView(generics.ListCreateAPIView):
    queryset = Dispatch_Of_Green_Nutmeg.objects.all()
    serializer_class = Dispatch_Of_Green_Nutmeg_Serializer
    
    
    
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)














class Cracking_Summary_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cracking_Summary.objects.all()
    serializer_class = Cracking_Summary_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)






class Cracking_Summary_CreateView(generics.ListCreateAPIView):
    queryset = Cracking_Summary.objects.all()
    serializer_class = Cracking_Summary_Serializer
    
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)












class Floation_Summary_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Floation_Summary.objects.all()
    serializer_class = Floation_Summary_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)






class Floation_Summary_CreateView(generics.ListCreateAPIView):
    queryset = Floation_Summary.objects.all()
    serializer_class = Floation_Summary_Serializer
    
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

















class Package_Ciontrol_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package_Ciontrol.objects.all()
    serializer_class = Package_Ciontrol_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)




class Package_Ciontrol_CreateView(generics.ListCreateAPIView):
    queryset = Package_Ciontrol.objects.all()
    serializer_class = Package_Ciontrol_Serializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)















class Editors_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editors.objects.all()
    serializer_class = Editors_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)


class Editors_CreateView(generics.ListCreateAPIView):
    queryset = Editors.objects.all()
    serializer_class = Editors_Serializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)











class Labour_support_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Labour_support.objects.all()
    serializer_class = Labour_support_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)


class Labour_support_CreateView(generics.ListCreateAPIView):
    queryset = Labour_support.objects.all()
    serializer_class = Labour_support_Serializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)









class Training_support_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Training_support.objects.all()
    serializer_class = Training_support_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)


class Training_support_CreateView(generics.ListCreateAPIView):
    queryset = Training_support.objects.all()
    serializer_class = Training_support_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)














class land_info_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = land_info.objects.all()
    serializer_class = land_info_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)

class land_info_CreateView(generics.ListCreateAPIView):
    queryset = land_info.objects.all()
    serializer_class = land_info_Serializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)











class Land_Tenur_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Land_Tenur.objects.all()
    serializer_class = Land_Tenur_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)




class Land_Tenur_CreateView(generics.ListCreateAPIView):
    queryset = Land_Tenur.objects.all()
    serializer_class = Land_Tenur_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


















class Nutmeg_Trees_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nutmeg_Trees.objects.all()
    serializer_class = Nutmeg_Trees_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)






class Nutmeg_Trees_CreateView(generics.ListCreateAPIView):
    queryset = Nutmeg_Trees.objects.all()
    serializer_class = Nutmeg_Trees_Serializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)



















class Nutmeg_Variety_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nutmeg_Variety.objects.all()
    serializer_class = Nutmeg_Variety_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)








class Nutmeg_Variety_CreateView(generics.ListCreateAPIView):
    queryset = Nutmeg_Variety.objects.all()
    serializer_class = Nutmeg_Variety_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)













class Other_Crops_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Other_Crops.objects.all()
    serializer_class = Other_Crops_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)










class Other_Crops_CreateView(generics.ListCreateAPIView):
    queryset = Other_Crops.objects.all()
    serializer_class = Other_Crops_Serializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)












class Coconut_Trees_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coconut_Trees.objects.all()
    serializer_class = Coconut_Trees_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)



class Coconut_Trees_CreateView(generics.ListCreateAPIView):
    queryset = Coconut_Trees.objects.all()
    serializer_class = Coconut_Trees_Serializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)









class Citrus_Mango_Trees_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Citrus_Mango_Trees.objects.all()
    serializer_class = Citrus_Mango_Trees_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)


class Citrus_Mango_Trees_CreateView(generics.ListCreateAPIView):
    queryset = Citrus_Mango_Trees.objects.all()
    serializer_class = Citrus_Mango_Trees_Serializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)













class Other_Spices_Trees_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Other_Spices_Trees.objects.all()
    serializer_class = Other_Spices_Trees_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)







class Other_Spices_Trees_CreateView(generics.ListCreateAPIView):
    queryset = Other_Spices_Trees.objects.all()
    serializer_class = Other_Spices_Trees_Serializer
    
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
   
   
   
    
    
    
    
    
    
    



class Other_Seasoning_Trees_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Other_Seasoning_Trees.objects.all()
    serializer_class = Other_Seasoning_Trees_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)





    
class Other_Seasoning_Trees_CreateView(generics.ListCreateAPIView):
    queryset = Other_Seasoning_Trees.objects.all()
    serializer_class = Other_Seasoning_Trees_Serializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


















class Other_Crops_Cultivated_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Other_Crops_Cultivated.objects.all()
    serializer_class = Other_Crops_Cultivated_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)







class Other_Crops_Cultivated_CreateView(generics.ListCreateAPIView):
    queryset = Other_Crops_Cultivated.objects.all()
    serializer_class = Other_Crops_Cultivated_Serializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
















class Condition_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Condition.objects.all()
    serializer_class = Condition_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)












class Condition_CreateView(generics.ListCreateAPIView):
    queryset = Condition.objects.all()
    serializer_class = Condition_Serializer



    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)





















class Nutmeg_Land_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nutmeg_Land.objects.all()
    serializer_class = Nutmeg_Land_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)


class Nutmeg_Land_CreateView(generics.ListCreateAPIView):
    queryset = Nutmeg_Land.objects.all()
    serializer_class = Nutmeg_Land_Serializer
    
    
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    
    
    
    
    
    
    
    


class Nutmeg_Frequency_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nutmeg_Frequency.objects.all()
    serializer_class = Nutmeg_Frequency_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)




    
    
class Nutmeg_Frequency_CreateView(generics.ListCreateAPIView):
    queryset = Nutmeg_Frequency.objects.all()
    serializer_class = Nutmeg_Frequency_Serializer



    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)













class Potential_Risks_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Potential_Risks.objects.all()
    serializer_class = Potential_Risks_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)





class Potential_Risks_CreateView(generics.ListCreateAPIView):
    queryset = Potential_Risks.objects.all()
    serializer_class = Potential_Risks_Serializer



    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

























class Policy_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Policy.objects.all()
    serializer_class = Policy_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)







class Policy_CreateView(generics.ListCreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = Policy_Serializer



    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)













class Road_Access_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Road_Access.objects.all()
    serializer_class = Road_Access_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)







class Road_Access_CreateView(generics.ListCreateAPIView):
    queryset = Road_Access.objects.all()
    serializer_class = Road_Access_Serializer
    
    
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

class Food_Safety_and_Quality_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food_Safety_and_Quality.objects.all()
    serializer_class = Food_Safety_and_Quality_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)

    
    
class Food_Safety_and_Quality_CreateView(generics.ListCreateAPIView):
    queryset = Food_Safety_and_Quality.objects.all()
    serializer_class = Food_Safety_and_Quality_Serializer



    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)










class Farm_Water_Source_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Farm_Water_Source.objects.all()
    serializer_class = Farm_Water_Source_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)

    

class Farm_Water_Source_CreateView(generics.ListCreateAPIView):
    queryset = Farm_Water_Source.objects.all()
    serializer_class = Farm_Water_Source_Serializer


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)













class Farm_House_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Farm_House.objects.all()
    serializer_class = Farm_House_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)






class Farm_House_CreateView(generics.ListCreateAPIView):
    queryset = Farm_House.objects.all()
    serializer_class = Farm_House_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)













class inspector_symmary_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = inspector_symmary.objects.all()
    serializer_class = inspector_symmary_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Retrieve IndexedDB IDs from the request header
        indexeddb_ids = json.loads(request.META.get('HTTP_X_INDEXEDDB_IDS', '[]'))

        logger.info(f"Instance ID: {instance.id}")
        logger.info(f"IndexedDB IDs: {indexeddb_ids}")

        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning("Allowed delete request.")
            return Response(status=status.HTTP_204_NO_CONTENT)







class inspector_symmary_CreateView(generics.ListCreateAPIView):
    queryset = inspector_symmary.objects.all()
    serializer_class = inspector_symmary_Serializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)











import json
from django.http import JsonResponse
from .models import Farmer_Info

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Farmer_Info
import json

@csrf_exempt
def sync_data_to_server(request):
    if request.method == 'POST':
        try:
            # Get the data from the request and deserialize JSON
            data = json.loads(request.body)

            # Update the Django database with the received data
            # For example, you can create or update records in the Farmer_Info model
            farmer, created = Farmer_Info.objects.get_or_create(pk=data['id'])
            farmer.field1 = data['field1']
            farmer.field2 = data['field2']
            # Add more fields as needed
            farmer.save()

            return JsonResponse({'message': 'Data synced with the server'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'message': 'Only POST requests are supported'}, status=405)



def edit_Visit(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')
    try:
        farmer_info_id = visit.objects.get(Nutmeg_ID_No=farmer_info_id)
    except visit.DoesNotExist:
        return redirect('error_table23')  

    if request.method == 'POST':
        form = visit_Form(request.POST, instance=farmer_info_id)
        if form.is_valid():
            form.save()
            return redirect('table') 
    else:
        form = visit_Form(instance=farmer_info_id)
    return render(request, 'gcna/edit_table3.html', {'form': form})











def view_Visit(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = visit.objects.filter(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}


	except visit.DoesNotExist:
		return redirect('error_table22')  


	return render(request, 'gcna/view_farm_24.html',context)














def view_Training(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Training_support.objects.filter(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}


	except Training_support.DoesNotExist:
		return redirect('error_table22')  


	return render(request, 'gcna/view_farm_22.html',context)









def view_labour(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Labour_support.objects.filter(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Labour_support.DoesNotExist:
		return redirect('error_table23')  



	return render(request, 'gcna/view_farm_23.html',context)







def edit_Training(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')
    try:
        farmer_info_id = Training_support.objects.get(Nutmeg_ID_No=farmer_info_id)
    except Training_support.DoesNotExist:
        return redirect('error_table22')  

    if request.method == 'POST':
        form = Training_support_Form(request.POST, instance=farmer_info_id)
        if form.is_valid():
            form.save()
            return redirect('table') 
    else:
        form = Training_support_Form(instance=farmer_info_id)
    return render(request, 'gcna/edit_table3.html', {'form': form})








def edit_labour(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')
    try:
        farmer_info_id = Labour_support.objects.get(Nutmeg_ID_No=farmer_info_id)
    except Labour_support.DoesNotExist:
        return redirect('error_table23')  

    if request.method == 'POST':
        form = Labour_support_Form(request.POST, instance=farmer_info_id)
        if form.is_valid():
            form.save()
            return redirect('table') 
    else:
        form = Labour_support_Form(instance=farmer_info_id)
    return render(request, 'gcna/edit_table3.html', {'form': form})

















def view_Training0(request):
	farmer_info_id = request.session['Nutmeg_ID_No']
 
 
	

	try:
		farmer_info_id = Training_support.objects.all()
		context = {
	        'farmer_info_id': farmer_info_id
		}


	except Training_support.DoesNotExist:
		return redirect('error_table22')  


	return render(request, 'gcna/view_farm0_22.html',context)









def view_labour0(request):
	farmer_info_id = request.session['Nutmeg_ID_No']
		

	try:
		farmer_info_id = Labour_support.objects.all()
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Labour_support.DoesNotExist:
		return redirect('error_table23')  



	return render(request, 'gcna/view_farm0_23.html',context)











def view_Sanitation_A(request):


	return render(request, 'gcna/view_farm0_24.html')

def view_Sanitation_B(request):


	return render(request, 'gcna/view_farm0_25.html')


def view_Sanitation_C(request):


	return render(request, 'gcna/view_farm0_26.html')



from .forms import Sanitation_A_Form 
from .forms import Sanitation_B_Form 
from .forms import Sanitation_C_Form 


def Sanitation_A_add_data(request):
	submitted = False

	form = Sanitation_A_Form()

	return render(request,'gcna/add_Sanitation_A.html',{'form':form, 'submitted':submitted})


def Sanitation_B_add_data(request):
	submitted = False

	form = Sanitation_B_Form()

	return render(request,'gcna/add_Sanitation_B.html',{'form':form, 'submitted':submitted})


def Sanitation_C_add_data(request):
	submitted = False

	form = Sanitation_C_Form()

	return render(request,'gcna/add_Sanitation_C.html',{'form':form, 'submitted':submitted})




from django.core.mail import send_mail
from django.http import JsonResponse
from django.core.mail import send_mail

def send_test_email(request):
    if request.method == 'POST':
        # Retrieve recipient's email address from the form data
        to_email = request.POST.get('to')

        # Sender's email address (your Gmail address)
        from_email = 'reportmail121@gmail.com'

        # Email subject and body
        subject = 'Test Email Subject'
        message = 'This is a test email message.'

        try:
            # Send email using send_mail function
            send_mail(subject, message, from_email, [to_email])

            # Return a success response
            return JsonResponse({'success': True})
        except Exception as e:
            # Return an error response if sending fails
            return JsonResponse({'success': False, 'error': str(e)})

    
    
    
    
    
    
    
    
    
    
    
    
# views.py

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

    
import logging
logger = logging.getLogger(__name__)

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email_content = data.get('content', '')

        if email_content.strip() != '':
            try:
                send_mail(
                    'Subject',  # Subject of the email
                    email_content,  # Content of the email
                    'reportmail121@gmail.com',  # Sender's email address
                    ['josiahbest422@gmail.com'],  # Recipient's email address
                    fail_silently=False,
                )
                return JsonResponse({'message': 'Message sent successfully'})
            except Exception as e:
                logger.error('Failed to send email: %s', str(e))  # Log the error
                return JsonResponse({'error': 'Failed to send message'}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)
    
    
def edit_Training0(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')
    try:
        farmer_info_id = Training_support.objects.get(Nutmeg_ID_No=farmer_info_id)
    except Training_support.DoesNotExist:
        return redirect('error_table22')  

    if request.method == 'POST':
        form = Training_support_Form(request.POST, instance=farmer_info_id)
        if form.is_valid():
            form.save()
            return redirect('table') 
    else:
        form = Training_support_Form(instance=farmer_info_id)
    return render(request, 'gcna/edit_table3.html', {'form': form})








def edit_labour0(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')
    try:
        farmer_info_id = Labour_support.objects.get(Nutmeg_ID_No=farmer_info_id)
    except Labour_support.DoesNotExist:
        return redirect('error_table23')  

    if request.method == 'POST':
        form = Labour_support_Form(request.POST, instance=farmer_info_id)
        if form.is_valid():
            form.save()
            return redirect('table') 
    else:
        form = Labour_support_Form(instance=farmer_info_id)
    return render(request, 'gcna/edit_table3.html', {'form': form})








def offline_auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Query your IndexedDB to check if the user's credentials match
        # the data stored in IndexedDB
        matching_data = YourIndexedDBQuery(username, password)

        if matching_data:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})









class EditorChartView(TemplateView):
    template_name = 'gcna/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Editors.objects.all()
        return context

     



def bar_chart(request):
    editors = Editors.objects.all()

    editor_names = []
    num_users = []

    for editor in editors:
        editor_names.append(editor.editor_name)
        num_users.append(editor.num_users)

    context = {
        'editor_names': editor_names,
        'num_users': num_users,
    }

    return render(request, 'gcna/bar_chart.html', context)




def bar_chart1(request):
    data = Dried_Moisture_Analysis_A.objects.all()

    nutmeg_ids = []
    sample_weights = []

    for entry in data:
        nutmeg_ids.append(entry.Nutmeg_ID_No)
        sample_weights.append(int(entry.Final_Sample_Weight))

    context = {
        'nutmeg_ids': nutmeg_ids,
        'sample_weights': sample_weights,
    }

    return render(request, 'gcna/bar_chart1.html', context)






def error_table0(request):

	return render(request, 'gcna/error_table0.html')


def error_table1(request):

	return render(request, 'gcna/error_table1.html')


def error_table2(request):

	return render(request, 'gcna/error_table2.html')


def error_table3(request):

	return render(request, 'gcna/error_table3.html')


def error_table4(request):

	return render(request, 'gcna/error_table4.html')


def error_table5(request):

	return render(request, 'gcna/error_table5.html')


def error_table6(request):

	return render(request, 'gcna/error_table6.html')


def error_table7(request):

	return render(request, 'gcna/error_table7.html')


def error_table8(request):

	return render(request, 'gcna/error_table8.html')


def error_table9(request):

	return render(request, 'gcna/error_table9.html')


def error_table10(request):

	return render(request, 'gcna/error_table10.html')


def error_table11(request):

	return render(request, 'gcna/error_table11.html')


def error_table12(request):

	return render(request, 'gcna/error_table12.html')


def error_table13(request):

	return render(request, 'gcna/error_table13.html')


def error_table14(request):

	return render(request, 'gcna/error_table14.html')


def error_table15(request):

	return render(request, 'gcna/error_table15.html')


def error_table16(request):

	return render(request, 'gcna/error_table16.html')


def error_table17(request):

	return render(request, 'gcna/error_table17.html')


def error_table18(request):

	return render(request, 'gcna/error_table18.html')


def error_table19(request):

	return render(request, 'gcna/error_table19.html')


def error_table20(request):

	return render(request, 'gcna/error_table20.html')


def error_table21(request):

	return render(request, 'gcna/error_table21.html')



def error_table22(request):

	return render(request, 'gcna/error_table22.html')


def error_table23(request):

	return render(request, 'gcna/error_table23.html')


def error_table24(request):

	return render(request, 'gcna/error_table24.html')




def error_table_driedA(request):

	return render(request, 'gcna/error_table_driedA.html')



def error_table_driedB(request):

	return render(request, 'gcna/error_table_driedB.html')



def error_table_floatA(request):

	return render(request, 'gcna/error_table_floatA.html')



def error_table_floatB(request):

	return render(request, 'gcna/error_table_floatB.html')



def error_table_quality(request):

	return render(request, 'gcna/error_table_quality.html')






def error_In_House(request):

	return render(request, 'gcna/error_In_House_Form.html')



def error_Dispatch_Dried_Nutmeg(request):

	return render(request, 'gcna/error_Dispatch_Dried_Nutmeg_Form.html')



def error_Dispatch_Green_Nutmeg(request):

	return render(request, 'gcna/error_Dispatch_Green_Nutmeg_Form.html')



def error_Cracking_Nutmeg(request):

	return render(request, 'gcna/error_Cracking_Nutmeg_Form.html')



def error_Floation(request):

	return render(request, 'gcna/error_Floation_Form.html')



def error_Package(request):

	return render(request, 'gcna/error_Package_Form.html')













def error_In_House_0(request):

	return render(request, 'gcna/error_In_House_Form_0.html')


                                      
def error_Dispatch_Dried_Nutmeg_0(request):

	return render(request, 'gcna/error_Dispatch_Dried_Nutmeg_Form_0.html')



def error_Dispatch_Green_Nutmeg_0(request):

	return render(request, 'gcna/error_Dispatch_Green_Nutmeg_Form_0.html')



def error_Cracking_Nutmeg_0(request):

	return render(request, 'gcna/error_Cracking_Nutmeg_Form_0.html')



def error_Floation_0(request):

	return render(request, 'gcna/error_Floation_Form_0.html')



def error_Package_0(request):

	return render(request, 'gcna/error_Package_Form_0.html')









def edit_table21(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = inspector_symmary.objects.get(Nutmeg_ID_No=farmer_info_id)
	except inspector_symmary.DoesNotExist:
		return redirect('error_table21')  

	if request.method == 'POST':
		form = inspector_symmary_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table21') 
	else:
		form = inspector_symmary_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_table21.html', {'form': form})





def display_table_data21(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = inspector_symmary.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except inspector_symmary.DoesNotExist:
	# 	return redirect('error_table21')

	return render(request, 'gcna/view_table21.html')















def edit_table20(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Farm_House.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Farm_House.DoesNotExist:
		return redirect('error_table20')  

	if request.method == 'POST':
		form = Farm_House_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table20') 
	else:
		form = Farm_House_Form(instance=farmer_info_id)





	return render(request, 'gcna/edit_table20.html', {'form': form})



def display_table_data20(request):

	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = Farm_House.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Farm_House.DoesNotExist:
	# 	return redirect('error_table20')


	return render(request, 'gcna/view_table20.html')
















def edit_table19(request):


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Farm_Water_Source.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Farm_Water_Source.DoesNotExist:
		return redirect('error_table19')  

	if request.method == 'POST':
		form = Farm_Water_Source_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table19') 
	else:
		form = Farm_Water_Source_Form(instance=farmer_info_id)




	return render(request, 'gcna/edit_table19.html', {'form': form})



def display_table_data19(request):

	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = Farm_Water_Source.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Farm_Water_Source.DoesNotExist:
	# 	return redirect('error_table19')


	return render(request, 'gcna/view_table19.html')

















def edit_table18(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Food_Safety_and_Quality.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Food_Safety_and_Quality.DoesNotExist:
		return redirect('error_table18')  

	if request.method == 'POST':
		form = Food_Safety_and_Quality_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table18') 
	else:
		form = Food_Safety_and_Quality_Form(instance=farmer_info_id)



	return render(request, 'gcna/edit_table18.html', {'form': form})



def display_table_data18(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = Food_Safety_and_Quality.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Food_Safety_and_Quality.DoesNotExist:
	# 	return redirect('error_table18')


	return render(request, 'gcna/view_table18.html')














def edit_table17(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Road_Access.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Road_Access.DoesNotExist:
		return redirect('error_table17')  

	if request.method == 'POST':
		form = Road_Access_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table17') 
	else:
		form = Road_Access_Form(instance=farmer_info_id)





	return render(request, 'gcna/edit_table17.html', {'form': form})



def display_table_data17(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = Road_Access.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Road_Access.DoesNotExist:
	# 	return redirect('error_table17')


	return render(request, 'gcna/view_table17.html')














def edit_table16(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Policy.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Policy.DoesNotExist:
		return redirect('error_table16')  

	if request.method == 'POST':
		form = Policy_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table16') 
	else:
		form = Policy_Form(instance=farmer_info_id)



	return render(request, 'gcna/edit_table16.html', {'form': form})



def display_table_data16(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = Policy.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Policy.DoesNotExist:
	# 	return redirect('error_table16')

	return render(request, 'gcna/view_table16.html')















def edit_table15(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Potential_Risks.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Potential_Risks.DoesNotExist:
		return redirect('error_table15')  

	if request.method == 'POST':
		form = Potential_Risks_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table15') 
	else:
		form = Potential_Risks_Form(instance=farmer_info_id)




	return render(request, 'gcna/edit_table15.html', {'form': form})



def display_table_data15(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = Potential_Risks.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Potential_Risks.DoesNotExist:
	# 	return redirect('error_table15')


	return render(request, 'gcna/view_table15.html')

















def edit_table14(request):


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Nutmeg_Frequency.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Nutmeg_Frequency.DoesNotExist:
		return redirect('error_table14')  

	if request.method == 'POST':
		form = NNutmeg_Frequency_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table14') 
	else:
		form = Nutmeg_Frequency_Cultivated_Form(instance=farmer_info_id)



	return render(request, 'gcna/edit_table14.html', {'form': form})



def display_table_data14(request):

	# farmer_info_id = request.session['Nutmeg_ID_No']
	# try:
	# 	farmer_info_id = Nutmeg_Frequency.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Nutmeg_Frequency.DoesNotExist:
	# 	return redirect('error_table14')



	return render(request, 'gcna/view_table14.html')






















def edit_table13(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Nutmeg_Land.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Nutmeg_Land.DoesNotExist:
		return redirect('error_table13')  

	if request.method == 'POST':
		form = Nutmeg_Land_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table13') 
	else:
		form = Nutmeg_Land_Cultivated_Form(instance=farmer_info_id)




	return render(request, 'gcna/edit_table13.html', {'form': form})



def display_table_data13(request):

	# farmer_info_id = request.session['Nutmeg_ID_No']
	# try:
	# 	farmer_info_id = Nutmeg_Land.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Nutmeg_Land.DoesNotExist:
	# 	return redirect('error_table13')


	return render(request, 'gcna/view_table13.html')




















def edit_table12(request):
	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Condition.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Condition.DoesNotExist:
		return redirect('error_table12')  

	if request.method == 'POST':
		form = Condition_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table12') 
	else:
		form = Other_Crops_Cultivated_Form(instance=farmer_info_id)




	return render(request, 'gcna/edit_table12.html', {'form': form})



def display_table_data12(request):

	# farmer_info_id = request.session['Nutmeg_ID_No']
	# try:
	# 	farmer_info_id = Condition.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Condition.DoesNotExist:
	# 	return redirect('error_table12')


	return render(request, 'gcna/view_table12.html')

























def edit_table11(request):


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Crops_Cultivated.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Other_Crops_Cultivated.DoesNotExist:
		return redirect('error_table11')  

	if request.method == 'POST':
		form = Other_Crops_Cultivated_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table11') 
	else:
		form = Other_Crops_Cultivated_Form(instance=farmer_info_id)




	return render(request, 'gcna/edit_table11.html', {'form': form})



def display_table_data11(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']
	# try:
	# 	farmer_info_id = Other_Crops_Cultivated.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Other_Crops_Cultivated.DoesNotExist:
	# 	return redirect('error_table11')




	return render(request, 'gcna/view_table11.html')
















def edit_table10(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Seasoning_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Other_Seasoning_Trees.DoesNotExist:
		return redirect('error_table10')  

	if request.method == 'POST':
		form = Other_Seasoning_Trees_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table10') 
	else:
		form = Other_Seasoning_Trees_Form(instance=farmer_info_id)




	return render(request, 'gcna/edit_table10.html', {'form': form})



def display_table_data10(request):

	# farmer_info_id = request.session['Nutmeg_ID_No']
	# try:
	# 	farmer_info_id = Other_Seasoning_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Other_Seasoning_Trees.DoesNotExist:
	# 	return redirect('error_table10')


	return render(request, 'gcna/view_table10.html')




















def edit_table9(request):



	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Spices_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Other_Spices_Trees.DoesNotExist:
		return redirect('error_table9')  

	if request.method == 'POST':
		form = Other_Spices_Trees_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table9') 
	else:
		form = Other_Spices_Trees_Form(instance=farmer_info_id)



	return render(request, 'gcna/edit_table9.html', {'form': form})



def display_table_data9(request):

	# farmer_info_id = request.session['Nutmeg_ID_No']
	# try:
	# 	farmer_info_id = Other_Spices_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Other_Spices_Trees.DoesNotExist:
	# 	return redirect('error_table9')


	return render(request, 'gcna/view_table9.html')     









def edit_table8(request):




	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Citrus_Mango_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Citrus_Mango_Trees.DoesNotExist:
		return redirect('error_table8')  

	if request.method == 'POST':
		form = Citrus_Mango_Trees_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table8') 
	else:
		form = Citrus_Mango_Trees_Form(instance=farmer_info_id)



	return render(request, 'gcna/edit_table8.html', {'form': form})


def display_table_data8(request):


	# farmer_info_id = request.session['Nutmeg_ID_No']
	# try:
	# 	farmer_info_id = Citrus_Mango_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Citrus_Mango_Trees.DoesNotExist:
	# 	return redirect('error_table8')



	return render(request, 'gcna/view_table8.html', context)















def edit_table7(request):



	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Coconut_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Coconut_Trees.DoesNotExist:
		return redirect('error_table7')  

	if request.method == 'POST':
		form = Coconut_Trees_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table7') 
	else:
		form = Coconut_Trees_Form(instance=farmer_info_id)



	return render(request, 'gcna/edit_table7.html', {'form': form})



def display_table_data7(request):


	# farmer_info_id = request.session['Nutmeg_ID_No']
	# try:
	# 	farmer_info_id = Coconut_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Coconut_Trees.DoesNotExist:
	# 	return redirect('error_table7')


	return render(request, 'gcna/view_table7.html', context)
















def edit_table6(request):


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Crops.objects.get(Nutmeg_ID_No=farmer_info_id)

	except Other_Crops.DoesNotExist:
		return redirect('error_table6')  

	if request.method == 'POST':
		form = Other_Crops_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table6') 
	else:
		form = Other_Crops_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_table6.html', {'form': form})



def display_table_data6(request):

	# farmer_info_id = request.session['Nutmeg_ID_No']
	# try:
	# 	farmer_info_id = Other_Crops.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Other_Crops.DoesNotExist:
	# 	return redirect('error_table6')


	return render(request, 'gcna/view_table6.html', context)





# def display_table_data_null_field(request):

	# farmer_info_id = request.session['Nutmeg_ID_No']
	# try:
	#     farmer_info_list = Other_Crops.objects.filter(Nutmeg_ID_No=farmer_info_id)
	#     context = {
	#         'farmer_info_list': farmer_info_list
	#     }

	# except Other_Crops.DoesNotExist:
	#     return redirect('error_table6')


	# return render(request, 'gcna/view_table6.html', context)





def edit_table5(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Nutmeg_Variety.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Nutmeg_Variety.DoesNotExist:
		return redirect('error_table5')  

	if request.method == 'POST':
		form = Nutmeg_Variety_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table5') 
	else:
		form = Nutmeg_Variety_Form(instance=farmer_info_id)



	return render(request, 'gcna/edit_table5.html', {'form': form})



def display_table_data5(request):

	# farmer_info_id = request.session['Nutmeg_ID_No']
	# try:
	# 	farmer_info_id = Nutmeg_Variety.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Nutmeg_Variety.DoesNotExist:
	# 	return redirect('error_table5')


	return render(request, 'gcna/view_table5.html', context)








def edit_table4(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')
    try:
        farmer_info_id = Nutmeg_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
    except Nutmeg_Trees.DoesNotExist:
        return redirect('error_table4')  

    if request.method == 'POST':
        form = Nutmeg_Trees_Form(request.POST, instance=farmer_info_id)
        if form.is_valid():
            form.save()
            return redirect('edit_table4') 
    else:
        form = Nutmeg_Trees_Form(instance=farmer_info_id)




    return render(request, 'gcna/edit_table4.html', {'form': form})











def display_table_data4(request):

	# farmer_info_id = request.session['Nutmeg_ID_No']
	# try:
	# 	farmer_info_id = Nutmeg_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Nutmeg_Trees.DoesNotExist:
	# 	return redirect('error_table4')


	return render(request, 'gcna/view_table4.html', context)






def edit_table3(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')
    try:
        farmer_info_id = Land_Tenur.objects.get(Nutmeg_ID_No=farmer_info_id)
    except Land_Tenur.DoesNotExist:
        return redirect('error_table3')  

    if request.method == 'POST':
        form = Land_Tenur_Form(request.POST, instance=farmer_info_id)
        if form.is_valid():
            form.save()
            return redirect('edit_table3') 
    else:
        form = Land_Tenur_Form(instance=farmer_info_id)
    return render(request, 'gcna/edit_table3.html', {'form': form})






def display_table_data3(request):

	# farmer_info_id = request.session['Nutmeg_ID_No']
	# try:
	# 	farmer_info_id = Land_Tenur.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Land_Tenur.DoesNotExist:
	# 	return redirect('error_table3')


	return render(request, 'gcna/view_table3.html', context)












def edit_table2(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')

    try:
        farmer_info_entries = land_info.objects.filter(Nutmeg_ID_No=farmer_info_id)
    except land_info.DoesNotExist:
        return redirect('error_table2')

    LandInfoFormSet = modelformset_factory(land_info, form=land_info_Form, extra=0)

    if request.method == 'POST':
        formset = LandInfoFormSet(request.POST, queryset=farmer_info_entries)
        if formset.is_valid():
            formset.save()
            return redirect('edit_table2')
    else:
        formset = LandInfoFormSet(queryset=farmer_info_entries)

    return render(request, 'gcna/edit_table2.html', {'formset': formset})







def display_table_data2(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = land_info.objects.filter(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except land_info.DoesNotExist:
	# 	return redirect('error_table2')


	return render(request, 'gcna/view_table2.html')












def edit_table1(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Farmer_Info.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Farmer_Info.DoesNotExist:
		return redirect('error_table1')  

	if request.method == 'POST':
		form = Farmer_Info_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table1') 
	else:
		form = Farmer_Info_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_table1.html', {'form': form})

def display_table_data1(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']
        
	# try:
	# 	farmer_info_id = Farmer_Info.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}


	# except Farmer_Info.DoesNotExist:
	# 	return redirect('error_table1')


	return render(request, 'gcna/view_table1.html')


def table(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = land_info.objects.filter(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except land_info.DoesNotExist:
	# 	pass


	return render(request, 'gcna/table_of_contents.html')


def Initial(request):


        
	return render(request, 'gcna/Initial_Form.html')

def rev_data00(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)           

        if form.is_valid():
            request.session['Worker_ID_No'] =  form.cleaned_data['Worker_ID_No']
            request.session['Nutmeg_ID_No'] =  form.cleaned_data['Nutmeg_ID_No']


            Worker_ID_No=request.session['Worker_ID_No']
            Nutmeg_ID_No=request.session['Nutmeg_ID_No']


            check2 = Worker_Info.objects.filter(Worker_ID_No=Worker_ID_No).first()

            if check2:

                Worker_ID_No = Worker_Info.objects.get(Worker_ID_No=Worker_ID_No)
                Worker_ID_No_id = Worker_ID_No.id


                return render(request, 'gcna/adhome.html',{'Worker_ID_No_id':Worker_ID_No_id})  
            
            else:

                return redirect('error_table0')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'gcna/adhome.html', context)
# views.py
from django.db.models import Sum, Avg
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from datetime import datetime, timedelta
from .models import Dried_Moisture_Analysis_A







def generate_report(request):
    today = datetime.now()
    current_month_start = datetime(today.year, today.month, 1)

    # Get all records for the current month
    records_current_month = Dried_Moisture_Analysis_A.objects.filter(
        Date_Created__range=[current_month_start, today]
    )

    # Calculate averages for the specified date range
    total_average_current_month = records_current_month.aggregate(avg=Avg('AVERAGE'))['avg'] if records_current_month.exists() else 0

    # Calculate sums for specific fields
    total_weight_current_month = records_current_month.aggregate(sum_total_weight=Sum('Total_Weight'))['sum_total_weight'] if records_current_month.exists() else 0
    initial_sample_weight_current_month = records_current_month.aggregate(sum_initial_sample_weight=Sum('Initial_Sample_Weight'))['sum_initial_sample_weight'] if records_current_month.exists() else 0
    insect_damaged_current_month = records_current_month.aggregate(sum_insect_damaged=Sum('Insect_Damaged'))['sum_insect_damaged'] if records_current_month.exists() else 0
    broken_current_month = records_current_month.aggregate(sum_broken=Sum('Broken'))['sum_broken'] if records_current_month.exists() else 0
    mould_current_month = records_current_month.aggregate(sum_mould=Sum('Mould'))['sum_mould'] if records_current_month.exists() else 0
    final_sample_weight_current_month = records_current_month.aggregate(sum_final_sample_weight=Sum('Final_Sample_Weight'))['sum_final_sample_weight'] if records_current_month.exists() else 0

    # Print sums for debugging
    print("Total Weight Current Month:", total_weight_current_month)
    print("Initial Sample Weight Current Month:", initial_sample_weight_current_month)
    print("Insect Damaged Current Month:", insect_damaged_current_month)
    print("Broken Current Month:", broken_current_month)
    print("Mould Current Month:", mould_current_month)
    print("Final Sample Weight Current Month:", final_sample_weight_current_month)

    # Render the HTML template with the calculated statistics
    template = get_template('gcna/report_template.html')
    context = {
        'total_average_current_month': total_average_current_month,
        'total_weight_current_month': total_weight_current_month,
        'initial_sample_weight_current_month': initial_sample_weight_current_month,
        'insect_damaged_current_month': insect_damaged_current_month,
        'broken_current_month': broken_current_month,
        'mould_current_month': mould_current_month,
        'final_sample_weight_current_month': final_sample_weight_current_month,
    }
    html = template.render(context)

    # Generate PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF creation error', status=500)

    return response

def add_to_session(request):
    if request.method == 'POST':
        farm_type = request.POST.get('farm_type')
        tenurship = request.POST.get('tenurship')
        training = request.POST.get('training')
        parish = request.POST.get('parish')
        village = request.POST.get('village')
        visit = request.POST.get('visit')
        # Get other field values if needed

        # Add the data to the session
        request.session['farm_type'] = farm_type
        request.session['tenurship'] = tenurship
        request.session['training'] = training
        request.session['parish'] = parish
        request.session['village'] = village
        request.session['visit'] = visit

 

        # Add other field values to the session
        
        return redirect('table')  
    else:
        return redirect('table001')  


 

# In your views.py or utils.py






from django.shortcuts import render, redirect
from .models import Worker_Info
from .forms import LoginForm

from .forms import SigninForm



# def rev_data0(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)           

#         if form.is_valid():
#             request.session['Worker_ID_No'] =  form.cleaned_data['Worker_ID_No']
#             request.session['Nutmeg_ID_No'] =  form.cleaned_data['Nutmeg_ID_No']


#             Worker_ID_No=request.session['Worker_ID_No']
#             Nutmeg_ID_No=request.session['Nutmeg_ID_No']



#             check2 = Worker_Info.objects.filter(Worker_ID_No=Worker_ID_No).first()

#             if check2:

#                 Worker_ID_No = Worker_Info.objects.get(Worker_ID_No=Worker_ID_No)
#                 Worker_ID_No_id = Worker_ID_No.id

#                 return redirect('table001')  
 
            
#             else:

#                 return redirect('error_table0_0')
#     else:
#         form = LoginForm()

#     context = {
#         'form': form,
#     }

#     return render(request, 'gcna/login.html', context)

    # form = LoginForm()
    # context = {'form': form}
    # return render(request, 'gcna/login.html', context)



# from reportlab.pdfgen import canvas
# from django.http import HttpResponse
# from django.db.models import Sum
# from .models import Dried_Moisture_Analysis_A



# def generate_monthly_report(request, month, year):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename=monthly_report_{month}_{year}.pdf'

#     # Create PDF document
#     p = canvas.Canvas(response)

#     # Query data for the given month and year
#     entries = Dried_Moisture_Analysis_A.objects.filter(
#         Date_Created__month=month,
#         Date_Created__year=year
#     )

#     # Group entries by station
#     stations = entries.values_list('STATION', flat=True).distinct()

#     # Set initial vertical position
#     y_position = 800

#     # Loop through stations and generate a summary for each
#     for station in stations:
#         station_entries = entries.filter(STATION=station)
        
#         # Calculate sums for each field
#         total_quantity_of_bags = station_entries.aggregate(Sum('Quantity_of_Bags'))['Quantity_of_Bags__sum']
#         total_quantity_of_sample = station_entries.aggregate(Sum('Quantity_of_Sample'))['Quantity_of_Sample__sum']
#         total_total_weight = station_entries.aggregate(Sum('Total_Weight'))['Total_Weight__sum']
#         # Add other fields as needed

#         # Draw a summary for each station
#         y_position = draw_station_summary(p, station, total_quantity_of_bags, total_quantity_of_sample, total_total_weight, y_position)

#     p.save()

#     return response

# def draw_station_summary(pdf, station, total_quantity_of_bags, total_quantity_of_sample, total_total_weight, y_position):
#     # Customize this function based on your specific needs
#     pdf.drawString(10, y_position, f"Station: {station}")
#     pdf.drawString(10, y_position - 20, f"Total Quantity of Bags: {total_quantity_of_bags}")
#     pdf.drawString(10, y_position - 40, f"Total Quantity of Sample: {total_quantity_of_sample}")
#     pdf.drawString(10, y_position - 60, f"Total Total Weight: {total_total_weight}")
#     # Add other fields as needed
#     pdf.drawString(10, y_position - 80, "-" * 50)  # Separator line

#     # Adjust the vertical position for the next station summary
#     return y_position - 100
# from reportlab.pdfgen import canvas
# from django.http import HttpResponse
# from django.db.models import Sum
# from .models import Dried_Moisture_Analysis_A
# from datetime import datetime, timedelta
# import matplotlib.pyplot as plt
# from io import BytesIO
# import matplotlib
# matplotlib.use('Agg')

# def generate_monthly_report(request, month, year):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename=monthly_report_{month}_{year}.pdf'

#     # Create PDF document
#     p = canvas.Canvas(response)

#     # Query data for the given month and year
#     entries = Dried_Moisture_Analysis_A.objects.filter(
#         Date_Created__month=month,
#         Date_Created__year=year
#     )

#     # Set initial vertical position
#     y_position = 800

#     # Overall summary for all entries in the month
#     overall_quantity_of_bags = entries.aggregate(Sum('Quantity_of_Bags'))['Quantity_of_Bags__sum']
#     overall_quantity_of_sample = entries.aggregate(Sum('Quantity_of_Sample'))['Quantity_of_Sample__sum']
#     overall_total_weight = entries.aggregate(Sum('Total_Weight'))['Total_Weight__sum']

#     # Draw overall summary
#     y_position = draw_station_summary(p, "Overall", overall_quantity_of_bags, overall_quantity_of_sample, overall_total_weight, y_position)

#     # Group entries by station
#     stations = entries.values_list('STATION', flat=True).distinct()

#     # Loop through stations and generate a summary for each
#     for station in stations:
#         station_entries = entries.filter(STATION=station)
        
#         # Calculate sums for each field
#         total_quantity_of_bags = station_entries.aggregate(Sum('Quantity_of_Bags'))['Quantity_of_Bags__sum']
#         total_quantity_of_sample = station_entries.aggregate(Sum('Quantity_of_Sample'))['Quantity_of_Sample__sum']
#         total_total_weight = station_entries.aggregate(Sum('Total_Weight'))['Total_Weight__sum']
#         # Add other fields as needed

#         # Draw a summary for each station
#         y_position = draw_station_summary(p, station, total_quantity_of_bags, total_quantity_of_sample, total_total_weight, y_position)

#     # Generate the bar graph comparing total weight between stations
#     generate_weight_comparison_graph(p, stations, entries)

#     p.save()

#     return response

# def draw_station_summary(pdf, station, total_quantity_of_bags, total_quantity_of_sample, total_total_weight, y_position):
#     # Customize this function based on your specific needs
#     pdf.drawString(10, y_position, f"Station: {station}")
#     pdf.drawString(10, y_position - 20, f"Total Quantity of Bags: {total_quantity_of_bags}")
#     pdf.drawString(10, y_position - 40, f"Total Quantity of Sample: {total_quantity_of_sample}")
#     pdf.drawString(10, y_position - 60, f"Total Total Weight: {total_total_weight}")
#     # Add other fields as needed
#     pdf.drawString(10, y_position - 80, "-" * 50)  # Separator line

#     # Adjust the vertical position for the next station summary
#     return y_position - 100
# import os


# def generate_weight_comparison_graph(pdf, stations, entries):
#     # Filter out stations with None values
#     stations = [station for station in stations if station is not None]

#     # Create a bar graph comparing total weight between stations
#     total_weights = []

#     for station in stations:
#         station_entries = entries.filter(STATION=station)
#         total_weight = station_entries.aggregate(Sum('Total_Weight'))['Total_Weight__sum'] or 0
#         total_weights.append(total_weight)

#     # Generate the bar graph
#     plt.figure(figsize=(10, 6))
#     plt.bar(stations, total_weights, color='purple')
#     plt.title('Total Weight Comparison Between Stations')
#     plt.xlabel('Station')
#     plt.ylabel('Total Weight')
#     plt.xticks(rotation=45, ha='right')

#     # Save the plot to a temporary file
#     temp_filename = 'temp_weight_comparison_plot.png'
#     plt.savefig(temp_filename, format='png')
#     plt.close()

#     # Create a new PDF page for the graph
#     pdf.showPage()

#     # Draw the saved image on the PDF
#     pdf.drawImage(temp_filename, 100, 400, width=400, height=200)

#     # Remove the temporary file
#     os.remove(temp_filename)

#     # Move back to the original page
#     pdf.showPage()
# from reportlab.pdfgen import canvas
# from django.http import HttpResponse
# from django.db.models import Sum
# from .models import Dried_Moisture_Analysis_A
# from datetime import datetime, timedelta
# import matplotlib
# import matplotlib.pyplot as plt
# from io import BytesIO
# import os
# import warnings

# warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
# matplotlib.use('module://matplotlib.backends.backend_agg')

# def generate_monthly_report(request, month, year):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename=monthly_report_{month}_{year}.pdf'

#     # Create PDF document
#     p = canvas.Canvas(response)

#     # Query data for the given month and year
#     entries = Dried_Moisture_Analysis_A.objects.filter(
#         Date_Created__month=month,
#         Date_Created__year=year
#     )

#     # Set initial vertical position
#     y_position = 800

#     # Overall summary for all entries in the month
#     overall_quantity_of_bags = entries.aggregate(Sum('Quantity_of_Bags'))['Quantity_of_Bags__sum']
#     overall_quantity_of_sample = entries.aggregate(Sum('Quantity_of_Sample'))['Quantity_of_Sample__sum']
#     overall_total_weight = entries.aggregate(Sum('Total_Weight'))['Total_Weight__sum']

#     # Draw overall summary
#     y_position = draw_station_summary(p, "Overall", overall_quantity_of_bags, overall_quantity_of_sample, overall_total_weight, y_position)

#     # Group entries by station
#     stations = entries.values_list('STATION', flat=True).distinct()

#     # Loop through stations and generate a summary for each
#     for station in stations:
#         station_entries = entries.filter(STATION=station)
        
#         # Calculate sums for each field
#         total_quantity_of_bags = station_entries.aggregate(Sum('Quantity_of_Bags'))['Quantity_of_Bags__sum']
#         total_quantity_of_sample = station_entries.aggregate(Sum('Quantity_of_Sample'))['Quantity_of_Sample__sum']
#         total_total_weight = station_entries.aggregate(Sum('Total_Weight'))['Total_Weight__sum']
#         # Add other fields as needed

#         # Draw a summary for each station
#         y_position = draw_station_summary(p, station, total_quantity_of_bags, total_quantity_of_sample, total_total_weight, y_position)

#     # Generate the bar graph comparing total weight between stations
#     generate_weight_comparison_graph(p, stations, entries)

#     p.save()

#     return response

# def draw_station_summary(pdf, station, total_quantity_of_bags, total_quantity_of_sample, total_total_weight, y_position):
#     # Customize this function based on your specific needs
#     pdf.drawString(10, y_position, f"Station: {station}")
#     pdf.drawString(10, y_position - 20, f"Total Quantity of Bags: {total_quantity_of_bags}")
#     pdf.drawString(10, y_position - 40, f"Total Quantity of Sample: {total_quantity_of_sample}")
#     pdf.drawString(10, y_position - 60, f"Total Total Weight: {total_total_weight}")
#     # Add other fields as needed
#     pdf.drawString(10, y_position - 80, "-" * 50)  # Separator line

#     # Adjust the vertical position for the next station summary
#     return y_position - 100

# def generate_weight_comparison_graph(pdf, stations, entries):
#     # Create a bar graph comparing total weight between stations
#     total_weights = []

#     for station in stations:
#         station_entries = entries.filter(STATION=station)
#         total_weight = station_entries.aggregate(Sum('Total_Weight'))['Total_Weight__sum']
#         total_weights.append(total_weight if total_weight is not None else 0)

#     # Convert the total_weights list to ensure all values are non-None
#     total_weights = [0 if weight is None else weight for weight in total_weights]

#     # Convert the stations list to strings to avoid issues with None values
#     stations = [str(station) for station in stations]

#     # Generate the bar graph
#     plt.figure(figsize=(10, 6))
#     plt.bar(stations, total_weights, color='purple')
#     plt.title('Total Weight Comparison Between Stations')
#     plt.xlabel('Station')
#     plt.ylabel('Total Weight')
#     plt.xticks(rotation=45, ha='right')

#     # Save the plot to a temporary file
#     temp_filename = 'temp_weight_comparison_plot.png'
#     plt.savefig(temp_filename, format='png')
#     plt.close()

#     # Create a new PDF page for the graph
#     pdf.drawImage(temp_filename, 100, 100, width=400, height=200)

#     # Remove the temporary file
#     os.remove(temp_filename)

#     # Move back to the original page
#     pdf.showPage()








# from reportlab.pdfgen import canvas
# from django.http import HttpResponse
# from django.db.models import Sum
# from .models import Dried_Moisture_Analysis_A
# from datetime import datetime, timedelta
# import matplotlib
# import matplotlib.pyplot as plt
# from io import BytesIO
# import os
# import warnings

# warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
# matplotlib.use('module://matplotlib.backends.backend_agg')

# def generate_monthly_report(request, month, year):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename=monthly_report_{month}_{year}.pdf'

#     # Create PDF document
#     p = canvas.Canvas(response)

#     # Query data for the given month and year
#     entries = Dried_Moisture_Analysis_A.objects.filter(
#         Date_Created__month=month,
#         Date_Created__year=year
#     )

#     # Set initial vertical position
#     y_position = 800

#     # Overall summary for all entries in the month
#     overall_quantity_of_bags = entries.aggregate(Sum('Quantity_of_Bags'))['Quantity_of_Bags__sum']
#     overall_quantity_of_sample = entries.aggregate(Sum('Quantity_of_Sample'))['Quantity_of_Sample__sum']
#     overall_total_weight = entries.aggregate(Sum('Total_Weight'))['Total_Weight__sum']

#     # Draw overall summary
#     overall_template = "Station: {}\nTotal Quantity of Bags: {}\nTotal Quantity of Sample: {}\nTotal Total Weight: {}"
#     y_position = draw_station_summary(p, "Overall", overall_quantity_of_bags, overall_quantity_of_sample, overall_total_weight, y_position, template=overall_template)

#     # Group entries by station
#     stations = entries.values_list('STATION', flat=True).distinct()

#     # Loop through stations and generate a summary for each
#     for station in stations:
#         station_entries = entries.filter(STATION=station)
        
#         # Calculate sums for each field
#         total_quantity_of_bags = station_entries.aggregate(Sum('Quantity_of_Bags'))['Quantity_of_Bags__sum']
#         total_quantity_of_sample = station_entries.aggregate(Sum('Quantity_of_Sample'))['Quantity_of_Sample__sum']
#         total_total_weight = station_entries.aggregate(Sum('Total_Weight'))['Total_Weight__sum']

#         # Define a custom template for the station summary
       
#         station_template = "Station: {}\nTotal Quantity of Bags: {}\nTotal Quantity of Sample: {}\nTotal Total Weight: {}"
        
#         # Draw a summary for each station
#         y_position = draw_station_summary(p, station, total_quantity_of_bags, total_quantity_of_sample, total_total_weight, y_position, template=station_template)

#     # Generate the bar graph comparing total weight between stations
#     generate_weight_comparison_graph(p, stations, entries)

#     p.save()

#     return response

# def draw_station_summary(pdf, station, total_quantity_of_bags, total_quantity_of_sample, total_total_weight, y_position, template=None):
#     # Customize this function based on your specific needs
#     if template is None:
#         # Use a default template if none is provided
#         template = "Station: {}\nTotal Quantity of Bags: {}\nTotal Quantity of Sample: {}\nTotal Total Weight: {}"

#     formatted_text = template.format(station, total_quantity_of_bags, total_quantity_of_sample, total_total_weight)
    
#     # Draw the formatted text
#     pdf.drawParagraph(formatted_text, 10, y_position)

#     # Add other fields as needed
#     pdf.drawString(10, y_position - 80, "-" * 50)  # Separator line

#     # Adjust the vertical position for the next station summary
#     return y_position - 100

# def generate_weight_comparison_graph(pdf, stations, entries):
#     # Create a bar graph comparing total weight between stations
#     total_weights = []

#     for station in stations:
#         station_entries = entries.filter(STATION=station)
#         total_weight = station_entries.aggregate(Sum('Total_Weight'))['Total_Weight__sum']
#         total_weights.append(total_weight if total_weight is not None else 0)

#     # Convert the total_weights list to ensure all values are non-None
#     total_weights = [0 if weight is None else weight for weight in total_weights]

#     # Convert the stations list to strings to avoid issues with None values
#     stations = [str(station) for station in stations]

#     # Generate the bar graph
#     plt.figure(figsize=(10, 6))
#     plt.bar(stations, total_weights, color='purple')
#     plt.title('Total Weight Comparison Between Stations')
#     plt.xlabel('Station')
#     plt.ylabel('Total Weight')
#     plt.xticks(rotation=45, ha='right')

#     # Save the plot to a temporary file
#     temp_filename = 'temp_weight_comparison_plot.png'
#     plt.savefig(temp_filename, format='png')
#     plt.close()

#     # Create a new PDF page for the graph
#     pdf.drawImage(temp_filename, 100, 100, width=400, height=200)

#     # Remove the temporary file
#     os.remove(temp_filename)

#     # Move back to the original page
#     pdf.showPage()
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.db.models import Sum
from .models import Dried_Moisture_Analysis_A
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import os
import warnings
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
matplotlib.use('module://matplotlib.backends.backend_agg')

def generate_monthly_report1(request, month, year):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=monthly_report_{month}_{year}.pdf'

    # Create PDF document
    p = canvas.Canvas(response)

    # Get the first day of the current month
    first_day_current_month = datetime(int(year), int(month), 1)

    # Get the last day of the previous month
    last_day_previous_month = first_day_current_month - timedelta(days=1)

    # Query data for the current month and last month
    current_month_entries = Dried_Moisture_Analysis_A.objects.filter(
        Date_Created__month=month,
        Date_Created__year=year
    )

    last_month_entries = Dried_Moisture_Analysis_A.objects.filter(
        Date_Created__month=last_day_previous_month.month,
        Date_Created__year=last_day_previous_month.year
    )

    # Set initial vertical position
    y_position = 800

    # Overall summary for all entries in the current month
    overall_quantity_of_bags_this_month = current_month_entries.aggregate(Sum('Quantity_of_Bags'))['Quantity_of_Bags__sum']
    overall_quantity_of_sample_this_month = current_month_entries.aggregate(Sum('Quantity_of_Sample'))['Quantity_of_Sample__sum']
    overall_total_weight_this_month = current_month_entries.aggregate(Sum('Total_Weight'))['Total_Weight__sum']

    # Overall summary for all entries in the last month
    overall_quantity_of_bags_last_month = last_month_entries.aggregate(Sum('Quantity_of_Bags'))['Quantity_of_Bags__sum']
    overall_quantity_of_sample_last_month = last_month_entries.aggregate(Sum('Quantity_of_Sample'))['Quantity_of_Sample__sum']
    overall_total_weight_last_month = last_month_entries.aggregate(Sum('Total_Weight'))['Total_Weight__sum']

    # Draw overall summary for this month and last month
    overall_template = (
        "{} Summary of December\n"
        "Total bags acquired over the month: {}\n"
        "Total samples acquired over the month: {}\n"
        "Total Total Weight: {}\n"
        "Difference from last month:\n"
        "  Quantity of Bags: {}\n"
        "  Quantity of Sample: {}\n"
        "  Total Weight: {}"
    )
    y_position = draw_station_summary(
        p,
        "Overall",
        overall_quantity_of_bags_this_month,
        overall_quantity_of_sample_this_month,
        overall_total_weight_this_month,
        y_position,
        template=overall_template,
        diff_quantity_of_bags=(
            overall_quantity_of_bags_this_month - overall_quantity_of_bags_last_month
            if overall_quantity_of_bags_last_month is not None else 0
        ),
        diff_quantity_of_sample=(
            overall_quantity_of_sample_this_month - overall_quantity_of_sample_last_month
            if overall_quantity_of_sample_last_month is not None else 0
        ),
        diff_total_weight=(
            overall_total_weight_this_month - overall_total_weight_last_month
            if overall_total_weight_last_month is not None else 0
        )
    )

    # Group entries by station
    stations = current_month_entries.values_list('STATION', flat=True).distinct()

    # Loop through stations and generate a summary for each
    for station in stations:
        station_entries_current_month = current_month_entries.filter(STATION=station)
        station_entries_last_month = last_month_entries.filter(STATION=station)

        # Calculate sums for each field
        total_quantity_of_bags_current_month = station_entries_current_month.aggregate(Sum('Quantity_of_Bags'))['Quantity_of_Bags__sum']
        total_quantity_of_sample_current_month = station_entries_current_month.aggregate(Sum('Quantity_of_Sample'))['Quantity_of_Sample__sum']
        total_total_weight_current_month = station_entries_current_month.aggregate(Sum('Total_Weight'))['Total_Weight__sum']

        total_quantity_of_bags_last_month = station_entries_last_month.aggregate(Sum('Quantity_of_Bags'))['Quantity_of_Bags__sum']
        total_quantity_of_sample_last_month = station_entries_last_month.aggregate(Sum('Quantity_of_Sample'))['Quantity_of_Sample__sum']
        total_total_weight_last_month = station_entries_last_month.aggregate(Sum('Total_Weight'))['Total_Weight__sum']

        # Define a custom template for the station summary
        station_template = (
            "Summary of {} Station \n"
            "Total bags acquired over the month: {}\n"
            "Total samples acquired over the month: {}\n"
            "Total Weight: {}\n"
            "Difference from last month:\n"
            "  Quantity of Bags: {}\n"
            "  Quantity of Sample: {}\n"
            "  Total Weight: {}"
        )

        # Draw a summary for each station
        y_position = draw_station_summary(
            p,
            station,
            total_quantity_of_bags_current_month,
            total_quantity_of_sample_current_month,
            total_total_weight_current_month,
            y_position,
            template=station_template,
            diff_quantity_of_bags=(
                total_quantity_of_bags_current_month - total_quantity_of_bags_last_month
                if total_quantity_of_bags_last_month is not None else 0
            ),
            diff_quantity_of_sample=(
                total_quantity_of_sample_current_month - total_quantity_of_sample_last_month
                if total_quantity_of_sample_last_month is not None else 0
            ),
            diff_total_weight=(
                total_total_weight_current_month - total_total_weight_last_month
                if total_total_weight_last_month is not None else 0
            )
        )

    # Generate the bar graph comparing total weight between stations
    generate_weight_comparison_graph(p, stations, current_month_entries)

    p.save()

    return response

def draw_station_summary(pdf, station, total_quantity_of_bags, total_quantity_of_sample, total_total_weight, y_position, template=None, diff_quantity_of_bags=0, diff_quantity_of_sample=0, diff_total_weight=0):
    # Customize this function based on your specific needs
    if template is None:
        # Use a default template if none is provided
        template = (
            "Summary of {} Station \n"
            "Total bags acquired over the month: {}\n"
            "Total samples acquired over the month: {}\n"
            "Total Weight: {}\n"
            "Difference from last month:\n"
            "  Quantity of Bags: {}\n"
            "  Quantity of Sample: {}\n"
            "  Total Weight: {}"
        )

    # Check if "{}" appears in the template
    if "{}" in template:
        # Adjust the vertical position for the first line
        y_position -= 12

    formatted_text = template.format(
        station,
        total_quantity_of_bags,
        total_quantity_of_sample,
        total_total_weight,
        diff_quantity_of_bags,
        diff_quantity_of_sample,
        diff_total_weight
    )

    # Create a TextObject to handle line breaks
    text_object = pdf.beginText(10, y_position)
    text_object.setFont("Helvetica", 12)

    # Split the formatted text into lines
    lines = formatted_text.split('\n')

    # Add each line to the TextObject
    for line in lines:
        text_object.textLine(line)

    # Draw the TextObject on the PDF
    pdf.drawText(text_object)

    # Add the separator line after drawing the text block
    separator_line_position = y_position - len(lines) * 14
    pdf.drawString(10, separator_line_position, "-" * 50)

    # Adjust the vertical position for the next station summary
    return separator_line_position - 20  # Adjust this value as needed

def generate_weight_comparison_graph(pdf, stations, entries):
    # Create a bar graph comparing total weight between stations
    total_weights = []

    for station in stations:
        station_entries = entries.filter(STATION=station)
        total_weight = station_entries.aggregate(Sum('Total_Weight'))['Total_Weight__sum']
        total_weights.append(total_weight if total_weight is not None else 0)

    # Convert the total_weights list to ensure all values are non-None
    total_weights = [0 if weight is None else weight for weight in total_weights]

    # Convert the stations list to strings to avoid issues with None values
    stations = [str(station) for station in stations]

    # Generate the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(stations, total_weights, color='purple')
    plt.title('Total Weight Comparison Between Stations')
    plt.xlabel('Station')
    plt.ylabel('Total Weight')
    plt.xticks(rotation=45, ha='right')

    # Save the plot to a temporary file
    temp_filename = 'temp_weight_comparison_plot.png'
    plt.savefig(temp_filename, format='png')
    plt.close()

    # Create a new PDF page for the graph
    pdf.drawImage(temp_filename, 100, 5, width=400, height=200)

    # Remove the temporary file
    os.remove(temp_filename)

    # Move back to the original page
    pdf.showPage()

    return pdf














from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.db.models import Sum
from .models import Dried_Moisture_Analysis_B  # Import the new model
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import os
import warnings
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
matplotlib.use('module://matplotlib.backends.backend_agg')

def generate_monthly_report2(request, month, year):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=monthly_report_{month}_{year}.pdf'

    # Create PDF document
    p = canvas.Canvas(response)

    # Get the first day of the current month
    first_day_current_month = datetime(int(year), int(month), 1)

    # Get the last day of the previous month
    last_day_previous_month = first_day_current_month - timedelta(days=1)

    # Query data for the current month and last month for the new model
    current_month_entries = Dried_Moisture_Analysis_B.objects.filter(
        Date_Created__month=month,
        Date_Created__year=year
    )

    last_month_entries = Dried_Moisture_Analysis_B.objects.filter(
        Date_Created__month=last_day_previous_month.month,
        Date_Created__year=last_day_previous_month.year
    )

    # Set initial vertical position
    y_position = 800

    # Overall summary for all entries in the current month
    overall_initial_sample_weight_this_month = current_month_entries.aggregate(Sum('Initial_Sample_Weight'))['Initial_Sample_Weight__sum']
    overall_final_sample_weight_this_month = current_month_entries.aggregate(Sum('Final_Sample_Weight'))['Final_Sample_Weight__sum']

    # Overall summary for all entries in the last month
    overall_initial_sample_weight_last_month = last_month_entries.aggregate(Sum('Initial_Sample_Weight'))['Initial_Sample_Weight__sum']
    overall_final_sample_weight_last_month = last_month_entries.aggregate(Sum('Final_Sample_Weight'))['Final_Sample_Weight__sum']

    # Draw overall summary for this month and last month for the new model
    overall_template = (
        "{} Summary of December\n"
        "Total Initial Sample Weight acquired over the month: {}\n"
        "Total Final Sample Weight acquired over the month: {}\n"
        "Difference from last month:\n"
        "  Initial Sample Weight: {}\n"
        "  Final Sample Weight: {}"
    )
    y_position = draw_station_summary2(
        p,
        "Overall",
        overall_initial_sample_weight_this_month,
        overall_final_sample_weight_this_month,
        y_position,
        template=overall_template,
        diff_initial_sample_weight=(
            overall_initial_sample_weight_this_month - overall_initial_sample_weight_last_month
            if overall_initial_sample_weight_last_month is not None else 0
        ),
        diff_final_sample_weight=(
            overall_final_sample_weight_this_month - overall_final_sample_weight_last_month
            if overall_final_sample_weight_last_month is not None else 0
        ),
    )

    # Group entries by station for the new model
    stations = current_month_entries.values_list('STATION', flat=True).distinct()

    # Loop through stations and generate a summary for each for the new model
    for station in stations:
        station_entries_current_month = current_month_entries.filter(STATION=station)
        station_entries_last_month = last_month_entries.filter(STATION=station)

        # Calculate sums for each field for the new model
        total_initial_sample_weight_current_month = station_entries_current_month.aggregate(Sum('Initial_Sample_Weight'))['Initial_Sample_Weight__sum']
        total_final_sample_weight_current_month = station_entries_current_month.aggregate(Sum('Final_Sample_Weight'))['Final_Sample_Weight__sum']

        total_initial_sample_weight_last_month = station_entries_last_month.aggregate(Sum('Initial_Sample_Weight'))['Initial_Sample_Weight__sum']
        total_final_sample_weight_last_month = station_entries_last_month.aggregate(Sum('Final_Sample_Weight'))['Final_Sample_Weight__sum']

        # Define a custom template for the station summary for the new model
        station_template = (
            "Summary of {} Station \n"
            "Total Initial Sample Weight acquired over the month: {}\n"
            "Total Final Sample Weight acquired over the month: {}\n"
            "Difference from last month:\n"
            "  Initial Sample Weight: {}\n"
            "  Final Sample Weight: {}"
        )

        # Draw a summary for each station for the new model
        y_position = draw_station_summary2(
            p,
            station,
            total_initial_sample_weight_current_month,
            total_final_sample_weight_current_month,
            y_position,
            template=station_template,
            diff_initial_sample_weight=(
                total_initial_sample_weight_current_month - total_initial_sample_weight_last_month
                if total_initial_sample_weight_last_month is not None else 0
            ),
            diff_final_sample_weight=(
                total_final_sample_weight_current_month - total_final_sample_weight_last_month
                if total_final_sample_weight_last_month is not None else 0
            ),
        )

    # Generate the bar graph comparing final sample weight between stations for the new model
    generate_weight_comparison_graph2(p, stations, current_month_entries, field='Final_Sample_Weight')

    p.save()

    return response

def draw_station_summary2(pdf, station, total_initial_sample_weight, total_final_sample_weight, y_position, template=None, diff_initial_sample_weight=0, diff_final_sample_weight=0):
    # Customize this function based on your specific needs
    if template is None:
        # Use a default template if none is provided
        template = (
            "Summary of {} Station \n"
            "Total Initial Sample Weight acquired over the month: {}\n"
            "Total Final Sample Weight acquired over the month: {}\n"
            "Difference from last month:\n"
            "  Initial Sample Weight: {}\n"
            "  Final Sample Weight: {}"
        )

    # Check if "{}" appears in the template
    if "{}" in template:
        # Adjust the vertical position for the first line
        y_position -= 12

    formatted_text = template.format(
        station,
        total_initial_sample_weight,
        total_final_sample_weight,
        diff_initial_sample_weight,
        diff_final_sample_weight
    )

    # Create a TextObject to handle line breaks
    text_object = pdf.beginText(10, y_position)
    text_object.setFont("Helvetica", 12)

    # Split the formatted text into lines
    lines = formatted_text.split('\n')

    # Add each line to the TextObject
    for line in lines:
        text_object.textLine(line)

    # Draw the TextObject on the PDF
    pdf.drawText(text_object)

    # Add the separator line after drawing the text block
    separator_line_position = y_position - len(lines) * 14
    pdf.drawString(10, separator_line_position, "-" * 50)

    # Adjust the vertical position for the next station summary
    return separator_line_position - 20  # Adjust this value as needed

def generate_weight_comparison_graph2(pdf, stations, entries, field):
    # Create a bar graph comparing the specified field between stations for the new model
    total_weights = []

    for station in stations:
        station_entries = entries.filter(STATION=station)
        total_weight = station_entries.aggregate(Sum(field))[f'{field}__sum']
        total_weights.append(total_weight if total_weight is not None else 0)

    # Convert the total_weights list to ensure all values are non-None
    total_weights = [0 if weight is None else weight for weight in total_weights]

    # Convert the stations list to strings to avoid issues with None values
    stations = [str(station) for station in stations]

    # Generate the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(stations, total_weights, color='purple')
    plt.title(f'Total {field} Comparison Between Stations')
    plt.xlabel('Station')
    plt.ylabel(f'Total {field}')
    plt.xticks(rotation=45, ha='right')

    # Save the plot to a temporary file
    temp_filename = f'temp_{field}_comparison_plot.png'
    plt.savefig(temp_filename, format='png')
    plt.close()

    # Create a new PDF page for the graph
    pdf.drawImage(temp_filename, 100, 5, width=400, height=200)

    # Remove the temporary file
    os.remove(temp_filename)

    # Move back to the original page
    pdf.showPage()

    return pdf




















from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.db.models import Sum
from .models import Floated_Moisture_Analysis_A
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import os
import warnings
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
matplotlib.use('module://matplotlib.backends.backend_agg')

def generate_monthly_report3(request, month, year):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=monthly_report_floated_{month}_{year}.pdf'

    # Create PDF document
    p = canvas.Canvas(response)

    # Get the first day of the current month
    first_day_current_month = datetime(int(year), int(month), 1)

    # Get the last day of the previous month
    last_day_previous_month = first_day_current_month - timedelta(days=1)

    # Query data for the current month and last month for the Floated_Moisture_Analysis_A model
    current_month_entries = Floated_Moisture_Analysis_A.objects.filter(
        Date_Created__month=month,
        Date_Created__year=year
    )

    last_month_entries = Floated_Moisture_Analysis_A.objects.filter(
        Date_Created__month=last_day_previous_month.month,
        Date_Created__year=last_day_previous_month.year
    )

    # Set initial vertical position
    y_position = 800

    # Overall summary for all entries in the current month
    overall_quantity_of_sample_H_this_month = current_month_entries.aggregate(Sum('Quantity_of_Sample_H'))['Quantity_of_Sample_H__sum']
    overall_total_weight_H_this_month = current_month_entries.aggregate(Sum('Total_Weight_H'))['Total_Weight_H__sum']
    overall_initial_sample_weight_H_this_month = current_month_entries.aggregate(Sum('Initial_Sample_Weight_H'))['Initial_Sample_Weight_H__sum']

    overall_quantity_of_sample_L_this_month = current_month_entries.aggregate(Sum('Quantity_of_Sample_L'))['Quantity_of_Sample_L__sum']
    overall_total_weight_L_this_month = current_month_entries.aggregate(Sum('Total_Weight_L'))['Total_Weight_L__sum']
    overall_initial_sample_weight_L_this_month = current_month_entries.aggregate(Sum('Initial_Sample_Weight_L'))['Initial_Sample_Weight_L__sum']

    # Overall summary for all entries in the last month
    overall_quantity_of_sample_H_last_month = last_month_entries.aggregate(Sum('Quantity_of_Sample_H'))['Quantity_of_Sample_H__sum']
    overall_total_weight_H_last_month = last_month_entries.aggregate(Sum('Total_Weight_H'))['Total_Weight_H__sum']
    overall_initial_sample_weight_H_last_month = last_month_entries.aggregate(Sum('Initial_Sample_Weight_H'))['Initial_Sample_Weight_H__sum']

    overall_quantity_of_sample_L_last_month = last_month_entries.aggregate(Sum('Quantity_of_Sample_L'))['Quantity_of_Sample_L__sum']
    overall_total_weight_L_last_month = last_month_entries.aggregate(Sum('Total_Weight_L'))['Total_Weight_L__sum']
    overall_initial_sample_weight_L_last_month = last_month_entries.aggregate(Sum('Initial_Sample_Weight_L'))['Initial_Sample_Weight_L__sum']

    # Draw overall summary for this month and last month for the Floated_Moisture_Analysis_A model
    overall_template = (
        "{} Summary of December\n"
        "Total High Quantity of Sample acquired over the month: {}\n"
        "Total High Total Weight acquired over the month: {}\n"
        "Total High Initial Sample Weight acquired over the month: {}\n"
        "Total Low Quantity of Sample acquired over the month: {}\n"
        "Total Low Total Weight acquired over the month: {}\n"
        "Total Low Initial Sample Weight acquired over the month: {}\n"
        "Difference from last month:\n"
        "  High Quantity of Sample: {}\n"
        "  High Total Weight: {}\n"
        "  High Initial Sample Weight: {}\n"
        "  Low Quantity of Sample: {}\n"
        "  Low Total Weight: {}\n"
        "  Low Initial Sample Weight: {}"
    )
    y_position = draw_station_summary_floated(
        p,
        "Overall",
        overall_quantity_of_sample_H_this_month,
        overall_total_weight_H_this_month,
        overall_initial_sample_weight_H_this_month,
        overall_quantity_of_sample_L_this_month,
        overall_total_weight_L_this_month,
        overall_initial_sample_weight_L_this_month,
        y_position,
        template=overall_template,
        diff_quantity_of_sample_H=(
            overall_quantity_of_sample_H_this_month - overall_quantity_of_sample_H_last_month
            if overall_quantity_of_sample_H_last_month is not None else 0
        ),
        diff_total_weight_H=(
            overall_total_weight_H_this_month - overall_total_weight_H_last_month
            if overall_total_weight_H_last_month is not None else 0
        ),
        diff_initial_sample_weight_H=(
            overall_initial_sample_weight_H_this_month - overall_initial_sample_weight_H_last_month
            if overall_initial_sample_weight_H_last_month is not None else 0
        ),
        diff_quantity_of_sample_L=(
            overall_quantity_of_sample_L_this_month - overall_quantity_of_sample_L_last_month
            if overall_quantity_of_sample_L_last_month is not None else 0
        ),
        diff_total_weight_L=(
            overall_total_weight_L_this_month - overall_total_weight_L_last_month
            if overall_total_weight_L_last_month is not None else 0
        ),
        diff_initial_sample_weight_L=(
            overall_initial_sample_weight_L_this_month - overall_initial_sample_weight_L_last_month
            if overall_initial_sample_weight_L_last_month is not None else 0
        ),
    )

    # Group entries by station for the Floated_Moisture_Analysis_A model
    stations = current_month_entries.values_list('STATION', flat=True).distinct()

    # Loop through stations and generate a summary for each for the Floated_Moisture_Analysis_A model
    for station in stations:
        station_entries_current_month = current_month_entries.filter(STATION=station)
        station_entries_last_month = last_month_entries.filter(STATION=station)

        # Calculate sums for each field for the Floated_Moisture_Analysis_A model
        total_quantity_of_sample_H_current_month = station_entries_current_month.aggregate(Sum('Quantity_of_Sample_H'))['Quantity_of_Sample_H__sum']
        total_total_weight_H_current_month = station_entries_current_month.aggregate(Sum('Total_Weight_H'))['Total_Weight_H__sum']
        total_initial_sample_weight_H_current_month = station_entries_current_month.aggregate(Sum('Initial_Sample_Weight_H'))['Initial_Sample_Weight_H__sum']

        total_quantity_of_sample_L_current_month = station_entries_current_month.aggregate(Sum('Quantity_of_Sample_L'))['Quantity_of_Sample_L__sum']
        total_total_weight_L_current_month = station_entries_current_month.aggregate(Sum('Total_Weight_L'))['Total_Weight_L__sum']
        total_initial_sample_weight_L_current_month = station_entries_current_month.aggregate(Sum('Initial_Sample_Weight_L'))['Initial_Sample_Weight_L__sum']

        total_quantity_of_sample_H_last_month = station_entries_last_month.aggregate(Sum('Quantity_of_Sample_H'))['Quantity_of_Sample_H__sum']
        total_total_weight_H_last_month = station_entries_last_month.aggregate(Sum('Total_Weight_H'))['Total_Weight_H__sum']
        total_initial_sample_weight_H_last_month = station_entries_last_month.aggregate(Sum('Initial_Sample_Weight_H'))['Initial_Sample_Weight_H__sum']

        total_quantity_of_sample_L_last_month = station_entries_last_month.aggregate(Sum('Quantity_of_Sample_L'))['Quantity_of_Sample_L__sum']
        total_total_weight_L_last_month = station_entries_last_month.aggregate(Sum('Total_Weight_L'))['Total_Weight_L__sum']
        total_initial_sample_weight_L_last_month = station_entries_last_month.aggregate(Sum('Initial_Sample_Weight_L'))['Initial_Sample_Weight_L__sum']

        # Define a custom template for the station summary for the Floated_Moisture_Analysis_A model
        station_template = (
            "Summary of {} Station \n"
            "Total High Quantity of Sample acquired over the month: {}\n"
            "Total High Total Weight acquired over the month: {}\n"
            "Total High Initial Sample Weight acquired over the month: {}\n"
            "Total Low Quantity of Sample acquired over the month: {}\n"
            "Total Low Total Weight acquired over the month: {}\n"
            "Total Low Initial Sample Weight acquired over the month: {}\n"
            "Difference from last month:\n"
            "  High Quantity of Sample: {}\n"
            "  High Total Weight: {}\n"
            "  High Initial Sample Weight: {}\n"
            "  Low Quantity of Sample: {}\n"
            "  Low Total Weight: {}\n"
            "  Low Initial Sample Weight: {}"
        )

        # Draw a summary for each station for the Floated_Moisture_Analysis_A model
        y_position = draw_station_summary_floated(
            p,
            station,
            total_quantity_of_sample_H_current_month,
            total_total_weight_H_current_month,
            total_initial_sample_weight_H_current_month,
            total_quantity_of_sample_L_current_month,
            total_total_weight_L_current_month,
            total_initial_sample_weight_L_current_month,
            y_position,
            template=station_template,
            diff_quantity_of_sample_H=(
                total_quantity_of_sample_H_current_month - total_quantity_of_sample_H_last_month
                if total_quantity_of_sample_H_last_month is not None else 0
            ),
            diff_total_weight_H=(
                total_total_weight_H_current_month - total_total_weight_H_last_month
                if total_total_weight_H_last_month is not None else 0
            ),
            diff_initial_sample_weight_H=(
                total_initial_sample_weight_H_current_month - total_initial_sample_weight_H_last_month
                if total_initial_sample_weight_H_last_month is not None else 0
            ),
            diff_quantity_of_sample_L=(
                total_quantity_of_sample_L_current_month - total_quantity_of_sample_L_last_month
                if total_quantity_of_sample_L_last_month is not None else 0
            ),
            diff_total_weight_L=(
                total_total_weight_L_current_month - total_total_weight_L_last_month
                if total_total_weight_L_last_month is not None else 0
            ),
            diff_initial_sample_weight_L=(
                total_initial_sample_weight_L_current_month - total_initial_sample_weight_L_last_month
                if total_initial_sample_weight_L_last_month is not None else 0
            ),
        )

    # Generate the bar graph comparing total weight between stations for the Floated_Moisture_Analysis_A model
    # generate_weight_comparison_graph_floated(p, stations, current_month_entries, 'Total_Weight_H')
    # generate_weight_comparison_graph_floated(p, stations, current_month_entries, 'Total_Weight_L')

    p.save()

    return response

def draw_station_summary_floated(pdf, station, quantity_of_sample_H, total_weight_H, initial_sample_weight_H, quantity_of_sample_L, total_weight_L, initial_sample_weight_L, y_position, template=None, diff_quantity_of_sample_H=0, diff_total_weight_H=0, diff_initial_sample_weight_H=0, diff_quantity_of_sample_L=0, diff_total_weight_L=0, diff_initial_sample_weight_L=0):
    # Customize this function based on your specific needs
    if template is None:
        # Use a default template if none is provided
        template = (
            "Summary of {} Station \n"
            "Total High Quantity of Sample acquired over the month: {}\n"
            "Total High Total Weight acquired over the month: {}\n"
            "Total High Initial Sample Weight acquired over the month: {}\n"
            "Total Low Quantity of Sample acquired over the month: {}\n"
            "Total Low Total Weight acquired over the month: {}\n"
            "Total Low Initial Sample Weight acquired over the month: {}\n"
            "Difference from last month:\n"
            "  High Quantity of Sample: {}\n"
            "  High Total Weight: {}\n"
            "  High Initial Sample Weight: {}\n"
            "  Low Quantity of Sample: {}\n"
            "  Low Total Weight: {}\n"
            "  Low Initial Sample Weight: {}"
        )

    # Check if "{}" appears in the template
    if "{}" in template:
        # Adjust the vertical position for the first line
        y_position -= 12

    formatted_text = template.format(
        station,
        quantity_of_sample_H,
        total_weight_H,
        initial_sample_weight_H,
        quantity_of_sample_L,
        total_weight_L,
        initial_sample_weight_L,
        diff_quantity_of_sample_H,
        diff_total_weight_H,
        diff_initial_sample_weight_H,
        diff_quantity_of_sample_L,
        diff_total_weight_L,
        diff_initial_sample_weight_L
    )

    # Create a TextObject to handle line breaks
    text_object = pdf.beginText(10, y_position)
    text_object.setFont("Helvetica", 12)

    # Split the formatted text into lines
    lines = formatted_text.split('\n')

    # Add each line to the TextObject
    for line in lines:
        text_object.textLine(line)

    # Draw the TextObject on the PDF
    pdf.drawText(text_object)

    # Add the separator line after drawing the text block
    separator_line_position = y_position - len(lines) * 14
    pdf.drawString(10, separator_line_position, "-" * 50)

    # Adjust the vertical position for the next station summary
    return separator_line_position - 20  # Adjust this value as needed

def generate_weight_comparison_graph_floated(pdf, stations, entries, field):
    # Create a bar graph comparing the specified field between stations for the Floated_Moisture_Analysis_A model
    total_weights = []

    for station in stations:
        station_entries = entries.filter(STATION=station)
        total_weight = station_entries.aggregate(Sum(field))[f'{field}__sum']
        total_weights.append(total_weight if total_weight is not None else 0)

    # Convert the total_weights list to ensure all values are non-None
    total_weights = [0 if weight is None else weight for weight in total_weights]

    # Convert the stations list to strings to avoid issues with None values
    stations = [str(station) for station in stations]

    # Generate the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(stations, total_weights, color='purple')
    plt.title(f'Total {field} Comparison Between Stations')
    plt.xlabel('Station')
    plt.ylabel(f'Total {field}')
    plt.xticks(rotation=45, ha='right')

    # Save the plot to a temporary file
    temp_filename = f'temp_{field}_comparison_plot.png'
    plt.savefig(temp_filename, format='png')
    plt.close()

    # Create a new PDF page for the graph
    pdf.drawImage(temp_filename, 100, 5, width=400, height=200)

    # Remove the temporary file
    os.remove(temp_filename)

    # Move back to the original page
    pdf.showPage()

    return pdf












from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.db.models import Sum
from .models import Floated_Moisture_Analysis_B
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import os
import warnings
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
matplotlib.use('module://matplotlib.backends.backend_agg')

def generate_monthly_report4(request, month, year):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=monthly_report_{month}_{year}.pdf'

    # Create PDF document
    p = canvas.Canvas(response)

    # Get the first day of the current month
    first_day_current_month = datetime(int(year), int(month), 1)

    # Get the last day of the previous month
    last_day_previous_month = first_day_current_month - timedelta(days=1)

    # Query data for the current month and last month
    current_month_entries = Floated_Moisture_Analysis_B.objects.filter(
        Date_Created__month=month,
        Date_Created__year=year
    )

    last_month_entries = Floated_Moisture_Analysis_B.objects.filter(
        Date_Created__month=last_day_previous_month.month,
        Date_Created__year=last_day_previous_month.year
    )

    # Set initial vertical position
    y_position = 800

    # Overall summary for all entries in the current month
    overall_total_quantity_of_bags_in_non_compliance_H_this_month = current_month_entries.aggregate(Sum('Total_Quantity_of_Bags_in_Non_Compliance_H'))['Total_Quantity_of_Bags_in_Non_Compliance_H__sum']
    overall_total_weight_of_nutmeg_in_non_compliance_H_this_month = current_month_entries.aggregate(Sum('Total_Weight_of_Nutmeg_in_Non_Compliance_H'))['Total_Weight_of_Nutmeg_in_Non_Compliance_H__sum']
    overall_additional_drying_period_days_H_this_month = current_month_entries.aggregate(Sum('Additional_Drying_Period_days_H'))['Additional_Drying_Period_days_H__sum']
    overall_total_weight_H_this_month = current_month_entries.aggregate(Sum('Total_Weight_H'))['Total_Weight_H__sum']

    # Overall summary for all entries in the last month
    overall_total_quantity_of_bags_in_non_compliance_H_last_month = last_month_entries.aggregate(Sum('Total_Quantity_of_Bags_in_Non_Compliance_H'))['Total_Quantity_of_Bags_in_Non_Compliance_H__sum']
    overall_total_weight_of_nutmeg_in_non_compliance_H_last_month = last_month_entries.aggregate(Sum('Total_Weight_of_Nutmeg_in_Non_Compliance_H'))['Total_Weight_of_Nutmeg_in_Non_Compliance_H__sum']
    overall_additional_drying_period_days_H_last_month = last_month_entries.aggregate(Sum('Additional_Drying_Period_days_H'))['Additional_Drying_Period_days_H__sum']
    overall_total_weight_H_last_month = last_month_entries.aggregate(Sum('Total_Weight_H'))['Total_Weight_H__sum']

    # Draw overall summary for this month and last month
    overall_template = (
        "{} Summary of December\n"
        "Total Quantity of Bags in Non-Compliance (High): {}\n"
        "Total Weight of Nutmeg in Non-Compliance (High): {}\n"
        "Total Additional Drying Period Days (High): {}\n"
        "Total Weight (High): {}\n"
        "Difference from last month:\n"
        "  Quantity of Bags (High): {}\n"
        "  Weight of Nutmeg (High): {}\n"
        "  Additional Drying Period Days (High): {}\n"
        "  Total Weight (High): {}"
    )
    y_position = draw_station_summary4(
        p,
        "Overall",
        overall_total_quantity_of_bags_in_non_compliance_H_this_month,
        overall_total_weight_of_nutmeg_in_non_compliance_H_this_month,
        overall_additional_drying_period_days_H_this_month,
        overall_total_weight_H_this_month,
        y_position,
        template=overall_template,
        diff_total_quantity_of_bags_in_non_compliance_H=(
            overall_total_quantity_of_bags_in_non_compliance_H_this_month - overall_total_quantity_of_bags_in_non_compliance_H_last_month
            if overall_total_quantity_of_bags_in_non_compliance_H_last_month is not None else 0
        ),
        diff_total_weight_of_nutmeg_in_non_compliance_H=(
            overall_total_weight_of_nutmeg_in_non_compliance_H_this_month - overall_total_weight_of_nutmeg_in_non_compliance_H_last_month
            if overall_total_weight_of_nutmeg_in_non_compliance_H_last_month is not None else 0
        ),
        diff_additional_drying_period_days_H=(
            overall_additional_drying_period_days_H_this_month - overall_additional_drying_period_days_H_last_month
            if overall_additional_drying_period_days_H_last_month is not None else 0
        ),
        diff_total_weight_H=(
            overall_total_weight_H_this_month - overall_total_weight_H_last_month
            if overall_total_weight_H_last_month is not None else 0
        )
    )

    # Group entries by station
    stations = current_month_entries.values_list('STATION', flat=True).distinct()

    # Loop through stations and generate a summary for each
    for station in stations:
        station_entries_current_month = current_month_entries.filter(STATION=station)
        station_entries_last_month = last_month_entries.filter(STATION=station)

        # Calculate sums for each field
        total_quantity_of_bags_in_non_compliance_H_current_month = station_entries_current_month.aggregate(Sum('Total_Quantity_of_Bags_in_Non_Compliance_H'))['Total_Quantity_of_Bags_in_Non_Compliance_H__sum']
        total_weight_of_nutmeg_in_non_compliance_H_current_month = station_entries_current_month.aggregate(Sum('Total_Weight_of_Nutmeg_in_Non_Compliance_H'))['Total_Weight_of_Nutmeg_in_Non_Compliance_H__sum']
        additional_drying_period_days_H_current_month = station_entries_current_month.aggregate(Sum('Additional_Drying_Period_days_H'))['Additional_Drying_Period_days_H__sum']
        total_weight_H_current_month = station_entries_current_month.aggregate(Sum('Total_Weight_H'))['Total_Weight_H__sum']

        total_quantity_of_bags_in_non_compliance_H_last_month = station_entries_last_month.aggregate(Sum('Total_Quantity_of_Bags_in_Non_Compliance_H'))['Total_Quantity_of_Bags_in_Non_Compliance_H__sum']
        total_weight_of_nutmeg_in_non_compliance_H_last_month = station_entries_last_month.aggregate(Sum('Total_Weight_of_Nutmeg_in_Non_Compliance_H'))['Total_Weight_of_Nutmeg_in_Non_Compliance_H__sum']
        additional_drying_period_days_H_last_month = station_entries_last_month.aggregate(Sum('Additional_Drying_Period_days_H'))['Additional_Drying_Period_days_H__sum']
        total_weight_H_last_month = station_entries_last_month.aggregate(Sum('Total_Weight_H'))['Total_Weight_H__sum']

        # Define a custom template for the station summary
        station_template = (
            "Summary of {} Station \n"
            "Total Quantity of Bags in Non-Compliance (High): {}\n"
            "Total Weight of Nutmeg in Non-Compliance (High): {}\n"
            "Total Additional Drying Period Days (High): {}\n"
            "Total Weight (High): {}\n"
            "Difference from last month:\n"
            "  Quantity of Bags (High): {}\n"
            "  Weight of Nutmeg (High): {}\n"
            "  Additional Drying Period Days (High): {}\n"
            "  Total Weight (High): {}"
        )

        # Draw a summary for each station
        y_position = draw_station_summary4(
            p,
            station,
            total_quantity_of_bags_in_non_compliance_H_current_month,
            total_weight_of_nutmeg_in_non_compliance_H_current_month,
            additional_drying_period_days_H_current_month,
            total_weight_H_current_month,
            y_position,
            template=station_template,
            diff_total_quantity_of_bags_in_non_compliance_H=(
                total_quantity_of_bags_in_non_compliance_H_current_month - total_quantity_of_bags_in_non_compliance_H_last_month
                if total_quantity_of_bags_in_non_compliance_H_last_month is not None else 0
            ),
            diff_total_weight_of_nutmeg_in_non_compliance_H=(
                total_weight_of_nutmeg_in_non_compliance_H_current_month - total_weight_of_nutmeg_in_non_compliance_H_last_month
                if total_weight_of_nutmeg_in_non_compliance_H_last_month is not None else 0
            ),
            diff_additional_drying_period_days_H=(
                additional_drying_period_days_H_current_month - additional_drying_period_days_H_last_month
                if additional_drying_period_days_H_last_month is not None else 0
            ),
            diff_total_weight_H=(
                total_weight_H_current_month - total_weight_H_last_month
                if total_weight_H_last_month is not None else 0
            )
        )

    # Generate the bar graph comparing total weight between stations
    generate_weight_comparison_graph4(p, stations, current_month_entries, 'Total_Weight_H')

    p.save()

    return response

def draw_station_summary4(pdf, station, total_quantity_of_bags_in_non_compliance_H, total_weight_of_nutmeg_in_non_compliance_H, additional_drying_period_days_H, total_weight_H, y_position, template=None, diff_total_quantity_of_bags_in_non_compliance_H=0, diff_total_weight_of_nutmeg_in_non_compliance_H=0, diff_additional_drying_period_days_H=0, diff_total_weight_H=0):
    # Customize this function based on your specific needs
    if template is None:
        # Use a default template if none is provided
        template = (
            "Summary of {} Station \n"
            "Total Quantity of Bags in Non-Compliance (High): {}\n"
            "Total Weight of Nutmeg in Non-Compliance (High): {}\n"
            "Total Additional Drying Period Days (High): {}\n"
            "Total Weight (High): {}\n"
            "Difference from last month:\n"
            "  Quantity of Bags (High): {}\n"
            "  Weight of Nutmeg (High): {}\n"
            "  Additional Drying Period Days (High): {}\n"
            "  Total Weight (High): {}"
        )

    # Check if "{}" appears in the template
    if "{}" in template:
        # Adjust the vertical position for the first line
        y_position -= 12

    formatted_text = template.format(
        station,
        total_quantity_of_bags_in_non_compliance_H,
        total_weight_of_nutmeg_in_non_compliance_H,
        additional_drying_period_days_H,
        total_weight_H,
        diff_total_quantity_of_bags_in_non_compliance_H,
        diff_total_weight_of_nutmeg_in_non_compliance_H,
        diff_additional_drying_period_days_H,
        diff_total_weight_H
    )

    # Create a TextObject to handle line breaks
    text_object = pdf.beginText(10, y_position)
    text_object.setFont("Helvetica", 12)

    # Split the formatted text into lines
    lines = formatted_text.split('\n')

    # Add each line to the TextObject
    for line in lines:
        text_object.textLine(line)

    # Draw the TextObject on the PDF
    pdf.drawText(text_object)

    # Add the separator line after drawing the text block
    separator_line_position = y_position - len(lines) * 14
    pdf.drawString(10, separator_line_position, "-" * 50)

    # Adjust the vertical position for the next station summary
    return separator_line_position - 20  # Adjust this value as needed

def generate_weight_comparison_graph4(pdf, stations, entries, field):
    # Create a bar graph comparing the specified field between stations for the new model
    total_weights = []

    for station in stations:
        station_entries = entries.filter(STATION=station)
        total_weight = station_entries.aggregate(Sum(field))[f'{field}__sum']
        total_weights.append(total_weight if total_weight is not None else 0)

    # Convert the total_weights list to ensure all values are non-None
    total_weights = [0 if weight is None else weight for weight in total_weights]

    # Convert the stations list to strings to avoid issues with None values
    stations = [str(station) for station in stations]

    # Generate the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(stations, total_weights, color='purple')
    plt.title(f'Total {field} Comparison Between Stations')
    plt.xlabel('Station')
    plt.ylabel(f'Total {field}')
    plt.xticks(rotation=45, ha='right')

    # Save the plot to a temporary file
    temp_filename = f'temp_{field}_comparison_plot.png'
    plt.savefig(temp_filename, format='png')
    plt.close()

    # Create a new PDF page for the graph
    pdf.drawImage(temp_filename, 100, 5, width=400, height=200)

    # Remove the temporary file
    os.remove(temp_filename)

    # Move back to the original page
    pdf.showPage()

    return pdf































from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.db.models import Sum
from .models import Quality_Control
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import os
import warnings
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
matplotlib.use('module://matplotlib.backends.backend_agg')

def generate_monthly_report5(request, month, year):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=monthly_report_{month}_{year}.pdf'

    # Create PDF document
    p = canvas.Canvas(response)

    # Get the first day of the current month
    first_day_current_month = datetime(int(year), int(month), 1)

    # Get the last day of the previous month
    last_day_previous_month = first_day_current_month - timedelta(days=1)

    # Query data for the current month and last month for the new model
    current_month_entries = Quality_Control.objects.filter(
        Date_Created__month=month,
        Date_Created__year=year
    )

    last_month_entries = Quality_Control.objects.filter(
        Date_Created__month=last_day_previous_month.month,
        Date_Created__year=last_day_previous_month.year
    )

    # Set initial vertical position
    y_position = 800

    # Overall summary for all entries in the current month
    overall_sample_weight_this_month = current_month_entries.aggregate(Sum('SAMPLE_WEIGHT'))['SAMPLE_WEIGHT__sum']
    overall_sounds_this_month = current_month_entries.aggregate(Sum('SOUNDS'))['SOUNDS__sum']
    overall_pinholes_this_month = current_month_entries.aggregate(Sum('PINHOLES'))['PINHOLES__sum']
    overall_cracked_this_month = current_month_entries.aggregate(Sum('CRACKED'))['CRACKED__sum']
    overall_broken_this_month = current_month_entries.aggregate(Sum('BROKEN'))['BROKEN__sum']
    overall_pieces_this_month = current_month_entries.aggregate(Sum('PIECES'))['PIECES__sum']

    # Overall summary for all entries in the last month
    overall_sample_weight_last_month = last_month_entries.aggregate(Sum('SAMPLE_WEIGHT'))['SAMPLE_WEIGHT__sum']
    overall_sounds_last_month = last_month_entries.aggregate(Sum('SOUNDS'))['SOUNDS__sum']
    overall_pinholes_last_month = last_month_entries.aggregate(Sum('PINHOLES'))['PINHOLES__sum']
    overall_cracked_last_month = last_month_entries.aggregate(Sum('CRACKED'))['CRACKED__sum']
    overall_broken_last_month = last_month_entries.aggregate(Sum('BROKEN'))['BROKEN__sum']
    overall_pieces_last_month = last_month_entries.aggregate(Sum('PIECES'))['PIECES__sum']

    # Draw overall summary for this month and last month for the new model
    overall_template = (
        "{} Summary of December\n"
        "Total Sample Weight acquired over the month: {}\n"
        "Total Sounds acquired over the month: {}\n"
        "Total Pinholes acquired over the month: {}\n"
        "Total Cracked acquired over the month: {}\n"
        "Total Broken acquired over the month: {}\n"
        "Total Pieces acquired over the month: {}\n"
        "Difference from last month:\n"
        "  Sample Weight: {}\n"
        "  Sounds: {}\n"
        "  Pinholes: {}\n"
        "  Cracked: {}\n"
        "  Broken: {}\n"
        "  Pieces: {}"
    )
    y_position = draw_station_summary5(
        p,
        "Overall",
        overall_sample_weight_this_month,
        overall_sounds_this_month,
        overall_pinholes_this_month,
        overall_cracked_this_month,
        overall_broken_this_month,
        overall_pieces_this_month,
        y_position,
        template=overall_template,
        diff_sample_weight=(
            overall_sample_weight_this_month - overall_sample_weight_last_month
            if overall_sample_weight_last_month is not None else 0
        ),
        diff_sounds=(
            overall_sounds_this_month - overall_sounds_last_month
            if overall_sounds_last_month is not None else 0
        ),
        diff_pinholes=(
            overall_pinholes_this_month - overall_pinholes_last_month
            if overall_pinholes_last_month is not None else 0
        ),
        diff_cracked=(
            overall_cracked_this_month - overall_cracked_last_month
            if overall_cracked_last_month is not None else 0
        ),
        diff_broken=(
            overall_broken_this_month - overall_broken_last_month
            if overall_broken_last_month is not None else 0
        ),
        diff_pieces=(
            overall_pieces_this_month - overall_pieces_last_month
            if overall_pieces_last_month is not None else 0
        )
    )

    # Generate the bar graph comparing total weight between stations for the new model
    generate_weight_comparison_graph5(p, ["Station1", "Station2", "Station3"], current_month_entries, "SAMPLE_WEIGHT")

    p.save()

    return response

def draw_station_summary5(
    pdf,
    station,
    total_sample_weight,
    total_sounds,
    total_pinholes,
    total_cracked,
    total_broken,
    total_pieces,
    y_position,
    template=None,
    diff_sample_weight=0,
    diff_sounds=0,
    diff_pinholes=0,
    diff_cracked=0,
    diff_broken=0,
    diff_pieces=0,
):
    # Customize this function based on your specific needs
    if template is None:
        # Use a default template if none is provided
        template = (
            "Summary of {} Station \n"
            "Total Sample Weight acquired over the month: {}\n"
            "Total Sounds acquired over the month: {}\n"
            "Total Pinholes acquired over the month: {}\n"
            "Total Cracked acquired over the month: {}\n"
            "Total Broken acquired over the month: {}\n"
            "Total Pieces acquired over the month: {}\n"
            "Difference from last month:\n"
            "  Sample Weight: {}\n"
            "  Sounds: {}\n"
            "  Pinholes: {}\n"
            "  Cracked: {}\n"
            "  Broken: {}\n"
            "  Pieces: {}"
        )

    # Check if "{}" appears in the template
    if "{}" in template:
        # Adjust the vertical position for the first line
        y_position -= 12

    formatted_text = template.format(
        station,
        total_sample_weight,
        total_sounds,
        total_pinholes,
        total_cracked,
        total_broken,
        total_pieces,
        diff_sample_weight,
        diff_sounds,
        diff_pinholes,
        diff_cracked,
        diff_broken,
        diff_pieces,
    )

    # Create a TextObject to handle line breaks
    text_object = pdf.beginText(10, y_position)
    text_object.setFont("Helvetica", 12)

    # Split the formatted text into lines
    lines = formatted_text.split('\n')

    # Add each line to the TextObject
    for line in lines:
        text_object.textLine(line)

    # Draw the TextObject on the PDF
    pdf.drawText(text_object)

    # Add the separator line after drawing the text block
    separator_line_position = y_position - len(lines) * 14
    pdf.drawString(10, separator_line_position, "-" * 50)

    # Adjust the vertical position for the next station summary
    return separator_line_position - 20  # Adjust this value as needed

def generate_weight_comparison_graph5(pdf, stations, entries, weight_field):
    # Create a bar graph comparing total weight between stations
    total_weights = []

    for station in stations:
        station_entries = entries.filter(STATION=station)
        total_weight = station_entries.aggregate(Sum(weight_field))[f'{weight_field}__sum']
        total_weights.append(total_weight if total_weight is not None else 0)

    # Convert the total_weights list to ensure all values are non-None
    total_weights = [0 if weight is None else weight for weight in total_weights]

    # Convert the stations list to strings to avoid issues with None values
    stations = [str(station) for station in stations]

    # Generate the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(stations, total_weights, color='purple')
    plt.title(f'Total {weight_field.capitalize()} Comparison Between Stations')
    plt.xlabel('Station')
    plt.ylabel(f'Total {weight_field.capitalize()}')
    plt.xticks(rotation=45, ha='right')

    # Save the plot to a temporary file
    temp_filename = f'temp_{weight_field}_comparison_plot.png'
    plt.savefig(temp_filename, format='png')
    plt.close()

    # Create a new PDF page for the graph
    pdf.drawImage(temp_filename, 100, 5, width=400, height=200)

    # Remove the temporary file
    os.remove(temp_filename)

    # Move back to the original page
    pdf.showPage()

    return pdf

    
    






















from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.db.models import Sum
from .models import In_House_Drying
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
matplotlib.use('module://matplotlib.backends.backend_agg')

def generate_monthly_report6(request, month, year):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=monthly_report_{month}_{year}.pdf'

    # Create PDF document
    p = canvas.Canvas(response)

    # Get the first day of the current month
    first_day_current_month = datetime(int(year), int(month), 1)

    # Get the last day of the previous month
    last_day_previous_month = first_day_current_month - timedelta(days=1)

    # Query data for the current month and last month for the new model
    current_month_entries = In_House_Drying.objects.filter(
        Date_Created__month=month,
        Date_Created__year=year
    )

    last_month_entries = In_House_Drying.objects.filter(
        Date_Created__month=last_day_previous_month.month,
        Date_Created__year=last_day_previous_month.year
    )

    # Set initial vertical position
    y_position = 800

    # Overall summary for all entries in the current month
    overall_total_farmers_this_month = current_month_entries.aggregate(Sum('TOTAL_NUM_OF_FARMERS'))['TOTAL_NUM_OF_FARMERS__sum']
    overall_total_lbs_nutmeg_bought_this_month = current_month_entries.aggregate(Sum('TOTAL_LBS_NUTMEG_BOUGHT'))['TOTAL_LBS_NUTMEG_BOUGHT__sum']
    overall_num_of_bags_this_month = current_month_entries.aggregate(Sum('NUM_OF_BAGS'))['NUM_OF_BAGS__sum']

    # Overall summary for all entries in the last month
    overall_total_farmers_last_month = last_month_entries.aggregate(Sum('TOTAL_NUM_OF_FARMERS'))['TOTAL_NUM_OF_FARMERS__sum']
    overall_total_lbs_nutmeg_bought_last_month = last_month_entries.aggregate(Sum('TOTAL_LBS_NUTMEG_BOUGHT'))['TOTAL_LBS_NUTMEG_BOUGHT__sum']
    overall_num_of_bags_last_month = last_month_entries.aggregate(Sum('NUM_OF_BAGS'))['NUM_OF_BAGS__sum']

    # Draw overall summary for this month and last month
    overall_template = (
        "{} Summary of December\n"
        "Total numbers of farmers: {}\n"
        "Total lbs of nutmeg bought: {}\n"
        "Number of bags: {}\n"
        "Difference from last month:\n"
        "  Total numbers of farmers: {}\n"
        "  Total lbs of nutmeg bought: {}\n"
        "  Number of bags: {}"
    )
    y_position = draw_station_summary6(
        p,
        "Overall",
        overall_total_farmers_this_month,
        overall_total_lbs_nutmeg_bought_this_month,
        overall_num_of_bags_this_month,
        y_position,
        template=overall_template,
        diff_total_farmers=(
            overall_total_farmers_this_month - overall_total_farmers_last_month
            if overall_total_farmers_last_month is not None else 0
        ),
        diff_total_lbs_nutmeg_bought=(
            overall_total_lbs_nutmeg_bought_this_month - overall_total_lbs_nutmeg_bought_last_month
            if overall_total_lbs_nutmeg_bought_last_month is not None else 0
        ),
        diff_num_of_bags=(
            overall_num_of_bags_this_month - overall_num_of_bags_last_month
            if overall_num_of_bags_last_month is not None else 0
        )
    )

    # Generate the bar graph comparing total lbs of nutmeg bought between entries
    generate_lbs_nutmeg_comparison_graph6(p, current_month_entries)

    p.save()

    return response

def draw_station_summary6(pdf, station, total_total_farmers, total_lbs_nutmeg_bought, total_num_of_bags, y_position, template=None, diff_total_farmers=0, diff_total_lbs_nutmeg_bought=0, diff_num_of_bags=0):
    # Customize this function based on your specific needs
    if template is None:
        # Use a default template if none is provided
        template = (
            "Summary of {} \n"
            "Total numbers of farmers: {}\n"
            "Total lbs of nutmeg bought: {}\n"
            "Number of bags: {}\n"
            "Difference from last month:\n"
            "  Total numbers of farmers: {}\n"
            "  Total lbs of nutmeg bought: {}\n"
            "  Number of bags: {}"
        )

    # Check if "{}" appears in the template
    if "{}" in template:
        # Adjust the vertical position for the first line
        y_position -= 12

    formatted_text = template.format(
        station,
        total_total_farmers,
        total_lbs_nutmeg_bought,
        total_num_of_bags,
        diff_total_farmers,
        diff_total_lbs_nutmeg_bought,
        diff_num_of_bags
    )

    # Create a TextObject to handle line breaks
    text_object = pdf.beginText(10, y_position)
    text_object.setFont("Helvetica", 12)

    # Split the formatted text into lines
    lines = formatted_text.split('\n')

    # Add each line to the TextObject
    for line in lines:
        text_object.textLine(line)

    # Draw the TextObject on the PDF
    pdf.drawText(text_object)

    # Add the separator line after drawing the text block
    separator_line_position = y_position - len(lines) * 14
    pdf.drawString(10, separator_line_position, "-" * 50)

    # Adjust the vertical position for the next station summary
    return separator_line_position - 20  # Adjust this value as needed

def generate_lbs_nutmeg_comparison_graph6(pdf, entries):
    # Create a bar graph comparing total lbs of nutmeg bought between entries
    total_lbs_nutmeg = []

    for entry in entries:
        total_lbs_nutmeg_bought = entry.TOTAL_LBS_NUTMEG_BOUGHT
        total_lbs_nutmeg.append(total_lbs_nutmeg_bought)

    # Generate the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(range(1, len(entries) + 1), total_lbs_nutmeg, color='blue')
    plt.title('Total lbs of Nutmeg Bought Comparison Between Entries')
    plt.xlabel('Entry')
    plt.ylabel('Total lbs of Nutmeg Bought')

    # Save the plot to a temporary file
    temp_filename = 'temp_lbs_nutmeg_comparison_plot.png'
    plt.savefig(temp_filename, format='png')
    plt.close()

    # Create a new PDF page for the graph
    pdf.drawImage(temp_filename, 100, 5, width=400, height=200)

    # Remove the temporary file
    os.remove(temp_filename)

    # Move back to the original page
    pdf.showPage()

    return pdf


























from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.db.models import Sum
from .models import Dispatch_Of_Green_Nutmeg
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
matplotlib.use('module://matplotlib.backends.backend_agg')

def generate_monthly_report8(request, month, year):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=dispatch_report_{month}_{year}.pdf'

    # Create PDF document
    p = canvas.Canvas(response)

    # Get the first day of the current month
    first_day_current_month = datetime(int(year), int(month), 1)

    # Get the last day of the previous month
    last_day_previous_month = first_day_current_month - timedelta(days=1)

    # Query data for the current month and last month for the Dispatch_Of_Green_Nutmeg model
    current_month_entries = Dispatch_Of_Green_Nutmeg.objects.filter(
        Date_Created__month=month,
        Date_Created__year=year
    )

    last_month_entries = Dispatch_Of_Green_Nutmeg.objects.filter(
        Date_Created__month=last_day_previous_month.month,
        Date_Created__year=last_day_previous_month.year
    )

    # Set initial vertical position
    y_position = 800

    # Overall summary for all entries in the current month
    overall_total_num_of_farmers_this_month = current_month_entries.aggregate(Sum('TOTAL_NUM_OF_FARMERS'))['TOTAL_NUM_OF_FARMERS__sum']
    overall_total_lbs_nutmeg_bought_this_month = current_month_entries.aggregate(Sum('TOTAL_LBS_NUTMEG_BOUGHT'))['TOTAL_LBS_NUTMEG_BOUGHT__sum']
    overall_num_of_bags_this_month = current_month_entries.aggregate(Sum('NUM_OF_BAGS'))['NUM_OF_BAGS__sum']

    # Overall summary for all entries in the last month
    overall_total_num_of_farmers_last_month = last_month_entries.aggregate(Sum('TOTAL_NUM_OF_FARMERS'))['TOTAL_NUM_OF_FARMERS__sum']
    overall_total_lbs_nutmeg_bought_last_month = last_month_entries.aggregate(Sum('TOTAL_LBS_NUTMEG_BOUGHT'))['TOTAL_LBS_NUTMEG_BOUGHT__sum']
    overall_num_of_bags_last_month = last_month_entries.aggregate(Sum('NUM_OF_BAGS'))['NUM_OF_BAGS__sum']

    # Draw overall summary for this month and last month for the Dispatch_Of_Green_Nutmeg model
    overall_template = (
        "{} Summary of December\n"
        "Total Numbers of Farmers: {}\n"
        "Total lbs of Nutmeg bought: {}\n"
        "Number of Bags: {}\n"
        "Difference from last month:\n"
        "  Total Numbers of Farmers: {}\n"
        "  Total lbs of Nutmeg bought: {}\n"
        "  Number of Bags: {}"
    )
    y_position = draw_dispatch_summary8(
        p,
        "Overall",
        overall_total_num_of_farmers_this_month,
        overall_total_lbs_nutmeg_bought_this_month,
        overall_num_of_bags_this_month,
        y_position,
        template=overall_template,
        diff_total_num_of_farmers=(
            overall_total_num_of_farmers_this_month - overall_total_num_of_farmers_last_month
            if overall_total_num_of_farmers_last_month is not None else 0
        ),
        diff_total_lbs_nutmeg_bought=(
            overall_total_lbs_nutmeg_bought_this_month - overall_total_lbs_nutmeg_bought_last_month
            if overall_total_lbs_nutmeg_bought_last_month is not None else 0
        ),
        diff_num_of_bags=(
            overall_num_of_bags_this_month - overall_num_of_bags_last_month
            if overall_num_of_bags_last_month is not None else 0
        )
    )

    # Generate the bar graph comparing total lbs of nutmeg bought between months
    generate_weight_comparison_graph8(p, "TOTAL_LBS_NUTMEG_BOUGHT", current_month_entries, last_month_entries)

    p.save()

    return response

def draw_dispatch_summary8(pdf, category, total_num_of_farmers, total_lbs_nutmeg_bought, num_of_bags, y_position, template=None, diff_total_num_of_farmers=0, diff_total_lbs_nutmeg_bought=0, diff_num_of_bags=0):
    # Customize this function based on your specific needs
    if template is None:
        # Use a default template if none is provided
        template = (
            "Summary of {} {}\n"
            "Total Numbers of Farmers: {}\n"
            "Total lbs of Nutmeg bought: {}\n"
            "Number of Bags: {}\n"
            "Difference from last month:\n"
            "  Total Numbers of Farmers: {}\n"
            "  Total lbs of Nutmeg bought: {}\n"
            "  Number of Bags: {}"
        )

    # Check if "{}" appears in the template
    if "{}" in template:
        # Adjust the vertical position for the first line
        y_position -= 12

    formatted_text = template.format(
        category,
        "Summary",
        total_num_of_farmers,
        total_lbs_nutmeg_bought,
        num_of_bags,
        diff_total_num_of_farmers,
        diff_total_lbs_nutmeg_bought,
        diff_num_of_bags
    )

    # Create a TextObject to handle line breaks
    text_object = pdf.beginText(10, y_position)
    text_object.setFont("Helvetica", 12)

    # Split the formatted text into lines
    lines = formatted_text.split('\n')

    # Add each line to the TextObject
    for line in lines:
        text_object.textLine(line)

    # Draw the TextObject on the PDF
    pdf.drawText(text_object)

    # Add the separator line after drawing the text block
    separator_line_position = y_position - len(lines) * 14
    pdf.drawString(10, separator_line_position, "-" * 50)

    # Adjust the vertical position for the next summary
    return separator_line_position - 20  # Adjust this value as needed

def generate_weight_comparison_graph8(pdf, field, current_month_entries, last_month_entries):
    # Create a bar graph comparing the specified field between months
    current_month_value = current_month_entries.aggregate(Sum(field))[f'{field}__sum']
    last_month_value = last_month_entries.aggregate(Sum(field))[f'{field}__sum']

    # Convert values to ensure they are non-None
    current_month_value = current_month_value if current_month_value is not None else 0
    last_month_value = last_month_value if last_month_value is not None else 0

    # Generate the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(['Current Month', 'Last Month'], [current_month_value, last_month_value], color='purple')
    plt.title(f'{field} Comparison Between Months')
    plt.xlabel('Month')
    plt.ylabel(field)
    plt.xticks(rotation=45, ha='right')

    # Save the plot to a temporary file
    temp_filename = f'temp_{field}_comparison_plot.png'
    plt.savefig(temp_filename, format='png')
    plt.close()

    # Create a new PDF page for the graph
    pdf.drawImage(temp_filename, 100, 5, width=400, height=200)

    # Remove the temporary file
    os.remove(temp_filename)

    # Move back to the original page
    pdf.showPage()

    return pdf























from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.db.models import Sum
from .models import Cracking_Summary
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
matplotlib.use('module://matplotlib.backends.backend_agg')

def generate_monthly_report9(request, month, year):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=monthly_report_cracking_{month}_{year}.pdf'

    # Create PDF document
    p = canvas.Canvas(response)

    # Get the first day of the current month
    first_day_current_month = datetime(int(year), int(month), 1)

    # Get the last day of the previous month
    last_day_previous_month = first_day_current_month - timedelta(days=1)

    # Query data for the current month and last month for the Cracking_Summary model
    current_month_entries = Cracking_Summary.objects.filter(
        Date_Created__month=month,
        Date_Created__year=year
    )

    last_month_entries = Cracking_Summary.objects.filter(
        Date_Created__month=last_day_previous_month.month,
        Date_Created__year=last_day_previous_month.year
    )

    # Set initial vertical position
    y_position = 800

    # Overall summary for all entries in the current month
    overall_num_of_bags_this_month = current_month_entries.aggregate(Sum('NUM_OF_BAGS'))['NUM_OF_BAGS__sum']
    overall_lbs_of_nutmegs_cracked_this_month = current_month_entries.aggregate(Sum('LBS_OF_NUTMEGS_CRACKED'))['LBS_OF_NUTMEGS_CRACKED__sum']

    # Overall summary for all entries in the last month
    overall_num_of_bags_last_month = last_month_entries.aggregate(Sum('NUM_OF_BAGS'))['NUM_OF_BAGS__sum']
    overall_lbs_of_nutmegs_cracked_last_month = last_month_entries.aggregate(Sum('LBS_OF_NUTMEGS_CRACKED'))['LBS_OF_NUTMEGS_CRACKED__sum']

    # Draw overall summary for this month and last month for the Cracking_Summary model
    overall_template = (
        "{} Cracking Summary of December\n"
        "Total number of bags cracked over the month: {}\n"
        "Total lbs of nutmegs cracked over the month: {}\n"
        "Difference from last month:\n"
        "  Number of Bags: {}\n"
        "  Lbs of Nutmegs Cracked: {}"
    )
    y_position = draw_cracking_summary(
        p,
        "Overall",
        overall_num_of_bags_this_month,
        overall_lbs_of_nutmegs_cracked_this_month,
        y_position,
        template=overall_template,
        diff_num_of_bags=(
            overall_num_of_bags_this_month - overall_num_of_bags_last_month
            if overall_num_of_bags_last_month is not None else 0
        ),
        diff_lbs_of_nutmegs_cracked=(
            overall_lbs_of_nutmegs_cracked_this_month - overall_lbs_of_nutmegs_cracked_last_month
            if overall_lbs_of_nutmegs_cracked_last_month is not None else 0
        ),
    )

    # Group entries by station for the Cracking_Summary model
    # Assuming Cracking_Summary model does not have 'STATION' field, modify as needed
    # If it has a different field for grouping, replace 'STATION' with the correct field
    stations = ["Station1", "Station2", "Station3"]  # Replace with actual station names

    # Loop through stations and generate a summary for each for the Cracking_Summary model
    for station in stations:
        station_entries_current_month = current_month_entries.filter(STATION=station)  # Replace with actual field name
        station_entries_last_month = last_month_entries.filter(STATION=station)  # Replace with actual field name

        # Calculate sums for each field for the Cracking_Summary model
        total_num_of_bags_current_month = station_entries_current_month.aggregate(Sum('NUM_OF_BAGS'))['NUM_OF_BAGS__sum']
        total_lbs_of_nutmegs_cracked_current_month = station_entries_current_month.aggregate(Sum('LBS_OF_NUTMEGS_CRACKED'))['LBS_OF_NUTMEGS_CRACKED__sum']

        total_num_of_bags_last_month = station_entries_last_month.aggregate(Sum('NUM_OF_BAGS'))['NUM_OF_BAGS__sum']
        total_lbs_of_nutmegs_cracked_last_month = station_entries_last_month.aggregate(Sum('LBS_OF_NUTMEGS_CRACKED'))['LBS_OF_NUTMEGS_CRACKED__sum']

        # Define a custom template for the station summary for the Cracking_Summary model
        station_template = (
            "Summary of {} Cracking Station\n"
            "Total number of bags cracked over the month: {}\n"
            "Total lbs of nutmegs cracked over the month: {}\n"
            "Difference from last month:\n"
            "  Number of Bags: {}\n"
            "  Lbs of Nutmegs Cracked: {}"
        )

        # Draw a summary for each station for the Cracking_Summary model
        y_position = draw_cracking_summary(
            p,
            station,
            total_num_of_bags_current_month,
            total_lbs_of_nutmegs_cracked_current_month,
            y_position,
            template=station_template,
            diff_num_of_bags=(
                total_num_of_bags_current_month - total_num_of_bags_last_month
                if total_num_of_bags_last_month is not None else 0
            ),
            diff_lbs_of_nutmegs_cracked=(
                total_lbs_of_nutmegs_cracked_current_month - total_lbs_of_nutmegs_cracked_last_month
                if total_lbs_of_nutmegs_cracked_last_month is not None else 0
            ),
        )

    # Generate the bar graph comparing lbs of nutmegs cracked between stations for the Cracking_Summary model
    generate_lbs_of_nutmegs_cracked_comparison_graph(p, stations, current_month_entries)

    p.save()

    return response

def draw_cracking_summary(pdf, station, total_num_of_bags, total_lbs_of_nutmegs_cracked, y_position, template=None, diff_num_of_bags=0, diff_lbs_of_nutmegs_cracked=0):
    # Customize this function based on your specific needs for the Cracking_Summary model
    if template is None:
        # Use a default template if none is provided for the Cracking_Summary model
        template = (
            "Summary of {} Cracking Station\n"
            "Total number of bags cracked over the month: {}\n"
            "Total lbs of nutmegs cracked over the month: {}\n"
            "Difference from last month:\n"
            "  Number of Bags: {}\n"
            "  Lbs of Nutmegs Cracked: {}"
        )

    # Check if "{}" appears in the template for the Cracking_Summary model
    if "{}" in template:
        # Adjust the vertical position for the first line
        y_position -= 12

    formatted_text = template.format(
        station,
        total_num_of_bags,
        total_lbs_of_nutmegs_cracked,
        diff_num_of_bags,
        diff_lbs_of_nutmegs_cracked
    )

    # Create a TextObject to handle line breaks for the Cracking_Summary model
    text_object = pdf.beginText(10, y_position)
    text_object.setFont("Helvetica", 12)

    # Split the formatted text into lines for the Cracking_Summary model
    lines = formatted_text.split('\n')

    # Add each line to the TextObject for the Cracking_Summary model
    for line in lines:
        text_object.textLine(line)

    # Draw the TextObject on the PDF for the Cracking_Summary model
    pdf.drawText(text_object)

    # Add the separator line after drawing the text block for the Cracking_Summary model
    separator_line_position = y_position - len(lines) * 14
    pdf.drawString(10, separator_line_position, "-" * 50)

    # Adjust the vertical position for the next station summary for the Cracking_Summary model
    return separator_line_position - 20  # Adjust this value as needed

def generate_lbs_of_nutmegs_cracked_comparison_graph(pdf, stations, entries):
    # Create a bar graph comparing lbs of nutmegs cracked between stations for the Cracking_Summary model
    total_lbs_of_nutmegs_cracked = []

    for station in stations:
        station_entries = entries.filter(STATION=station)  # Replace with actual field name
        lbs_of_nutmegs_cracked = station_entries.aggregate(Sum('LBS_OF_NUTMEGS_CRACKED'))['LBS_OF_NUTMEGS_CRACKED__sum']
        total_lbs_of_nutmegs_cracked.append(lbs_of_nutmegs_cracked if lbs_of_nutmegs_cracked is not None else 0)

    # Convert the total_lbs_of_nutmegs_cracked list to ensure all values are non-None
    total_lbs_of_nutmegs_cracked = [0 if lbs_cracked is None else lbs_cracked for lbs_cracked in total_lbs_of_nutmegs_cracked]

    # Convert the stations list to strings to avoid issues with None values
    stations = [str(station) for station in stations]

    # Generate the bar graph for the Cracking_Summary model
    plt.figure(figsize=(10, 6))
    plt.bar(stations, total_lbs_of_nutmegs_cracked, color='purple')
    plt.title('Total lbs of Nutmegs Cracked Comparison Between Stations')
    plt.xlabel('Station')
    plt.ylabel('Total lbs of Nutmegs Cracked')
    plt.xticks(rotation=45, ha='right')

    # Save the plot to a temporary file for the Cracking_Summary model
    temp_filename = 'temp_lbs_of_nutmegs_cracked_comparison_plot.png'
    plt.savefig(temp_filename, format='png')
    plt.close()

    # Create a new PDF page for the graph for the Cracking_Summary model
    pdf.drawImage(temp_filename, 100, 5, width=400, height=200)

    # Remove the temporary file for the Cracking_Summary model
    os.remove(temp_filename)

    # Move back to the original page for the Cracking_Summary model
    pdf.showPage()

    return pdf




def generate_lbs_of_nutmegs_cracked_comparison_graph(pdf, stations, entries):
    # Create a bar graph comparing lbs of nutmegs cracked between stations for the Cracking_Summary model
    total_lbs_of_nutmegs_cracked = []

    for station in stations:
        station_entries = entries.filter(STATION=station)  # Replace with actual field name
        lbs_of_nutmegs_cracked = station_entries.aggregate(Sum('LBS_OF_NUTMEGS_CRACKED'))['LBS_OF_NUTMEGS_CRACKED__sum']
        total_lbs_of_nutmegs_cracked.append(lbs_of_nutmegs_cracked if lbs_of_nutmegs_cracked is not None else 0)

    # Convert the total_lbs_of_nutmegs_cracked list to ensure all values are non-None
    total_lbs_of_nutmegs_cracked = [0 if lbs_cracked is None else lbs_cracked for lbs_cracked in total_lbs_of_nutmegs_cracked]

    # Convert the stations list to strings to avoid issues with None values
    stations = [str(station) for station in stations]

    # Generate the bar graph for the Cracking_Summary model
    plt.figure(figsize=(10, 6))
    plt.bar(stations, total_lbs_of_nutmegs_cracked, color='purple')
    plt.title('Total lbs of Nutmegs Cracked Comparison Between Stations')
    plt.xlabel('Station')
    plt.ylabel('Total lbs of Nutmegs Cracked')
    plt.xticks(rotation=45, ha='right')

    # Save the plot to a temporary file for the Cracking_Summary model
    temp_filename = 'temp_lbs_of_nutmegs_cracked_comparison_plot.png'
    plt.savefig(temp_filename, format='png')
    plt.close()

    # Create a new PDF page for the graph for the Cracking_Summary model
    pdf.drawImage(temp_filename, 100, 5, width=400, height=200)

    # Remove the temporary file for the Cracking_Summary model
    os.remove(temp_filename)

    # Move back to the original page for the Cracking_Summary model
    pdf.showPage()

    return pdf












from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.db.models import Sum
from .models import Package_Ciontrol
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
matplotlib.use('module://matplotlib.backends.backend_agg')

def generate_monthly_report11(request, month, year):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=monthly_report_{month}_{year}.pdf'

    # Create PDF document
    p = canvas.Canvas(response)

    # Get the first day of the current month
    first_day_current_month = datetime(int(year), int(month), 1)

    # Get the last day of the previous month
    last_day_previous_month = first_day_current_month - timedelta(days=1)

    # Query data for the current month and last month
    current_month_entries = Package_Ciontrol.objects.filter(
        Date_Created__month=month,
        Date_Created__year=year
    )

    last_month_entries = Package_Ciontrol.objects.filter(
        Date_Created__month=last_day_previous_month.month,
        Date_Created__year=last_day_previous_month.year
    )

    # Set initial vertical position
    y_position = 800

    # Overall summary for all entries in the current month
    overall_quantity_of_bags_this_month = current_month_entries.aggregate(Sum('QUANTITY_OF_BAGS'))['QUANTITY_OF_BAGS__sum']
    overall_total_weight_this_month = current_month_entries.aggregate(Sum('TOTAL_WEIGHT_LBS'))['TOTAL_WEIGHT_LBS__sum']

    # Overall summary for all entries in the last month
    overall_quantity_of_bags_last_month = last_month_entries.aggregate(Sum('QUANTITY_OF_BAGS'))['QUANTITY_OF_BAGS__sum']
    overall_total_weight_last_month = last_month_entries.aggregate(Sum('TOTAL_WEIGHT_LBS'))['TOTAL_WEIGHT_LBS__sum']

    # Draw overall summary for this month and last month
    overall_template = (
        "{} Summary of December\n"
        "Total bags acquired over the month: {}\n"
        "Total Total Weight: {}\n"
        "Difference from last month:\n"
        "  Quantity of Bags: {}\n"
        "  Total Weight: {}"
    )
    y_position = draw_station_summary11(
        p,
        "Overall",
        overall_quantity_of_bags_this_month,
        overall_total_weight_this_month,
        y_position,
        template=overall_template,
        diff_quantity_of_bags=(
            overall_quantity_of_bags_this_month - overall_quantity_of_bags_last_month
            if overall_quantity_of_bags_last_month is not None else 0
        ),
        diff_total_weight=(
            overall_total_weight_this_month - overall_total_weight_last_month
            if overall_total_weight_last_month is not None else 0
        )
    )

    # Generate the bar graph comparing total weight between entries
    generate_weight_comparison_graph11(p, current_month_entries)

    p.save()

    return response

def draw_station_summary11(pdf, station, total_quantity_of_bags, total_total_weight, y_position, template=None, diff_quantity_of_bags=0, diff_total_weight=0):
    # Customize this function based on your specific needs
    if template is None:
        # Use a default template if none is provided
        template = (
            "Summary of {} Station \n"
            "Total bags acquired over the month: {}\n"
            "Total Weight: {}\n"
            "Difference from last month:\n"
            "  Quantity of Bags: {}\n"
            "  Total Weight: {}"
        )

    # Check if "{}" appears in the template
    if "{}" in template:
        # Adjust the vertical position for the first line
        y_position -= 12

    formatted_text = template.format(
        station,
        total_quantity_of_bags,
        total_total_weight,
        diff_quantity_of_bags,
        diff_total_weight
    )

    # Create a TextObject to handle line breaks
    text_object = pdf.beginText(10, y_position)
    text_object.setFont("Helvetica", 12)

    # Split the formatted text into lines
    lines = formatted_text.split('\n')

    # Add each line to the TextObject
    for line in lines:
        text_object.textLine(line)

    # Draw the TextObject on the PDF
    pdf.drawText(text_object)

    # Add the separator line after drawing the text block
    separator_line_position = y_position - len(lines) * 14
    pdf.drawString(10, separator_line_position, "-" * 50)

    # Adjust the vertical position for the next station summary
    return separator_line_position - 20  # Adjust this value as needed

def generate_weight_comparison_graph11(pdf, entries):
    # Create a bar graph comparing total weight between all entries
    total_weights = entries.aggregate(Sum('TOTAL_WEIGHT_LBS'))['TOTAL_WEIGHT_LBS__sum']

    # Ensure total_weights is non-None
    total_weights = total_weights if total_weights is not None else 0

    # Generate the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(['Overall'], [total_weights], color='purple')
    plt.title('Total Weight Comparison')
    plt.xlabel('Category')
    plt.ylabel('Total Weight (lbs)')
    plt.xticks(rotation=45, ha='right')

    # Save the plot to a temporary file
    temp_filename = 'temp_weight_comparison_plot.png'
    plt.savefig(temp_filename, format='png')
    plt.close()

    # Create a new PDF page for the graph
    pdf.drawImage(temp_filename, 100, 5, width=400, height=200)

    # Remove the temporary file
    os.remove(temp_filename)

    # Move back to the original page
    pdf.showPage()

    return pdf













from django.http import JsonResponse
from django.shortcuts import render




def get_options(request):
    # Retrieve options from the database or any other source
    options1 = ['Option 1', 'Option 2', 'Option 3']
    options2 = ['Option 1', 'Option 2', 'Option 3']
    options3 = ['Option 1', 'Option 2', 'Option 3']
    options4 = ['Option 1', 'Option 2', 'Option 3']
    options5 = ['Option 1', 'Option 2', 'Option 3']
    options6 = ['Option 1', 'Option 2', 'Option 3']

    return JsonResponse({ 'options1': options1,'options2': options2,'options3': options3,'options4': options4,'options5': options5,})






     





def rev_data0(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            request.session['Worker_ID_No'] = form.cleaned_data['Worker_ID_No']
            request.session['Nutmeg_ID_No'] = form.cleaned_data['Nutmeg_ID_No']

            Worker_ID_No = request.session['Worker_ID_No']
            Nutmeg_ID_No = request.session['Nutmeg_ID_No']

            check2 = Worker_Info.objects.filter(Worker_ID_No=Worker_ID_No).first()

            if check2:
                Worker_ID_No = Worker_Info.objects.get(Worker_ID_No=Worker_ID_No)
                Worker_ID_No_id = Worker_ID_No.id

                return redirect('table001')
            else:
                return redirect('error_table0_0')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'gcna/login.html', context)





def newSignin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)

        if form.is_valid():
            request.session['Worker_ID_No'] = form.cleaned_data['Worker_ID_No']
            request.session['Nutmeg_ID_No'] = form.cleaned_data['Nutmeg_ID_No']

            Worker_ID_No = request.session['Worker_ID_No']
            Nutmeg_ID_No = request.session['Nutmeg_ID_No']

            check2 = Worker_Info.objects.filter(Worker_ID_No=Worker_ID_No).first()

            if check2:
                Worker_ID_No = Worker_Info.objects.get(Worker_ID_No=Worker_ID_No)
                Worker_ID_No_id = Worker_ID_No.id

                return redirect('table001')
            else:
                return redirect('error_table0_0')
    else:
        form = SigninForm()

    context = {
        'form': form,
    }

    return render(request, 'gcna/new_login.html', context)













def nav_data0(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            request.session['Worker_ID_No'] = form.cleaned_data['Worker_ID_No']
            request.session['Nutmeg_ID_No'] = form.cleaned_data['Nutmeg_ID_No']

            Worker_ID_No = request.session['Worker_ID_No']
            Nutmeg_ID_No = request.session['Nutmeg_ID_No']

            check2 = Worker_Info.objects.filter(Worker_ID_No=Worker_ID_No).first()

            if check2:
                Worker_ID_No = Worker_Info.objects.get(Worker_ID_No=Worker_ID_No)
                Worker_ID_No_id = Worker_ID_No.id

                return redirect('table001')
            else:
                return redirect('error_table0_0')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'gcna/over_nav.html', context)







def rev_data3230(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            request.session['Nutmeg_ID_No'] =  form.cleaned_data['Nutmeg_ID_No']
            request.session['name'] =  form.cleaned_data['name']

            return redirect('table')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'gcna/login.html', context)


# def second_page(request):
#     if request.method == 'POST':
#         form = Form2(request.POST)
# 		if form.is_valid():

#     else:
#         form = Form2()


#         if 'farmer_name' in request.session:
#             form.fields['name'].initial = request.session['farmer_name']
#         if 'farmer_address' in request.session:
#             form.fields['address'].initial = request.session['farmer_address']

#     context = {
#         'form': form,
#     }

#     return render(request, 'second_page.html', context)



def signin(request):
	submitted = False
	if request.method == "POST":
		form = Farmer_Info_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/table')
	else:
		form = Farmer_Info_Form()



		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']
		if 'name' in request.session:
			form.fields['name'].initial = request.session['name']

	return render(request,'gcna/signin.html',{
		'form':form,
		'submitted':submitted})





def deny_entry(request):

	return render(request, 'gcna/deny_entry.html')


def Stirring_Log_Form(request):

	return render(request, 'gcna/stirring_log.html')




def rev_data1(request):
	submitted = False



	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Farmer_Info.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Farmer_Info.DoesNotExist:


		if request.method == "POST":
			form = Farmer_Info_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_1')
		else:
			form = Farmer_Info_Form()



			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'name' in request.session:
				form.fields['name'].initial = request.session['name']

	return render(request,'gcna/revform1.html',{
		'form':form,
		'submitted':submitted})




def rev_data2(request):
	submitted = False



	farmer_info_id = request.session.get('Nutmeg_ID_No')


	if request.method == "POST":
		form = land_info_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/gcna00_2')
	else:
		form = land_info_Form()

	if 'Nutmeg_ID_No' in request.session:
		form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

	if 'Worker_ID_No' in request.session:
		form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']

	 
	if 'submitted' in request.GET:
		submitted = True

	return render(request,'gcna/revform2.html',{
		'form':form,
		'submitted':submitted})


def rev_data3(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Land_Tenur.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Land_Tenur.DoesNotExist:


		if request.method == "POST":
			form = Land_Tenur_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_3')
		else:
			form = Land_Tenur_Form()


			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']

			if 'farm_type' in request.session:
				form.fields['farm_type'].initial = request.session['farm_type']




			if 'parish' in request.session:
				form.fields['parish'].initial = request.session['parish']

			if 'tenurship' in request.session:
				form.fields['tenurship'].initial = request.session['tenurship']

			if 'training' in request.session:
				form.fields['training'].initial = request.session['training']

			if 'village' in request.session:
				form.fields['village'].initial = request.session['village']	


			if 'submitted' in request.GET:
				submitted = True
 
	return render(request,'gcna/revform3.html',{
		'form':form,
		'submitted':submitted})


def rev_data4(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Nutmeg_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Nutmeg_Trees.DoesNotExist:



		if request.method == "POST":
			form = Nutmeg_Trees_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_4')
		else:
			form = Nutmeg_Trees_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform4.html',{
		'form':form,
		'submitted':submitted})





def rev_data5(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Nutmeg_Variety.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Nutmeg_Variety.DoesNotExist:



		if request.method == "POST":
			form = Nutmeg_Variety_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_5')
		else:
			form = Nutmeg_Variety_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform5.html',{
		'form':form,
		'submitted':submitted})












def rev_data6(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Crops.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Other_Crops.DoesNotExist:




		if request.method == "POST":
			form = Other_Crops_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_6')
		else:
			form = Other_Crops_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform6.html',{
		'form':form,
		'submitted':submitted})






def rev_data7(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Coconut_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Coconut_Trees.DoesNotExist:



		if request.method == "POST":
			form = Coconut_Trees_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_7')
		else:
			form = Coconut_Trees_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform7.html',{
		'form':form,
		'submitted':submitted})




def rev_data8(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Citrus_Mango_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Citrus_Mango_Trees.DoesNotExist:


		if request.method == "POST":
			form = Citrus_Mango_Trees_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_8')
		else:
			form = Citrus_Mango_Trees_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform8.html',{
		'form':form,
		'submitted':submitted})





def rev_data9(request):
	submitted = False

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Spices_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Other_Spices_Trees.DoesNotExist:




		if request.method == "POST":
			form = Other_Spices_Trees_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_9')
		else:
			form = Other_Spices_Trees_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform9.html',{
		'form':form,
		'submitted':submitted})







def rev_data10(request):
	submitted = False

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Seasoning_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Other_Seasoning_Trees.DoesNotExist:



		if request.method == "POST":
			form = Other_Seasoning_Trees_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_10')
		else:
			form = Other_Seasoning_Trees_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform10.html',{
		'form':form,
		'submitted':submitted})
















def rev_data11(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Crops_Cultivated.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Other_Crops_Cultivated.DoesNotExist:



		if request.method == "POST":
			form = Other_Crops_Cultivated_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_11')
		else:
			form = Other_Crops_Cultivated_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform11.html',{
		'form':form,
		'submitted':submitted})












def rev_data12(request):
	submitted = False

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Condition.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Condition.DoesNotExist:




		if request.method == "POST":
			form = Condition_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_12')
		else:
			form = Condition_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform12.html',{
		'form':form,
		'submitted':submitted})









def rev_data13(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Nutmeg_Land.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Nutmeg_Land.DoesNotExist:



		if request.method == "POST":
			form = Nutmeg_Land_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_13')
		else:
			form = Nutmeg_Land_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform13.html',{
		'form':form,
		'submitted':submitted})


def rev_data14(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Nutmeg_Frequency.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Nutmeg_Frequency.DoesNotExist:


		if request.method == "POST":
			form = Nutmeg_Frequency_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_14')
		else:
			form = Nutmeg_Frequency_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform14.html',{
		'form':form,
		'submitted':submitted})





def rev_data15(request):
	submitted = False

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Potential_Risks.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Potential_Risks.DoesNotExist:



		if request.method == "POST":
			form = Potential_Risks_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_15')
		else:
			form = Potential_Risks_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform15.html',{
		'form':form,
		'submitted':submitted})












def rev_data16(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Policy.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Policy.DoesNotExist:



		if request.method == "POST":
			form = Policy_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_16')
		else:
			form = Policy_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform16.html',{
		'form':form,
		'submitted':submitted})






def rev_data17(request):
	submitted = False

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Road_Access.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Road_Access.DoesNotExist:


		if request.method == "POST":
			form = Road_Access_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_17')
		else:
			form = Road_Access_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform17.html',{
		'form':form,
		'submitted':submitted})




def rev_data18(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Food_Safety_and_Quality.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Food_Safety_and_Quality.DoesNotExist:


		if request.method == "POST":
			form = Food_Safety_and_Quality_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_18')
		else:
			form = Food_Safety_and_Quality_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform18.html',{
		'form':form,
		'submitted':submitted})





def rev_data19(request):
	submitted = False

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Farm_Water_Source.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Farm_Water_Source.DoesNotExist:


		if request.method == "POST":
			form = Farm_Water_Source_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_19')
		else:
			form = Farm_Water_Source_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform19.html',{
		'form':form,
		'submitted':submitted})







def rev_data20(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Farm_House.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Farm_House.DoesNotExist:



		if request.method == "POST":
			form = Farm_House_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_20')
		else:
			form = Farm_House_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform20.html',{
		'form':form,
		'submitted':submitted})



def rev_data21(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = inspector_symmary.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except inspector_symmary.DoesNotExist:

	
		if request.method == "POST":
			form = inspector_symmary_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_21')
		else:
			form = inspector_symmary_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform21.html',{
		'form':form,
		'submitted':submitted})









def rev_data22(request):
	submitted = False



	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Training_support.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Training_support.DoesNotExist:

	
		if request.method == "POST":
			form = Training_support_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_21')
		else:
			form = Training_support_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform22.html',{
		'form':form,
		'submitted':submitted})










def rev_data23(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Labour_support.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Labour_support.DoesNotExist:

	
		if request.method == "POST":
			form = Labour_support_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_21')
		else:
			form = Labour_support_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform23.html',{
		'form':form,
		'submitted':submitted})








def rev_data24(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = visit.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except visit.DoesNotExist:

	
		if request.method == "POST":
			form = visit_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_24')
		else:
			form = visit_Form()



			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform24.html',{
		'form':form,
		'submitted':submitted})










def rev_data0_22(request):
	submitted = False



	farmer_info_id = request.session.get('Nutmeg_ID_No')


	if request.method == "POST":
		form = Training_support_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/gcna00_21')
	else:
		form = Training_support_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_22.html',{
		'form':form,
		'submitted':submitted})










def rev_data0_23(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')



	if request.method == "POST":
		form = Labour_support_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/gcna00_21')
	else:
		form = Labour_support_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_23.html',{
		'form':form,
		'submitted':submitted})










def rev_data0_1(request):
	submitted = False
	if request.method == "POST":
		form = Farmer_Info_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_1')
	else:
		form = Farmer_Info_Form()



		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



	return render(request,'gcna/revform0_1.html',{
		'form':form,
		'submitted':submitted})




def rev_data0_2(request):
	submitted = False
	if request.method == "POST":
		form = land_info_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_2')
	else:
		form = land_info_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']

 
		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_2.html',{
		'form':form,
		'submitted':submitted})


def rev_data0_3(request):
	submitted = False
	if request.method == "POST":
		form = Land_Tenur_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_3')
	else:
		form = Land_Tenur_Form()


		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_3.html',{
		'form':form,
		'submitted':submitted})


def rev_data0_4(request):
	submitted = False
	if request.method == "POST":
		form = Nutmeg_Trees_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_4')
	else:
		form = Nutmeg_Trees_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_4.html',{
		'form':form,
		'submitted':submitted})





def rev_data0_5(request):
	submitted = False
	if request.method == "POST":
		form = Nutmeg_Variety_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_5')
	else:
		form = Nutmeg_Variety_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_5.html',{
		'form':form,
		'submitted':submitted})












def rev_data0_6(request):
	submitted = False
	if request.method == "POST":
		form = Other_Crops_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_6')
	else:
		form = Other_Crops_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_6.html',{
		'form':form,
		'submitted':submitted})






def rev_data0_7(request):
	submitted = False
	if request.method == "POST":
		form = Coconut_Trees_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_7')
	else:
		form = Coconut_Trees_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_7.html',{
		'form':form,
		'submitted':submitted})




def rev_data0_8(request):
	submitted = False
	if request.method == "POST":
		form = Citrus_Mango_Trees_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_8')
	else:
		form = Citrus_Mango_Trees_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_8.html',{
		'form':form,
		'submitted':submitted})





def rev_data0_9(request):
	submitted = False
	if request.method == "POST":
		form = Other_Spices_Trees_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_9')
	else:
		form = Other_Spices_Trees_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_9.html',{
		'form':form,
		'submitted':submitted})







def rev_data0_10(request):
	submitted = False
	if request.method == "POST":
		form = Other_Seasoning_Trees_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_10')
	else:
		form = Other_Seasoning_Trees_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_10.html',{
		'form':form,
		'submitted':submitted})
















def rev_data0_11(request):
	submitted = False
	if request.method == "POST":
		form = Other_Crops_Cultivated_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_11')
	else:
		form = Other_Crops_Cultivated_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_11.html',{
		'form':form,
		'submitted':submitted})












def rev_data0_12(request):
	submitted = False
	if request.method == "POST":
		form = Condition_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_12')
	else:
		form = Condition_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_12.html',{
		'form':form,
		'submitted':submitted})









def rev_data0_13(request):
	submitted = False
	if request.method == "POST":
		form = Nutmeg_Land_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_13')
	else:
		form = Nutmeg_Land_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_13.html',{
		'form':form,
		'submitted':submitted})


def rev_data0_14(request):
	submitted = False
	if request.method == "POST":
		form = Nutmeg_Frequency_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_14')
	else:
		form = Nutmeg_Frequency_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_14.html',{
		'form':form,
		'submitted':submitted})





def rev_data0_15(request):
	submitted = False
	if request.method == "POST":
		form = Potential_Risks_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_15')
	else:
		form = Potential_Risks_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_15.html',{
		'form':form,
		'submitted':submitted})












def rev_data0_16(request):
	submitted = False
	if request.method == "POST":
		form = Policy_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_16')
	else:
		form = Policy_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_16.html',{
		'form':form,
		'submitted':submitted})






def rev_data0_17(request):
	submitted = False
	if request.method == "POST":
		form = Road_Access_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_17')
	else:
		form = Road_Access_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_17.html',{
		'form':form,
		'submitted':submitted})




def rev_data0_18(request):
	submitted = False
	if request.method == "POST":
		form = Food_Safety_and_Quality_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_18')
	else:
		form = Food_Safety_and_Quality_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_18.html',{
		'form':form,
		'submitted':submitted})





def rev_data0_19(request):
	submitted = False
	if request.method == "POST":
		form = Farm_Water_Source_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_19')
	else:
		form = Farm_Water_Source_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_19.html',{
		'form':form,
		'submitted':submitted})







def rev_data0_20(request):
	submitted = False
	if request.method == "POST":
		form = Farm_House_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_20')
	else:
		form = Farm_House_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_20.html',{
		'form':form,
		'submitted':submitted})



def rev_data0_21(request):
	submitted = False
	if request.method == "POST":
		form = inspector_symmary_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_21')
	else:
		form = inspector_symmary_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_21.html',{
		'form':form,
		'submitted':submitted})














# def step1(request):
#     if request.method == 'POST':
#         form = Full_Form(request.POST, prefix='step1')
#         if form.is_valid():
#             request.session['step1_data'] = form.cleaned_data
#             return redirect('step2')
#     else:
#         form = Full_Form(prefix='step1')
#     return render(request, 'gcna/step1.html', {'form': form})

# def step2(request):
#     if request.method == 'POST':
#         form = Full_Form(request.POST, prefix='step2')
#         if form.is_valid():
#             step1_data = request.session.get('step1_data')
#             if step1_data:
#                 step1_data.update(form.cleaned_data)
#                 request.session['step1_data'] = step1_data
#             else:
#                 request.session['step1_data'] = form.cleaned_data
#             return redirect('step3')
#     else:
#         step1_data = request.session.get('step1_data')
#         form = Full_Form(step1_data, prefix='step2')
#     return render(request, 'gcna/step2.html', {'form': form})

# def step3(request):
#     if request.method == 'POST':
#         form = Full_Form(request.POST, prefix='step3')
#         if form.is_valid():
#             step1_data = request.session.get('step1_data')
#             if step1_data:
#                 step1_data.update(form.cleaned_data)
#                 form = Full_Form(step1_data, prefix='step3')
#                 if form.is_valid():
#                     form.save()
#                     del request.session['step1_data']
#                     return redirect('submit')
#     else:
#         step1_data = request.session.get('step1_data')
#         form = Full_Form(step1_data, prefix='step3')
#     return render(request, 'gcna/step3.html', {'form': form})

# def submit(request):
#     if request.method == 'POST':
#         # Process the submitted form data
#         form_data = request.session.get('step1_data')
#         if form_data:
#             form = Full_Form(form_data)
#             if form.is_valid():
#                 form.save()
#                 del request.session['step1_data']
#                 return render(request, 'gcna/submit.html', {'form_data': form_data})
#     return redirect('`````````````````')


# def export(request):
#     person_resource = Land_tenurshipResource()
#     dataset = person_resource.export()
#     response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="persons.xls"'
#     return response

def import_exel(request):
    if request.method == 'POST':
        person_resource = fullformResources()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
            print(data[1])
            value = fullform(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
        		data[4],
        		data[5]



        		)
            value.save()       
        
 
    return render(request, 'gcna/import_form.html')



def import_dried_A_exel(request):
    if request.method == 'POST':
        person_resource = Dried_Form_A_Resources()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
            print(data[1])
            value = Dried_Moisture_Analysis_A(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
        		data[4],
        		data[5],
        		data[6],
        		data[7],
        		data[8],
        		data[9],
        		data[10],
        		data[12],
        		data[13],
        		data[14],
        		data[15],
        		data[16],
        		data[17],
        		data[18],
        		data[19],
        		data[20],
        		data[21],
        		data[22],
        		data[23],
        		)
            value.save()       
        
 
    return render(request, 'gcna/import_driedA.html')


def import_dried_B_exel(request):
    if request.method == 'POST':
        person_resource = Dried_Form_B_Resources()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
            print(data[1])
            value = Dried_Moisture_Analysis_B(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
        		data[4],
        		data[5],
        		data[6],
        		data[7],
        		data[8],
        		data[9],
        		data[10],
        		data[12],
        		data[13],
        		data[14],
        		data[15],
        		data[16],
        		data[17],
        		data[18],
        		data[19],
        		data[20],
        		data[21],
        		data[22],
        		data[23],
        		)
            value.save()       
        


    return render(request, 'gcna/import_driedB.html')






def import_floated_A_exel(request):
    if request.method == 'POST':
        person_resource = Floated_Form_A_Resources()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
            print(data[1])
            value = Floated_Moisture_Analysis_A(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
        		data[4],
        		data[5],
        		data[6],
        		data[7],
        		data[8],
        		data[9],
        		data[10],
        		data[12],
        		data[13],
        		data[14],
        		data[15],
        		data[16],
        		data[17],
        		data[18],
        		data[19],
        		data[20],
        		data[21],
        		data[22],
        		data[23],
        		data[24],
        		data[25],
        		data[26],
        		data[27],
        		data[28],
        		data[29],
        		data[30],
        		data[31],
        		data[32],
        		data[33],
        		data[34],
        		data[35],
        		data[36],
        		data[37],
        		data[38],
        		data[39],
        		data[40],
        		)
            value.save()       
        
 
    return render(request, 'gcna/import_floatedA.html')


def import_floated_B_exel(request):
    if request.method == 'POST':
        person_resource = Floated_Form_B_Resources()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
            print(data[1])
            value = Floated_Moisture_Analysis_B(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
        		data[4],
        		data[5],
        		data[6],
        		data[7],
        		data[8],
        		data[9],
        		data[10],
        		data[12],
        		data[13],
        		data[14],
        		data[15],
        		data[16],
        		data[17],
        		data[18],
        		data[19],
        		data[20],
        		data[21],
        		data[22],
        		data[23],
        		data[24],
        		data[25],
        		data[26],
        		data[27],
        		data[28],
        		data[29],
        		data[30],
        		data[31],
        		data[32],
        		data[33],
        		data[34],
        		data[35],
        		data[36],
        		data[37],
        		data[38],
        		data[39],
        		data[40],
        		data[41],
        		)
            value.save()       
        
 
    return render(request, 'gcna/import_floatedB.html')




def import_Quality_Control_exel(request):
    if request.method == 'POST':
        person_resource = Quality_Control_Resources()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
            print(data[1])
            value = Quality_Control(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
        		data[4],
        		data[5],
        		data[6],
        		data[7],
        		data[8],
        		data[9],
        		data[10],
        		data[11],
        		data[12],
        		data[13],
        		data[14],
        		data[15],
        		data[16],
        		data[17],
        		data[18],
        		data[19],
        		data[20],
        		)
            value.save()       
        
 
    return render(request, 'gcna/import_quality.html')

 


# def form_start_view(request):
#     return redirect('page1_view')


def your_view(request):
    if request.method == 'POST':
        form1 = Form1(request.POST)
        form2 = Form2(request.POST)
        if form1.is_valid() and form2.is_valid():
            field1_value = form1.cleaned_data['field1']
            form2.cleaned_data['field2'] = field1_value  # Set field2 value based on field1
            # Further processing or saving of form data

    else:
        form1 = Form1()
        form2 = Form2()

    context = {
        'form1': form1,
        'form2': form2
    }

    return render(request, 'your_template.html', context)







def comp_data(request):
	submitted = False
	if request.method == "POST":
		form1 = User_info_Form(request.POST)
		form2 = Land_tenurship_Form(request.POST)
		form3 = tree_Form(request.POST)
		form4 = farm_Form(request.POST)
		form5 = state_Form(request.POST)
		form6 = symmary_Form(request.POST)

		if all([form1.is_valid(),form2.is_valid(),form3.is_valid(),form4.is_valid(),form5.is_valid()]):
			# field1_value = form1.cleaned_data['farmer_ID']   
			# form2.cleaned_data['farmer_ID'] = field1_value
			# form3.cleaned_data['farmer_ID'] = field1_value
			# form4.cleaned_data['farmer_ID'] = field1_value
			# form5.cleaned_data['farmer_ID'] = field1_value
			# form6.cleaned_data['farmer_ID'] = field1_value


			form1.save()
			form2.save()
			form3.save()
			form4.save()
			form5.save()
			form6.save()

			return HttpResponseRedirect('/gcna0')
 


	else:
		form1 = User_info_Form
		form2 = Land_tenurship_Form
		form3 = tree_Form
		form4 = farm_Form
		form5 = state_Form
		form6 = symmary_Form

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/compform.html',{
		'form1':form1,
		'form2':form2,
		'form3':form3,
		'form4':form4,
		'form5':form5,
		'form6':form6,
		'submitted':submitted})




def comp_data1(request):
	submitted = False
	if request.method == "POST":
		form1 = User_info_Form(request.POST,request.FILES)
		if form1.is_valid():
			form1.save()
			return HttpResponseRedirect('/gcna0_1')
	else:
		form1 = User_info_Form

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/compform1.html',{
		'form1':form1,
		'submitted':submitted})



def comp_data2(request):
	submitted = False
	if request.method == "POST":
		form2 = Land_tenurship_Form(request.POST)
		if form2.is_valid():
			form2.save()
			return HttpResponseRedirect('/gcna0_2')
	else:
		form2 = Land_tenurship_Form

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/compform2.html',{
		'form2':form2,
		'submitted':submitted})


def comp_data3(request):
	submitted = False
	if request.method == "POST":
		form3 = tree_Form(request.POST)
		if form3.is_valid():
			form3.save()
			return HttpResponseRedirect('/gcna0_3')
	else:
		form3 = tree_Form

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/compform3.html',{
		'form3':form3,
		'submitted':submitted})









def comp_data4(request):
	submitted = False
	if request.method == "POST":
		form4 = farm_Form(request.POST)
		if form4.is_valid():
			form4.save()
			return HttpResponseRedirect('/gcna0_4')
	else:
		form4 = farm_Form

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/compform4.html',{
		'form4':form4,
		'submitted':submitted})





def comp_data5(request):
	submitted = False
	if request.method == "POST":
		form5 = state_Form(request.POST)
		if form5.is_valid():
			form5.save()
			return HttpResponseRedirect('/gcna0_5')
	else:
		form5 = state_Form

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/compform5.html',{
		'form5':form5,
		'submitted':submitted})





def comp_data6(request):
	submitted = False
	if request.method == "POST":
		form6 = symmary_Form(request.POST)
		if form6.is_valid():
			form6.save()
			return HttpResponseRedirect('/gcna0_6')
	else:
		form6 = symmary_Form

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/compform6.html',{
		'form6':form6,
		'submitted':submitted})






def add_data(request):
	submitted = False
	if request.method == "POST":
		form = Full_Form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/gcna7')

	else:
		form = Full_Form
		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/fillform.html',{'form':form, 'submitted':submitted})


def Dried_A_add_data(request):
	submitted = False
	if request.method == "POST":
		form1 = Dried_Form_A(request.POST)
		if form1.is_valid():
			form1.save()
			return HttpResponseRedirect('/gcna8')

	else:
		form1 = Dried_Form_A()

		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/DriedA.html',{'form1':form1, 'submitted':submitted})











def Dried_B_add_data(request):
	submitted = False
	if request.method == "POST":
		form2 = Dried_Form_B(request.POST)
		if form2.is_valid():
			form2.save()
			return HttpResponseRedirect('/gcna9')

	else:
		form2 = Dried_Form_B()



		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/DriedB.html',{'form2':form2, 'submitted':submitted})








def Floated_A_add_data(request):
	submitted = False
	if request.method == "POST":
		form3 = Floated_Form_A(request.POST)
		if form3.is_valid():
			form3.save()
			return HttpResponseRedirect('/gcna10')

	else:
		form3 = Floated_Form_A()



		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/FloatA.html',{'form3':form3, 'submitted':submitted})







def Floated_B_add_data(request):
	submitted = False
	if request.method == "POST":
		form4 = Floated_Form_B(request.POST)
		if form4.is_valid():
			form4.save()
			return HttpResponseRedirect('/gcna11')

	else:
		form4 = Floated_Form_B()



		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/FloatB.html',{'form4':form4, 'submitted':submitted})








def Quality_add_data(request):
	submitted = False
	if request.method == "POST":
		form5 = Quality_Form(request.POST)
		if form5.is_valid():
			form5.save()
			return HttpResponseRedirect('/gcna12')

	else:
		form5 = Quality_Form()




		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/Quality.html',{'form5':form5, 'submitted':submitted})































def Dried0_A_add_data(request):
	submitted = False
	if request.method == "POST":
		form1 = Dried_Form_A(request.POST)
		if form1.is_valid():
			form1.save()
			return redirect('Dried0_A_add_data')

	else:
		form1 = Dried_Form_A()




		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/Dried0A.html',{'form1':form1, 'submitted':submitted})











def Dried0_B_add_data(request):
	submitted = False
	if request.method == "POST":
		form2 = Dried_Form_B(request.POST)
		if form2.is_valid():
			form2.save()
			return redirect('Dried0_B_add_data')

	else:
		form2 = Dried_Form_B()



		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/Dried0B.html',{'form2':form2, 'submitted':submitted})








def Floated0_A_add_data(request):
	submitted = False
	if request.method == "POST":
		form3 = Floated_Form_A(request.POST)
		if form3.is_valid():
			form3.save()
			return redirect('Floated0_A_add_data')

	else:
		form3 = Floated_Form_A()



		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/Float0A.html',{'form3':form3, 'submitted':submitted})







def Floated0_B_add_data(request):
	submitted = False
	if request.method == "POST":
		form4 = Floated_Form_B(request.POST)
		if form4.is_valid():
			form4.save()
			return redirect('Floated0_B_add_data')

	else:
		form4 = Floated_Form_B()



		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/Float0B.html',{'form4':form4, 'submitted':submitted})








def Quality0_add_data(request):
	submitted = False
	if request.method == "POST":
		form5 = Quality_Form(request.POST)
		if form5.is_valid():
			form5.save()
			return redirect('Quality0_add_data')

	else:
		form5 = Quality_Form()




		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/Quality0.html',{'form5':form5, 'submitted':submitted})













# def page1_view(request):
#     if request.method == 'POST':
#         form = Full_Form(request.POST)
#         if form.is_valid():
#             # Store form data in the session
#             request.session['page1_data'] = form.cleaned_data
#             return redirect('page2_view')
#     else:
#         form = Full_Form()
#     return render(request, 'gcna/step1.html', {'form': form})

# def page2_view(request):
#     if request.method == 'POST':
#         form = Full_Form(request.POST)
#         if form.is_valid():
#             # Retrieve form data from the session
#             page1_data = request.session.get('page1_data')

#             # Combine form data from all pages
#             combined_data = {**page1_data, **form.cleaned_data}

#             # Create and save the model instance
#             MyModel.objects.create(**combined_data)

#             # Clear the session data
#             del request.session['page1_data']

#             return render(request, 'gcna/step2.html')
#     else:
#         form = Full_Form()
#     return render(request, 'gcna/step2.html', {'form': form})



def Full_farmB(request):
	user_list = User_info.objects.all()
	Land_tenurship_list = Land_tenurship.objects.all()
	tree_list = tree.objects.all()
	farm_list = farm.objects.all()
	state_list = state.objects.all()
	symmary_list = symmary.objects.all()
	return render(request,'gcna/farm_view 5.html',{
		'user_list': user_list,
		'Land_tenurship_list':Land_tenurship_list,
		'tree_list':tree_list,
		'farm_list':farm_list,
		'state_list':state_list,
		'symmary_list':symmary_list})



def all_farm(request):
	user_list = User_info.objects.all()
	return render(request,'gcna/farm_view.html',{'user_list': user_list})

def all_farm1(request):
	Land_tenurship_list = Land_Tenur.objects.all()
	return render(request,'gcna/farm_view 1.html',{'Land_tenurship_list': Land_tenurship_list})

def all_farm2(request):
	tree_list = tree.objects.all()
	return render(request,'gcna/farm_view 2.html',{'tree_list': tree_list})

def all_farm3(request):
	farm_list = farm.objects.all()
	return render(request,'gcna/farm_view 3.html',{'farm_list': farm_list})



def all_farm4(request):
	state_list = state.objects.all()
	return render(request,'gcna/farm_view 4.html',{'state_list': state_list})


def all_farm5(request):
	symmary_list = symmary.objects.all()
	return render(request,'gcna/farm_view 5.html',{'symmary_list': symmary_list})


def all_farm6(request):
	fullform_list = fullform.objects.all()
	return render(request,'gcna/farm_view 6.html',{'fullform_list': fullform_list})

def dried_A_Form(request):
	dried_A_list = Dried_Moisture_Analysis_A.objects.all()
	return render(request,'gcna/view_driedA.html',{'dried_A_list': dried_A_list})

def dried_B_Form(request):
	dried_B_list = Dried_Moisture_Analysis_B.objects.all()
	return render(request,'gcna/view_driedB.html',{'dried_B_list': dried_B_list})


def floated_A_Form(request):
	float_A_list = Floated_Moisture_Analysis_A.objects.all()
	return render(request,'gcna/view_floatedA.html',{'float_A_list': float_A_list})


def floated_B_Form(request):
	float_B_list = Floated_Moisture_Analysis_B.objects.all()
	return render(request,'gcna/view_floatedB.html',{'float_B_list': float_B_list})


def quality_Form(request):
	# test = Quality_Control.objects.get(pk=id)

	quality_list = Quality_Control.objects.all()
	return render(request,'gcna/view_quality.html',{'quality_list': quality_list})



def delete_quality(request, pk):
    quality = get_object_or_404(Quality_Control, pk=pk)
    if request.method == 'POST':
        quality.delete()
        return redirect('view_quality') 
    return redirect('error_page') 


def edit_quality(request, pk):
    quality = get_object_or_404(Quality_Control, pk=pk)
    if request.method == 'POST':
        form = Quality_Form(request.POST, instance=quality)
        if form.is_valid():
            form.save()
            return redirect('view_quality') 
    else:
        form = Quality_Form(instance=quality)
    return render(request, 'gcna/edit_quality.html', {'form': form})


def delete_dried_A(request, pk):
    dried = Dried_Moisture_Analysis_A.objects.get(pk=pk)
    dried.delete()
    return redirect('view_driedA')  


def delete_dried_B(request, pk):
    dried = Dried_Moisture_Analysis_B.objects.get(pk=pk)
    dried.delete()
    return redirect('view_driedB')  # Redirect to the desired URL after deletion

def delete_floated_A(request, pk):
    dried = Floated_Moisture_Analysis_A.objects.get(pk=pk)
    dried.delete()
    return redirect('view_floatedA')  # Redirect to the desired URL after deletion

def delete_floated_B(request, pk):
    dried = Floated_Moisture_Analysis_B.objects.get(pk=pk)
    dried.delete()
    return redirect('view_floatedB')  # Redirect to the desired URL after deletion

def edit_floated_A(request, pk):
    float_A = Floated_Moisture_Analysis_A.objects.get(pk=pk)
    if request.method == 'POST':
        form = Floated_Form_A(request.POST, instance=float_A)
        if form.is_valid():
            form.save()
            return redirect('view_floatedA') 
    else:
        form = Floated_Form_A(instance=float_A)
    return render(request, 'gcna/edit_floated_A.html', {'form': form})

def edit_floated_B(request, pk):
    dried = Floated_Moisture_Analysis_B.objects.get(pk=pk)
    if request.method == 'POST':
        form = Floated_Form_B(request.POST, instance=dried)
        if form.is_valid():
            form.save()
            return redirect('view_floatedB') 
    else:
        form = Floated_Form_B(instance=dried)
    return render(request, 'gcna/edit_floated_B.html', {'form': form})

def edit_dried_B(request, pk):
    dried = Dried_Moisture_Analysis_B.objects.get(pk=pk)
    if request.method == 'POST':
        form = Dried_Form_B(request.POST, instance=dried)
        if form.is_valid():
            form.save()
            return redirect('view_driedB') 
    else:
        form = Dried_Form_B(instance=dried)
    return render(request, 'gcna/edit_dried_B.html', {'form': form})


def edit_dried_A(request, pk):
    dried = Dried_Moisture_Analysis_A.objects.get(pk=pk)
    if request.method == 'POST':
        form = Dried_Form_A(request.POST, instance=dried)
        if form.is_valid():
            form.save()
            return redirect('view_driedA') 
    else:
        form = Dried_Form_A(instance=dried)
    return render(request, 'gcna/edit_dried_A.html', {'form': form})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
# def home(request):
	request.session['Nutmeg_ID_No'] = ' '
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)
	month = month.capitalize()
	cal = HTMLCalendar().formatmonth(year, month_number)
	now = datetime.now()
	current_year= now.year
	time = now.strftime('%I:%M:%S %p')


	return render(request,'gcna/home.html', {
		"year":year,
		"month":month,
		"month_number":month_number,
		"cal":cal,
		"current_year":current_year,
		"time":time,
		})








def view_Farm_table1(request):
	farmer_info_id = Farmer_Info.objects.all()
	return render(request,'gcna/view_farm1.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table2(request):
	farmer_info_id = land_info.objects.all()
	return render(request,'gcna/view_farm2.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table3(request):
	farmer_info_id = Land_Tenur.objects.all()
	return render(request,'gcna/view_farm3.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table4(request):
	farmer_info_id = Nutmeg_Trees.objects.all()
	return render(request,'gcna/view_farm4.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table5(request):
	farmer_info_id = Nutmeg_Variety.objects.all()
	return render(request,'gcna/view_farm5.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table6(request):
	farmer_info_id = Other_Crops.objects.all()
	return render(request,'gcna/view_farm6.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table7(request):
	farmer_info_id = Coconut_Trees.objects.all()
	return render(request,'gcna/view_farm7.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table8(request):
	farmer_info_id = Citrus_Mango_Trees.objects.all()
	return render(request,'gcna/view_farm8.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table9(request):
	farmer_info_id = Other_Spices_Trees.objects.all()
	return render(request,'gcna/view_farm9.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table10(request):
	farmer_info_id = Other_Seasoning_Trees.objects.all()
	return render(request,'gcna/view_farm10.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table11(request):
	farmer_info_id = Other_Crops_Cultivated.objects.all()
	return render(request,'gcna/view_farm11.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table12(request):
	farmer_info_id = Condition.objects.all()
	return render(request,'gcna/view_farm12.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table13(request):
	farmer_info_id = Nutmeg_Land.objects.all()
	return render(request,'gcna/view_farm13.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table14(request):
	farmer_info_id = Nutmeg_Frequency.objects.all()
	return render(request,'gcna/view_farm14.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table15(request):
	farmer_info_id = Potential_Risks.objects.all()
	return render(request,'gcna/view_farm15',{'farmer_info_id': farmer_info_id})

def view_Farm_table16(request):
	farmer_info_id = Policy.objects.all()
	return render(request,'gcna/view_farm16.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table17(request):
	farmer_info_id = Road_Access.objects.all()
	return render(request,'gcna/view_farm17.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table18(request):
	farmer_info_id = Food_Safety_and_Quality.objects.all()
	return render(request,'gcna/view_farm18.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table19(request):
	farmer_info_id = Farm_Water_Source.objects.all()
	return render(request,'gcna/view_farm19.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table20(request):
	farmer_info_id = Farm_House.objects.all()
	return render(request,'gcna/view_farm20.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table21(request):
	farmer_info_id = inspector_symmary.objects.all()
	return render(request,'gcna/view_farm21.html',{'farmer_info_id': farmer_info_id})












def view_Farm_table0_1(request):
	farmer_info_id = Farmer_Info.objects.all()
	return render(request,'gcna/view_farm0_1.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_2(request):
	farmer_info_id = land_info.objects.all()
	return render(request,'gcna/view_farm0_2.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_3(request):
	farmer_info_id = Land_Tenur.objects.all()
	return render(request,'gcna/view_farm0_3.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_4(request):
	farmer_info_id = Nutmeg_Trees.objects.all()
	return render(request,'gcna/view_farm0_4.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_5(request):
	farmer_info_id = Nutmeg_Variety.objects.all()
	return render(request,'gcna/view_farm0_5.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_6(request):
	farmer_info_id = Other_Crops.objects.all()
	return render(request,'gcna/view_farm0_6.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_7(request):
	farmer_info_id = Coconut_Trees.objects.all()
	return render(request,'gcna/view_farm0_7.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_8(request):
	farmer_info_id = Citrus_Mango_Trees.objects.all()
	return render(request,'gcna/view_farm0_8.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_9(request):
	farmer_info_id = Other_Spices_Trees.objects.all()
	return render(request,'gcna/view_farm0_9.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_10(request):
	farmer_info_id = Other_Seasoning_Trees.objects.all()
	return render(request,'gcna/view_farm0_10.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_11(request):
	farmer_info_id = Other_Crops_Cultivated.objects.all()
	return render(request,'gcna/view_farm0_11.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_12(request):
	farmer_info_id = Condition.objects.all()
	return render(request,'gcna/view_farm0_12.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_13(request):
	farmer_info_id = Nutmeg_Land.objects.all()
	return render(request,'gcna/view_farm0_13.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_14(request):
	farmer_info_id = Nutmeg_Frequency.objects.all()
	return render(request,'gcna/view_farm0_14.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_15(request):
	farmer_info_id = Potential_Risks.objects.all()
	return render(request,'gcna/view_farm0_15.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_16(request):
	farmer_info_id = Policy.objects.all()
	return render(request,'gcna/view_farm0_16.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_17(request):
	farmer_info_id = Road_Access.objects.all()
	return render(request,'gcna/view_farm0_17.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_18(request):
	farmer_info_id = Food_Safety_and_Quality.objects.all()
	return render(request,'gcna/view_farm0_18.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_19(request):
	farmer_info_id = Farm_Water_Source.objects.all()
	return render(request,'gcna/view_farm0_19.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_20(request):
	farmer_info_id = Farm_House.objects.all()
	return render(request,'gcna/view_farm0_20.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_21(request):
	farmer_info_id = inspector_symmary.objects.all()
	return render(request,'gcna/view_farm0_21.html',{'farmer_info_id': farmer_info_id})










def edit_table0_1(request, pk):
	pk = Farmer_Info.objects.get(pk=pk)
	if request.method == 'POST':
		form = Farmer_Info_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_1') 
	else:
		form = Farmer_Info_Form(instance=pk)

	return render(request, 'gcna/edit_table0_1.html', {'form': form})





def edit_table0_2(request, pk):
	pk = land_info.objects.get(pk=pk)
	if request.method == 'POST':
		form = land_info_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('table001') 
	else:
		form = land_info_Form(instance=pk)

	return render(request, 'gcna/edit_table0_2.html', {'form': form})





def edit_table0_3(request, pk):
	pk = Land_Tenur.objects.get(pk=pk)
	if request.method == 'POST':
		form = Land_Tenur_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_3') 
	else:
		form = Land_Tenur_Form(instance=pk)

	return render(request, 'gcna/edit_table0_3.html', {'form': form})








def edit_table0_4(request, pk):
	pk = Nutmeg_Trees.objects.get(pk=pk)
	if request.method == 'POST':
		form = Nutmeg_Trees_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_4') 
	else:
		form = Nutmeg_Trees_Form(instance=pk)

	return render(request, 'gcna/edit_table0_4.html', {'form': form})





def edit_table0_5(request, pk):
	pk = Nutmeg_Variety.objects.get(pk=pk)
	if request.method == 'POST':
		form = Nutmeg_Variety_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_5') 
	else:
		form = Nutmeg_Variety_Form(instance=pk)

	return render(request, 'gcna/edit_table0_5.html', {'form': form})






def edit_table0_6(request, pk):
	pk = Other_Crops.objects.get(pk=pk)
	if request.method == 'POST':
		form = Other_Crops_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_6') 
	else:
		form = Other_Crops_Form(instance=pk)

	return render(request, 'gcna/edit_table0_6.html', {'form': form})





def edit_table0_7(request, pk):
	pk = Coconut_Trees.objects.get(pk=pk)
	if request.method == 'POST':
		form = Coconut_Trees_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_7') 
	else:
		form = Coconut_Trees_Form(instance=pk)

	return render(request, 'gcna/edit_table0_7.html', {'form': form})







def edit_table0_8(request, pk):
	pk = Citrus_Mango_Trees.objects.get(pk=pk)
	if request.method == 'POST':
		form = Citrus_Mango_Trees_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_8') 
	else:
		form = Citrus_Mango_Trees_Form(instance=pk)

	return render(request, 'gcna/edit_table0_8.html', {'form': form})



def edit_table0_9(request, pk):
	pk = Other_Spices_Trees.objects.get(pk=pk)
	if request.method == 'POST':
		form = Other_Spices_Trees_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_9') 
	else:
		form = Other_Spices_Trees_Form(instance=pk)

	return render(request, 'gcna/edit_table0_9.html', {'form': form})








def edit_table0_10(request, pk):
	pk = Other_Seasoning_Trees.objects.get(pk=pk)
	if request.method == 'POST':
		form = Other_Seasoning_Trees_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_10') 
	else:
		form = Other_Seasoning_Trees_Form(instance=pk)

	return render(request, 'gcna/edit_table_10.html', {'form': form})






def edit_table0_11(request, pk):
	pk = Other_Crops_Cultivated.objects.get(pk=pk)
	if request.method == 'POST':
		form = Other_Crops_Cultivated_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_11') 
	else:
		form = Other_Crops_Cultivated_Form(instance=pk)

	return render(request, 'gcna/edit_table_11.html', {'form': form})




def edit_table0_12(request, pk):
	pk = Condition.objects.get(pk=pk)
	if request.method == 'POST':
		form = Condition_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_12') 
	else:
		form = Condition_Form(instance=pk)

	return render(request, 'gcna/edit_table_12.html', {'form': form})




def edit_table0_13(request, pk):
	pk = Nutmeg_Land.objects.get(pk=pk)
	if request.method == 'POST':
		form = Nutmeg_Land_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_13') 
	else:
		form = Nutmeg_Land_Form(instance=pk)

	return render(request, 'gcna/edit_table_13.html', {'form': form})






def edit_table0_14(request, pk):
	pk = Nutmeg_Frequency.objects.get(pk=pk)
	if request.method == 'POST':
		form = Nutmeg_Frequency_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_14') 
	else:
		form = Nutmeg_Frequency_Form(instance=pk)

	return render(request, 'gcna/edit_table_14.html', {'form': form})



def edit_table0_15(request, pk):
	pk = Potential_Risks.objects.get(pk=pk)
	if request.method == 'POST':
		form = Potential_Risks_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_15') 
	else:
		form = Potential_Risks_Form(instance=pk)

	return render(request, 'gcna/edit_table_15.html', {'form': form})




def edit_table0_16(request, pk):
	pk = Policy.objects.get(pk=pk)
	if request.method == 'POST':
		form = Policy_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_16') 
	else:
		form = Policy_Form(instance=pk)

	return render(request, 'gcna/edit_table_16.html', {'form': form})




def edit_table0_17(request, pk):
	pk = Road_Access.objects.get(pk=pk)
	if request.method == 'POST':
		form = Road_Access_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_17') 
	else:
		form = Road_Access_Form(instance=pk)

	return render(request, 'gcna/edit_table0_17.html', {'form': form})




def edit_table0_18(request, pk):
	pk = Food_Safety_and_Quality.objects.get(pk=pk)
	if request.method == 'POST':
		form = Food_Safety_and_Quality_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_18') 
	else:
		form = Food_Safety_and_Quality_Form(instance=pk)

	return render(request, 'gcna/edit_table0_18.html', {'form': form})




def edit_table0_19(request, pk):
	pk = Farm_Water_Source.objects.get(pk=pk)
	if request.method == 'POST':
		form = Farm_Water_Source_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_19') 
	else:
		form = Farm_Water_Source_Form(instance=pk)

	return render(request, 'gcna/edit_table0_19.html', {'form': form})




def edit_table0_20(request, pk):
	pk = Farm_House.objects.get(pk=pk)
	if request.method == 'POST':
		form = Farm_House_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_20') 
	else:
		form = Farm_House_Form(instance=pk)

	return render(request, 'gcna/edit_table0_20.html', {'form': form})







def edit_table0_21(request, pk):
	pk = inspector_symmary.objects.get(pk=pk)
	if request.method == 'POST':
		form = inspector_symmary_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_21') 
	else:
		form = inspector_symmary_Form(instance=pk)

	return render(request, 'gcna/edit_table0_21.html', {'form': form})







def edit_table0_22(request, pk):
	pk = Training_support.objects.get(pk=pk)
	if request.method == 'POST':
		form = Training_support_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_22') 
	else:
		form = Training_support_Form(instance=pk)

	return render(request, 'gcna/edit_table0_22.html', {'form': form})



  



def edit_table0_23(request, pk):
	pk = Labour_support.objects.get(pk=pk)
	if request.method == 'POST':
		form = Labour_support_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_23') 
	else:
		form = Labour_support_Form(instance=pk)

	return render(request, 'gcna/edit_table0_23.html', {'form': form})







def edit_dried0_A(request):

	# farmer_info_id = request.session.get('Nutmeg_ID_No')
	# try:
	# 	farmer_info_id = Dried_Moisture_Analysis_A.objects.get(Nutmeg_ID_No=farmer_info_id)
	# except Dried_Moisture_Analysis_A.DoesNotExist:
	# 	return redirect('error_table_driedA')  


	# if request.method == 'POST':
	# 	form = Dried_Form_A(request.POST, instance=farmer_info_id)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('table') 
	# else:
	# 	form = Dried_Form_A(instance=farmer_info_id)
	return render(request, 'gcna/edit_dried0_A.html', {'form': form})








def display_dried0_A(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = Dried_Moisture_Analysis_A.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Dried_Moisture_Analysis_A.DoesNotExist:
	# 	return redirect('error_table_driedA')

	return render(request, 'gcna/view_dried0_A.html')









def edit_dried0_B(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Dried_Moisture_Analysis_B.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Dried_Moisture_Analysis_B.DoesNotExist:
		return redirect('error_table_driedB')  


	if request.method == 'POST':
		form = Dried_Form_B(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Dried_Form_B(instance=farmer_info_id)
	return render(request, 'gcna/edit_dried0_B.html', {'form': form})

  




def display_dried0_B(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = Dried_Moisture_Analysis_B.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Dried_Moisture_Analysis_B.DoesNotExist:
	# 	return redirect('error_table_driedB')

	return render(request, 'gcna/view_dried0_B.html')















def edit_floated0_A(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Floated_Moisture_Analysis_A.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Floated_Moisture_Analysis_A.DoesNotExist:
		return redirect('error_table_floatA')  


	if request.method == 'POST':
		form = Floated_Form_A(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Floated_Form_A(instance=farmer_info_id)
	return render(request, 'gcna/edit_floated0_A.html', {'form': form})






def display_floated0_A(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = Floated_Moisture_Analysis_A.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Floated_Moisture_Analysis_A.DoesNotExist:
	# 	return redirect('error_table_floatA')

	return render(request, 'gcna/view_floated0_A.html')












def edit_floated0_B(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Floated_Moisture_Analysis_B.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Floated_Moisture_Analysis_B.DoesNotExist:
		return redirect('error_table_floatB')  


	if request.method == 'POST':
		form = Floated_Form_B(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Floated_Form_B(instance=farmer_info_id)
	return render(request, 'gcna/edit_floated0_B.html', {'form': form})




def display_floated0_B(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = Floated_Moisture_Analysis_B.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Floated_Moisture_Analysis_B.DoesNotExist:
	# 	return redirect('error_table_floatB')

	return render(request, 'gcna/view_floated0_B.html')










def edit_quality0(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Quality_Control.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Quality_Control.DoesNotExist:
		return redirect('error_table_quality')  


	if request.method == 'POST':
		form = Quality_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Quality_Form(instance=farmer_info_id)
	return render(request, 'gcna/edit_quality0_.html', {'form': form})





def display_quality0(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = Quality_Control.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Quality_Control.DoesNotExist:
	# 	return redirect('error_table_quality')

	return render(request, 'gcna/view_quality0_.html')







def display_table_data21(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = inspector_symmary.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except inspector_symmary.DoesNotExist:
		return redirect('error_table21')

	return render(request, 'gcna/view_table21.html', context)









def delete_table0_1(request, id):
    if request.method == 'POST':
        try:
            # Implement your deletion logic here, e.g., using Django ORM
            farmer = Farmer_Info.objects.get(pk=id)
            farmer.delete()
            
            # If successful, return a JSON response indicating success
            return JsonResponse({'message': 'Deletion successful'})
        except Farmer_Info.DoesNotExist:
            # If the record doesn't exist, return an error response
            return JsonResponse({'message': 'Record not found'}, status=404)
 


def delete_table0_2(request, pk):
    pk = land_info.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_2')  


def delete_table0_3(request, pk):
    pk = Land_Tenur.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_3')  



def delete_table0_4(request, pk):
    pk = Nutmeg_Trees.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_4')  



def delete_table0_5(request, pk):
    pk = Nutmeg_Variety.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_5')  



def delete_table0_6(request, pk):
    pk = Other_Crops.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_6')  



def delete_table0_7(request, pk):
    pk = Coconut_Trees.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_7')  



def delete_table0_8(request, pk):
    pk = Citrus_Mango_Trees.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_8')  



def delete_table0_9(request, pk):
    pk = Other_Spices_Trees.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_9')  



def delete_table0_10(request, pk):
    pk = Other_Seasoning_Trees.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_10')  



def delete_table0_11(request, pk):
    pk = Other_Crops_Cultivated.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_11')  



def delete_table0_12(request, pk):
    pk = Condition.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_12')  



def delete_table0_13(request, pk):
    pk = Nutmeg_Land.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_13')  



def delete_table0_14(request, pk):
    pk = Nutmeg_Frequency.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_14')  



def delete_table0_15(request, pk):
    pk = Potential_Risks.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_15')  



def delete_table0_16(request, pk):
    pk = Policy.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_16')  



def delete_table0_17(request, pk):
    pk = Road_Access.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_17')  



def delete_table0_18(request, pk):
    pk = Food_Safety_and_Quality.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_18')  



def delete_table0_19(request, pk):
    pk = Farm_Water_Source.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_19')  



def delete_table0_20(request, pk):
    pk = Farm_House.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_20')  



def delete_table0_21(request, pk):
    pk = inspector_symmary.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_21')  


def delete_table0_22(request, pk):
    pk = Farm_House.objects.get(pk=pk)
    pk.delete()
    return redirect('Training_support')  



def delete_table0_23(request, pk):
    pk = inspector_symmary.objects.get(pk=pk)
    pk.delete()
    return redirect('Labour_support')  

 



def In_House_add_data(request):
	# submitted = False
	# if request.method == "POST":
		

	# 	form = In_House_Drying_Form(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('view_IH')

	# else:
	# 	form = In_House_Drying_Form()

	# 	if 'Nutmeg_ID_No' in request.session:
	# 		form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

	# 	# if 'Worker_ID_No' in request.session:
	# 	# 	form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


	# 	if 'submitted' in request.GET:
	# 		submitted = True

	return render(request,'gcna/In_House.html',{'form':form, 'submitted':submitted})
















def Dispatch_Dried_add_data(request):
	# submitted = False
	# if request.method == "POST":
	# 	form = Dispatch_Of_Dried_Nutmeg_Form(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('add_Dispatch_Dried')

	# else:
	# 	form = Dispatch_Of_Dried_Nutmeg_Form()

	# 	if 'Nutmeg_ID_No' in request.session:
	# 		form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

	# 	if 'submitted' in request.GET:
	# 		submitted = True

	return render(request,'gcna/Dispatched_Dried.html',{'form':form, 'submitted':submitted})

def Dispatch_Green_add_data(request):
	# submitted = False
	# if request.method == "POST":
	# 	form = Dispatch_Of_Green_Nutmeg_Form(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('add_Dispatch_Green')

	# else:
	# 	form = Dispatch_Of_Green_Nutmeg_Form()

	# 	if 'Nutmeg_ID_No' in request.session:
	# 		form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

	# 	if 'submitted' in request.GET:
	# 		submitted = True

	return render(request,'gcna/Dispatched_Green.html',{'form':form, 'submitted':submitted})

def Cracking_add_data(request):
	# submitted = False
	# if request.method == "POST":
	# 	form = Cracking_Summary_Form(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('add_Cracking')

	# else:
	# 	form = Cracking_Summary_Form()

	# 	if 'Nutmeg_ID_No' in request.session:
	# 		form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

	# 	if 'submitted' in request.GET:
	# 		submitted = True

	return render(request,'gcna/Cracking.html',{'form':form, 'submitted':submitted})

def Floation_add_data(request):
	# submitted = False
	# if request.method == "POST":
	# 	form = Floation_Summary_Form(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('add_Floation')

	# else:
	# 	form = Floation_Summary_Form()

	# 	if 'Nutmeg_ID_No' in request.session:
	# 		form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

	# 	if 'submitted' in request.GET:
	# 		submitted = True

	return render(request,'gcna/Floation.html',{'form':form, 'submitted':submitted})


def Package_add_data(request):
	# submitted = False
	# if request.method == "POST":
	# 	form = Package_Ciontrol_Form(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('add_Package')

	# else:
	# 	form = Package_Ciontrol_Form()

	# 	if 'Nutmeg_ID_No' in request.session:
	# 		form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

	# 	if 'submitted' in request.GET:
	# 		submitted = True

	return render(request,'gcna/Package.html',{'form':form, 'submitted':submitted})









def Pending_add_data(request):
	submitted = False
	# if request.method == "POST":
	# 	form = In_House_Drying_Form(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('add_In_House_0')

	# else:
	form = In_House_Drying_Form()
	form1 = Shelves_Form()


	# 	if 'Nutmeg_ID_No' in request.session:
	# 		form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

	# 	if 'submitted' in request.GET:
	# 		submitted = True

	return render(request,'gcna/InHouse_Pending.html',{'form':form,'form1':form1, 'submitted':submitted})





def In_House_0_add_data(request):
	submitted = False
	# if request.method == "POST":
	# 	form = In_House_Drying_Form(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('add_In_House_0')

	# else:
	form = In_House_Drying_Form()
	form1 = Shelves_Form()
	form2 = SectionForm()



	# 	if 'Nutmeg_ID_No' in request.session:
	# 		form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

	# 	if 'submitted' in request.GET:
	# 		submitted = True

	return render(request,'gcna/In_House_0.html',{'form':form,'form1':form1,'form2':form2, 'submitted':submitted})




def Dispatch_Dried_0_add_data(request):
	submitted = False
	# if request.method == "POST":
	# 	form = Dispatch_Of_Dried_Nutmeg_Form(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('add_Dispatch_Dried_0')

	# else:
	form1 = SectionForm()
	form = Dispatch_Of_Dried_Nutmeg_Form()
	form_popups= Vehicle_Inspection_Form()


		# if 'Nutmeg_ID_No' in request.session:
		# 	form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		# if 'submitted' in request.GET:
		# 	submitted = True


	return render(request,'gcna/Dispatched_Dried_0.html',{'form':form, 'form1':form1,'form_popups':form_popups, 'submitted':submitted})






def Dispatch_Green_0_add_data(request):
	submitted = False
	# if request.method == "POST":
	# form = Dispatch_Of_Green_Nutmeg_Form(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('add_Dispatch_Green_0')

	# else:
	form = Dispatch_Of_Green_Nutmeg_Form()

	# 	if 'Nutmeg_ID_No' in request.session:
	# 		form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

	# 	if 'submitted' in request.GET:
	# 		submitted = True

	return render(request,'gcna/Dispatched_Green_0.html',{'form':form, 'submitted':submitted})



def pending_cracking(request):
    return render(request, 'gcna/pending-cracking.html')



def pending_mace_purchase(request):
    return render(request, 'gcna/view_Mace_Purchase_Pending.html')

def pending_floating(request):
    return render(request, 'gcna/pending-floating.html')

def Cracking_0_add_data(request):
	submitted = False
	# if request.method == "POST":
	# form = Cracking_Summary_Form(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('add_Cracking_0')

	# else:
	form = Cracking_Summary_Form()

	# 	if 'Nutmeg_ID_No' in request.session:
	# 		form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

	# 	if 'submitted' in request.GET:
	# 		submitted = True

	return render(request,'gcna/Cracking_0.html',{'form':form, 'submitted':submitted})





def Cracking_Extraction_0_add_data(request):
	submitted = False

	form = Cracking_Extraction_Summary_Form()

	return render(request,'gcna/Cracking_Extraction_0.html',{'form':form, 'submitted':submitted})







def view_Cracking_Extraction_table_0(request):
	submitted = False

	form = Cracking_Extraction_Summary_Form()

	return render(request,'gcna/Cracking_Extraction_0.html',{'form':form, 'submitted':submitted})





def Floation_0_add_data(request):
	submitted = False
	# if request.method == "POST":
	# form = Floation_Summary_Form(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('add_Floation_0')

	# else:
	form = Floation_Summary_Form()

	# 	if 'Nutmeg_ID_No' in request.session:
	# 		form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

	# 	if 'submitted' in request.GET:
	# 		submitted = True

	return render(request,'gcna/Floation_0.html',{'form':form, 'submitted':submitted})





def Package_0_add_data(request):
	submitted = False
	# if request.method == "POST":
	# form = Package_Ciontrol_Form(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('add_Package_0')

	# else:
	form = Package_Ciontrol_Form()

	# 	if 'Nutmeg_ID_No' in request.session:
	# 		form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

	# 	if 'submitted' in request.GET:
	# 		submitted = True

	return render(request,'gcna/Package_0.html',{'form':form, 'submitted':submitted})



















def view_In_House_Drying_table(request):
	form = In_House_Drying.objects.all()
	return render(request,'gcna/view_IHD.html',{'form': form})

def view_Dispatch_Of_Dried_Nutmeg_table(request):
	form = Dispatch_Of_Dried_Nutmeg.objects.all()
	return render(request,'gcna/view_DDN.html',{'form': form})


def view_Dispatch_Of_Green_Nutmeg_table(request):
	form = Dispatch_Of_Green_Nutmeg.objects.all()
	return render(request,'gcna/view_DGN.html',{'form': form})


def view_Cracking_Summary_table(request):
	form = Cracking_Summary.objects.all()
	return render(request,'gcna/view_CS.html',{'form': form})


def view_Floation_Summary_table(request):
	form = Floation_Summary.objects.all()
	return render(request,'gcna/view_FS.html',{'form': form})



def view_Package_Ciontrol_table(request):
	form = Package_Ciontrol.objects.all()
	return render(request,'gcna/view_PK.html',{'form': form})













def view_In_House_Drying_table_0(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']


	# try:
	# 	farmer_info_id = In_House_Drying.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	# 		'farmer_info_id': farmer_info_id
	# 	}

	# except In_House_Drying.DoesNotExist:
	# 	return redirect('error_table_driedA')
	


	form = In_House_Drying_Form()
	form1 = Shelves_Form()
	form2 = SectionForm()








	return render(request,'gcna/view_IHD_0.html',{'form':form,'form1':form1,'form2':form2})




def view_Dispatch_Of_Dried_Nutmeg_table_0(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']


	# try:
	# 	farmer_info_id = Dispatch_Of_Dried_Nutmeg.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Dispatch_Of_Dried_Nutmeg.DoesNotExist:
	# 	return redirect('error_table_driedA')




	return render(request,'gcna/view_DDN_0.html')


def view_Dispatch_Of_Green_Nutmeg_table_0(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']


	# try:
	# 	farmer_info_id = Dispatch_Of_Green_Nutmeg.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Dispatch_Of_Green_Nutmeg.DoesNotExist:
	# 	return redirect('error_table_driedA')




	return render(request,'gcna/view_DGN_0.html')


def view_Cracking_Summary_table_0(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']


	# try:
	# 	farmer_info_id = Cracking_Summary.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Cracking_Summary.DoesNotExist:
	# 	return redirect('error_table_driedA')





	return render(request,'gcna/view_CS_0.html')


def view_Floation_Summary_table_0(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']


	# try:
	# 	farmer_info_id = Floation_Summary.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Floation_Summary.DoesNotExist:
	# 	return redirect('error_table_driedA')



	return render(request,'gcna/view_FS_0.html')




def view_Package_Ciontrol_table_0(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']

	form = Package_Ciontrol_Form()

	context = {
	        'form': form
		}




	return render(request,'gcna/view_PK_0.html',context)










def edit_In_House_Drying_table_0(request, pk):
	pk = In_House_Drying.objects.get(pk=pk)
	if request.method == 'POST':
		form = In_House_Drying_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_1') 
	else:
		form = In_House_Drying_Form(instance=pk)

	return render(request, 'gcna/edit_IHD_0.html', {'form': form})









def edit_Dispatch_Of_Dried_Nutmeg_table_0(request, pk):
	pk = Dispatch_Of_Dried_Nutmeg.objects.get(pk=pk)
	if request.method == 'POST':
		form = Dispatch_Of_Dried_Nutmeg_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_1') 
	else:
		form = Dispatch_Of_Dried_Nutmeg_Form(instance=pk)

	return render(request, 'gcna/edit_DDN_0.html', {'form': form})







def edit_Dispatch_Of_Green_Nutmeg_table_0(request, pk):
	pk = Dispatch_Of_Green_Nutmeg.objects.get(pk=pk)
	if request.method == 'POST':
		form = Dispatch_Of_Green_Nutmeg_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_1') 
	else:
		form = Dispatch_Of_Green_Nutmeg_Form(instance=pk)

	return render(request, 'gcna/edit_DGN_0.html', {'form': form})







def edit_Cracking_Summary_table_0(request, pk):
	pk = Cracking_Summary.objects.get(pk=pk)
	if request.method == 'POST':
		form = Cracking_Summary_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_1') 
	else:
		form = Cracking_Summary_Form(instance=pk)

	return render(request, 'gcna/edit_CS_0.html', {'form': form})







def edit_Floation_Summary_table_0(request, pk):
	pk = Floation_Summary.objects.get(pk=pk)
	if request.method == 'POST':
		form = Floation_Summary_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_1') 
	else:
		form = Floation_Summary_Form(instance=pk)

	return render(request, 'gcna/edit_FS_0.html', {'form': form})







def edit_Package_Ciontrol_table_0(request, pk):
	pk = Package_Ciontrol.objects.get(pk=pk)
	if request.method == 'POST':
		form = Package_Ciontrol_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_1') 
	else:
		form = Package_Ciontrol_Form(instance=pk)

	return render(request, 'gcna/edit_PC_0.html', {'form': form})






def edit_In_House_Drying_table(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = In_House_Drying.objects.get(Nutmeg_ID_No=farmer_info_id)
	except In_House_Drying.DoesNotExist:
		return redirect('error_In_House')  

	if request.method == 'POST':
		form = In_House_Drying_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = In_House_Drying_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_IHD.html', {'form': form})








def edit_Dispatch_Of_Dried_Nutmeg_table(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Dispatch_Of_Dried_Nutmeg.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Dispatch_Of_Dried_Nutmeg.DoesNotExist:
		return redirect('error_Dispatch_Dried_Nutmeg')  

	if request.method == 'POST':
		form = Dispatch_Of_Dried_Nutmeg_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Dispatch_Of_Dried_Nutmeg_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_DDN.html', {'form': form})










def edit_Dispatch_Of_Green_Nutmeg_table(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Dispatch_Of_Green_Nutmeg.objects.get(Nutmeg_ID_No=farmer_info_id)

	except Dispatch_Of_Green_Nutmeg.DoesNotExist:
		return redirect('error_Dispatch_Green_Nutmeg')  

	if request.method == 'POST':
		form = Dispatch_Of_Green_Nutmeg_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Dispatch_Of_Green_Nutmeg_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_DGN.html', {'form': form})













def edit_Cracking_Summary_table(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Cracking_Summary.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Cracking_Summary.DoesNotExist:
		return redirect('error_Cracking_Nutmeg')  

	if request.method == 'POST':
		form = Cracking_Summary_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Cracking_Summary_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_CS.html', {'form': form})








def edit_Floation_Summary_table(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Floation_Summary.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Floation_Summary.DoesNotExist:
		return redirect('error_Floation')  

	if request.method == 'POST':
		form = Floation_Summary_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Floation_Summary_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_FS.html', {'form': form})










def edit_Package_Ciontrol_table(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Package_Ciontrol.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Package_Ciontrol.DoesNotExist:
		return redirect('error_Package')  

	if request.method == 'POST':
		form = Package_Ciontrol_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Package_Ciontrol_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_PC.html', {'form': form})

























def display_dried0_A(request):
	# farmer_info_id = request.session['Nutmeg_ID_No']

	# try:
	# 	farmer_info_id = Dried_Moisture_Analysis_A.objects.get(Nutmeg_ID_No=farmer_info_id)
	# 	context = {
	#         'farmer_info_id': farmer_info_id
	# 	}

	# except Dried_Moisture_Analysis_A.DoesNotExist:
	# 	return redirect('error_table_driedA')

	return render(request, 'gcna/view_dried0_A.html')







def adhome(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
# def home(request):
	request.session['Nutmeg_ID_No'] = ' '
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)
	month = month.capitalize()
	cal = HTMLCalendar().formatmonth(year, month_number)
	now = datetime.now()
	current_year= now.year
	time = now.strftime('%I:%M:%S %p')


	return render(request,'gcna/adhome.html', {
		"year":year,
		"month":month,
		"month_number":month_number,
		"cal":cal,
		"current_year":current_year,
		"time":time,
		})