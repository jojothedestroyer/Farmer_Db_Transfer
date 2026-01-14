from django import forms 
from django.forms import ModelForm
# from .models import fullform
from .models import Dried_Moisture_Analysis_A 
from .models import Dried_Moisture_Analysis_B 
from .models import Floated_Moisture_Analysis_A 
from .models import Floated_Moisture_Analysis_B 
from .models import Quality_Control 
from datetime import date

# from .models import User_info
# from .models import Land_tenurship 
# from .models import tree 
# from .models import farm 
# from .models import state
# from .models import symmary 
# from .models import fullform
import calculation
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.contrib.contenttypes.models import ContentType


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





from .models import In_House_Drying 
from .models import Dispatch_Of_Dried_Nutmeg 
from .models import Dispatch_Of_Green_Nutmeg 
from .models import Cracking_Summary 
from .models import Floation_Summary 
from .models import Package_Ciontrol 

from .models import Labour_support 
from .models import Training_support 
from .models import visit 



from .models import Sanitation_A 
from .models import Sanitation_B 
from .models import Sanitation_C 



from .models import Cracking_Schedule 
from .models import Assorting_Log 
from .models import Extractor_Log
from .models import Fumigation_Log
from .models import Shelves




from .models import Vehicle_Inspection
from .models import Final_Weight_Inspection
from .models import Final_Weight_Inspection_fields




from .models import Dispatch_Of_Dried_Nutmeg_Rec
from .models import Dispatch_Of_Green_Nutmeg_Rec



from .models import Mace_Dispatched
from .models import Mace_Purchase

from .models import Mace_Dispatched_Rec

from .models import Cracking_Extraction_Summary

from .models import Day_Of_Loading
from .models import TruckEntry
from .models import Container_Inspection_Log















class Container_Inspection_Log_Form(ModelForm):
    class Meta:
        model = Container_Inspection_Log
        fields = '__all__'
        widgets = {
              


            # # Inspection Details
            # 'Date_Of_Inspection': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            # 'Time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            # 'Date_Of_Intended_Use': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            
            # # Container Pre-Inspection (Dropdown Selects)
            # 'Free_From_Dent': forms.Select(attrs={'class': 'form-control'}),
            # 'Free_From_Holes': forms.Select(attrs={'class': 'form-control'}),
            # 'Free_From_Rust': forms.Select(attrs={'class': 'form-control'}),
            # 'Seals_Without_Vents': forms.Select(attrs={'class': 'form-control'}),
            # 'Locking_Mech_Func': forms.Select(attrs={'class': 'form-control'}),

            # # Floor Inside
            # 'FL_Clean': forms.Select(attrs={'class': 'form-control'}),
            # 'FL_Dry': forms.Select(attrs={'class': 'form-control'}),
            # 'FL_Surface': forms.Select(attrs={'class': 'form-control'}),
            # 'FL_Odors': forms.Select(attrs={'class': 'form-control'}),

            # # Roof Inside
            # 'RF_Free_From_Dent': forms.Select(attrs={'class': 'form-control'}),
            # 'RF_Free_From_Holes': forms.Select(attrs={'class': 'form-control'}),
            # 'RF_Free_From_Rust': forms.Select(attrs={'class': 'form-control'}),
            # 'RF_Dry': forms.Select(attrs={'class': 'form-control'}),

            # # Right Inside
            # 'RI_Free_From_Dent': forms.Select(attrs={'class': 'form-control'}),
            # 'RI_Free_From_Holes': forms.Select(attrs={'class': 'form-control'}),
            # 'RI_Free_From_Rust': forms.Select(attrs={'class': 'form-control'}),
            # 'RI_Dry': forms.Select(attrs={'class': 'form-control'}),

            # # Left Inside
            # 'LI_Free_From_Dent': forms.Select(attrs={'class': 'form-control'}),
            # 'LI_Free_From_Holes': forms.Select(attrs={'class': 'form-control'}),
            # 'LI_Free_From_Rust': forms.Select(attrs={'class': 'form-control'}),
            # 'LI_Dry': forms.Select(attrs={'class': 'form-control'}),

            # # Approval and Recommendation
            # 'Recommend': forms.Select(attrs={'class': 'form-control'}),
            # 'Approved': forms.Select(attrs={'class': 'form-control'}),

            # # Loading Details
            # 'Date_Of_Loading': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            # 'Time_Loading_Start': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            # 'Time_Loading_End': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),

            # # Container Details
            # 'Container_Size': forms.Select(attrs={'class': 'form-control'}),
            # 'Container_Condition': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            # 'Absorabant_Used': forms.Select(attrs={'class': 'form-control'}),
            # 'Placement': forms.Select(attrs={'class': 'form-control'}),
            # 'Fumigant': forms.Select(attrs={'class': 'form-control'}),

            # # Inspected and Reviewed Dates
            # 'inspected_Date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

            # 'reviewed_Date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),






# class Container_Inspection_Log(models.Model):






    'entryCheck' : forms.TextInput(attrs={'class': 'form-control'}),
    'Date_Of_Inspection': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    'Time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
    'Date_Of_Intended_Use': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    'Agent': forms.TextInput(attrs={'class': 'form-control'}),
    'Size_Of_Container': forms.TextInput(attrs={'class': 'form-control'}),
    'Location_Of_Container': forms.TextInput(attrs={'class': 'form-control'}),
    'Container_Number': forms.TextInput(attrs={'class': 'form-control'}),
    'Intended_Customer': forms.TextInput(attrs={'class': 'form-control'}),
    'Products_To_Be_Shipped': forms.TextInput(attrs={'class': 'form-control'}),
    'Goods_Prev_Stored': forms.Textarea(attrs={'class': 'form-control'}),
    'Free_From_Dent': forms.Select(attrs={'class': 'form-control'}),
    'Free_From_Holes': forms.Select(attrs={'class': 'form-control'}),
    'Free_From_Rust': forms.Select(attrs={'class': 'form-control'}),
    'Seals_Without_Vents': forms.Select(attrs={'class': 'form-control'}),
    'Locking_Mech_Func': forms.Select(attrs={'class': 'form-control'}),
    'FL_Clean': forms.Select(attrs={'class': 'form-control'}),
    'FL_Dry': forms.Select(attrs={'class': 'form-control'}),
    'FL_Surface': forms.Select(attrs={'class': 'form-control'}),
    'FL_Odors': forms.Select(attrs={'class': 'form-control'}),
    'RF_Free_From_Dent': forms.Select(attrs={'class': 'form-control'}),
    'RF_Free_From_Holes': forms.Select(attrs={'class': 'form-control'}),
    'RF_Free_From_Rust': forms.Select(attrs={'class': 'form-control'}),
    'RF_Dry': forms.Select(attrs={'class': 'form-control'}),
    'RI_Free_From_Dent': forms.Select(attrs={'class': 'form-control'}),
    'RI_Free_From_Holes': forms.Select(attrs={'class': 'form-control'}),
    'RI_Free_From_Rust': forms.Select(attrs={'class': 'form-control'}),
    'RI_Dry': forms.Select(attrs={'class': 'form-control'}),
    'LI_Free_From_Dent': forms.Select(attrs={'class': 'form-control'}),
    'LI_Free_From_Holes': forms.Select(attrs={'class': 'form-control'}),
    'LI_Free_From_Rust': forms.Select(attrs={'class': 'form-control'}),
    'LI_Dry': forms.Select(attrs={'class': 'form-control'}),
    'Other_Comments': forms.Textarea(attrs={'class': 'form-control'}),
    'Inspected_By': forms.TextInput(attrs={'class': 'form-control'}),
    'Recommend': forms.Textarea(attrs={'class': 'form-control'}),
    'Approved': forms.Select(attrs={'class': 'form-control'}),
    'Date_Of_Loading': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    'Time_Loading_Start': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
    'Time_Loading_End' : forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
    'Port_of_Loading': forms.TextInput(attrs={'class': 'form-control'}),
    'Container_Number': forms.TextInput(attrs={'class': 'form-control'}),
    'Container_Size': forms.Select(attrs={'class': 'form-control'}),
    'Container_Condition': forms.TextInput(attrs={'class': 'form-control'}),#Make CheckBoxs with the following options Dry,Cleasn,Free from Ordor, Free from Holes, Closes Tightly.Multiple shouldnbe clicked
    'Container_Condition_st': forms.TextInput(attrs={'class': 'form-control'}),#Make CheckBoxs with the following options Dry,Cleasn,Free from Ordor, Free from Holes, Closes Tightly.Multiple shouldnbe clicked
    'Customer': forms.TextInput(attrs={'class': 'form-control'}),
    'Seal_Number': forms.TextInput(attrs={'class': 'form-control'}),
    'Bill_Of_Lading': forms.TextInput(attrs={'class': 'form-control'}),
    'Absorabant_Used': forms.Select(attrs={'class': 'form-control'}),
    'Placement': forms.Select(attrs={'class': 'form-control'}),
    'Fumigant': forms.Select(attrs={'class': 'form-control'}),
    'Fumigated_By': forms.TextInput(attrs={'class': 'form-control'}),
    'Comments': forms.Textarea(attrs={'class': 'form-control'}),
    'Inspected_And_Prepared_By': forms.TextInput(attrs={'class': 'form-control'}),
    'inspected_Date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    'Reviewed_By': forms.TextInput(attrs={'class': 'form-control'}),
    'reviewed_Date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})

        }



