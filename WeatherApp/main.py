from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        
        home = pytz.timezone(result) 
        Label(root, text=home, font="arial 24").place(x=500, y=20)
        Label(root, text=f"{round(location.latitude, 4)}°, {round(location.longitude, 4)}°", font="arial 14").place(x=510, y=60)
        local_time = datetime.now()
        current = local_time.strftime("%I:%M %p")
        clock.config(text=current)
        name.config(text="CURRENT WEATHER")
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a0f0adeafb53c3f3217338a506f7fd43"
        
        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        pressure = json_data["main"]["pressure"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"] - 273.15)
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        t.config(text=(temp,  "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))
        
        d.config(text=description)
        w.config(text=wind)
        h.config(text=humidity)
        p.config(text=pressure)

    except Exception:
        messagebox.showerror("Weather App", "Invalid City/Province")

root = Tk()
root.title("Weather App")
root.geometry("900x500") 
root.resizable(0, 0)

icon = PhotoImage(file="CodeChoi/WeatherApp/logo.png")
root.iconphoto(False, icon)

search_img = PhotoImage(file="CodeChoi/WeatherApp/Rounded Rectangle 3.png")
my_img = Label(image=search_img)
my_img.place(x=40, y=20)


textfield = Entry(root, justify=CENTER, width=15, font=("poppins", 25, "bold"), bg="#203243", border=0, fg="white")
textfield.place(x=110, y=30)
textfield.focus()

search_ico = PhotoImage(file="CodeChoi/WeatherApp/Layer 6.png")
myimg_ico = Button(image=search_ico, bd=0, cursor="hand2", bg="#203243", command=getWeather)
myimg_ico.place(x=417, y=24)

Label(image=icon).place(x=150, y=100)

lgfr = PhotoImage(file="CodeChoi/WeatherApp/Copy of Box.png")
frame = Label(image=lgfr)
frame.pack(padx=5, pady=5, side=BOTTOM)

Label(root, text="WIND", font="Helvetica 15 bold", fg="white", bg="#1ab5ef").place(x=120, y=400)
Label(root, text="HUMIDITY", font="Helvetica 15 bold", fg="white", bg="#1ab5ef").place(x=245, y=400) # add 20
Label(root, text="DESCRIPTION", font="Helvetica 15 bold", fg="white", bg="#1ab5ef").place(x=430, y=400)
Label(root, text="PRESSURE", font="Helvetica 15 bold", fg="white", bg="#1ab5ef").place(x=650, y=400)

t = Label(font="arial 70 bold", fg="#ee666d")
t.place(x=400, y=150)
c = Label(font="arial 15 bold")
c.place(x=400, y=250)

w = Label(text="...", font="arial 20 bold", bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font="arial 20 bold", bg="#1ab5ef")
h.place(x=278, y=430)
d = Label(text="...", font="arial 20 bold", bg="#1ab5ef")
d.place(x=440, y=430)
p = Label(text="...", font="arial 20 bold", bg="#1ab5ef")
p.place(x=675, y=430)

name = Label(root, font="arial 15 bold")
name.place(x=30, y=100)
clock = Label(root, font="helvetica 20")
clock.place(x=30, y=130)

root.mainloop()