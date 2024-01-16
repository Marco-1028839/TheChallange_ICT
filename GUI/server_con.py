import requests
import json
import random

from  config import *



class kluis_api_connectie:
    headers = {'Content-Type': 'application/json'}


    def __init__(self) -> None:
        pass

    def get_all_kluizen(self):
        pass

    def get_specific_kluis(self,kluis_id):
        response = requests.get(f"{URL}/kluis/{kluis_id}", headers=self.headers)
        return response.json()
    


