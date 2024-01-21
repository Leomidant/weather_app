from tkinter import * 
import tkinter as tk
from tkinter import ttk, messagebox
from urllib import request
import requests
from datetime import datetime, timedelta
from PIL import Image, ImageTk
from io import BytesIO
import atexit
import os
import shutil

root=Tk()
root. title("Weather App")
root. geometry ("890x470+300+200")
root. configure(bg="#57adff")
root. resizable(False,False)
folder_to_clean = "icon_temp"
os.makedirs(folder_to_clean, exist_ok=True)
def cleanup_icon_temp():
    try:
        # Delete the folder and its contents
        shutil.rmtree(folder_to_clean)
    except OSError as e:
        print(f"Error: {e}")

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        return Image.open(image_data)
    else:
        return None

def download_all_images(json_data):
    for i in range(0,7):
        image_url = "https:" + str(json_data['forecast']['forecastday'][i]['day']['condition']['icon'])
        image = download_image(image_url)
        if image:
        # Process the image as needed, for example, save it to a file or display it
            image.save("icon_temp/"+ str(i+1) +".png")
        else:
            print(f"Failed to download image from {image_url}")

def getWeather():
    
    cityName = textfield.get()
    url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        'key': '66eb9a168e7d4b07ba1234657241901',
        'q': cityName,
        'days': 7
    }

    json_data = requests.get(url, params=params).json()

    temp = json_data['current']['temp_c']
    humidity = json_data['current'][ 'humidity']
    pressure = json_data['current']['pressure_in']
    wind = json_data['current']['wind_kph']
    description = json_data['current']['condition']['text']
    region = json_data['location']['region']
    country = json_data['location'][ 'country']
    localtime = json_data['location']['localtime']
    tz_id = json_data['location']['tz_id']
    lon = json_data['location']['lon']
    lat = json_data['location']['lat']
    current_max_temp = json_data['forecast']['forecastday'][0]['day']['maxtemp_c']
    current_min_temp = json_data['forecast']['forecastday'][0]['day']['mintemp_c']

    currentMaxMinTempString = "Max Temp: " + str(current_max_temp) + "\n" + "Min Temp: " + str(current_min_temp)
    

    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s") )
    d.config(text=description)
    clock.config(text=localtime)
    timezone.config(text=tz_id)
    long_lat.config(text="Longtitude: " + str(lon) + "\n" + "Latitude: " + str(lat))

    download_all_images(json_data)
    first = datetime.now()
    day1.config(text=first.strftime("%A")[:3], fg='white')
    photo1 = ImageTk.PhotoImage(file="./icon_temp/1.png")
    firstImage.config(image=photo1)
    firstImage.image=photo1
    day1MaxMinTemp.config(text=currentMaxMinTempString)

    second = first + timedelta(days=1)
    day2.config(text=second.strftime("%A")[:3], fg='white')
    photo2 = ImageTk.PhotoImage(file="./icon_temp/2.png")
    secondImage.config(image=photo2)
    secondImage.image=photo2

    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A")[:3], fg='white')
    photo3 = ImageTk.PhotoImage(file="./icon_temp/3.png")
    thirdImage.config(image=photo3)
    thirdImage.image=photo3

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A")[:3], fg='white')
    photo4 = ImageTk.PhotoImage(file="./icon_temp/4.png")
    fourthImage.config(image=photo4)
    fourthImage.image=photo4

    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A")[:3], fg='white')
    photo5 = ImageTk.PhotoImage(file="./icon_temp/5.png")
    fifthImage.config(image=photo5)
    fifthImage.image=photo5

    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A")[:3], fg='white')
    photo6 = ImageTk.PhotoImage(file="./icon_temp/6.png")
    sixthImage.config(image=photo6)
    sixthImage.image=photo6

    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime("%A")[:3], fg='white')
    photo7 = ImageTk.PhotoImage(file="./icon_temp/7.png")
    seventhImage.config(image=photo7)
    seventhImage.image=photo7



image_icon=PhotoImage(file="Images/logo.png")
root. iconphoto (False, image_icon)
Round_box=PhotoImage(file="Images/round1.png")
Label(root, image=Round_box, bg="#57adff").place(x=40,y=110)