class Day_Of_Loading_Form(ModelForm):
    class Meta:
        model = Day_Of_Loading
        fields = '__all__'
        widgets = {
            'Date_Of_Inspection': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'Time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'Date_Of_Intended_Use': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'Free_From_Dent': forms.Select(attrs={'class': 'form-control'}),
            'Free_From_Holes': forms.Select(attrs={'class': 'form-control'}),
            'Free_From_Rust': forms.Select(attrs={'class': 'form-control'}),
            'Seals_Without_Vents': forms.Select(attrs={'class': 'form-control'}),
            'Locking_Mech_Func': forms.Select(attrs={'class': 'form-control'}),
            'FL_Clean': forms.Select(attrs={'class': 'form-control'}),
            'FL_Dry': forms.Select(attrs={'class': 'form-control'}),
            'FL_Surface': forms.Select(attrs={'class': 'form-control'}),
            'FL_Odors': forms.Select(attrs={'class': 'form-control'}),
            'RF_Free_From_Dent': forms.Select(attrs={'class': 'form-control'}),
            'RF_Free_From_Holes': forms.Select(attrs={'class': 'form-control'}),
            'RF_Free_From_Rust': forms.Select(attrs={'class': 'form-control'}),
            'RF_Dry': forms.Select(attrs={'class': 'form-control'}),
            'RI_Free_From_Dent': forms.Select(attrs={'class': 'form-control'}),
            'RI_Free_From_Holes': forms.Select(attrs={'class': 'form-control'}),
            'RI_Free_From_Rust': forms.Select(attrs={'class': 'form-control'}),
            'RI_Dry': forms.Select(attrs={'class': 'form-control'}),
            'LI_Free_From_Dent': forms.Select(attrs={'class': 'form-control'}),
            'LI_Free_From_Holes': forms.Select(attrs={'class': 'form-control'}),
            'LI_Free_From_Rust': forms.Select(attrs={'class': 'form-control'}),
            'LI_Dry': forms.Select(attrs={'class': 'form-control'}),
            'Recommend': forms.Select(attrs={'class': 'form-control'}),
            'Approved': forms.Select(attrs={'class': 'form-control'}),
            'Date_Of_Loading': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'Time_Loading_Start': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'Time_Loading_End': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'Approved': forms.Select(attrs={'class': 'form-control'}),
            'Container_Size': forms.Select(attrs={'class': 'form-control'}),
            'Container_Condition': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'Absorabant_Used': forms.Select(attrs={'class': 'form-control'}),
            'Placement': forms.Select(attrs={'class': 'form-control'}),
            'Fumigant': forms.Select(attrs={'class': 'form-control'}),
            'inspected_Date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'reviewed_Date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class TruckEntry_Form(ModelForm):
    class Meta:
        model = TruckEntry
        fields = '__all__'
        widgets = {
            'Type_Of_Bag': forms.Select(),
            'Tarpaulin_Used': forms.Select(),
            'Condition_On_Arrival': forms.Select(),
        }



# class Day_Of_Loading_Form(ModelForm):
#     class Meta:
#         model = Day_Of_Loading
#         fields = '__all__'
#         widgets ={


#         }
		








# class TruckEntry_Form(ModelForm):
#     class Meta:
#         model = TruckEntry
#         fields = '__all__'
#         widgets ={


#         }
		





class Cracking_Extraction_Summary_Form(ModelForm):
    class Meta:
        model = Cracking_Extraction_Summary
        fields = '__all__'
        widgets ={


        }
		




class Mace_Dispatched_Rec_Form(ModelForm):

    DATE_CREATED = forms.DateField(
        initial=date.today, 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )


    class Meta:
        model = Mace_Dispatched_Rec
        fields = '__all__'
        widgets ={

    'Date': forms.DateInput(attrs={'type':'date','class':'form-control'}),

    'STATION': forms.Select(attrs={'class':'form-control'}),    
    'BATCH_CODE': forms.TextInput(attrs={'class':'form-control'}),
    'DATE_OF_PURCHASE': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'PLACE_OF_PURCHASE': forms.Select(attrs={'class':'form-control'}),    
    'TOTAL_NUM_OF_FARMERS': forms.NumberInput(attrs={'class':'form-control'}),
    'TOTAL_LBS_NUTMEG_BOUGHT': forms.NumberInput(attrs={'class':'form-control'}),
    'NUM_OF_BAGS': forms.NumberInput(attrs={'class':'form-control'}),
    

    'MACE_1': forms.NumberInput(attrs={'class':'form-control'}),
    'BATCH_CODE_M1': forms.TextInput(attrs={'class':'form-control'}),

    'MACE_2': forms.NumberInput(attrs={'class':'form-control'}),
    'BATCH_CODE_M2': forms.TextInput(attrs={'class':'form-control'}),
    'Vehicle_number': forms.TextInput(attrs={'class':'form-control'}),    


    'MACE_3': forms.NumberInput(attrs={'class':'form-control'}),
    'BATCH_CODE_M3': forms.TextInput(attrs={'class':'form-control'}),

     'Delivery_advice_num': forms.TextInput(attrs={'class':'form-control'}),
'Station_rec':forms.TextInput(attrs={'class':'form-control'}),
'Product' :forms.TextInput(attrs={'class':'form-control'}),
'Num_Bags': forms.NumberInput(attrs={'class':'form-control'}),
'Weight': forms.NumberInput(attrs={'class':'form-control'}),
'conf_Product':forms.TextInput(attrs={'class':'form-control'}),
'conf_Num_Bags': forms.NumberInput(attrs={'class':'form-control'}),
'conf_Weight': forms.NumberInput(attrs={'class':'form-control'}),

        }
 






class Mace_Dispatched_Form(ModelForm):

    DATE_CREATED = forms.DateField(
        initial=date.today, 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )


    class Meta:
        model = Mace_Dispatched
        fields = '__all__'
        widgets ={

    'STATION': forms.Select(attrs={'class':'form-control'}),   
    'BATCH_CODE_M1': forms.TextInput(attrs={'class':'form-control'}),

    'BATCH_CODE_M2': forms.TextInput(attrs={'class':'form-control'}),

    'BATCH_CODE_M3': forms.TextInput(attrs={'class':'form-control'}),
    'Delivery_advice_num': forms.TextInput(attrs={'class':'form-control'}),

     'BATCH_CODE': forms.TextInput(attrs={'class':'form-control'}),
    'DATE_OF_PURCHASE': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'PLACE_OF_PURCHASE': forms.Select(attrs={'class':'form-control'}),    
    'TOTAL_NUM_OF_FARMERS': forms.NumberInput(attrs={'class':'form-control'}),
    'TOTAL_LBS_NUTMEG_BOUGHT': forms.NumberInput(attrs={'class':'form-control'}),
    'NUM_OF_BAGS': forms.NumberInput(attrs={'class':'form-control'}),
    

    'MACE_1': forms.NumberInput(attrs={'class':'form-control'}),
    'BATCH_CODE_M1': forms.TextInput(attrs={'class':'form-control'}),

    'MACE_2': forms.NumberInput(attrs={'class':'form-control'}),
    'BATCH_CODE_M2': forms.TextInput(attrs={'class':'form-control'}),
    'Vehicle_number': forms.TextInput(attrs={'class':'form-control'}),    


    'MACE_3': forms.NumberInput(attrs={'class':'form-control'}),
    'BATCH_CODE_M3': forms.TextInput(attrs={'class':'form-control'}),

     'Delivery_advice_num': forms.TextInput(attrs={'class':'form-control'}),

        }
 

class Mace_Purchase_Form(ModelForm):

    DATE_CREATED = forms.DateField(
        initial=date.today, 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )


    class Meta:
        model = Mace_Purchase
        fields = '__all__'
        widgets ={





    'STATION': forms.Select(attrs={'class':'form-control'}),    
 


    'DATE_OF_PURCHASE': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'PLACE_OF_PURCHASE': forms.Select(attrs={'class':'form-control'}),    
    'TOTAL_NUM_OF_FARMERS': forms.NumberInput(attrs={'class':'form-control'}),
    'TOTAL_LBS_NUTMEG_BOUGHT': forms.DecimalField(attrs={'class':'form-control','step': 'any'}),
    
    'NUM_OF_BAGS': forms.NumberInput(attrs={'class':'form-control'}),

    'MACE_1': forms.DecimalField(attrs={'class':'form-control','step': 'any'}),
    'BATCH_CODE_M1': forms.TextInput(attrs={'class':'form-control'}),


    'MACE_2': forms.DecimalField(attrs={'class':'form-control','step': 'any'}),
    'BATCH_CODE_M2': forms.TextInput(attrs={'class':'form-control'}),



    'MACE_3': forms.DecimalField(attrs={'class':'form-control','step': 'any'}),
    'BATCH_CODE_M3': forms.TextInput(attrs={'class':'form-control'}),


        }
 










class Dispatch_Of_Dried_Nutmeg_Rec_Form(ModelForm):
    Date = forms.DateField(
        initial=date.today,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Dispatch_Of_Dried_Nutmeg_Rec
        fields = '__all__'
        widgets = {
            'Station': forms.Select(attrs={'class':'form-control'}),    
            'BatchCode': forms.TextInput(attrs={'class':'form-control'}),
            'Vehicle_number': forms.TextInput(attrs={'class':'form-control'}),
            'Delivery_advice_num': forms.TextInput(attrs={'class':'form-control'}),
            'WAREHOUSE_RECEIPT_NUMBER': forms.TextInput(attrs={'class':'form-control'}),
            'Station_rec': forms.Select(attrs={'class':'form-control'}),    
            'Product': forms.TextInput(attrs={'class':'form-control'}),
            'Num_Bags': forms.TextInput(attrs={'class':'form-control'}),
            'Weight': forms.TextInput(attrs={'class':'form-control'}),
            'conf_Product': forms.TextInput(attrs={'class':'form-control'}),
            'conf_Num_Bags': forms.TextInput(attrs={'class':'form-control'}),
            'conf_Weight': forms.TextInput(attrs={'class':'form-control'}),
        }


date

class Dispatch_Of_Green_Nutmeg_Rec_Form(ModelForm):
    Date = forms.DateField(
        initial=date.today,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Dispatch_Of_Green_Nutmeg_Rec
        fields = '__all__'
        widgets = {
            'Station': forms.Select(attrs={'class':'form-control'}),
            'BatchCode': forms.TextInput(attrs={'class':'form-control'}),
            'WAREHOUSE_RECEIPT_NUMBER': forms.TextInput(attrs={'class':'form-control'}),
            'Delivery_advice_num': forms.TextInput(attrs={'class':'form-control'}),
            'Station_rec': forms.TextInput(attrs={'class':'form-control'}),
            'Product': forms.TextInput(attrs={'class':'form-control'}),
            'Num_Bags': forms.TextInput(attrs={'class':'form-control'}),
            'Weight': forms.TextInput(attrs={'class':'form-control'}),
            'conf_Product': forms.TextInput(attrs={'class':'form-control'}),
            'conf_Num_Bags': forms.TextInput(attrs={'class':'form-control'}),
            'conf_Weight': forms.TextInput(attrs={'class':'form-control'}),
                        'Vehicle_number': forms.TextInput(attrs={'class':'form-control'}),

        }



class Vehicle_Inspection_Form(ModelForm):
    class Meta:
        model = Vehicle_Inspection
        fields = '__all__'
        widgets ={




    'Provider': forms.Select(attrs={'class':'form-control'}),    
    'Provider_cont': forms.TextInput(attrs={'class':'form-control'}),
    'Vehicle_number': forms.TextInput(attrs={'class':'form-control'}),
    'Driver_name': forms.TextInput(attrs={'class':'form-control'}),
    'liscense_check': forms.Select(attrs={'class':'form-control'}),    
    'insurance_check': forms.Select(attrs={'class':'form-control'}),    

#General Conditions on vehicles
    'Clean_check': forms.Select(attrs={'class':'form-control'}),




    'Oil_Spill': forms.Select(attrs={'class':'form-control'}),    


    'Tyres_fit': forms.Select(attrs={'class':'form-control'}),    


    
    #Condition of vehicle Tray

    'Resisdue_prev_Cargo': forms.Select(attrs={'class':'form-control'}),
    'Presence_of_Debris': forms.Select(attrs={'class':'form-control'}),
    'Tarpaulin_present': forms.Select(attrs={'class':'form-control'}),

    #Security of Cargo



    'Cargo_present': forms.Select(attrs={'class':'form-control'}),
    'Cargo_present_cont': forms.Textarea(attrs={'class':'form-control'}),

    
    'Condition_of_cargo': forms.Select(attrs={'class':'form-control'}),
    'covered_goods': forms.Select(attrs={'class':'form-control'}),

    #Vehicle fit for use
    'vehicle_for_use': forms.Select(attrs={'class':'form-control'}),
    #Weather Conditions
    'Weather': forms.Select(attrs={'class':'form-control'}),

    'comments':forms.Textarea(attrs={'class':'form-control'}),
    'inspected_by': forms.TextInput(attrs={'class':'form-control'}),
    'verified_by': forms.TextInput(attrs={'class':'form-control'}),

    'inspected_by_date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'verified_by_date': forms.DateInput(attrs={'type':'date','class':'form-control'}),

        }







class Final_Weight_Inspection_Form(ModelForm):
    class Meta:
        model = Final_Weight_Inspection
        fields = '__all__'
        widgets ={
'Date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
'Purchase_order': forms.TextInput(attrs={'class':'form-control'}),
'product_description': forms.TextInput(attrs={'class':'form-control'}),
'Batch_number': forms.TextInput(attrs={'class':'form-control'}),
'linkCheck': forms.TextInput(attrs={'class':'form-control'}),

        }








class Final_Weight_Inspection_fields_Form(ModelForm):
    class Meta:
        model = Final_Weight_Inspection_fields
        fields = '__all__'
        widgets ={


        }















from django import forms

class SectionForm(forms.Form):
    # section_choices = [(i, str(i)) for i in range(1, 11)]
    section_choices = [
    # ('', '--Select Section--'),
    ('1', 'A'),
    ('2', 'B'),
    ('3', 'C'),
    ('4', 'D'),
    ('5', 'E'),
    ('6', 'F'),
    ('7', 'G'),
    ('8', 'H'),
    ('9', 'I'),
    ('10', 'J'),
    ('11', 'K'),
    ('12', 'L'),
    ('13', 'M'),
    ('14', 'N'),
    ('15', 'O'),
    ('16', 'P'),
    ('17', 'Q'),
    ('18', 'R'),
    ('19', 'S'),
    ('20', 'T'),
]
    section1 = forms.ChoiceField(
        label='Section 1',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    section2 = forms.ChoiceField(
        label='Section 2',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )






    Section1G_GF = forms.ChoiceField(
        label='Section G Ground Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1G_1F = forms.ChoiceField(
        label='Section G First Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1G_2F = forms.ChoiceField(
        label='Section G Second Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1G_FL = forms.ChoiceField(
        label='Section G Floor Level',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1H_GF = forms.ChoiceField(
        label='Section H Ground Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1H_1F = forms.ChoiceField(
        label='Section H First Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1H_2F = forms.ChoiceField(
        label='Section H Second Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1H_FL = forms.ChoiceField(
        label='Section H Floor Level',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1M_GF = forms.ChoiceField(
        label='Section M Ground Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1M_1F = forms.ChoiceField(
        label='Section M First Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1M_2F = forms.ChoiceField(
        label='Section M Second Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1M_FL = forms.ChoiceField(
        label='Section M Floor Level',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1U_GF = forms.ChoiceField(
        label='Section U Ground Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1U_1F = forms.ChoiceField(
        label='Section U First Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1U_2F = forms.ChoiceField(
        label='Section U Second Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1U_FL = forms.ChoiceField(
        label='Section U Floor Level',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1GP_GF = forms.ChoiceField(
        label='Section GP Ground Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1GP_1F = forms.ChoiceField(
        label='Section GP First Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1GP_2F = forms.ChoiceField(
        label='Section GP Second Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section1GP_FL = forms.ChoiceField(
        label='Section GP Floor Level',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )


























    Section2G_GF = forms.ChoiceField(
        label='Section G Ground Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2G_1F = forms.ChoiceField(
        label='Section G First Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2G_2F = forms.ChoiceField(
        label='Section G Second Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2G_FL = forms.ChoiceField(
        label='Section G Floor Level',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2H_GF = forms.ChoiceField(
        label='Section H Ground Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2H_1F = forms.ChoiceField(
        label='Section H First Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2H_2F = forms.ChoiceField(
        label='Section H Second Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2H_FL = forms.ChoiceField(
        label='Section H Floor Level',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2M_GF = forms.ChoiceField(
        label='Section M Ground Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2M_1F = forms.ChoiceField(
        label='Section M First Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2M_2F = forms.ChoiceField(
        label='Section M Second Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2M_FL = forms.ChoiceField(
        label='Section M Floor Level',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2U_GF = forms.ChoiceField(
        label='Section U Ground Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2U_1F = forms.ChoiceField(
        label='Section U First Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2U_2F = forms.ChoiceField(
        label='Section U Second Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2U_FL = forms.ChoiceField(
        label='Section U Floor Level',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2GP_GF = forms.ChoiceField(
        label='Section GP Ground Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2GP_1F = forms.ChoiceField(
        label='Section GP First Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2GP_2F = forms.ChoiceField(
        label='Section GP Second Floor',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Section2GP_FL = forms.ChoiceField(
        label='Section GP Floor Level',
        choices=section_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )








    


class Shelves_Form(ModelForm):
    class Meta:
        model = Shelves
        fields = '__all__'
        widgets ={



    'entry': forms.HiddenInput(attrs={'class':'form-control'}),
    'floor': forms.HiddenInput(attrs={'class':'form-control'}),
    'station': forms.HiddenInput(attrs={'class':'form-control'}),
    'Shelf': forms.TextInput(attrs={'class':'form-control'}),
    'Tray': forms.TextInput(attrs={'class':'form-control'}),
    'Section': forms.TextInput(attrs={'class':'form-control'}),

        }















class Cracking_Schedule_Form(ModelForm):
    class Meta:
        model = Cracking_Schedule
        fields = '__all__'
        widgets ={

    'Date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'Batch_Code': forms.TextInput(attrs={'class':'form-control'}),
    'Total_Bags_Used': forms.NumberInput(attrs={'class':'form-control'}),
    'new_code': forms.TextInput(attrs={'class':'form-control'}),
    'remaining_bags': forms.NumberInput(attrs={'class':'form-control'}),
    'station': forms.TextInput(attrs={'class':'form-control'}),


        }







class Assorting_Log_Form(ModelForm):
    class Meta:
        model = Assorting_Log
        fields = '__all__'
        widgets ={


    'Date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'Name': forms.TextInput(attrs={'class':'form-control'}),
    'amount_assorted': forms.NumberInput(attrs={'class':'form-control'}),
    'contract_num': forms.TextInput(attrs={'class':'form-control'}),



        }








class Extractor_Log_Form(ModelForm):
    class Meta:
        model = Extractor_Log
        fields = '__all__'
        widgets ={
    'Date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'Name': forms.TextInput(attrs={'class':'form-control'}),
    'amount_extracted': forms.NumberInput(attrs={'class':'form-control'}),
    'contract_num': forms.TextInput(attrs={'class':'form-control'}),

        }


6







class Fumigation_Log_Form(ModelForm):
    class Meta:
        model = Fumigation_Log
        fields = '__all__'
        widgets ={
    'Date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'Name': forms.TextInput(attrs={'class':'form-control'}),
    'contract_num': forms.TextInput(attrs={'class':'form-control'}),
      
        }


















class Sanitation_A_Form(ModelForm):
    class Meta:
        model = Sanitation_A
        fields = '__all__'
        widgets ={
            'Station': forms.TextInput(attrs={'class': 'form-control'}),
            'Period': forms.TextInput(attrs={'class': 'form-control'}),
            'Ceiling_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Ceiling_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Ceiling_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Ceiling_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Ceiling_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Ceiling_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Windows_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Windows_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Windows_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Windows_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Windows_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Windows_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Screens_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Screens_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Screens_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Screens_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Screens_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Screens_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Grinder_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Grinder_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Grinder_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Grinder_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Grinder_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Grinder_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Winnower_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Winnower_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Winnower_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Winnower_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Winnower_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Winnower_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Sinks_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Sinks_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Sinks_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Sinks_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Sinks_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Sinks_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Scales_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Scales_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Scales_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Scales_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Scales_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Scales_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Hoist_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Hoist_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Hoist_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Hoist_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Hoist_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Hoist_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Drying_Racks_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Drying_Racks_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Drying_Racks_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Drying_Racks_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Drying_Racks_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Drying_Racks_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Shining_Cloths_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Shining_Cloths_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Shining_Cloths_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Shining_Cloths_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Shining_Cloths_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Shining_Cloths_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Stencil_Room_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Stencil_Room_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Stencil_Room_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Stencil_Room_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Stencil_Room_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Stencil_Room_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Packaging_Store_Room_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Packaging_Store_Room_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Packaging_Store_Room_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Packaging_Store_Room_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Packaging_Store_Room_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Packaging_Store_Room_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Fumigation_Room_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Fumigation_Room_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Fumigation_Room_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Fumigation_Room_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Fumigation_Room_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Fumigation_Room_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Immersion_Room_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Immersion_Room_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Immersion_Room_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Immersion_Room_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Immersion_Room_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Immersion_Room_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Chambers_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Chambers_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Chambers_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Chambers_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Chambers_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Chambers_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Tourist_Shop_week_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Tourist_Shop_week_2': forms.TextInput(attrs={'class': 'form-control'}),
            'Tourist_Shop_week_3': forms.TextInput(attrs={'class': 'form-control'}),
            'Tourist_Shop_week_4': forms.TextInput(attrs={'class': 'form-control'}),
            'Tourist_Shop_week_5': forms.TextInput(attrs={'class': 'form-control'}),
            'Tourist_Shop_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Verified_by': forms.TextInput(attrs={'class': 'form-control'}),
            'Date': forms.DateInput(attrs={'class': 'form-control'}),
        }


class Sanitation_B_Form(ModelForm):
    class Meta:
        model = Sanitation_B
        fields = '__all__'
        widgets ={
            'Station': forms.TextInput(attrs={'class': 'form-control'}),
            'Week_of': forms.TextInput(attrs={'class': 'form-control'}),
            'Pavement_Loading_Dock_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Pavement_Loading_Dock_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Pavement_Loading_Dock_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Pavement_Loading_Dock_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Pavement_Loading_Dock_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Pavement_Loading_Dock_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Receiving_Area_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Receiving_Area_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Receiving_Area_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Receiving_Area_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Receiving_Area_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Receiving_Area_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Agitating_Tray_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Agitating_Tray_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Agitating_Tray_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Agitating_Tray_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Agitating_Tray_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Agitating_Tray_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Cracker_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Cracker_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Cracker_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Cracker_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Cracker_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Cracker_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Rakes_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Rakes_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Rakes_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Rakes_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Rakes_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Rakes_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Wire_Baskets_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Wire_Baskets_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Wire_Baskets_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Wire_Baskets_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Wire_Baskets_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Wire_Baskets_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Buckets_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Buckets_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Buckets_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Buckets_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Buckets_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Buckets_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Scoops_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Scoops_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Scoops_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Scoops_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Scoops_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Scoops_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Administrative_Officer_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Administrative_Officer_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Administrative_Officer_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Administrative_Officer_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Administrative_Officer_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Administrative_Officer_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Restrooms_Luncheon_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Restrooms_Luncheon_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Restrooms_Luncheon_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Restrooms_Luncheon_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Restrooms_Luncheon_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Restrooms_Luncheon_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Change_Room_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Change_Room_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Change_Room_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Change_Room_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Change_Room_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Change_Room_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Kitchen_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Kitchen_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Kitchen_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Kitchen_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Kitchen_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Kitchen_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Process_Floor_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Process_Floor_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Process_Floor_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Process_Floor_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Process_Floor_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Process_Floor_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Immersion_Room_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Immersion_Room_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Immersion_Room_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Immersion_Room_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Immersion_Room_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Immersion_Room_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Sinks_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Sinks_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Sinks_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Sinks_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Sinks_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Sinks_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Tourist_Shop_monday': forms.TextInput(attrs={'class': 'form-control'}),
            'Tourist_Shop_tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Tourist_Shop_wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'Tourist_Shop_thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'Tourist_Shop_friday': forms.TextInput(attrs={'class': 'form-control'}),
            'Tourist_Shop_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Verified_by': forms.TextInput(attrs={'class': 'form-control'}),
            'Date': forms.DateInput(attrs={'class': 'form-control'}),
        }




class Sanitation_C_Form(ModelForm):
    class Meta:
        model = Sanitation_C
        fields = '__all__'
        widgets ={
            'Station': forms.TextInput(attrs={'class': 'form-control'}),
            'Week_of': forms.TextInput(attrs={'class': 'form-control'}),
            'Drains_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Drains_Date': forms.DateInput(attrs={'class': 'form-control'}),
            'Pavement_load_dock_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Pavement_load_dock_Date': forms.DateInput(attrs={'class': 'form-control'}),
            'General_Grounds_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'General_Grounds_Date': forms.DateInput(attrs={'class': 'form-control'}),
            'Receiving_area_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Receiving_area_Date': forms.DateInput(attrs={'class': 'form-control'}),
            'Walls_vents_blocks_signature': forms.TextInput(attrs={'class': 'form-control'}),
            'Walls_vents_blocks_Date': forms.DateInput(attrs={'class': 'form-control'}),
            'comments': forms.TextInput(attrs={'class': 'form-control'}),
            'Verified_by': forms.TextInput(attrs={'class': 'form-control'}),
            'Date': forms.DateInput(attrs={'class': 'form-control'}),
        }





class visit_Form(ModelForm):
    class Meta:
        model = visit
        fields = '__all__'
        widgets ={

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

 
    'purpose_of_visit': forms.TextInput(attrs={'class':'form-control'}),
    'Date_of_visit' : forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'parish' : forms.TextInput(attrs={'class':'form-control'}),
    'training' : forms.TextInput(attrs={'class':'form-control'}),
    'tenurship' : forms.Select(attrs={'class':'form-control'}),
    'tenurship_cont' : forms.TextInput(attrs={'class':'form-control'}),
    'visit': forms.TextInput(attrs={'class':'form-control'}),
    'village' : forms.TextInput(attrs={'class':'form-control'}),



        }




class visit_Form(ModelForm):
    class Meta:
        model = visit
        fields = '__all__'
        widgets ={

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

 
    'purpose_of_visit': forms.TextInput(attrs={'class':'form-control'}),
    'Date_of_visit' : forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'parish' : forms.TextInput(attrs={'class':'form-control'}),
    'training' : forms.TextInput(attrs={'class':'form-control'}),
    'tenurship' : forms.Select(attrs={'class':'form-control'}),
    'tenurship_cont' : forms.TextInput(attrs={'class':'form-control'}),
    'visit': forms.TextInput(attrs={'class':'form-control'}),
    'village' : forms.TextInput(attrs={'class':'form-control'}),



        }








class Labour_support_Form(ModelForm):
    class Meta:
        model = Labour_support
        fields = '__all__'
        widgets ={

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),
    'Type_of_Assistance': forms.Select(attrs={'class':'form-control'}),
    'Date_Recieved': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'Nature_of_Assistance': forms.Select(attrs={'class':'form-control'}),
    'Nature_of_Assistance_cont': forms.TextInput(attrs={'class':'form-control'}),
    'Objective_of_the_Assistance': forms.Select(attrs={'class':'form-control'}),
    'Objective_of_the_Assistance_cont': forms.TextInput(attrs={'class':'form-control'}),
    'Facilitator_of_the_Assistance': forms.Select(attrs={'class':'form-control'}),
    'Facilitator_of_the_Assistance_cont': forms.TextInput(attrs={'class':'form-control'}),
        }





class Training_support_Form(ModelForm):
    class Meta:
        model = Training_support
        fields = '__all__'
        widgets ={

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),


    'Type_of_Training': forms.Select(attrs={'class':'form-control'}),

    'Type_of_Training_cont': forms.Select(attrs={'class':'form-control'}),

    'Date_Recieved': forms.DateInput(attrs={'type':'date','class':'form-control'}),

    'Objective_of_the_Training': forms.Select(attrs={'class':'form-control'}),

    'Objective_of_the_Training_cont': forms.Select(attrs={'class':'form-control'}),
    
    'Facilitator_of_the_Training': forms.Select(attrs={'class':'form-control'}),

    'Facilitator_of_the_Training_cont': forms.TextInput(attrs={'class':'form-control'}),


        }




    
class Farmer_Info_Form(ModelForm):



    class Meta:
        model = Farmer_Info
        fields = '__all__'
        widgets = {

    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No': forms.TextInput(attrs={'class':'form-control'}),

	'name' : forms.TextInput(attrs={'class':'form-control'}),

    'name': forms.TextInput(attrs={'class':'form-control'}),
    'age' : forms.Select(attrs={'class':'form-control'}),

    'parish' : forms.TextInput(attrs={'class':'form-control'}),

    'village' : forms.TextInput(attrs={'class':'form-control'}),
    'latitude' : forms.TextInput(attrs={'class':'form-control'}),
    'longitude': forms.TextInput(attrs={'class':'form-control'}),
    'acreage' : forms.TextInput(attrs={'class':'form-control'}),
    'insurance_zone': forms.TextInput(attrs={'class':'form-control'}),
    'home_phone': forms.TextInput(attrs={'class':'form-control'}),
    'mobile_phone': forms.TextInput(attrs={'class':'form-control'}),
    'email': forms.EmailInput(attrs={'class':'form-control'}),

		}

class land_info_Form(ModelForm):
	class Meta:
		model = land_info
		fields = '__all__'
		widgets ={


    'Land_ID_N0': forms.TextInput(attrs={'class':'form-control'}),
    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
	'Nutmeg_ID_No' : forms.TextInput(attrs={'class':'form-control'}),
    'land_elevation': forms.Select(attrs={'class':'form-control'}),
    'soil_type': forms.Select(attrs={'class':'form-control'}),
    'rainfall_pattern': forms.Select(attrs={'class':'form-control'}),










    'farm_type' : forms.Select(attrs={'class':'form-control'}),

    'Worker_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No'  : forms.HiddenInput(attrs={'class':'form-control'}),
    'parish' : forms.TextInput(attrs={'class':'form-control'}),
    'training': forms.TextInput(attrs={'class':'form-control'}),
    'tenurship': forms.Select(attrs={'class':'form-control'}),
    'visit' : forms.TextInput(attrs={'class':'form-control'}),

    'village' : forms.TextInput(attrs={'class':'form-control'}),
    'latitude' : forms.TextInput(attrs={'class':'form-control'}),
    'longitude' : forms.TextInput(attrs={'class':'form-control'}),
    'acreage' : forms.TextInput(attrs={'class':'form-control'}),
    'insurance_zone' : forms.TextInput(attrs={'class':'form-control'}),
    'land_elevation' : forms.Select(attrs={'class':'form-control'}),
    'soil_type' : forms.Select(attrs={'class':'form-control'}),
    'rainfall_pattern' : forms.Select(attrs={'class':'form-control'}),


    'Mature_trees_25_years_quantity' : forms.NumberInput(attrs={'class':'form-control'}),
    'Mature_trees_25_years_estimated_production' : forms.NumberInput(attrs={'class':'form-control'}),
    'Bearing_trees_16_24_years_quantity': forms.NumberInput(attrs={'class':'form-control'}),
    'Bearing_trees_16_24_years': forms.NumberInput(attrs={'class':'form-control'}),
    'Bearing_trees_6_15_years_quantity': forms.NumberInput(attrs={'class':'form-control'}),
    'Bearing_trees_6_15_years_estimated_production': forms.NumberInput(attrs={'class':'form-control'}),
    'Non_Bearing_trees_5_years_quantity': forms.NumberInput(attrs={'class':'form-control'}),
    'Non_Bearing_trees_5_years_estimated_production': forms.NumberInput(attrs={'class':'form-control'}),
    'Estimated_peak_period' : forms.NumberInput(attrs={'class':'form-control'}),




    'End_Use_Atlantic_Tall' : forms.TextInput(attrs={'class':'form-control'}),
    'End_Use_Dwarf' : forms.TextInput(attrs={'class':'form-control'}),
    'No_of_Bearing_Trees_Atlantic_Tall': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Bearing_Trees_Dwarf': forms.NumberInput(attrs={'class':'form-control'}),
    'Estimated_Productiom_Atlantic_Tall': forms.NumberInput(attrs={'class':'form-control'}),
    'Estimated_Productiom_Dwarf': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Non_Bearing_Trees_Atlantic_Tall': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Non_Bearing_Trees_Dwarf': forms.NumberInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Atlantic_Tall' : forms.TextInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Dwarf' : forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Atlantic_Tall' : forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Dwarf' : forms.TextInput(attrs={'class':'form-control'}),











		}

class Land_Tenur_Form(ModelForm):
	class Meta:
		model = Land_Tenur
		fields = '__all__'
		widgets ={
    

    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
	'Owner_Legal_Title': forms.TextInput(attrs={'class':'form-control'}),
    'Freehold' : forms.TextInput(attrs={'class':'form-control'}),
    'Family': forms.TextInput(attrs={'class':'form-control'}),
    'Leashold' : forms.TextInput(attrs={'class':'form-control'}),
    'Leashold_comment': forms.Textarea(attrs={'class':'form-control'}),
    'Caretaker': forms.TextInput(attrs={'class':'form-control'}),
    'Agent': forms.TextInput(attrs={'class':'form-control'}),
    'No_Legal_Title' : forms.TextInput(attrs={'class':'form-control'}),
    'Status': forms.TextInput(attrs={'class':'form-control'}),
    'farm_type': forms.Select(attrs={'class':'form-control'}),

		}

class Nutmeg_Trees_Form(ModelForm):
	class Meta:
		model = Nutmeg_Trees
		fields = '__all__'
		widgets={
    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Mature_trees_25_years_quantity' : forms.NumberInput(attrs={'class':'form-control'}),
    'Mature_trees_25_years_estimated_production' : forms.NumberInput(attrs={'class':'form-control'}),
    'Bearing_trees_16_24_years_quantity': forms.NumberInput(attrs={'class':'form-control'}),
    'Bearing_trees_16_24_years': forms.NumberInput(attrs={'class':'form-control'}),
    'Bearing_trees_6_15_years_quantity': forms.NumberInput(attrs={'class':'form-control'}),
    'Bearing_trees_6_15_years_estimated_production': forms.NumberInput(attrs={'class':'form-control'}),
    'Non_Bearing_trees_5_years_quantity': forms.NumberInput(attrs={'class':'form-control'}),
    'Non_Bearing_trees_5_years_estimated_production': forms.NumberInput(attrs={'class':'form-control'}),
    'Estimated_peak_period': forms.NumberInput(attrs={'class':'form-control'}),
		}

class Nutmeg_Variety_Form(ModelForm):
	class Meta:
		model = Nutmeg_Variety
		fields = '__all__'
		widgets={
    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),


    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),

    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Banda': forms.TextInput(attrs={'class':'form-control'}),
    'Papua': forms.TextInput(attrs={'class':'form-control'}),
    'Malayan_Indonesia': forms.TextInput(attrs={'class':'form-control'}),
    'dominant_Variety': forms.TextInput(attrs={'class':'form-control'}),
		}

class Other_Crops_Form(ModelForm):
	class Meta:
		model = Other_Crops
		fields = '__all__'
		widgets={
    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),


    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'other_crops':  forms.CheckboxSelectMultiple(attrs={}),
		}



class Coconut_Trees_Form(ModelForm):
	class Meta:
		model = Coconut_Trees
		fields = '__all__'
		widgets={
    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),
    
    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'End_Use_Atlantic_Tall': forms.TextInput(attrs={'class':'form-control'}),
    'End_Use_Dwarf': forms.TextInput(attrs={'class':'form-control'}),
    'No_of_Bearing_Trees_Atlantic_Tall': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Bearing_Trees_Dwarf': forms.NumberInput(attrs={'class':'form-control'}),
    'Estimated_Productiom_Atlantic_Tall': forms.NumberInput(attrs={'class':'form-control'}),
    'Estimated_Productiom_Dwarf': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Non_Bearing_Trees_Atlantic_Tall': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Non_Bearing_Trees_Dwarf': forms.NumberInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Atlantic_Tall': forms.TextInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Dwarf': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Atlantic_Tall': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Dwarf': forms.TextInput(attrs={'class':'form-control'}),
		}

class Citrus_Mango_Trees_Form(ModelForm):
	class Meta:
		model = Citrus_Mango_Trees
		fields = '__all__'
		widgets={
    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),


    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'No_of_Bearing_Trees_Lime': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Bearing_Trees_Lemon': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Bearing_Trees_Mangoes': forms.NumberInput(attrs={'class':'form-control'}),
    'Estimated_Productiom_Lime': forms.NumberInput(attrs={'class':'form-control'}),
    'Estimated_Productiom_Lemon': forms.NumberInput(attrs={'class':'form-control'}),
    'Estimated_Productiom_Mangoes': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Non_Bearing_Trees_Lime': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Non_Bearing_Trees_Lemon': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Non_Bearing_Trees_Mangoes': forms.NumberInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Lime': forms.TextInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Lemon': forms.TextInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Mangoes': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Lime': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Lemon': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Mangoes': forms.TextInput(attrs={'class':'form-control'}),


		}

class Other_Spices_Trees_Form(ModelForm):
	class Meta:
		model = Other_Spices_Trees
		fields = '__all__'
		widgets={
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),


    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'No_of_Bearing_Trees_Clove': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Bearing_Trees_Cinnamon': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Bearing_Trees_Bayleaf': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Bearing_Trees_Tumeric': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Bearing_Trees_Ginger': forms.NumberInput(attrs={'class':'form-control'}),
    'Estimated_Productiom_Clove': forms.NumberInput(attrs={'class':'form-control'}),
    'Estimated_Productiom_Cinnamon': forms.NumberInput(attrs={'class':'form-control'}),
    'Estimated_Productiom_Bayleaf': forms.NumberInput(attrs={'class':'form-control'}),
    'Estimated_Productiom_Tumeric': forms.NumberInput(attrs={'class':'form-control'}),
    'Estimated_Productiom_Ginger': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Non_Bearing_Trees_Clove': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Non_Bearing_Trees_Cinnamon': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Non_Bearing_Trees_Bayleaf': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Non_Bearing_Trees_Tumeric': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Non_Bearing_Trees_Ginger': forms.NumberInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Clove': forms.TextInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Cinnamon': forms.TextInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Bayleaf': forms.TextInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Tumeric': forms.TextInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Ginger': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Clove': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Cinnamon': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Bayleaf': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Tumeric': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Ginger': forms.TextInput(attrs={'class':'form-control'}),

		}

class Other_Seasoning_Trees_Form(ModelForm):
	class Meta:
		model = Other_Seasoning_Trees
		fields = '__all__'
		widgets={

    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'No_of_Stools_chive': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Stools_Thyme': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Stools_Celery': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Stools_Parsley': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Stools_Petit_Bum': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Stools_Seasoning_Pepper': forms.NumberInput(attrs={'class':'form-control'}),
    'No_of_Stools_Hot_Pepper': forms.NumberInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_chive': forms.TextInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Thyme': forms.TextInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Celery': forms.TextInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Parsley': forms.TextInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Petit_Bum': forms.TextInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Seasoning_Pepper': forms.TextInput(attrs={'class':'form-control'}),
    'Presence_of_Disease_Hot_Pepper': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_chive': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Thyme': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Celery': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Parsley': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Petit_Bum': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Seasoning_Pepper': forms.TextInput(attrs={'class':'form-control'}),
    'Cultivation_Hot_Pepper': forms.TextInput(attrs={'class':'form-control'}),
    
		}

class Other_Crops_Cultivated_Form(ModelForm):
	class Meta:
		model = Other_Crops_Cultivated
		fields = '__all__'
		widgets={
    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Name_of_Crops': forms.TextInput(attrs={'class':'form-control'}),
    'Number_of_Trees_or_stools': forms.TextInput(attrs={'class':'form-control'}),
		}

class Condition_Form(ModelForm):
	class Meta:
		model = Condition
		fields = '__all__'
		widgets={
    
    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Weeds': forms.Select(attrs={'class':'form-control'}),
    'Drains': forms.Select(attrs={'class':'form-control'}),
    'Fertilizing' : forms.Select(attrs={'class':'form-control'}),
    'Pruning': forms.Select(attrs={'class':'form-control'}),
    'Harvesting' : forms.Select(attrs={'class':'form-control'}),
    'Land_Clearing': forms.Select(attrs={'class':'form-control'}),
    'Planting': forms.Select(attrs={'class':'form-control'}),
    'Presence_of_pest_and_diseases_on_nutmegs': forms.Select(attrs={'class':'form-control'}),
    'Presence_of_pest_and_diseases_on_nutmegs_cont' : forms.TextInput(attrs={'class':'form-control'}),
		}




class Nutmeg_Land_Form(ModelForm):
	class Meta:
		model = Nutmeg_Land
		fields = '__all__'
		widgets={
    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'norm_land' : forms.TextInput(attrs={'class':'form-control'}),
    'Seasonal' : forms.TextInput(attrs={'class':'form-control'}),
    'Abandoned' : forms.TextInput(attrs={'class':'form-control'}),

    'farm_type': forms.Select(attrs={'class':'form-control'}),


		}





class Nutmeg_Frequency_Form(ModelForm):
	class Meta:
		model = Nutmeg_Frequency
		fields = '__all__'
		widgets={
    
    
    
    
    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    
    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Regular' : forms.TextInput(attrs={'class':'form-control'}),
    'Occasional' : forms.TextInput(attrs={'class':'form-control'}),
    'Never' : forms.TextInput(attrs={'class':'form-control'}),

    'Frequency': forms.Select(attrs={'class':'form-control'}),

		}





class Potential_Risks_Form(ModelForm):
	class Meta:
		model = Potential_Risks
		fields = '__all__'
		widgets={
   
   
   
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

   
    
    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Slides': forms.Select(attrs={'class':'form-control'}),
    'Flooding': forms.Select(attrs={'class':'form-control'}),
    'Heavy_Metal': forms.Select(attrs={'class':'form-control'}),
    'Chemical_Spills': forms.Select(attrs={'class':'form-control'}),
    'Dumping_of_trash': forms.Select(attrs={'class':'form-control'}),
    'Feedlot': forms.Select(attrs={'class':'form-control'}),

		}



class Policy_Form(ModelForm):
	class Meta:
		model = Policy
		fields = '__all__'
		widgets={
    
    
    
    
    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    
    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Pesticides': forms.Select(attrs={'class':'form-control'}),
    'Septic_Tanks': forms.Select(attrs={'class':'form-control'}),
    'Other': forms.Select(attrs={'class':'form-control'}),
	
		}




class Road_Access_Form(ModelForm):
	class Meta:
		model = Road_Access
		fields = '__all__'
		widgets={
    
    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    
    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),


    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Road_Access': forms.Select(attrs={'class':'form-control'}),
		}




class Food_Safety_and_Quality_Form(ModelForm):
	class Meta:
		model = Food_Safety_and_Quality
		fields = '__all__'
		widgets={
    
    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    
    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Fertilizer': forms.Select(attrs={'class':'form-control'}),
    'Fertilizer_cont': forms.TextInput(attrs={'class':'form-control'}),
    'Last_application': forms.TextInput(attrs={'class':'form-control'}),
    'Raw_Manure': forms.Select(attrs={'class':'form-control'}),
    'Raw_Manure_cont': forms.TextInput(attrs={'class':'form-control'}),
    'Composed_manure': forms.Select(attrs={'class':'form-control'}),
    'Other': forms.TextInput(attrs={'class':'form-control'}),
		}




class Farm_Water_Source_Form(ModelForm):
	class Meta:
		model = Farm_Water_Source
		fields = '__all__'
		widgets={
    
    
    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),
    
    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Municipal_Nawasa': forms.Select(attrs={'class':'form-control'}),
    'River': forms.Select(attrs={'class':'form-control'}),
    'Spring': forms.Select(attrs={'class':'form-control'}),
    'Well': forms.Select(attrs={'class':'form-control'}),
    'Harvested_Rain_Water': forms.Select(attrs={'class':'form-control'}),
    'is_water_treated': forms.Select(attrs={'class':'form-control'}),
    'is_water_treated_cont': forms.TextInput(attrs={'class':'form-control'}),
		}




class Farm_House_Form(ModelForm):
	class Meta:
		model = Farm_House
		fields = '__all__'
		widgets={
    
    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    
    
    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),


    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Farm_House': forms.Select(attrs={'class':'form-control'}),
		}



class inspector_symmary_Form(ModelForm):
	class Meta:
		model = inspector_symmary
		fields = '__all__'
		widgets={
    
    'parish' : forms.HiddenInput(attrs={'class':'form-control'}),
    'training': forms.HiddenInput(attrs={'class':'form-control'}),
    'tenurship': forms.HiddenInput(attrs={'class':'form-control'}),
    'visit': forms.HiddenInput(attrs={'class':'form-control'}),
    'village': forms.HiddenInput(attrs={'class':'form-control'}),


    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'estimated_annual_production' : forms.TextInput(attrs={'class':'form-control'}),
    'estimated_peak_productions' : forms.TextInput(attrs={'class':'form-control'}),
    'inspected_by' : forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'date' : forms.DateInput(attrs={'type':'date','class':'form-control'}),

    
		}







class LoginForm(forms.Form):
    Worker_ID_No = forms.CharField(label='Enter Worker ID Number',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    Nutmeg_ID_No = forms.CharField(label='Enter Nutmeg ID Number',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))






class SigninForm(forms.Form):
    Worker_ID_No = forms.CharField(label='Enter Worker ID Number',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    Worker_Name = forms.CharField(label='Enter Name',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))











class In_House_Drying_Form(ModelForm):

    DATE_CREATED = forms.DateField(
        initial=date.today, 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = In_House_Drying
        fields = '__all__'
        widgets={

 
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),
    'entryCheck': forms.HiddenInput(attrs={'class':'form-control'}),

    'PLACE_OF_PURCHASE': forms.Select(attrs={'class':'form-control'}),
    'Worker_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Worker_ID_Name': forms.HiddenInput(attrs={'class':'form-control'}),
    

    'Nutmeg_ID_No': forms.TextInput(attrs={'class':'form-control'}),
    'STATION': forms.Select(attrs={'class':'form-control'}),
    'DATE_OF_PURCHASE': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'TOTAL_NUM_OF_FARMERS': forms.NumberInput(attrs={'class':'form-control'}),
    'TOTAL_LBS_NUTMEG_BOUGHT': forms.NumberInput(attrs={'class':'form-control'}),
    'NUM_OF_BAGS': forms.NumberInput(attrs={'class':'form-control'}),
    'START_DRYING_DATE': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'APPROX_END_DRYING_DATE': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'END_DRYING_DATE': forms.DateInput(attrs={'type':'date','class':'form-control'}),




# PLACEMENT ON SHELF

     # LOCATION1  
    # 'Ground_1': forms.TextInput(attrs={'class':'form-control'}), 
    # 'Floor_1st_1': forms.TextInput(attrs={'class':'form-control'}),
    # 'Floor_2nd_1': forms.TextInput(attrs={'class':'form-control'}),
    # 'Floor_Loft_1': forms.TextInput(attrs={'class':'form-control'}),

   'Shelf': forms.Select(attrs={'class':'form-control'}),
    'Tray': forms.Select(attrs={'class':'form-control'}),
    'Section': forms.Select(attrs={'class':'form-control'}),

    'ShelfG': forms.Select(attrs={'class':'form-control'}),
    'TrayG': forms.Select(attrs={'class':'form-control'}),
    'SectionG': forms.Select(attrs={'class':'form-control'}),

    'ShelfG_0': forms.Select(attrs={'class':'form-control'}),
    'TrayG_0': forms.Select(attrs={'class':'form-control'}),
    'SectionG_0': forms.TextInput(attrs={'class':'form-control'}),












   'ShelfG_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayG_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionG_GF': forms.TextInput(attrs={'class':'form-control'}),



   'ShelfG_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayG_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionG_1F': forms.TextInput(attrs={'class':'form-control'}),


   'ShelfG_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayG_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionG_2F': forms.TextInput(attrs={'class':'form-control'}),



   'ShelfG_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayG_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionG_FL': forms.TextInput(attrs={'class':'form-control'}),


   'ShelfH_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayH_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionH_GF': forms.TextInput(attrs={'class':'form-control'}),



   'ShelfH_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayH_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionH_1F': forms.TextInput(attrs={'class':'form-control'}),



   'ShelfH_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayH_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionH_2F': forms.TextInput(attrs={'class':'form-control'}),




   'ShelfH_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayH_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionH_FL': forms.TextInput(attrs={'class':'form-control'}),






   'ShelfM_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayM_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionM_GF': forms.TextInput(attrs={'class':'form-control'}),



   'ShelfM_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayM_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionM_1F': forms.TextInput(attrs={'class':'form-control'}),




   'ShelfM_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayM_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionM_2F': forms.TextInput(attrs={'class':'form-control'}),



   'ShelfM_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayM_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionM_FL': forms.TextInput(attrs={'class':'form-control'}),




   'ShelfU_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayU_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionU_GF': forms.TextInput(attrs={'class':'form-control'}),





   'ShelfU_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayU_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionU_1F': forms.TextInput(attrs={'class':'form-control'}),





   'ShelfU_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayU_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionU_2F': forms.TextInput(attrs={'class':'form-control'}),




   'ShelfU_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayU_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionU_FL': forms.TextInput(attrs={'class':'form-control'}),




   'ShelfGP_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayGP_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionGP_GF': forms.TextInput(attrs={'class':'form-control'}),


   'ShelfGP_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayGP_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionGP_1F': forms.TextInput(attrs={'class':'form-control'}),


   'ShelfGP_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayGP_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionGP_2F': forms.TextInput(attrs={'class':'form-control'}),


   'ShelfGP_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayGP_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionGP_FL': forms.TextInput(attrs={'class':'form-control'}),


# MOISTURE TESTING (Weeks 3, 6, 8)



   # LOCATION2    




   'ShelfG_0_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayG_0_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionG_0_GF': forms.Select(attrs={'class':'form-control'}),




   'ShelfG_0_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayG_0_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionG_0_1F': forms.Select(attrs={'class':'form-control'}),




   'ShelfG_0_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayG_0_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionG_0_2F': forms.Select(attrs={'class':'form-control'}),




   'ShelfG_0_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayG_0_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionG_0_FL': forms.Select(attrs={'class':'form-control'}),





   'ShelfH_0_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayH_0_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionH_0_GF': forms.Select(attrs={'class':'form-control'}),



   'ShelfH_0_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayH_0_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionH_0_1F': forms.Select(attrs={'class':'form-control'}),




   'ShelfH_0_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayH_0_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionH_0_2F': forms.Select(attrs={'class':'form-control'}),



   'ShelfH_0_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayH_0_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionH_0_FL': forms.Select(attrs={'class':'form-control'}),










   'ShelfM_0_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayM_0_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionM_0_GF': forms.Select(attrs={'class':'form-control'}),






   'ShelfM_0_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayM_0_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionM_0_1F': forms.Select(attrs={'class':'form-control'}),




   'ShelfM_0_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayM_0_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionM_0_2F': forms.Select(attrs={'class':'form-control'}),




   'ShelfM_0_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayM_0_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionM_0_FL': forms.Select(attrs={'class':'form-control'}),








   'ShelfU_0_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayU_0_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionU_0_GF': forms.Select(attrs={'class':'form-control'}),




   'ShelfU_0_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayU_0_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionU_0_1F': forms.Select(attrs={'class':'form-control'}),




   'ShelfU_0_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayU_0_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionU_0_2F': forms.Select(attrs={'class':'form-control'}),



   'ShelfU_0_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayU_0_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionU_0_FL': forms.Select(attrs={'class':'form-control'}),










   'ShelfGP_0_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayGP_0_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionGP_0_GF': forms.Select(attrs={'class':'form-control'}),





   'ShelfGP_0_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayGP_0_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionGP_0_1F': forms.Select(attrs={'class':'form-control'}),




   'ShelfGP_0_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayGP_0_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionGP_0_2F': forms.Select(attrs={'class':'form-control'}),




   'ShelfGP_0_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayGP_0_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionGP_0_FL': forms.Select(attrs={'class':'form-control'}),











# MOISTURE TESTING (Weeks 3, 6, 8)



   # LOCATION2    

    'Ground_2': forms.TextInput(attrs={'class':'form-control'}),
    'Floor_1st_2': forms.TextInput(attrs={'class':'form-control'}),
    'Floor_2nd_2': forms.TextInput(attrs={'class':'form-control'}),
    'Floor_Loft_2': forms.TextInput(attrs={'class':'form-control'}),


# MONITORING AND INSPECTION
    'STATION2': forms.TextInput(attrs={'class':'form-control'}),  

    'LOCATION3': forms.Select(attrs={'class':'form-control'}),    

    'DEFECT': forms.Select(attrs={'class':'form-control'}),   

    'PREDOMINANT_DEFECT': forms.Select(attrs={'class':'form-control'}),  

    'ALERT': forms.Select(attrs={'class':'form-control'}),
    'ALERT_cont': forms.Textarea(attrs={'class':'form-control'}),

    'Sampling_from_gouyvae': forms.TextInput(attrs={'class':'form-control'}),

    # Guideline_for_pickupmoisture_<6.5%_inhouse

    'Control_number': forms.TextInput(attrs={'class':'form-control'}),



        }









class Dispatch_Of_Dried_Nutmeg_Form(ModelForm):
    class Meta:
        model = Dispatch_Of_Dried_Nutmeg
        fields = '__all__'
        widgets={


    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

        'Worker_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Worker_ID_Name': forms.HiddenInput(attrs={'class':'form-control'}),
    
    'STATION_recieved': forms.Select(attrs={'class':'form-control'}),

    'Nutmeg_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'STATION': forms.Select(attrs={'class':'form-control'}),
    'DATE_OF_PICK_UP': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'FINAL_MOISTURE_CONTENT': forms.NumberInput(attrs={'class':'form-control'}),
       'BATCH_CODES': forms.TextInput(attrs={'class':'form-control'}),
       'BATCH_NUMBER': forms.TextInput(attrs={'class':'form-control'}),


    'Weight': forms.TextInput(attrs={'class':'form-control'}),
    'Product': forms.TextInput(attrs={'class':'form-control'}),
    'Num_Bags': forms.NumberInput(attrs={'class':'form-control'}),
    'Weight': forms.NumberInput(attrs={'class':'form-control'}),


    # LOCATION1
    # 'Ground_1': forms.NumberInput(attrs={'class':'form-control'}), 
    # 'Floor_1st_1': forms.NumberInput(attrs={'class':'form-control'}),
    # 'Floor_2nd_1': forms.NumberInput(attrs={'class':'form-control'}),
    # 'Floor_Loft_1': forms.NumberInput(attrs={'class':'form-control'}),
    # LOCATION2
    # 'Ground_2': forms.NumberInput(attrs={'class':'form-control'}), 
    # 'Floor_1st_2': forms.NumberInput(attrs={'class':'form-control'}),
    # 'Floor_2nd_2': forms.NumberInput(attrs={'class':'form-control'}),
    # 'Floor_Loft_2': forms.NumberInput(attrs={'class':'form-control'}),




    # Ground_1= models.IntegerField('Ground',default= 0) 
    'Shelf_Ground_1': forms.Select(attrs={'class':'form-control'}),
    'Tray_Ground_1': forms.Select(attrs={'class':'form-control'}),
    'Section_Ground_1': forms.Select(attrs={'class':'form-control'}),




    # Floor_1st_1= models.IntegerField('1st Floor',default= 0)
    'Shelf_Floor_1st_1': forms.Select(attrs={'class':'form-control'}),
    'Tray_Floor_1st_1': forms.Select(attrs={'class':'form-control'}),
    'Section_Floor_1st_1': forms.Select(attrs={'class':'form-control'}),



    # Floor_2nd_1= models.IntegerField('2nd Floor',default= 0)
    'Shelf_Floor_2nd_1': forms.Select(attrs={'class':'form-control'}),
    'Tray_Floor_2nd_1': forms.Select(attrs={'class':'form-control'}),
    'Section_Floor_2nd_1': forms.Select(attrs={'class':'form-control'}),




    # Floor_Loft_1= models.IntegerField('Loft',default= 0)
    'Shelf_Floor_Loft_1': forms.Select(attrs={'class':'form-control'}),
    'Tray_Floor_Loft_1': forms.Select(attrs={'class':'form-control'}),
    'Section_Floor_Loft_1': forms.Select(attrs={'class':'form-control'}),




    # LOCATION2

   
    # Ground_2= models.IntegerField('Ground',default= 0) 
    'Shelf_Ground_2': forms.Select(attrs={'class':'form-control'}),
    'Tray_Ground_2': forms.Select(attrs={'class':'form-control'}),
    'Section_Ground_2': forms.Select(attrs={'class':'form-control'}),




    # Floor_1st_2= models.IntegerField('1st Floor',default= 0)
    'Shelf_Floor_1st_2': forms.Select(attrs={'class':'form-control'}),
    'Tray_Floor_1st_2': forms.Select(attrs={'class':'form-control'}),
    'Section_Floor_1st_2': forms.Select(attrs={'class':'form-control'}),



    # Floor_2nd_2= models.IntegerField('2nd Floor',default= 0)
    'Shelf_Floor_2nd_2': forms.Select(attrs={'class':'form-control'}),
    'Tray_Floor_2nd_2': forms.Select(attrs={'class':'form-control'}),
    'Section_Floor_2nd_2': forms.Select(attrs={'class':'form-control'}),




    # Floor_Loft_2= models.IntegerField('Loft',default= 0)
    'Shelf_Floor_Loft_2': forms.Select(attrs={'class':'form-control'}),
    'Tray_Floor_Loft_2': forms.Select(attrs={'class':'form-control'}),
    'Section_Floor_Loft_2': forms.Select(attrs={'class':'form-control'}),























   'ShelfG_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayG_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionG_GF': forms.Select(attrs={'class':'form-control'}),
    'MoistureG_GF': forms.NumberInput(attrs={'class':'form-control'}),



   'ShelfG_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayG_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionG_1F': forms.Select(attrs={'class':'form-control'}),
    'MoistureG_1F': forms.NumberInput(attrs={'class':'form-control'}),


   'ShelfG_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayG_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionG_2F': forms.Select(attrs={'class':'form-control'}),
    'MoistureG_2F': forms.NumberInput(attrs={'class':'form-control'}),



   'ShelfG_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayG_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionG_FL': forms.Select(attrs={'class':'form-control'}),
    'MoistureG_FL': forms.NumberInput(attrs={'class':'form-control'}),


   'ShelfH_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayH_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionH_GF': forms.Select(attrs={'class':'form-control'}),
    'MoistureH_GF': forms.NumberInput(attrs={'class':'form-control'}),



   'ShelfH_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayH_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionH_1F': forms.Select(attrs={'class':'form-control'}),
    'MoistureH_1F': forms.NumberInput(attrs={'class':'form-control'}),



   'ShelfH_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayH_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionH_2F': forms.Select(attrs={'class':'form-control'}),
    'MoistureH_2F': forms.NumberInput(attrs={'class':'form-control'}),




   'ShelfH_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayH_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionH_FL': forms.Select(attrs={'class':'form-control'}),
    'MoistureH_FL': forms.NumberInput(attrs={'class':'form-control'}),






   'ShelfM_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayM_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionM_GF': forms.Select(attrs={'class':'form-control'}),
    'MoistureM_GF': forms.NumberInput(attrs={'class':'form-control'}),



   'ShelfM_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayM_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionM_1F': forms.Select(attrs={'class':'form-control'}),
    'MoistureM_1F': forms.NumberInput(attrs={'class':'form-control'}),




   'ShelfM_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayM_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionM_2F': forms.Select(attrs={'class':'form-control'}),
    'MoistureM_2F': forms.NumberInput(attrs={'class':'form-control'}),



   'ShelfM_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayM_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionM_FL': forms.Select(attrs={'class':'form-control'}),
    'MoistureM_FL': forms.NumberInput(attrs={'class':'form-control'}),




   'ShelfU_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayU_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionU_GF': forms.Select(attrs={'class':'form-control'}),
    'MoistureU_GF': forms.NumberInput(attrs={'class':'form-control'}),





   'ShelfU_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayU_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionU_1F': forms.Select(attrs={'class':'form-control'}),
    'MoistureU_1F': forms.NumberInput(attrs={'class':'form-control'}),





   'ShelfU_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayU_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionU_2F': forms.Select(attrs={'class':'form-control'}),
    'MoistureU_2F': forms.NumberInput(attrs={'class':'form-control'}),




   'ShelfU_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayU_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionU_FL': forms.Select(attrs={'class':'form-control'}),
    'MoistureU_FL': forms.NumberInput(attrs={'class':'form-control'}),




   'ShelfGP_GF': forms.Select(attrs={'class':'form-control'}),
    'TrayGP_GF': forms.Select(attrs={'class':'form-control'}),
    'SectionGP_GF': forms.Select(attrs={'class':'form-control'}),
    'MoistureGP_GF': forms.NumberInput(attrs={'class':'form-control'}),


   'ShelfGP_1F': forms.Select(attrs={'class':'form-control'}),
    'TrayGP_1F': forms.Select(attrs={'class':'form-control'}),
    'SectionGP_1F': forms.Select(attrs={'class':'form-control'}),
    'MoistureGP_1F': forms.NumberInput(attrs={'class':'form-control'}),


   'ShelfGP_2F': forms.Select(attrs={'class':'form-control'}),
    'TrayGP_2F': forms.Select(attrs={'class':'form-control'}),
    'SectionGP_2F': forms.Select(attrs={'class':'form-control'}),
    'MoistureGP_2F': forms.NumberInput(attrs={'class':'form-control'}),


   'ShelfGP_FL': forms.Select(attrs={'class':'form-control'}),
    'TrayGP_FL': forms.Select(attrs={'class':'form-control'}),
    'SectionGP_FL': forms.Select(attrs={'class':'form-control'}),
    'MoistureGP_FL': forms.NumberInput(attrs={'class':'form-control'}),




















    'BATCH_NUMBER': forms.TextInput(attrs={'class':'form-control'}),

    'CORRESPONDING_DELIVERY_ADVICE': forms.TextInput(attrs={'class':'form-control'}),

    'Control_number': forms.TextInput(attrs={'class':'form-control'}),


        }



class Dispatch_Of_Green_Nutmeg_Form(ModelForm):
    class Meta:
        model = Dispatch_Of_Green_Nutmeg
        fields = '__all__'
        widgets={
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

        'Worker_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Worker_ID_Name': forms.HiddenInput(attrs={'class':'form-control'}),
    'DATE_CREATED': forms.DateInput(attrs={'type':'date','class':'form-control'}),

    'Nutmeg_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'STATION': forms.Select(attrs={'class':'form-control'}),
    'DATE_OF_PURCHASE': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'TOTAL_NUM_OF_FARMERS': forms.NumberInput(attrs={'class':'form-control'}),
    'TOTAL_LBS_NUTMEG_BOUGHT': forms.NumberInput(attrs={'class':'form-control'}),
    'NUM_OF_BAGS': forms.NumberInput(attrs={'class':'form-control'}),
    'DELIVERY_ADVICE_NUMBER': forms.TextInput(attrs={'class':'form-control'}),
    'WAREHOUSE_RECEIPT_NUMBER': forms.TextInput(attrs={'class':'form-control'}),
    'CONTROL_NUMBER': forms.TextInput(attrs={'class':'form-control'}),
    'BATCH_CODES': forms.TextInput(attrs={'class':'form-control'}),
        }


class Cracking_Summary_Form(ModelForm):
    class Meta:
        model = Cracking_Summary
        fields = '__all__'
        widgets={

    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'Worker_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Worker_ID_Name': forms.HiddenInput(attrs={'class':'form-control'}),
    
    'Nutmeg_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'STATION': forms.Select(attrs={'class':'form-control'}),
    'DATE_OF_CRACKING': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'WAREHOUSE_RECEIPT_NUMBERS': forms.TextInput(attrs={'class':'form-control'}),
    'NUM_OF_BAGS': forms.NumberInput(attrs={'class':'form-control'}),
    'LBS_OF_NUTMEGS_CRACKED': forms.NumberInput(attrs={'class':'form-control'}),
            'STATION': forms.Select(attrs={'class':'form-control'}),
            'WAREHOUSE_RECEIPT_NUMBERS': forms.TextInput(attrs={'class':'form-control'}),
            'NUM_OF_BAGS': forms.NumberInput(attrs={'class':'form-control'}),
            'LBS_OF_NUTMEGS_CRACKED': forms.NumberInput(attrs={'class':'form-control'}),
            'Delivery_Advice_Num': forms.TextInput(attrs={'class':'form-control'}),
            'Control_Num': forms.TextInput(attrs={'class':'form-control'}),
            'BatchCodes': forms.TextInput(attrs={'class':'form-control'}),
            'num_pieces': forms.TextInput(attrs={'class':'form-control'}),
            'fragments': forms.TextInput(attrs={'class':'form-control'}),
            'regular_nutmeg': forms.TextInput(attrs={'class':'form-control'}),
            'escape_nutmeg': forms.TextInput(attrs={'class':'form-control'}),
            'num_floaters': forms.TextInput(attrs={'class':'form-control'}),
            'lbs_floated': forms.TextInput(attrs={'class':'form-control'}),
            'date': forms.TextInput(attrs={'class':'form-control'}),
            'lbs_lights': forms.TextInput(attrs={'class':'form-control'}),
            'lbs_heavies': forms.TextInput(attrs={'class':'form-control'}),

        }



class Floation_Summary_Form(ModelForm):
    class Meta:
        model = Floation_Summary
        fields = '__all__'
        widgets={
    'Worker_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Worker_ID_Name': forms.HiddenInput(attrs={'class':'form-control'}),
    
    'Nutmeg_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'STATION': forms.Select(attrs={'class':'form-control'}),
    'START_DRYING_DATE': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'APPROX_END_DRYING_DATE': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'END_DRYING_DATE': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),





    'entryCheck': forms.HiddenInput(attrs={'class':'form-control'}),



    'ShelfG_light': forms.Select(attrs={'class':'form-control'}),
    'TrayG_light': forms.Select(attrs={'class':'form-control'}),
    'SectionG_light': forms.Select(attrs={'class':'form-control'}),
    'MoistureG_light': forms.TextInput(attrs={'class':'form-control'}),

    'ShelfG_heavy': forms.Select(attrs={'class':'form-control'}),
    'TrayG_heavy': forms.Select(attrs={'class':'form-control'}),
    'SectionG_heavy': forms.Select(attrs={'class':'form-control'}),
    'MoistureG_heavy': forms.TextInput(attrs={'class':'form-control'}),


    'ShelfH_light': forms.Select(attrs={'class':'form-control'}),
    'TrayH_light': forms.Select(attrs={'class':'form-control'}),
    'SectionH_light': forms.Select(attrs={'class':'form-control'}),
    'MoistureH_light': forms.TextInput(attrs={'class':'form-control'}),

    'ShelfH_heavy': forms.Select(attrs={'class':'form-control'}),
    'TrayH_heavy': forms.Select(attrs={'class':'form-control'}),
    'SectionH_heavy': forms.Select(attrs={'class':'form-control'}),
    'MoistureH_heavy': forms.TextInput(attrs={'class':'form-control'}),


    'ShelfM_light': forms.Select(attrs={'class':'form-control'}), 
    'TrayM_light': forms.Select(attrs={'class':'form-control'}),
    'SectionM_light': forms.Select(attrs={'class':'form-control'}),
    'MoistureM_light': forms.TextInput(attrs={'class':'form-control'}),

    'ShelfM_heavy': forms.Select(attrs={'class':'form-control'}),
    'TrayM_heavy': forms.Select(attrs={'class':'form-control'}),
    'SectionM_heavy': forms.Select(attrs={'class':'form-control'}),
    'MoistureM_heavy': forms.TextInput(attrs={'class':'form-control'}),



    'ShelfU_light': forms.Select(attrs={'class':'form-control'}), 
    'TrayU_light': forms.Select(attrs={'class':'form-control'}),
    'SectionU_light': forms.Select(attrs={'class':'form-control'}),
    'MoistureU_light': forms.TextInput(attrs={'class':'form-control'}),



    'ShelfU_heavy': forms.Select(attrs={'class':'form-control'}),
    'TrayU_heavy': forms.Select(attrs={'class':'form-control'}),
    'SectionU_heavy': forms.Select(attrs={'class':'form-control'}),
    'MoistureU_heavy': forms.TextInput(attrs={'class':'form-control'}),



    'ShelfGP_light': forms.Select(attrs={'class':'form-control'}),
    'TrayGP_light': forms.Select(attrs={'class':'form-control'}),
    'SectionGP_light': forms.Select(attrs={'class':'form-control'}),
    'MoistureGP_light': forms.TextInput(attrs={'class':'form-control'}),

    'ShelfGP_heavy': forms.Select(attrs={'class':'form-control'}), 
    'TrayGP_heavy': forms.Select(attrs={'class':'form-control'}),
    'SectionGP_heavy': forms.Select(attrs={'class':'form-control'}),
    'MoistureGP_heavy': forms.TextInput(attrs={'class':'form-control'}),












# LOCATION - PLACEMENT ON SHELF 


    # HEAVIES
    'Ground_Floorh': forms.TextInput(attrs={'class':'form-control'}),
    'Shelfh': forms.Select(attrs={'class':'form-control'}),
    'Trayh': forms.Select(attrs={'class':'form-control'}),
    'Sectionh': forms.Select(attrs={'class':'form-control'}),


    # LIGHTS
    'Ground_Floorl': forms.TextInput(attrs={'class':'form-control'}),
    'Shelfl': forms.Select(attrs={'class':'form-control'}),
    'Trayl': forms.Select(attrs={'class':'form-control'}),
    'Sectionl': forms.Select(attrs={'class':'form-control'}),


# MOISTURE TESTING 

    'FINAL_MOISTURE_H': forms.TextInput(attrs={'class':'form-control'}),
    'FINAL_MOISTURE_L' : forms.TextInput(attrs={'class':'form-control'}),



      #Heavies/Lights (drop down box)
    'BATCH_NUMBER': forms.TextInput(attrs={'class':'form-control'}),
    'Control_NUMBER': forms.TextInput(attrs={'class':'form-control'}),

        }



class Package_Ciontrol_Form(ModelForm):
    class Meta:
        model = Package_Ciontrol
        fields = '__all__'
        widgets={
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'Worker_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Worker_ID_Name': forms.HiddenInput(attrs={'class':'form-control'}),
    
    'Nutmeg_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'PRODUCT_DESCRIPTION': forms.Select(attrs={'class':'form-control'}),    
    'PRODUCT_DESCRIPTION_cont': forms.Textarea(attrs={'class':'form-control'}),

# PACKAGING DATE

    'START': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'END': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'QUANTITY_OF_BAGS': forms.NumberInput(attrs={'class':'form-control'}),
    'TOTAL_WEIGHT_LBS': forms.TextInput(attrs={'class':'form-control'}),
    'PACKAGING_MATERIAL': forms.Select(attrs={'class':'form-control'}),    
    'BATCH_NUMBER': forms.TextInput(attrs={'class':'form-control'}),
    'CONTRACT_NUMBER': forms.TextInput(attrs={'class':'form-control'}),
    'OFFICIAL_LAB_RESULTS': forms.TextInput(attrs={'class':'form-control'}),
'PACKAGING_MATERIAL_cont': forms.Textarea(attrs={'class':'form-control'}),
    'Physical_Analysis': forms.Select(attrs={'class':'form-control'}),     
    'Chemical_Analysis': forms.Select(attrs={'class':'form-control'}),       
    'Microbiological_Analysis': forms.Select(attrs={'class':'form-control'}),   





        }













# class Full_Form(ModelForm):
# 	class Meta:
# 		model = fullform
# 		fields = '__all__'
# 		widgets ={

#             'Nutmeg_ID_No' : forms.TextInput(attrs={'class':'form-control'}),
# 		 	'farmer_ID': forms.TextInput(attrs={'class':'form-control'}),
# 		    'name' : forms.TextInput(attrs={'class':'form-control'}),
# 		    'village' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'parish': forms.TextInput(attrs={'class':'form-control'}),
# 		    'GPS_location' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'email': forms.EmailInput(attrs={'class':'form-control'}),
# 		    'phone' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'age' : forms.Select(attrs={'class':'form-control'}),

# 		    'titles': forms.TextInput(attrs={'class':'form-control'}),
# 		    'family': forms.TextInput(attrs={'class':'form-control'}),
# 		    'lease' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'caretaker': forms.TextInput(attrs={'class':'form-control'}),
# 		    'agent' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'comments' :forms.Textarea(attrs={'class':'form-control'}),

# 		    'Tree_types' :forms.Select(attrs={'class':'form-control'}),
# 		    'Mature_trees': forms.NumberInput(attrs={'class':'form-control'}),
# 		    'Bearing_trees' :forms.NumberInput(attrs={'class':'form-control'}),
# 		    'NonBearing_trees': forms.NumberInput(attrs={'class':'form-control'}),


# 		    'land_elevation': forms.Select(attrs={'class':'form-control'}),
# 		    'soil_type' :forms.Select(attrs={'class':'form-control'}),
# 		    'rainfall_pattern' :forms.Select(attrs={'class':'form-control'}),
# 		    'other_crops': forms.CheckboxSelectMultiple(attrs={}),
# 		    'intercrop' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'pure_stand' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'norm_land' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'seas_land' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'aban_land': forms.TextInput(attrs={'class':'form-control'}),

# 		    'road_access' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'land_slide': forms.TextInput(attrs={'class':'form-control'}),
# 		    'flooding' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'heavy_metals': forms.TextInput(attrs={'class':'form-control'}),
# 		    'chemical_spills': forms.TextInput(attrs={'class':'form-control'}),
# 		    'dumping' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'feedlot': forms.TextInput(attrs={'class':'form-control'}),
# 		    'pesticides' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'septic_tanks' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'manical': forms.Select(attrs={'class':'form-control'}),
# 		    'river' :forms.Select(attrs={'class':'form-control'}),
# 		    'spring' :forms.Select(attrs={'class':'form-control'}),
# 		    'well': forms.Select(attrs={'class':'form-control'}),
# 		    'harvested' :forms.Select(attrs={'class':'form-control'}),
# 		    'treated' :forms.Select(attrs={'class':'form-control'}),

# 		    'annual_production' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'peak_productions': forms.TextInput(attrs={'class':'form-control'}),
# 		    'inspected_by' :forms.DateInput(attrs={'type':'date','class':'form-control'}),
# 		    'date': forms.DateInput(attrs={'type':'date','class':'form-control'}),



# 		 }



# class User_info_Form(ModelForm):
# 	class Meta:
# 		model = User_info
# 		fields = '__all__'
# 		widgets ={

# 		 	'farmer_ID': forms.TextInput(attrs={'class':'form-control'}),
# 		    'name' : forms.TextInput(attrs={'class':'form-control'}),
# 		    'village' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'parish': forms.TextInput(attrs={'class':'form-control'}),
#    			'latitude':forms.NumberInput(attrs={'class':'form-control'}),
#    			'longitude':forms.NumberInput(attrs={'class':'form-control'}),
# 		    'email': forms.EmailInput(attrs={'class':'form-control'}),
# 		    'phone' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'age' : forms.Select(attrs={'class':'form-control'}),


# 		}




# class Land_tenurship_Form(ModelForm):
# 	class Meta:
# 		model = Land_tenurship
# 		fields = '__all__'
# 		widgets ={
# 			'farmer_ID': forms.Select(attrs={'class':'form-control'}),
#  		    'tenure_status': forms.Select(attrs={'class':'form-control'}),
# 		    'family': forms.TextInput(attrs={'class':'form-control'}),
# 		    'lease' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'caretaker': forms.TextInput(attrs={'class':'form-control'}),
# 		    'agent' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'comments' :forms.Textarea(attrs={'class':'form-control'}),
# 		}




# class tree_Form(ModelForm):
# 	class Meta:
# 		model = tree
# 		fields = '__all__'
# 		widgets ={
# 			'farmer_ID': forms.Select(attrs={'class':'form-control'}),
# 		    'Tree_types' :forms.Select(attrs={'class':'form-control'}),
# 		    'Mature_trees': forms.NumberInput(attrs={'class':'form-control'}),
# 		    'Bearing_trees' :forms.NumberInput(attrs={'class':'form-control'}),
# 		    'NonBearing_trees': forms.NumberInput(attrs={'class':'form-control'}),
# 		}




# class farm_Form(ModelForm):
# 	class Meta:
# 		model = farm
# 		fields = '__all__'
# 		widgets ={

# 			'farmer_ID': forms.Select(attrs={'class':'form-control'}),
# 		    'land_elevation': forms.Select(attrs={'class':'form-control'}),
# 		    'soil_type' :forms.Select(attrs={'class':'form-control'}),
# 		    'rainfall_pattern' :forms.Select(attrs={'class':'form-control'}),
# 		    'other_crops': forms.CheckboxSelectMultiple(attrs={}),
# 		    'intercrop' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'pure_stand' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'norm_land' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'seas_land' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'aban_land': forms.TextInput(attrs={'class':'form-control'}),

# 		}




# class state_Form(ModelForm):
# 	class Meta:
# 		model = state
# 		fields = '__all__'
# 		widgets ={

# 			'farmer_ID': forms.Select(attrs={'class':'form-control'}),
# 		    'road_access' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'land_slide': forms.TextInput(attrs={'class':'form-control'}),
# 		    'flooding' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'heavy_metals': forms.TextInput(attrs={'class':'form-control'}),
# 		    'chemical_spills': forms.TextInput(attrs={'class':'form-control'}),
# 		    'dumping' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'feedlot': forms.TextInput(attrs={'class':'form-control'}),
# 		    'pesticides' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'septic_tanks' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'manical': forms.Select(attrs={'class':'form-control'}),
# 		    'river' :forms.Select(attrs={'class':'form-control'}),
# 		    'spring' :forms.Select(attrs={'class':'form-control'}),
# 		    'well': forms.Select(attrs={'class':'form-control'}),
# 		    'harvested' :forms.Select(attrs={'class':'form-control'}),
# 		    'treated' :forms.Select(attrs={'class':'form-control'}),


# 		}




# class symmary_Form(ModelForm):
# 	class Meta:
# 		model = symmary
# 		fields = '__all__'
# 		widgets ={

# 			'farmer_ID': forms.Select(attrs={'class':'form-control'}),
# 		    'annual_production' :forms.TextInput(attrs={'class':'form-control'}),
# 		    'peak_productions': forms.TextInput(attrs={'class':'form-control'}),
# 		    'inspected_by' :forms.DateInput(attrs={'type':'date','class':'form-control'}),
# 		    'date': forms.DateInput(attrs={'type':'date','class':'form-control'}),


#   		}




class Dried_Form_A(ModelForm):
	class Meta:
		model = Dried_Moisture_Analysis_A
		fields = '__all__'
		widgets ={
    
    
    
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),
    'Worker_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Worker_ID_Name': forms.HiddenInput(attrs={'class':'form-control'}),
    

    'Nutmeg_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'DATE_OF_SAMPLING': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'STATION':forms.TextInput(attrs={'class':'form-control'}),
    'BATCH_CODE' :forms.TextInput(attrs={'class':'form-control'}),
    'Quantity_of_Bags' :forms.NumberInput(attrs={'class':'form-control'}),
    'Quantity_of_Sample' :forms.NumberInput(attrs={'class':'form-control'}),
    'Total_Weight':forms.NumberInput(attrs={'class':'form-control'}),
    'Initial_Sample_Weight':forms.NumberInput(attrs={'class':'form-control'}),
    # Weight 
    'Insect_Damaged':forms.NumberInput(attrs={'class':'form-control'}),
    'Broken':forms.NumberInput(attrs={'class':'form-control'}),
    'Mould':forms.NumberInput(attrs={'class':'form-control'}),
    'Final_Sample_Weight':calculation.FormulaInput('Initial_Sample_Weight-(Insect_Damaged+Broken+Mould)',attrs={'class':'form-control'}),

    # MOISTURE CONTENT RESULTS (%)


    # CRITERIA 

    'READING_1':forms.TextInput(attrs={'class':'form-control'}),
    'READING_2':forms.TextInput(attrs={'class':'form-control'}),
    'READING_3':forms.TextInput(attrs={'class':'form-control'}),
    'AVERAGE':forms.TextInput(attrs={'class':'form-control'}),
    'DECISION':forms.Select(attrs={'class':'form-control'}),
    'Comments':forms.Textarea(attrs={'class':'form-control'}),
    'TEST_PERFORMED_BY':forms.TextInput(attrs={'class':'form-control'}),
    'DATE': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'APPROVED_BY':forms.TextInput(attrs={'class':'form-control'}),
    'DATE_OF_REPORT': forms.DateInput(attrs={'type':'date','class':'form-control'}),


    # CHECKED BY QA OFFICER

    'SIGNED_BY_QUALITY_ASSURANCE_OFFICER':forms.TextInput(attrs={'class':'form-control'}),
    'DATE': forms.DateInput(attrs={'type':'date','class':'form-control'}),



 

  	 }
  
