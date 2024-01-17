import requests
import json
import random

URL = "http://127.0.0.1:5000"

class email_api_connectie:
    headers = {'Content-Type': 'application/json'}

    def __init__(self) -> None:
        pass

    def get_all_emails(self):
        pass

    def get_specific_email(self,email_id):
        response = requests.get(f"{URL}/emails/{email_id}", headers=self.headers)
        return response.json()
    
    def make_email(self,email_id,reciever,title,body,date):
        data = {
            "reciever": reciever,
            "title": title,
            "body": body,
            "date": date
        }
        response = requests.post(f"{URL}/emails/{email_id}", headers=self.headers, data=json.dumps(data))
        return response.json()
    
    def delete_email(self,email_id):
        response = requests.delete(f"{URL}/emails/{email_id}", headers=self.headers)
        return response.json()
    
class kluis_api_connectie:
    headers = {'Content-Type': 'application/json'}


    def __init__(self) -> None:
        pass

    def get_all_kluizen(self):
        response = requests.get(f"{URL}/kluis", headers=self.headers)
        return response.json()

    def get_specific_kluis(self,kluis_id):
        response = requests.get(f"{URL}/kluis/{kluis_id}", headers=self.headers)
        return response.json()
    
    def make_kluis(self,kluis_id,code,adres_id,gebruiker_id,status,pakket_id):
        data = {
            "code": code,
            "adres_id": adres_id,
            "gebruiker_id": gebruiker_id,
            "status": status,
            "pakket_id": pakket_id
        }
        response = requests.post(f"{URL}/kluis/{kluis_id}", headers=self.headers, data=json.dumps(data))
        return response.json()
    
    def change_status(self,kluis_id,status):
        data = {
            "status": status
        }
        response = requests.patch(f"{URL}/kluis/{kluis_id}", headers=self.headers, data=json.dumps(data))
        return response.json()
    
    def change_code(self,kluis_id,code):
        data = {
            "code": code
        }
        response = requests.patch(f"{URL}/kluis/{kluis_id}", headers=self.headers, data=json.dumps(data))
        return response.json()


