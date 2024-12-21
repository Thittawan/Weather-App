import requests
from tkinter import *
from PIL import ImageTk, Image
import time
from datetime import date
root = Tk()
root.title('Weather app')
root.configure(bg='lightblue')
img=PhotoImage(file='C:Background\Images\weather-forecast.png')
root.iconphoto(False, img)
#API key
api_key = '23529f6c1d359e09fd4a1905a91b4ed7'


#Function after press enter
def show_weather(event):

   #Put a layer box on top so the new and old don't overlap
   my_img = Image.open('C:Background\Images\Rounded Rectangle 1.png')
   resized_image = my_img.resize((300, 200))
   img = ImageTk.PhotoImage(resized_image)
   label1 = Label(image=img, bg='lightblue')
   label1.image = img
   label1.place(x=30, y=90)

   y = txt.get()
   url = f'https://api.openweathermap.org/data/2.5/weather?q={y}&appid={api_key}&units=metric'
   final = requests.get(url).json()

   weather = final['weather'][0]['main']
   description = final['weather'][0]['description']
   temp = final['main']['temp']
   feel_like = final['main']['feels_like']
   pressure = final['main']['pressure']
   humidity = final['main']['humidity']
   icon = final['weather'][0]['icon']
   time = final['dt']

   Label(root, text=f'Weather: {weather}', fg='White', font=('Times New Roman', 15), background='#203243').place(x=40, y=100)
   Label(root, text=f'Description: {description}', fg='White', font=('Times New Roman', 15), background='#203243').place(x=40, y=130)
   Label(root, text=f'Temperature: {temp} °C', fg='White', font=('Times New Roman', 15), background='#203243').place(x=40, y=160)
   Label(root, text=f'Feel Like: {feel_like} °C', fg='White', font=('Times New Roman', 15), background='#203243').place(x=40, y=190)
   Label(root, text=f'Pressure: {pressure} Pa', fg='White', font=('Times New Roman', 15), background='#203243').place(x=40, y=220)
   Label(root, text=f'Humidity: {humidity}%', fg='White', font=('Times New Roman', 15), background='#203243').place(x=40, y=250)

   #Change icon
   my_img = Image.open(f'C:weather icon/{icon}@2x.png')
   resized_image = my_img.resize((200, 200))
   img = ImageTk.PhotoImage(resized_image)
   label1 = Label(image=img, bg='lightblue')
   label1.image = img
   label1.place(x=390, y=70)

   hour(y)
   '''
   long = final['coord']['lon']
   lat = final['coord']['lat']
   tf = timezonefinder.TimezoneFinder()
   timezone_str = tf.certain_timezone_at(lat=lat, lng=-long)
   timezone = pytz.timezone(timezone_str)
   dt = datetime.datetime.utcnow()
   x = "%s is %s" % (timezone_str, dt + timezone.utcoffset(dt))
   x = x.split()
   
   Label(root, text=f'{x[3]}', fg='White', font=('Times New Roman', 50), background='lightblue').place(x=640, y=100)
   Label(root, text=f'{x[2]}', fg='White', font=('Times New Roman', 20), background='lightblue').place(x=630, y=170)
   '''
def hour(n):

   url = f'https://api.openweathermap.org/data/2.5/forecast?q={n}&appid={api_key}&units=metric&cnt=7'

   now = requests.get(url).json()

   temp = []
   feel = []
   for i in range(7):
      x = now['list'][i]['main']
      for i in x:
         if i == 'temp':
            temp.append(x[i])
         elif i == 'feels_like':
            feel.append(x[i])
   des = []
   icon = []
   for i in range(7):
      x = now['list'][i]['weather']
      for i in x:
         for j in i:
            if j == 'description':
               des.append(i[j])
            elif j == 'icon':
               icon.append(i[j])
   x = 0
   for i in range(4):
      my_img = Image.open(f'C:weather icon/{icon[i]}@2x.png')
      resized_image = my_img.resize((90, 90))
      img = ImageTk.PhotoImage(resized_image)
      label1 = Label(image=img, bg='#212120')
      label1.image = img
      label1.place(x=8 + x, y=315)

      Label(root, text=f'Description:\n{des[i]}        ', fg='White', font=('Times New Roman', 9),background='#212120').place(x=5 + x, y=410)
      Label(root, text=f'Temperature:{temp[i]} ', fg='White', font=('Times New Roman', 9), background='#212120').place(x=5 + x,y=445)
      Label(root, text=f'Feel Like:{feel[i]} ', fg='White', font=('Times New Roman', 9), background='#212120').place(x=7 + x,y=470)

      x += 125
   for i in range(4, 7):
      my_img = Image.open(f'C:weather icon/{icon[i]}@2x.png')
      resized_image = my_img.resize((90, 90))
      img = ImageTk.PhotoImage(resized_image)
      label1 = Label(image=img, bg='#212120')
      label1.image = img
      label1.place(x=x, y=315)

      Label(root, text=f'Description:\n{des[i]}             ', fg='White', font=('Times New Roman', 9),background='#212120').place(x=x, y=410)
      Label(root, text=f'Temperature:{temp[i]} ', fg='White', font=('Times New Roman', 9), background='#212120').place(x=x,y=445)
      Label(root, text=f'Feel Like:{feel[i]} ', fg='White', font=('Times New Roman', 9), background='#212120').place(x=x,y=470)

      x += 125
      label1.lift()
      label2.lift()
      label3.lift()
      label4.lift()
      label5.lift()
      label6.lift()
      Label(root, text='+3 hour', fg='White', font=('Times New Roman', 17), background='#212120').place(x=20, y=299.5)
      Label(root, text='+6 hour', fg='White', font=('Times New Roman', 17), background='#212120').place(x=145, y=299.5)
      Label(root, text='+9 hour', fg='White', font=('Times New Roman', 17), background='#212120').place(x=270, y=299.5)
      Label(root, text='+12 hour', fg='White', font=('Times New Roman', 17), background='#212120').place(x=385, y=299.5)
      Label(root, text='+15 hour', fg='White', font=('Times New Roman', 17), background='#212120').place(x=500, y=299.5)
      Label(root, text='+18 hour', fg='White', font=('Times New Roman', 17), background='#212120').place(x=615, y=299.5)
      Label(root, text='+21 hour', fg='White', font=('Times New Roman', 17), background='#212120').place(x=740, y=299.5)

