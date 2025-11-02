from flask import Flask, render_template, url_for, redirect, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import os
from dotenv import  load_dotenv
import joblib
import numpy as np

#making the Flask class instance, trained model and loading env
model  = joblib.load("model.pkl")
app = Flask(__name__)
load_dotenv()

#adding all of the important stuff for new login everytime 
app.secret_key = os.getenv("SECRET_KEY")
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSIN_COOKIE_SECURE=False, #True with http only
    SESSION_PERMANENT=False #makes session temporary
)

#DATABASE STUFF WILL COME HERE
db_host = os.getenv("DB_HOST")
db_username = os.getenv("DB_USERNAME")
db_name = os.getenv("DB_NAME")
db_pass = os.getenv("DB_PASSWORD")

#adding all routes and starting the app

@app.route("/", methods=["POST", "GET"])
def login():
    session.permanent = False
    if request.method == "POST":
        email_login = request.form.get("email")
        password_login = request.form.get("password")
        connection = mysql.connector.connect(
            host=db_host,
            user=db_username,
            password=db_pass,
            database=db_name
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_logs WHERE gmail = %s", (email_login,))
        user = cursor.fetchone()
        if not user:
            cursor.close()
            connection.close()
            return render_template("index.html", error="No User Found, SignUp")
        elif not check_password_hash(user[3], password_login):
            cursor.close()
            connection.close()
            return render_template("index.html", error="Wrong Password")
        else:
            session["user_id"] = user[0]
            session["user_name"] = user[1]
            session["gmail"] = user[2]
            cursor.close()
            connection.close()
            return redirect(url_for("home"))
    return render_template("index.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        user_name = request.form.get('name')
        email_signup = request.form.get('email')
        password_signup = request.form.get('password')
        hashed_pass = generate_password_hash(password_signup ,method='pbkdf2:sha256' , salt_length=10)
        connection = mysql.connector.connect(
            host=db_host,
            user=db_username,
            password=db_pass,
            database=db_name
        )
        cursor = connection.cursor()
        cursor.execute("SELECT user_id FROM user_logs WHERE gmail = %s", (email_signup,))
        if cursor.fetchone():
            cursor.close()
            connection.close()
            return render_template("signup.html", error_signup="User is already registered, Login")
        cursor.execute(
            "INSERT INTO user_logs (name, gmail, password) VALUES (%s, %s, %s)",
            (user_name, email_signup, hashed_pass)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/logout")
def logout():
    if "user_id" not in session:   # check session
        return redirect(url_for("login"))
    else:
        session.clear()   # clears all session data
        return redirect(url_for('login'))
    
@app.route("/home", methods=["POST", "GET"])
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))
    user_id = session.get("user_id")
    if request.method == "POST":
        user_income = int(request.form.get("income"))
        user_house_age = int(request.form.get("house_age"))
        user_rooms = int(request.form.get("rooms"))
        user_bedrooms = int(request.form.get("bedrooms"))
        user_population = int(request.form.get("population"))
        house_people = int(request.form.get("occupants"))
        user_city = request.form.get("city")
        if (
            user_income > 15000 and
            3 <= user_rooms <= 20 and
            1 <= user_house_age <= 30 and
            1 <= user_bedrooms <= user_rooms and
            200 <= user_population <= 35000 and
            1 <= house_people <= user_bedrooms
        ):
            city_to_coords = {
            "sanfrancisco": (37.77, -122.42),
            "losangeles": (34.05, -118.24),
            "sandiego": (32.72, -117.16),
            "sacramento": (38.58, -121.49)
            }
            lat, lon = city_to_coords.get(user_city, (36.77, -119.42))
            input_data = np.array([[user_income / 10000, user_house_age, user_rooms,
                        user_bedrooms, user_population, house_people,
                        lat, lon]])
            predicted_value = model.predict(input_data)[0]
            price_usd = predicted_value * 100000
            connection = mysql.connector.connect(
                host=db_host,
                username=db_username,
                password=db_pass,
                database=db_name
            )
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO users_history 
                (user_id, income, rooms, house_age, bedrooms, population, people_in_house, city, predicted_price)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (user_id, user_income, user_rooms, user_house_age, user_bedrooms, user_population,
                house_people, user_city, price_usd))
            connection.commit()
            cursor.close()
            connection.close()
            return render_template("home.html", price=price_usd)
        else:
            error = "Invalid Information"
            return render_template("home.html", error=error)
    return render_template("home.html")

@app.route("/about", methods=["GET"])
def about():
    if "user_id" not in session:
        return redirect(url_for("login"))        
    return render_template("about.html")

@app.route("/history", methods=["GET"])
def history():
    if "user_id" not in session:
        return redirect(url_for("login"))
    user_id = session.get("user_id")
    gmail = session.get("gmail")
    connection = mysql.connector.connect(
                host=db_host,
                user=db_username,
                password=db_pass,
                database=db_name
    )
    cursor = connection.cursor()
    cursor.execute("""SELECT income, rooms, house_age, bedrooms, population, people_in_house, city, predicted_price,
                    created_at from users_history WHERE user_id = %s ORDER BY created_at DESC LIMIT 5""",(user_id,))
    history = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("history.html", history=history)

if __name__=="__main__":
    app.run(debug=True)