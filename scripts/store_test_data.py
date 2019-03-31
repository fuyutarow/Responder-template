import pandas as pd

# comment out if `pi run manage shell < myscript.py``
# from api.models import Dodoit
# global Dodoit

text_list = pd.read_csv('test_dodoits.csv', header=None)[0]

dodoits = [Dodoit(content=text) for text in text_list]

Dodoit.objects.bulk_create(dodoits)
