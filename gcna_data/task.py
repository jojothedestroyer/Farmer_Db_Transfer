#from django.test import TestCase

# Create your tests here.
# tasks.py
from GCNA_db.celery import shared_task
import indexeddb
from .models import Dried_Moisture_Analysis_A

@shared_task
def transfer_dried_a_data_from_indexeddb_to_database():
    db = indexeddb.open('GCNA', 2)
    transaction = db.transaction(['DriedA'], 'readonly')
    object_store = transaction.objectStore('DriedA')
    data = object_store.getAll()

    for item in data:
        dried_a_instance = Dried_Moisture_Analysis_A(**item)
        dried_a_instance.save()
