# Add your computer Python code here.
import requests
import time
import serial
ser = serial.Serial('/dev/ttyACM0',115200)
site="things.ubidots.com"
device="microbit"
variable_t="temperature"
variable_l="light"
token="<token> "
def post(outPut,url=site,device=device,token=token):
    try:
        url = "http://{}/api/v1.6/devices/{}".format(url, device)
        headers = {"X-Auth-Token": token, "Content-Type": "application/json"}
        a=0
        status_code=400
        while status_code>=400 and a<5:
            request=requests.post(url=url,headers=headers,json=outPut)
            status_code=request.status_code
            a +=1
        
    except Exception as e:
        print(request.status_code)
        print("[ERROR] Error posting, details: {}".format(e))
x = ser.readline()

while True:
    x = ser.readline()
    
    x=str(x)
    x=x.split(" ")
    light_level=x[1]
    
    x[0]=x[0].split("'")
    x[0]=x[0][1]
    temp=x[0]
    temp={"temperature":temp}
    post(temp)
    light={"light":light_level}
    post(light)
    time.sleep(30)
    

