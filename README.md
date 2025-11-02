# 🏠 House Price Predictor (Flask + Machine Learning + MySQL)

An AI-powered web application that predicts **California house prices** based on user inputs like income, rooms, house age, and more — built with **Flask**, **Scikit-learn**, and **MySQL**, featuring a sleek **Neon UI design**.

---

## 🚀 Features

✅ Predicts house prices using a **trained Linear Regression model**  
✅ Built with **Flask** for backend routing and API handling  
✅ Stores **user authentication and prediction history** in MySQL  
✅ Interactive, futuristic **Neon UI (HTML + CSS + Jinja2)**  
✅ Fully responsive layout — optimized for all screens  
✅ Secure model loading from `model.pkl`  
✅ SEO-optimized and portfolio-ready project  

---

## 🧠 Machine Learning Model

- **Algorithm:** Linear Regression  
- **Dataset:** California Housing Dataset (from `sklearn.datasets`)  
- **Target:** Median House Value (`MedHouseVal`)  
- **Features Used:**  
  - `MedInc` — Median Income  
  - `HouseAge` — Age of the House  
  - `AveRooms` — Average Number of Rooms  
  - `AveBedrms` — Average Bedrooms  
  - `Population` — Area Population  
  - `AveOccup` — Average House Occupancy  
  - `Latitude` and `Longitude` — Location  

- **Model File:** `model.pkl` (exported using Joblib)  
- **R² Score:** ~0.57 (to be improved in later versions)

---

## 🧩 Tech Stack

| Layer | Technology Used |
|--------|----------------|
| **Frontend** | HTML, CSS (Neon Dark Theme), Jinja2 |
| **Backend** | Flask (Python) |
| **Database** | MySQL |
| **Machine Learning** | Scikit-learn |
| **Model Handling** | Joblib |
| **Version Control** | Git + GitHub |

---

## 🛠 Setup Instructions

1️⃣ Clone this repository
2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
git clone https://github.com/codingsheep17/house-price-predictor.git
cd house-price-predictor
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Set up the .env file
Create a .env file in the project root:
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASS=your_mysql_password
DB_NAME=house_price_predictor
SECRET_KEY=your_flask_secret_key
5️⃣ Run the app
python app.py
Then visit 👉 http://127.0.0.1:5000/ in your browser.

📂 Project Structure
House-Price-Predictor/
│
├── app.py                  # Main Flask application
├── model.pkl               # Trained ML model
├── requirements.txt        # Dependencies
├── .env                    # Environment variables
│
├── static/
│   ├── css/
│   │   ├── home.css
│   │   ├── login.css
│   │   ├── footer.css
│   │   └── navbar.css
│   └── images/
│
├── templates/
│   ├── layout.html
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── about.html
│   └── history.html
│
└── README.md

📊 Example Prediction Flow
1️⃣ User logs in or signs up
2️⃣ Inputs data such as income, rooms, and city
3️⃣ Flask sends data to the model
4️⃣ Model predicts price using model.pkl
5️⃣ Predicted result + input is saved in MySQL history table
6️⃣ User can view last 5 predictions in the History page

💡 Future Improvements
🔹 Improve accuracy using Polynomial Regression / Random Forest
🔹 Integrate interactive charts with Chart.js
🔹 Deploy using Render / Railway / AWS
🔹 Add user dashboard analytics

👨‍💻 Author: Syed Haseeb Shah
📧 Gmail: codingsheep17@gmail.com
🌐 LinkedIn: syedhaseebshah19
💻 GitHub: codingsheep17
