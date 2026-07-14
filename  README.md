# 🏠 Delhi House Price Prediction System

A Machine Learning-based web application that predicts residential property prices in Delhi using property features such as area, number of bedrooms, bathrooms, building type, and location. The project demonstrates an end-to-end machine learning workflow including data preprocessing, feature engineering, model training, evaluation, and deployment using Flask.

## 📌 Project Overview

The objective of this project is to estimate house prices in Delhi based on property characteristics. The model is trained on a cleaned real-estate dataset and can provide instant price predictions through a user-friendly web interface.

## 🚀 Features

- Predicts house prices using Machine Learning
- Interactive Flask web application
- Data cleaning and preprocessing pipeline
- Feature engineering for improved accuracy
- Automatic handling of categorical variables using One-Hot Encoding
- Professional responsive user interface
- Ready for cloud deployment

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- HTML
- CSS
- Git
- GitHub
- Render

## 📊 Dataset

The project uses a Delhi Housing Dataset containing residential property information.

### Features Used

- Area (Square Feet)
- Bedrooms
- Bathrooms
- Type of Building
- Location

### Target Variable

- House Price

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Removed unnecessary columns
- Handled missing values
- Extracted location information from address
- Grouped rare locations into an **"Other"** category
- Removed location-wise price-per-square-foot outliers
- Applied One-Hot Encoding to categorical variables
- Standardized numerical features for linear models

---

## 🤖 Machine Learning Models Evaluated

- Linear Regression
- Random Forest Regressor
- Ridge Regression

After comparing model performance, the final trained model was saved using Pickle for deployment.

## 📈 Model Evaluation

Evaluation Metrics:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

These metrics were used to compare model performance and select the final prediction model.

## 📂 Project Structure

```
House_Price_Prediction
│
├── main.py
├── README.md
├── requirements.txt
├──Delhi_house_price_prediction.ipynb
├── HousePriceModel.pkl
├── templates
│     └── index.html
├── screenshots
│     ├── home.png
│     └── prediction_result.png
```
## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/House_Price_Prediction.git
```

Move into the project directory

```bash
cd House_Price_Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000/
```

---

## 💻 Web Application

Users can enter:

- Area
- Bedrooms
- Bathrooms
- Building Type
- Location

The application predicts the estimated market price instantly.

---

## 📸 Screenshots

```
Home Page

Prediction Result
```

---

## 🌐 Deployment

The application is deployed on Render.

**Live Demo**

Paste your Render deployment link here.

---

## 👨‍💻 Author

**Saurav Kumar**

B.Tech, Civil Engineering  
National Institute of Technology Warangal