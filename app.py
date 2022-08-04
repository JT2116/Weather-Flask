from ctypes.wintypes import PINT
from distutils.command.config import config
from pip import main
from requests import request
import requests
from flask import Flask, render_template, url_for, redirect, request, flash, current_app
import mariadb
from forms import registerCity
import os

app = app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

config = { # Configuracion para la base de datos
    'user': 'root',
    'password': '1011',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'ciudades'
}


@app.route("/")
def index():
    
    conn = mariadb.connect(**config)
    cur = conn.cursor()
        
    cur.execute("select Nombre from ciudades")
    cities = cur.fetchall()

    cur.close()
    conn.close()

    # city = 'London'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b65498bd83bb91eaf34edf249595fdac'

    # r = requests.get(url.format(city)).json()
    
    climas = []

    for city in cities:
        # print(city[0])
        r = requests.get(url.format(city[0])).json()
        clima = {
            'city' : city[0],
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        climas.append(clima)

    return render_template('weather.html', climas = climas)

@app.route("/data_<city>")
def data_city(city):
    # print(city)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b65498bd83bb91eaf34edf249595fdac'

    r = requests.get(url.format(city)).json()
    
    clima = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'temperatureMax' : r['main']['temp_max'],
        'temperatureMin' : r['main']['temp_min'],
        'humidity' : r['main']['humidity'],
        'wind_speed' : r['wind']['speed'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }


    return render_template('data_weather.html',clima = clima)

@app.route("/register",methods=['GET','POST'])
def registers_city():

    if request.method == 'POST':
        newCity =  request.form.get('nombreCiudad')
        # print(newCity)
        conn = mariadb.connect(**config)
        cur = conn.cursor()
        
        cur.execute("select count(Nombre) from ciudades where Nombre = ?",(newCity,))
        cities = cur.fetchall()

        Bcities = format(cities[0][0])

        if Bcities == '0':
            cur.execute("insert into Ciudades (Nombre) values (?)",(newCity,))                   
            conn.commit()
        else:

            success_message = 'That country is already registered'
            flash(success_message)

            cur.close()
            conn.close()

            return render_template('register_city.html',form = registerCity())


            

        cur.close()
        conn.close()



        return redirect(url_for('index'))

    

    return render_template('register_city.html',form = registerCity())



if __name__ == '__main__':
	app.run(debug = True)