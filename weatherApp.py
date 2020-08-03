try:
  from tkinter import *
  import requests
except Exception as e:
  print('Modules are Missing! \n\n {}'.format(e))

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		output = 'City: %s\n Conditions: %s\n Temperature (°F): %s' % (name, desc, temp)
	except:
		output = 'There was a problem retrieving information!'

	return output

def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()
	label['text'] = format_response(weather)

root = Tk()
canvas = Canvas(root, height=500, width=600)
canvas.pack()

background_image = PhotoImage(file='./img/landscape.png')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()