class Dried_Form_B(ModelForm):
	class Meta:
		model = Dried_Moisture_Analysis_B
		fields = '__all__'
		widgets ={




    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'DATE_OF_SAMPLING': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'STATION':forms.TextInput(attrs={'class':'form-control'}),
    'BATCH_CODE' :forms.TextInput(attrs={'class':'form-control'}),
    'Total_Quantity_of_Bags_in_Non_Compliance':forms.NumberInput(attrs={'class':'form-control'}),
    'Total_Weight_of_Nutmeg_in_Non_Compliance' :forms.NumberInput(attrs={'class':'form-control'}),
    'Additional_Drying_Period' :forms.TextInput(attrs={'class':'form-control'}),
    'Initial_Sample_Weight' :forms.NumberInput(attrs={'class':'form-control'}),

    'Insect_Damaged' :forms.NumberInput(attrs={'class':'form-control'}),
    'Broken':forms.NumberInput(attrs={'class':'form-control'}),
    'Mould':forms.NumberInput(attrs={'class':'form-control'}),
    'Final_Sample_Weight':calculation.FormulaInput('Initial_Sample_Weight-(Insect_Damaged+Broken+Mould)',attrs={'class':'form-control'}),
 
    'READING_1' :forms.NumberInput(attrs={'class':'form-control'}),
    'READING_2' :forms.NumberInput(attrs={'class':'form-control'}),
    'READING_3' :forms.NumberInput(attrs={'class':'form-control'}),
    'AVERAGE' :forms.TextInput(attrs={'class':'form-control'}),
    'DECISION' :forms.Select(attrs={'class':'form-control'}),
    'Comments' :forms.Textarea(attrs={'class':'form-control'}),
    'TEST_PERFORMED_BY':forms.TextInput(attrs={'class':'form-control'}),
    'APPROVED_BY':forms.TextInput(attrs={'class':'form-control'}),
    'DATE_OF_REPORT': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'SIGNED_BY_QUALITY_ASSURANCE_OFFICER':forms.TextInput(attrs={'class':'form-control'}),
    'DATE': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'Additional_Drying_Period1': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'Additional_Drying_Period2': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'Additional_Drying_Period3': forms.DateInput(attrs={'type':'date','class':'form-control'}),

  		}
  




