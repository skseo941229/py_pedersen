import requests
import json

url = "http://0.0.0.0:8001"

headers = {
    'Content-Type':'application/json',
}

if __name__ == "__main__":
    print("----------Menu----------")
    print("1: Get commitment value")
    print("2: Get h, r, v") 
    print("3: Exit the ")
    print("------------------------") 
    
    while True:
        menu = input("Type the menu number you want: ")
        if menu == "3":
            break      
        if menu == "1": 
            value = input("Type the value you want to hide")
            data = requests.post(url+"/commitment", data=json.dumps({'value':value}), headers=headers).json()
            print(data)
        elif menu == "2":
            data = requests.get(url+"/opening").json()
            print(data)
        