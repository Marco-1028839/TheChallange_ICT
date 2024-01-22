import requests
import json
import random

from  config import *

class personen_api_connectie:
    headers = {'Content-Type': 'application/json'}

    def __init__(self) -> None:
        pass
        
    def get_all_persons(self):
        response = requests.get(f"{URL}/gebruiker", headers=self.headers)
        return response.json()
    
    def get_specific_person(self,person_id):
        response = requests.get(f"{URL}/gebruiker/{person_id}", headers=self.headers)
        return response.json()
    
    def make_person(self,person_id,username,email,telefoon):
        data = {
            "id": person_id,
            "username": username,
            "email": email,
            "telefoon": telefoon
        }
        response = requests.put(f"{URL}/gebruiker/{person_id}", headers=self.headers, data=json.dumps(data))
        return response.json()
    
    def delete_person(self,person_id):
        response = requests.delete(f"{URL}/gebruiker/{person_id}", headers=self.headers)
        return response.json()

class email_api_connectie:
    headers = {'Content-Type': 'application/json'}

    def __init__(self) -> None:
        pass

    def get_all_emails(self):
        response = requests.get(f"{URL}/emails", headers=self.headers)
        return response.json()

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
        response = requests.put(f"{URL}/emails/{email_id}", headers=self.headers, data=json.dumps(data))
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
        response = requests.put(f"{URL}/kluis/{kluis_id}", headers=self.headers, data=json.dumps(data))
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

# testing
"""
person = personen_api_connectie()
print("Done with person")
for id in range(10):
    print(f"{id}")
    response = person.make_person(id,f"test{id}",f"John@doe{str(id)}.nl",f"061234567{id}")
    print(response)




email = email_api_connectie()
print("done with email")
for id in range(10):
    print(f"{id}")
    response = email.make_email(id,"john@doe.com","test","f f f f f ff d asfdasfas asf sad","17-1-2024")
    print(response)



kluis = kluis_api_connectie()
for id in range(25):
    if id < 10: 
        response = kluis.make_kluis(id, f"00{id}-00{id}-001", 0, 0, 0, 0)
        print(response)
    else:
        response = kluis.make_kluis(id, f"0{id}-0{id}-001", 0, 0, 0, 0)
        print(response)
"""