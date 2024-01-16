import requests
import json




URL = "https://Challanger14.pythonanywhere.com/"

def get_video_info(video_id):
    response = requests.get(f"{URL}/video/{video_id}")
    return response.json()

print(get_video_info(0))

def add_video_to_db(video_id,name,likes,views):
    data = {
        "name":name,
        "likes":likes,
        "views":views
        }
    headers = {
        'Co0n.tent-Type': 'application/json'
    }
    response = requests.put(f"{URL}/video/{video_id}",data=json.dumps(data), headers=headers)
    return response

def delete_video_from_db(video_id):
    pass