class Floated_Form_A(ModelForm):
	class Meta:
		model = Floated_Moisture_Analysis_A
		fields = '__all__'
		widgets={
        'Worker_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Worker_ID_Name': forms.HiddenInput(attrs={'class':'form-control'}),
    

    'Nutmeg_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
     'BATCH_CODE' :forms.TextInput(attrs={'class':'form-control'}),
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    'DATE_OF_SAMPLING': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'DATE_OF_SAMPLING_L': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'STATION' :forms.TextInput(attrs={'class':'form-control'}),

    # HEAVIES
    'Quantity_of_Sample_H':forms.NumberInput(attrs={'class':'form-control'}),
    'Total_Weight_H':forms.NumberInput(attrs={'class':'form-control'}),
    'Initial_Sample_Weight_H' :forms.NumberInput(attrs={'class':'form-control'}),


    # LIGHTS
    'Quantity_of_Sample_L' :forms.NumberInput(attrs={'class':'form-control'}),
    'Total_Weight_L':forms.NumberInput(attrs={'class':'form-control'}),
    'Initial_Sample_Weight_L' :forms.NumberInput(attrs={'class':'form-control'}),


    # Weight 

    # HEAVIES
    'Insect_Damaged_H' :forms.NumberInput(attrs={'class':'form-control'}),
    'Broken_H' :forms.NumberInput(attrs={'class':'form-control'}),
    'Mould_H' :forms.NumberInput(attrs={'class':'form-control'}),
    'Final_Sample_Weight_H' :calculation.FormulaInput('Initial_Sample_Weight_H-(Insect_Damaged_H+Broken_H+Mould_H)',attrs={'class':'form-control'}),


    # LIGHTS
    'Insect_Damaged_L' :forms.NumberInput(attrs={'class':'form-control'}),
    'Broken_L' :forms.NumberInput(attrs={'class':'form-control'}),
    'Mould_L' :forms.NumberInput(attrs={'class':'form-control'}),
    'Final_Sample_Weight_L' :calculation.FormulaInput('Initial_Sample_Weight_L-(Insect_Damaged_L+Broken_L+Mould_L)',attrs={'class':'form-control'}),



    # HEAVIES
    'READING_1_H' :forms.NumberInput(attrs={'class':'form-control'}),
    'READING_2_H' :forms.NumberInput(attrs={'class':'form-control'}),
    'READING_3_H' :forms.NumberInput(attrs={'class':'form-control'}),
    'AVERAGE_H' :calculation.FormulaInput('(READING_1_H+READING_2_H+READING_3_H)/3',attrs={'class':'form-control'}),
    'DECISION_H'  :forms.Select(attrs={'class':'form-control'}),
    'Comments_H' :forms.Textarea(attrs={'class':'form-control'}),
    'TEST_PERFORMED_BY_H'  :forms.TextInput(attrs={'class':'form-control'}),
    'DATE_H': forms.DateInput(attrs={'type':'date','class':'form-control'}),


    # LIGHTS
    'READING_1_L':forms.NumberInput(attrs={'class':'form-control'}),
    'READING_2_L' :forms.NumberInput(attrs={'class':'form-control'}),
    'READING_3_L' :forms.NumberInput(attrs={'class':'form-control'}),
    'AVERAGE_L' :calculation.FormulaInput('(READING_1_L+READING_2_L+READING_3_L)/3',attrs={'class':'form-control'}),
    'DECISION_L':forms.Select(attrs={'class':'form-control'}),
    'Comments_L' :forms.Textarea(attrs={'class':'form-control'}),
    'TEST_PERFORMED_BY_L'  :forms.TextInput(attrs={'class':'form-control'}),
    'DATE_L': forms.DateInput(attrs={'type':'date','class':'form-control'}),



    'SIGNED_BY' :forms.TextInput(attrs={'class':'form-control'}),
    'Station_Manager':forms.TextInput(attrs={'class':'form-control'}),
    'DATE_OF_REPORT': forms.DateInput(attrs={'type':'date','class':'form-control'}),

    # CHECKED BY QA OFFICER
    'SIGNED_BY_Quality_Assurance_Officer':forms.TextInput(attrs={'class':'form-control'}),
    'DATE': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'Approved_BY':forms.TextInput(attrs={'class':'form-control'}),

  		}




  
