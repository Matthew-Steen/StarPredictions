from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import pandas as pd
import math

import pickle

with open("pickle_model_numPlanets.pkl", 'rb') as file1:
   pickle_model1 = pickle.load(file1, encoding='ISO-8859-1')

with open("pickle_model_PlanetRadius.pkl", 'rb') as file2:
   pickle_model2 = pickle.load(file2, encoding='ISO-8859-1')
   
with open("pickle_model_planetStarDistanceOverStarRadius.pkl", 'rb') as file3:
   pickle_model3 = pickle.load(file3, encoding='ISO-8859-1')

stars= pd.read_csv("stars.csv")
dataframe = stars[["tce_plnt_num", "tce_period","tce_ror","tce_dor","tce_incl","tce_prad","tce_steff","tce_sradius"]]


luminosity_sun=3.828e26
mass_sun=1.989e30
a=3.5
gConstant = 6.67e-11

window = None 
i = 0
j = 0
e1=0
e2=0
e3=0
e4=0



def view_data():

    global dataframe
    global stars
    global j
    global window
    global i
    global label11,label22,label33,label44,label55,label66,label77,label88
    i=1
    window.destroy()
    window = Tk()
    window["bg"] = "dark slate blue"
    window.title("Stargazer")
    window.geometry('600x400')
    title = Label(window, text="View Stargazer Data",font=400, bg='dark slate blue',fg='snow')
    title.place(x = 10, y = 0, width=200, height=50)

    
    label1=Label(window, text="Planet Number",bg = 'dark slate blue', fg ='white')
    label1.place(x = 20, y = 40, width=140, height=50)
    label2=Label(window, text="Orbital Period /Days",bg = 'dark slate blue', fg ='white')
    label2.place(x = 20, y = 80, width=140, height=50)
    label3=Label(window, text="Planet-Star Radius Ratio",bg = 'dark slate blue', fg ='white')
    label3.place(x = 20, y = 120, width=140, height=50)
    label4=Label(window, text="Planet-Star Distance Ratio",bg = 'dark slate blue', fg ='white')
    label4.place(x = 20, y = 160, width=140, height=50)
    label5=Label(window, text="Inclination /Degrees",bg = 'dark slate blue', fg ='white')
    label5.place(x = 20, y = 200, width=140, height=50)
    label6=Label(window, text="Planetary Radius /Earth Radii",bg = 'dark slate blue', fg ='white')
    label6.place(x = 20, y = 240, width=140, height=50)
    label7=Label(window, text="Stellar Effective Temperature/K",bg = 'dark slate blue', fg ='white')
    label7.place(x = 20, y = 280, width=140, height=50)
    label8=Label(window, text="Stellar Radius/Solar Radii",bg = 'dark slate blue', fg ='white')
    label8.place(x = 20, y = 320, width=140, height=50)

    label11=Label(window, text=dataframe['tce_plnt_num'][j],bg = 'dark slate blue', fg ='white')
    label11.place(x = 200, y = 40, width=140, height=50)
    label22=Label(window, text=dataframe["tce_period"][j],bg = 'dark slate blue', fg ='white')
    label22.place(x = 200, y = 80, width=140, height=50)
    label33=Label(window, text=dataframe["tce_ror"][j],bg = 'dark slate blue', fg ='white')
    label33.place(x = 200, y = 120, width=140, height=50)
    label44=Label(window, text=dataframe["tce_dor"][j],bg = 'dark slate blue', fg ='white')
    label44.place(x = 200, y = 160, width=140, height=50)
    label55=Label(window, text=dataframe["tce_incl"][j],bg = 'dark slate blue', fg ='white')
    label55.place(x = 200, y = 200, width=140, height=50)
    label66=Label(window, text=dataframe["tce_prad"][j],bg = 'dark slate blue', fg ='white')
    label66.place(x = 200, y = 240, width=140, height=50)
    label77=Label(window, text=dataframe["tce_steff"][j],bg = 'dark slate blue', fg ='white')
    label77.place(x = 200, y = 280, width=140, height=50)
    label88=Label(window, text=dataframe["tce_sradius"][j],bg = 'dark slate blue', fg ='white')
    label88.place(x = 200, y = 320, width=140, height=50)

    next = Button(window,width=10,text = 'Next',bg='coral1',fg='snow',command=next_view_data)
    next.place(x=170, y=360, width =40, height =40)
           
    home = Button(window, text="Home",bg='coral1',fg='snow',command = main_menu)
    home.place(x=530, y=0, width=70, height=40)      
    
    previous = Button(window, text="Prev",bg='coral1',fg='snow',command=prev_view_data)
    previous.place(x=10, y=360, width=40, height=40)
    window.mainloop()

