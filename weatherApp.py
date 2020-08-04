try: # checking if the modules are installed
  from tkinter import *
  import requests

except Exception as e: # printing a message if there is an issue with the packages
  print('Modules are Missing! \n\n {}'.format(e))

def get_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
		output = 'City: %s\n Conditions: %s\n Temperature (°F): %s' % (name, desc, temp)
	except:
		output = 'Having a problem retrieving information!'

	return output

def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()
	label['text'] = get_response(weather)

app = Tk() # creating the app! 
canvas = Canvas(app, height=500, width=600) # creating a canvas!
canvas.pack() # making it to fillout

background_image = PhotoImage(file='./img/landscape.png') # setting bg image!
background_label = Label(app, image=background_image) # labling the image!
background_label.place(relwidth=1, relheight=1) # placing that label

frame = Frame(app, bg='#80c1ff', bd=5) # initial new frame!
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n') # placing the frame!

entry = Entry(frame, font=40) # creating the entry(typing bar)
entry.place(relwidth=0.65, relheight=1) # placing that entry!

button = Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get())) # creating button!
button.place(relx=0.7, relheight=1, relwidth=0.3) # placing the button!

second_frame = Frame(app, bg='#80c1ff', bd=10) # making another new frame!
second_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n') #placing the new frame!

label = Label(second_frame) # labling the second frame!
label.place(relwidth=1, relheight=1) #placing the frame!

app.mainloop() # runing the app!