class Floated_Form_B(ModelForm):
	class Meta:
		model = Floated_Moisture_Analysis_B
		fields = '__all__'
		widgets={

    'Worker_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Nutmeg_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

    # Corrective Action for Floated Nutmeg Above 10% Moisture Content
    'DATE_OF_SAMPLING_H': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'DATE_OF_SAMPLING_L': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'STATION':forms.TextInput(attrs={'class':'form-control'}),

    # HEAVIES
    'Total_Quantity_of_Bags_in_Non_Compliance_H' :forms.NumberInput(attrs={'class':'form-control'}),
    'Total_Weight_of_Nutmeg_in_Non_Compliance_H' :forms.NumberInput(attrs={'class':'form-control'}),
    'Additional_Drying_Period_days_H'  :forms.NumberInput(attrs={'class':'form-control'}),
    'Total_Weight_H'   :forms.NumberInput(attrs={'class':'form-control'}),
    'Total_Weight_L'  :forms.NumberInput(attrs={'class':'form-control'}),
    # LIGHTS

    'Total_Quantity_of_Bags_in_Non_Compliance_L' :forms.NumberInput(attrs={'class':'form-control'}),
    'Total_Weight_of_Nutmeg_in_Non_Compliance_L' :forms.NumberInput(attrs={'class':'form-control'}),
    'Additional_Drying_Period_days_L'  :forms.NumberInput(attrs={'class':'form-control'}),


    # Weight (oz/lbs)


    # HEAVIES
    'Initial_Sample_Weight_H' :forms.NumberInput(attrs={'class':'form-control'}),
    'Broken_H'  :forms.NumberInput(attrs={'class':'form-control'}),
    'Mould_H' :forms.NumberInput(attrs={'class':'form-control'}),
    'Insect_Damaged_H' :forms.NumberInput(attrs={'class':'form-control'}),
    'Final_Sample_Weight_H' :calculation.FormulaInput('Initial_Sample_Weight_H-(Insect_Damaged_H+Broken_H+Mould_H)',attrs={'class':'form-control'}),


    # LIGHTS
    'Initial_Sample_Weight_L' :forms.NumberInput(attrs={'class':'form-control'}),
    'Broken_L' :forms.NumberInput(attrs={'class':'form-control'}),
    'Mould_L' :forms.NumberInput(attrs={'class':'form-control'}),
    'Insect_Damaged_L'  :forms.NumberInput(attrs={'class':'form-control'}),
    'Final_Sample_Weight_L' :calculation.FormulaInput('Initial_Sample_Weight_L-(Insect_Damaged_L+Broken_L+Mould_L)',attrs={'class':'form-control'}),




    # HEAVIES

    'READING_1_H'  :forms.NumberInput(attrs={'class':'form-control'}),
    'READING_2_H' :forms.NumberInput(attrs={'class':'form-control'}),
    'READING_3_H'  :forms.NumberInput(attrs={'class':'form-control'}),
    'AVERAGE_H'  :calculation.FormulaInput('(READING_1_H+READING_2_H+READING_3_H)/3',attrs={'class':'form-control'}),
    'DECISION_H' :forms.TextInput(attrs={'class':'form-control'}),
    'Comments_H' :forms.Textarea(attrs={'class':'form-control'}),
    'TEST_PERFORMED_BY_H':forms.TextInput(attrs={'class':'form-control'}),
    'DATE_H': forms.DateInput(attrs={'type':'date','class':'form-control'}),



    # LIGHTS
    'READING_1_L' :forms.NumberInput(attrs={'class':'form-control'}),
    'READING_2_L'  :forms.NumberInput(attrs={'class':'form-control'}),
    'READING_3_L' :forms.NumberInput(attrs={'class':'form-control'}),
    'AVERAGE_L'  :calculation.FormulaInput('(READING_1_L+READING_2_L+READING_3_L)/3',attrs={'class':'form-control'}),
    'DECISION_L':forms.TextInput(attrs={'class':'form-control'}),
    'Comments_L' :forms.Textarea(attrs={'class':'form-control'}),
    'TEST_PERFORMED_BY_L':forms.TextInput(attrs={'class':'form-control'}),
    'DATE_L' : forms.DateInput(attrs={'type':'date','class':'form-control'}),




    'SIGNED_BY' :forms.TextInput(attrs={'class':'form-control'}),
    'Station_Manager':forms.TextInput(attrs={'class':'form-control'}),
    'DATE_OF_REPORT': forms.DateInput(attrs={'type':'date','class':'form-control'}),


    # CHECKED BY QA OFFICER

    'SIGNED_BY_Quality_Assurance_Officer':forms.TextInput(attrs={'class':'form-control'}),
    'DATE': forms.DateInput(attrs={'type':'date','class':'form-control'}),

	}

  