def predict_data():

    def predict():
        radius=float(e1.get())*695508
        orbital=float(e2.get())
        temp=float(e3.get())
        inclination=float(e4.get())
        prelabel11.configure(text=e1.get())
        prelabel22.configure(text=e2.get())
        prelabel33.configure(text=e3.get())
        prelabel44.configure(text=e4.get())
        numberPlanets= pickle_model1.predict([[e1.get(),e2.get(),e4.get(),e3.get()]])
        planetStarDistance=pickle_model2.predict([[e1.get(),e2.get(),e4.get(),e3.get()]])
        planetStarRatio = pickle_model3.predict([[e1.get(),e2.get(),e4.get(),e3.get()]])
        mass_star=(radius**3)/(gConstant*((orbital*24*60*60/((2*math.pi)**2))))
        luminosity=luminosity_sun*((mass_star/mass_sun)**3.5)
        innerZone=(luminosity/1.1)**0.5
        outerZone=(luminosity/0.53)**0.5
        goldilocks=outerZone-innerZone
        if planetStarDistance>0 and planetStarDistance<goldilocks:
            print("It's in the goldilocks zone!")
        prelabel55.configure(text=numberPlanets)
        prelabel66.configure(text=planetStarDistance)
        prelabel77.configure(text=planetStarRatio)
        prelabel88.configure(text=luminosity)
        anotherlabel1.configure(text=innerZone)
        anotherlabel2.configure(text=outerZone)

    
    global window
    global i
    global stars
    global dataframe
    i=1
    window.destroy()
    window = Tk()
    window["bg"] = "dark slate blue"
    window.title("Stargazer")
    window.geometry('800x400')
    title = Label(window, text="Predict Stargazer Data",font=400, bg='dark slate blue',fg='snow')
    title.place(x = 10, y = 0, width=200, height=50)

    e1 = Entry(window)
    e1.place(x=150,y=80,width = 100,height=40)
    e2 = Entry(window)
    e2.place(x=150,y=130,width = 100,height=40)
    e3 = Entry(window)
    e3.place(x=150,y=180,width = 100,height=40)
    e4 = Entry(window)
    e4.place(x=150,y=230,width = 100,height=40)

    label1=Label(window, text="Radius / Solar Radii",bg = 'dark slate blue', fg ='white')
    label2=Label(window, text="Orbital Period /Days",bg = 'dark slate blue', fg ='white')
    label3=Label(window, text="Temperature/Kelvin",bg = 'dark slate blue', fg ='white')
    label4=Label(window, text="Inclination /Degrees",bg = 'dark slate blue', fg ='white')


    label1.place(x = 0, y = 80, width=140, height=50)
    label2.place(x = 0, y = 130, width=140, height=50)
    label3.place(x = 0, y = 180 , width=140, height=50)
    label4.place(x = 0, y = 230, width=140, height=50)



    prelabel1=Label(window, text="Radius",bg = 'dark slate blue', fg ='white')
    prelabel1.place(x = 280, y = 40, width=140, height=50)
    prelabel2=Label(window, text="Orbital Period /Days",bg = 'dark slate blue', fg ='white')
    prelabel2.place(x = 280, y = 80, width=140, height=50)
    prelabel3=Label(window, text="Temperature/Kelvin",bg = 'dark slate blue', fg ='white')
    prelabel3.place(x = 280, y = 120, width=140, height=50)
    prelabel4=Label(window, text="Inclination/Degrees",bg = 'dark slate blue', fg ='white')
    prelabel4.place(x = 280, y = 160, width=140, height=50)
    prelabel5=Label(window, text="Number of Planets",bg = 'dark slate blue', fg ='white')
    prelabel5.place(x =280, y = 200, width=140, height=50)
    prelabel6=Label(window, text="Planet Star Distance",bg = 'dark slate blue', fg ='white')
    prelabel6.place(x = 280, y = 240, width=140, height=50)
    prelabel7=Label(window, text="Planet Star Radius Ratio",bg = 'dark slate blue', fg ='white')
    prelabel7.place(x =280, y = 280, width=140, height=50)
    prelabel8=Label(window, text="Star Luminosity",bg = 'dark slate blue', fg ='white')
    prelabel8.place(x =280, y = 320, width=140, height=50)

    prelabel11=Label(window, text="Hello",bg = 'dark slate blue', fg ='white')
    prelabel11.place(x = 400, y = 40, width=140, height=50)
    prelabel22=Label(window, text="Hello",bg = 'dark slate blue', fg ='white')
    prelabel22.place(x = 400, y = 80, width=140, height=50)
    prelabel33=Label(window, text="Hello",bg = 'dark slate blue', fg ='white')
    prelabel33.place(x = 400, y = 120, width=140, height=50)
    prelabel44=Label(window, text="Hello",bg = 'dark slate blue', fg ='white')
    prelabel44.place(x = 400, y = 160, width=140, height=50)
    prelabel55=Label(window, text="Hello",bg = 'dark slate blue', fg ='white')
    prelabel55.place(x = 400, y = 200, width=140, height=50)
    prelabel66=Label(window, text="Hello",bg = 'dark slate blue', fg ='white')
    prelabel66.place(x = 400, y = 240, width=140, height=50)
    prelabel77=Label(window, text="Hello",bg = 'dark slate blue', fg ='white')
    prelabel77.place(x = 400, y = 280, width=140, height=50)
    prelabel88=Label(window, text="Hello",bg = 'dark slate blue', fg ='white')
    prelabel88.place(x = 400, y = 320, width=140, height=50)

    extralabel1=Label(window, text="Inner Range",bg = 'dark slate blue', fg ='white')
    extralabel1.place(x=500,y=40, width = 200, height = 50)
    extralabel2=Label(window, text="Outer Range",bg = 'dark slate blue', fg ='white')
    extralabel2.place(x=500,y=80, width = 200, height = 50)

    anotherlabel1=Label(window, text="Hello",bg = 'dark slate blue', fg ='white')
    anotherlabel1.place(x=650,y=40, width = 200, height = 50)
    anotherlabel2=Label(window, text="Hello",bg = 'dark slate blue', fg ='white')
    anotherlabel2.place(x=650,y=80, width = 200, height = 50)


    predictButton = Button(window,width=10,text = 'Predict',bg='coral1',fg='snow',command=predict)
    predictButton.place(x=80, y=360, width =80, height =40)
           

    home = Button(window, text="Home",bg='coral1',fg='snow',command = main_menu)
    home.place(x=730, y=0, width=70, height=40)      
    
    window.mainloop()

