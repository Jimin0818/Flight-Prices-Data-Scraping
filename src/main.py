import tkinter as tk
from tkinter import messagebox
from flask import Flask, render_template
import requests
import json
from time import strftime

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)


def my_time():
  time_string = strftime('%x')
  time1_str.set(time_string)


def search_flights():
  fromDest = fromDest_entry.get()
  toDest = toDest_entry.get()
  flightDate = flightDate_entry.get()

  #if not fromDestination or not toDestination or not dateDep:
  #messagebox.showwarning("Input Error", "Please fill in all fields")
  #return

  try:
    response = requests.post('http://localhost:5000/search',
                             json={
                                 'fromDest': fromDest,
                                 'toDest': toDest,
                                 'flightDate': flightDate
                             })
    flights = response.json()
    display_flights(flights)
  except Exception as e:
    messagebox.showerror("Error", f"Failed to retrieve")


def display_flights(flights):
  Lb.delete(1, tk.END)
  for flight in flights:
    Lb.insert(tk.END,
              f"Flight: {flight['flight']}, Price: {flight['price']}\n")


app = tk.Tk()
#Title of the Website
app.title("Flight Data Scraper")

#Background Color
app.geometry("400x300")
canvas = tk.Frame(app, bg='powderblue')
canvas.place(relwidth=1, relheight=1)

#From and To Destination Location and Entry
tk.Label(app, text='From Destination', font='BodoniMTBlack',
         bg='powderblue').grid(row=2, column=0)
tk.Label(app, text='To Destination', font='BodoniMTBlack',
         bg='powderblue').grid(row=2, column=1)
fromDest_entry = tk.Entry(app, bd='4')
toDest_entry = tk.Entry(app, bd='4')
fromDest_entry.grid(row=3, column=0)
toDest_entry.grid(row=3, column=1)

#Flight Date Location and Entry
tk.Label(app,
         text='Flight Date',
         font='BodoniMTBlack',
         bg='powderblue',
         bd='4').grid(row=2, column=2)
flightDate_entry = tk.Entry(app, bd='4')
flightDate_entry.grid(row=3, column=2)

#Displays Current Date and Time
tk.Label(app, text='Current Date', font='BodoniMTBlack',
         bg='powderblue').grid(row=0, column=1)
time1_str = tk.StringVar()
my_font = ('boldfont', 35)
time1 = tk.Label(app,
                 textvariable=time1_str,
                 font=my_font,
                 bg='powderblue',
                 fg='red')
time1.grid(row=1, column=1)
my_time()

#Search Button/ Enter Button
search_button = tk.Button(app,
                          bg='gold',
                          text="Search Flights",
                          command=search_flights,
                          font='BodoniMTBlack',
                          bd='4')
search_button.grid(row=4, column=1)

#Results
Lb = tk.Listbox(app, height=45, width=100, bd=4)
Lb.insert(1, '1jlhdasbflikjabkjldsnbN;OIUJSD')
Lb.insert(2, '2')
Lb.insert(3, '3')
Lb.insert(4, '4')
Lb.insert(5, '5')
Lb.grid(row=5, column=0, columnspan=3)

app.mainloop()