class Quality_Form(ModelForm):
	class Meta:
		model = Quality_Control
		fields = '__all__'
		widgets={

        'Worker_ID_No' : forms.HiddenInput(attrs={'class':'form-control'}),
    'Worker_ID_Name': forms.HiddenInput(attrs={'class':'form-control'}),
    

    'Nutmeg_ID_No': forms.HiddenInput(attrs={'class':'form-control'}),
    'Land_ID_N0': forms.HiddenInput(attrs={'class':'form-control'}),

	'DATE_1': forms.DateInput(attrs={'type':'date','class':'form-control'}),
    'STATION':forms.Select(attrs={'class':'form-control'}),
    'BATCH_NUMBER' :forms.TextInput(attrs={'class':'form-control'}),
    'REWORK':forms.Select(attrs={'class':'form-control'}),
    'SAMPLE_WEIGHT' :forms.NumberInput(attrs={'class':'form-control'}),
    'Nutmeg_Assorted':forms.Select(attrs={'class':'form-control'}),
    'Nutmeg_Assorted_cont':forms.TextInput(attrs={'class':'form-control'}),
    # TOLERANCE LIMITS FOR DEFECTS

    # Free_of_extraneous matter - Inshell (Whole) and Shelled - 0.5%
    # Broken/damaged – Inshell Whole2%
    # Broken/damaged Shelled - 3%


    # WEIGHT (oz/lbs)

    'ASSORTOR':forms.TextInput(attrs={'class':'form-control'}),
    'SOUNDS' :forms.NumberInput(attrs={'class':'form-control'}),
    'PINHOLES' :forms.NumberInput(attrs={'class':'form-control'}),
    'CRACKED'  :forms.NumberInput(attrs={'class':'form-control'}),
    'BROKEN'  :forms.NumberInput(attrs={'class':'form-control'}),
    'PIECES' :forms.NumberInput(attrs={'class':'form-control'}),
    'FOREIGN_MATTER'  :forms.NumberInput(attrs={'class':'form-control'}),

    'SUPERVISOR' :forms.TextInput(attrs={'class':'form-control'}),
    'COMMENTS' :forms.Textarea(attrs={'class':'form-control'}),


    'SIGNED_BY':forms.TextInput(attrs={'class':'form-control'}),
    'Station_Manager':forms.TextInput(attrs={'class':'form-control'}),    
    'DATE_OF_REPORT': forms.DateInput(attrs={'type':'date','class':'form-control'}),

    # CHECKED BY QA OFFICER

    'SIGNED_BY_QUALITY_ASSURANCE_OFFICER' :forms.TextInput(attrs={'class':'form-control'}),
    'DATE_2' : forms.DateInput(attrs={'type':'date','class':'form-control'}),




    'ASSORTOR1' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR1_A' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR1_B' :forms.TextInput(attrs={'class':'form-control'}),   
    'ASSORTOR1_C' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR1_D' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR1_E' :forms.TextInput(attrs={'class':'form-control'}),












    'ASSORTOR1' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR2' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR3' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR4' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR5' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR6' :forms.TextInput(attrs={'class':'form-control'}),


    'ASSORTOR1_A' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR1_B' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR1_C' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR1_D' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR1_E' :forms.TextInput(attrs={'class':'form-control'}),





    'ASSORTOR2' :forms.TextInput(attrs={'class':'form-control'}),


    'ASSORTOR2_A' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR2_B' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR2_C' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR2_D' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR2_E' :forms.TextInput(attrs={'class':'form-control'}),







    'ASSORTOR3' :forms.TextInput(attrs={'class':'form-control'}),


    'ASSORTOR3_A' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR3_B' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR3_C' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR3_D' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR3_E' :forms.TextInput(attrs={'class':'form-control'}),


    'ASSORTOR4' :forms.TextInput(attrs={'class':'form-control'}),


    'ASSORTOR4_A' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR4_B' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR4_C' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR4_D' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR4_E' :forms.TextInput(attrs={'class':'form-control'}),


    'ASSORTOR5' :forms.TextInput(attrs={'class':'form-control'}),
    'Approved_BY':forms.TextInput(attrs={'class':'form-control'}),



    'ASSORTOR5_A' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR5_B' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR5_C' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR5_D' :forms.TextInput(attrs={'class':'form-control'}),
    'ASSORTOR5_E' :forms.TextInput(attrs={'class':'form-control'}),

    'SUPERVISOR_A' :forms.TextInput(attrs={'class':'form-control'}),
    'SUPERVISOR_B' :forms.TextInput(attrs={'class':'form-control'}),
    'SUPERVISOR_C' :forms.TextInput(attrs={'class':'form-control'}),
    'SUPERVISOR_D' :forms.TextInput(attrs={'class':'form-control'}),
    'SUPERVISOR_E' :forms.TextInput(attrs={'class':'form-control'}),


}







    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     if commit:
    #         instance.save()
    #     return instance


