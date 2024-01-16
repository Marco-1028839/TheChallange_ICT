import requests
import json
url = "http://127.0.0.1:5000"



# ----------------------- Kluis -----------------------
headers = {
    'Content-Type': 'application/json'
}


response = requests.get(f"{url}/kluis/", headers=headers)
print(response.json())



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


"""
headers = {
    'Content-Type': 'application/json'
}


for kluis_id in range(25):
    data = {
    'code': f"001-{kluis_id}-001",
    'adres_id': 0,
    'gebruiker_id': 0,
    'status': 0,
    'pakket_id': 0
}
    response = requests.put(f"{url}/kluis/{kluis_id}", data=json.dumps(data), headers=headers)
    print(response.json())

#PUT code -----------------------

# ----------------------- kluis_adres -----------------------


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