#Bind enter
root.bind('<Return>', show_weather)

#Bottom box
frame = Frame(root, width=900, height=200, bg='#212120').pack(side=BOTTOM)

#Box display current weather
my_img = Image.open('C:Background\Images\Rounded Rectangle 1.png')
resized_image = my_img.resize((300,200))
img = ImageTk.PhotoImage(resized_image)
label1 = Label(image=img, bg='lightblue')
label1.image = img
label1.place(x=30, y=90)

#Search box
my_img = Image.open('C:Background\Images\Rounded Rectangle 3.png')
resized_image = my_img.resize((300,50))
img = ImageTk.PhotoImage(resized_image)
label1 = Label(image=img, bg='lightblue')
label1.image = img
label1.place(x=30, y=20)

#Textbox
txt = StringVar()
box = Entry(root,justify='center',textvariable=txt, bg='#203243', border=0, fg='white', font=('Times New Roman', 20)).place(x=58, y=24, width=220, height=45)

#Search botton
my_img = Image.open('C:Background\Images\Layer 6.png')
resized_image = my_img.resize((35,35))
img = ImageTk.PhotoImage(resized_image)
label1 = Label(image=img, bg='#203243')
label1.image = img
label1.place(x=280, y=25)

#Current weather icon
my_img = Image.open('C:pic/01d.png')
resized_image = my_img.resize((200,200))
img = ImageTk.PhotoImage(resized_image)
label1 = Label(image=img, bg='lightblue')
label1.image = img
label1.place(x=390, y=70)

#3 hour weather diplay
my_img = Image.open('C:Background\Images\white-line.png')
resized_image = my_img.resize((10,210))
img = ImageTk.PhotoImage(resized_image)
label1 = Label(image=img, bg='#212120')
label1.image = img
label1.place(x=120, y=299.5)
label1.lift()

my_img = Image.open('C:Background\Images\white-line.png')
resized_image = my_img.resize((10,210))
img = ImageTk.PhotoImage(resized_image)
label2 = Label(image=img, bg='#212120')
label2.image = img
label2.place(x=240, y=299.5)
label2.lift()

my_img = Image.open('C:Background\Images\white-line.png')
resized_image = my_img.resize((10,210))
img = ImageTk.PhotoImage(resized_image)
label3 = Label(image=img, bg='#212120')
label3.image = img
label3.place(x=360, y=299.5)
label3.lift()

my_img = Image.open('C:Background\Images\white-line.png')
resized_image = my_img.resize((10,210))
img = ImageTk.PhotoImage(resized_image)
label4 = Label(image=img, bg='#212120')
label4.image = img
label4.place(x=480, y=299.5)
label4.lift()

my_img = Image.open('C:Background\Images\white-line.png')
resized_image = my_img.resize((10,210))
img = ImageTk.PhotoImage(resized_image)
label5 = Label(image=img, bg='#212120')
label5.image = img
label5.place(x=600, y=299.5)
label5.lift()

my_img = Image.open('C:Background\Images\white-line.png')
resized_image = my_img.resize((10,210))
img = ImageTk.PhotoImage(resized_image)
label6 = Label(image=img, bg='#212120')
label6.image = img
label6.place(x=720, y=299.5)
label6.lift()
#Time
x = time.localtime()
current_time = time.strftime("%H:%M", x)
my_time = Label(root, text=f'{current_time}', fg='White', font=('Times New Roman', 50), background='lightblue').place(x=640, y=100)
#Date
today = date.today()
my_date = Label(root, text=f'{today}', fg='White', font=('Times New Roman', 20), background='lightblue').place(x=655, y=170)


#+3 hrs
three = Label(root, text='+3 hour', fg='White', font=('Times New Roman', 17), background='#212120').place(x=20, y=299.5)
six = Label(root, text='+6 hour', fg='White', font=('Times New Roman', 17), background='#212120').place(x=145, y=299.5)
nine = Label(root, text='+9 hour', fg='White', font=('Times New Roman', 17), background='#212120').place(x=270, y=299.5)
tw = Label(root, text='+12 hour', fg='White', font=('Times New Roman', 17), background='#212120').place(x=385, y=299.5)
fif = Label(root, text='+15 hour', fg='White', font=('Times New Roman', 17), background='#212120').place(x=500, y=299.5)
eightt = Label(root, text='+18 hour', fg='White', font=('Times New Roman', 17), background='#212120').place(x=615, y=299.5)
twone = Label(root, text='+21 hour', fg='White', font=('Times New Roman', 17), background='#212120').place(x=740, y=299.5)

#App size
root.geometry('850x500+450+150') #600x500 is size (+450+150 is where the app appear on screen)
root.mainloop()