# class step1(models.Model):
#     farmer_ID :forms.TextInput(attrs={'class':'form-control'}),
#     name :forms.TextInput(attrs={'class':'form-control'}),
#     village = models.CharField(max_length=50, null=True)
#     parish = models.CharField(max_length=50, null=True)
#     GPS_location = models.CharField(max_length=50, null=True)
#     email = models.EmailField(max_length=50, null=True)
#     phone = models.CharField(max_length=50,null=True)
#     age = models.CharField(max_length=1, choices=age_range, default='A')



# class step2(models.Model):
#     titles = models.CharField(max_length=50, null=True)
#     family = models.CharField(max_length=50, null=True)
#     lease = models.CharField(max_length=100, null=True)
#     caretaker = models.CharField(max_length=50, null=True)
#     agent = models.CharField(max_length=50, null=True)
#     comments = models.TextField(blank=True)
#     Tree_types = models.CharField(max_length=50,choices=trees, default='A')
#     Mature_trees = models.IntegerField(default= 0)
#     Bearing_trees = models.IntegerField(default= 0)
#     NonBearing_trees = models.IntegerField(default= 0)


# class step3(models.Model):
#     land_elevation = models.CharField(max_length=100, choices=LAND_ELEVATION, default='P')
#     soil_type = models.CharField(max_length=100, choices=SOIL_TYPE, default='P')
#     rainfall_pattern = models.CharField(max_length=100, choices=RAINFALL_PATTERN, default='P')
#     other_crops = models.ManyToManyField(crop)
#     intercrop = models.CharField(max_length=50, null=True)
#     pure_stand = models.CharField(max_length=50, null=True)
#     norm_land = models.CharField(max_length=50, null=True)
#     seas_land = models.CharField(max_length=50, null=True)
#     aban_land = models.CharField(max_length=50, null=True)