label1=Label(root, text="Temperature",font=('Helvetica' ,11),fg="white",bg="#203243")
label1. place (x=50,y=120)
label2=Label(root, text="Humitidy",font=('Helvetica' ,11),fg="white",bg="#203243")
label2. place (x=50,y=140)
label3=Label(root, text="Pressure",font=('Helvetica' ,11),fg="white",bg="#203243")
label3. place (x=50,y=160)
label4=Label(root, text="Wind Speed",font=('Helvetica' ,11),fg="white",bg="#203243")
label4. place (x=50,y=180)
label5=Label(root, text="Description",font=('Helvetica' ,11),fg="white",bg="#203243")
label5. place (x=50,y=200)


temp_icon=PhotoImage(file="Images/temp.png")
Label(root, image=temp_icon, bg="SystemTransparent").place(x=290,y=122)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

search_icon=PhotoImage(file="Images/searchbox.png")
search_icon1=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="SystemTransparent",command=getWeather)
search_icon1.place(x=645,y=122)






frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)


mainbox=PhotoImage(file="Images/round1.png")


#Forecast Days
firstFrame = Frame(root,width=230, height=132, bg='#212120')
firstFrame.place(x=35,y=325)
day1 = Label(firstFrame, font="arial 20", bg="#212120", fg="#fff")
day1.place(x=100, y=5)
firstImage = Label(firstFrame, bg="#212120")
firstImage.place(x=1, y=40)
day1MaxMinTemp = Label(firstFrame, font="arial 20", bg="#212120", fg="white")
day1MaxMinTemp.place(x=70, y=45)


secondFrame = Frame(root,width=70, height=115,bg='#212120')
secondFrame.place(x=305,y=325)
day2 = Label(secondFrame, font="arial 20", bg="#212120", fg="white")
day2.place(x=10, y=5)
secondImage = Label(secondFrame, bg="#212120")
secondImage.place(x=0,y=40)


thirdFrame = Frame(root,width=70, height=115,bg='#212120')
thirdFrame.place(x=405,y=325)
day3 = Label(thirdFrame, font="arial 20", bg="#212120", fg="#fff")
day3.place(x=10, y=5)
thirdImage = Label(thirdFrame, bg="#212120")
thirdImage.place(x=0,y=40)

fourthFrame = Frame(root,width=70, height=115, bg="#212120")
fourthFrame.place(x=505,y=325)
day4 = Label(fourthFrame, font="arial 20", bg="#212120", fg="#fff")
day4.place(x=10, y=5)
fourthImage = Label(fourthFrame, bg="#212120")
fourthImage.place(x=0,y=40)

fifthFrame = Frame(root,width=70, height=115, bg="#212120")
fifthFrame.place(x=605,y=325)
day5 = Label(fifthFrame, font="arial 20", bg="#212120", fg="#fff")
day5.place(x=10, y=5)
fifthImage = Label(fifthFrame, bg="#212120")
fifthImage.place(x=0,y=40)

sixthFrame = Frame(root,width=70, height=115, bg="#212120")
sixthFrame.place(x=705,y=325)
day6 = Label(sixthFrame, font="arial 20", bg="#212120", fg="#fff")
day6.place(x=10, y=5)
sixthImage = Label(sixthFrame, bg="#212120")
sixthImage.place(x=0,y=40)

seventhFrame = Frame(root,width=70, height=115, bg="#212120")
seventhFrame.place(x=805,y=325)
day7 = Label(seventhFrame, font="arial 20", bg="#212120", fg="#fff")
day7.place(x=10, y=5)
seventhImage = Label(seventhFrame, bg="#212120")
seventhImage.place(x=0,y=40)




#clock (here we will place time)
clock=Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#57adff")
clock. place (x=30,y=20)

#timezone
timezone=Label (root, font=("Helvetica", 20), fg="white",bg="#57adff")
timezone. place (x=700,y=20)
long_lat=Label (root, font=("Helvetica",10), fg="white",bg="#57adff")
long_lat. place(x=700,y=50)

#thpwd
t=Label (root, font=("Helvetica",11),fg="white",bg="#203243")
t. place (x=150,y=120)
h=Label (root, font=("Helvetica",11),fg="white", bg="#203243")
h. place (x=150,y=140)
p=Label (root, font=("Helvetica", 11), fg="white", bg="#203243")
p. place (x=150,y=160)
w=Label (root, font=("Helvetica",11), fg="white",bg="#203243")
w. place (x=150,y=180)
d=Label (root, font=("Helvetica", 11),fg="white",bg="#203243")
d.place(x=150,y=200)



atexit.register(cleanup_icon_temp)



root.mainloop()
