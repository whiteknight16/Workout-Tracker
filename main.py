
import requests
import datetime
import os

APPLICATION_ID=(os.environ["APPLICATION_ID"])
APPLICATION_KEY=(os.environ["APPLICATION_KEY"])


NUTRITIONIX_END_POINT="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT=(os.environ["SHEETY_ENDPOINT"])


obj=datetime.datetime.now()
date=obj.strftime("%d/%m/%Y")
time=obj.strftime("%H:%M:%S")

header_file={
    "x-app-id":APPLICATION_ID,
    "x-app-key":APPLICATION_KEY,
    "Content-Type":"application/json"
}

user_exercise=input("Enter the exercises you did: ")

post_parameters={
    "query":user_exercise,
}
data_post=requests.post(NUTRITIONIX_END_POINT,json=post_parameters,headers=header_file)
data_obj=data_post.json()

sheety_header={
    "Content-Type":"application/json",
    "Authorization":os.environ["Authorization"]
}
for i in range(len(data_obj["exercises"])):
    exercise_data={
        "sheet1":{
            "date":date,
            "time":time,
            "exercise":data_obj["exercises"][i]["name"].title(),
            "duration":data_obj["exercises"][i]["duration_min"],
            "calories":data_obj["exercises"][i]["nf_calories"]
        }
    }
    posting=requests.post(SHEETY_ENDPOINT,json=exercise_data,headers=sheety_header)
    print(posting.status_code)