# class step4(models.Model):
#     road_access = models.CharField(max_length=50, null=True)
#     land_slide = models.CharField(max_length=50, null=True)
#     flooding = models.CharField(max_length=50, null=True)
#     heavy_metals = models.CharField(max_length=50, null=True)
#     chemical_spills = models.CharField(max_length=50, null=True)
#     dumping = models.CharField(max_length=50, null=True)
#     feedlot = models.CharField(max_length=50, null=True)
#     pesticides = models.CharField(max_length=50, null=True)
#     septic_tanks = models.CharField(max_length=50, null=True)
#     manical = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
#     river = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
#     spring = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
#     well = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
#     harvested = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')




# class step5(models.Model):
#     treated = models.CharField(max_length=1, choices=TREATED_WATER, default='P')
#     annual_production = models.CharField(max_length=50, null=True)
#     peak_productions = models.CharField(max_length=50, null=True)
#     inspected_by = models.DateField('Inspection Date',null=True)
#     date = models.DateField('Current Date',null=True)
















# # class step1(forms.Form):
# #     farmer_ID = forms.CharField(max_length=50, null=True)
# #     name = forms.CharField(max_length=50, null=True)
# #     village = forms.CharField(max_length=50, null=True)
# #     parish = forms.CharField(max_length=50, null=True)
# #     GPS_location = forms.CharField(max_length=50, null=True)
# #     email = forms.EmailField(max_length=50, null=True)
# #     phone = forms.CharField(max_length=50,null=True)
# #     age = forms.CharField(max_length=1, choices=age_range, default='A')



# # class step2(forms.Form):
# #     titles = forms.CharField(max_length=50, null=True)
# #     family = forms.CharField(max_length=50, null=True)
# #     lease = forms.CharField(max_length=100, null=True)
# #     caretaker = forms.CharField(max_length=50, null=True)
# #     agent = forms.CharField(max_length=50, null=True)
# #     comments = forms.TextField(blank=True)
# #     Tree_types = forms.CharField(max_length=50,choices=trees, default='A')
# #     Mature_trees = forms.IntegerField(default= 0)
# #     Bearing_trees = forms.IntegerField(default= 0)
# #     NonBearing_trees = forms.IntegerField(default= 0)


# # class step3(forms.Form):
# #     land_elevation = forms.CharField(max_length=100, choices=LAND_ELEVATION, default='P')
# #     soil_type = forms.CharField(max_length=100, choices=SOIL_TYPE, default='P')
# #     rainfall_pattern = forms.CharField(max_length=100, choices=RAINFALL_PATTERN, default='P')
# #     other_crops = forms.ManyToManyField(crop)
# #     intercrop = forms.CharField(max_length=50, null=True)
# #     pure_stand = forms.CharField(max_length=50, null=True)
# #     norm_land = forms.CharField(max_length=50, null=True)
# #     seas_land = forms.CharField(max_length=50, null=True)
# #     aban_land = forms.CharField(max_length=50, null=True)



# # class step4(forms.Form):
# #     road_access = forms.CharField(max_length=50, null=True)
# #     land_slide = forms.CharField(max_length=50, null=True)
# #     flooding = forms.CharField(max_length=50, null=True)
# #     heavy_metals = forms.CharField(max_length=50, null=True)
# #     chemical_spills = forms.CharField(max_length=50, null=True)
# #     dumping = forms.CharField(max_length=50, null=True)
# #     feedlot = forms.CharField(max_length=50, null=True)
# #     pesticides = forms.CharField(max_length=50, null=True)
# #     septic_tanks = forms.CharField(max_length=50, null=True)
# #     manical = forms.CharField(max_length=1, choices=WATER_SOURCE, default='P')
# #     river = forms.CharField(max_length=1, choices=WATER_SOURCE, default='P')
# #     spring = forms.CharField(max_length=1, choices=WATER_SOURCE, default='P')
# #     well = forms.CharField(max_length=1, choices=WATER_SOURCE, default='P')
# #     harvested = forms.CharField(max_length=1, choices=WATER_SOURCE, default='P')




# # class step5(forms.Form):
# #     treated = forms.CharField(max_length=1, choices=TREATED_WATER, default='P')
# #     annual_production = forms.CharField(max_length=50, null=True)
# #     peak_productions = forms.CharField(max_length=50, null=True)
# #     inspected_by = forms.DateField('Inspection Date',null=True)
# #     date = forms.DateField('Current Date',null=True)