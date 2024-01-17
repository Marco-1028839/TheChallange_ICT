import requests
import json
import server_con_test as server_con

URL = "http://127.0.0.1:5000"



email = server_con.email_api_connectie()
for id in range(10):
    response = email.make_email(id,"john@doe.com","test","f f f f f ff d asfdasfas asf sad","17-1-2024")
    print(response.json())

kluis = server_con.kluis_api_connectie()
for id in range(25):
    if id < 10: 
        response = kluis.make_kluis(id, f"001-00{id}-001", 0, 0, 0, 0)
        print(response.json())
    else:
        response = kluis.make_kluis(id, f"001-0{id}-001", 0, 0, 0, 0)
        print(response.json())