def next_view_data():
    global dataframe
    global j
    j+=1
    label11.configure(text=dataframe['tce_plnt_num'][j])
    label22.configure(text=dataframe["tce_period"][j])
    label33.configure(text=dataframe["tce_ror"][j])
    label44.configure(text=dataframe["tce_dor"][j])
    label55.configure(text=dataframe["tce_incl"][j])
    label66.configure(text=dataframe["tce_prad"][j])
    label77.configure(text=dataframe["tce_steff"][j])
    label88.configure(text=dataframe["tce_sradius"][j])
    return j



def prev_view_data():
    global dataframe
    global j
    j-=1
    if j<0:
        j=0
    label11.configure(text=dataframe['tce_plnt_num'][j])
    label22.configure(text=dataframe["tce_period"][j])
    label33.configure(text=dataframe["tce_ror"][j])
    label44.configure(text=dataframe["tce_dor"][j])
    label55.configure(text=dataframe["tce_incl"][j])
    label66.configure(text=dataframe["tce_prad"][j])
    label77.configure(text=dataframe["tce_steff"][j])
    label88.configure(text=dataframe["tce_sradius"][j])
    return j




def main_menu():
    global window
    if i>=1:
        window.destroy()
    window = Tk()
    window["bg"] = "dark slate blue"
    window.title("Stargazer")
    window.geometry('300x400')
    
    title = Label(window, text="Welcome to Stargazer",font=200, bg='dark slate blue',fg='snow')
    title.place(x = 10, y = 0, width=300, height=100)

    viewData = Button(window,width=10,text = 'View Data',bg='coral1',fg='snow',command = view_data)
    viewData.place(x=60, y=100, width =200, height =40)
    

    predictData = Button(window, text="Predict Data",bg='coral1',fg='snow',command = predict_data)
    predictData.place(x=60, y=200, width=200, height=40)

    exitMenu = Button(window, text="Exit",bg='coral1',fg='snow',command = exit)
    exitMenu.place(x=60, y=300, width=200, height=40)
    window.mainloop()



main_menu()