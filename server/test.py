import requests
import json
import random
url = "https://challanger14.pythonanywhere.com/"



data = {
    'name': "MR.Polo",
    'password': "Pinda2003!",
    'admin': True
}
headers = {
    'Content-Type': 'application/json'
}
response = requests.put(f"{url}/Paard/0",data=json.dumps(data), headers=headers)
print(response.json())

# ----------------------- Kluis -----------------------

data = {
    'code': f"001-{random.randint(200000000,500000000)}-001",
    'adres_id': 0,
    'gebruiker_id': 0,
    'status': 0,
    'pakket_id': 0
}

headers = {
    'Content-Type': 'application/json'
}
kluis_id = random.randint(200000000,500000000)


# GET code -----------------------
response = requests.get(f"{url}/kluis/4", headers=headers)
print("Get")
print(response.json())

#PUT code -----------------------
response = requests.put(f"{url}/kluis/{kluis_id}", data=json.dumps(data), headers=headers)
print("Put")
print(response.json())

#PATCH code -----------------------
data = {
    'code': f'{random.randint(9999999999999999,999999999999999999999)}'
}
response = requests.patch(f"{url}/kluis/4", data=json.dumps(data), headers=headers)
print("Patch")
print(response.json())

# DELETE code -----------------------
kluis_id = 1
response = requests.delete(f"{url}/kluis/{kluis_id}", headers=headers)
print("Delete")
print(response.json())


"""
# ----------------------- kluis_adres -----------------------
data = {
    'kluis_id': 1,
    'postcode': "2902xb",
    'street': "lullenstraat",
    'huisnummer': 75
}

headers = {
    'Content-Type': 'application/json'
}
kluis_adres_id = 0
response = requests.put(f"{url}/kluis_adres/{kluis_adres_id}", data=json.dumps(data), headers=headers)
print(response.json())

# ----------------------- gebruiker -----------------------
data = {
    'username': "PVVGaming",
    'email': "test@test.nl",
    'telefoon': "0102270351"
}

headers = {
    'Content-Type': 'application/json'
}
gebruiker_id = 0
response = requests.put(f"{url}/gebruiker/{gebruiker_id}", data=json.dumps(data), headers=headers)
print(response.json())

# ----------------------- pakket -----------------------

data = {
    'naam': "test pakket",
    'inhoud': "pindakaas, brood, je vader, melk",
    'houdbaarheid': "20-2-2024, Je vader kom niet meer terug"
}

headers = {
    'Content-Type': 'application/json'
}
pakket_id = 0
response = requests.put(f"{url}/pakket/{pakket_id}", data=json.dumps(data), headers=headers)
print(response.json())

"""