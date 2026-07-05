# Human Development Index (HDI) Prediction

## Project Description

The Human Development Index (HDI) Prediction project is a Machine Learning based web application developed using Python and Flask. The application predicts the Human Development Index (HDI) of a country using important development indicators such as Life Expectancy, Mean Years of Schooling, Expected Years of Schooling, and Gross National Income (GNI) per Capita.

The prediction model is trained using an HDI dataset and integrated into a Flask web application to provide quick and accurate predictions through an interactive user interface.

---

## Features

- Predicts Human Development Index (HDI)
- Machine Learning based prediction system
- Interactive Flask web application
- Simple and user-friendly interface
- Fast prediction results
- Trained model using Scikit-learn

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Scikit-learn
- Pandas
- NumPy
- Pickle
- Jupyter Notebook

---

## Project Structure


Human Development Index/

├── Dataset/
│   └── HDI.csv
│
├── Flask/
│   ├── app.py
│   ├── requirements.txt
│   ├── HDI.pkl
│   ├── country_encoder.pkl
│   └── templates/
│       ├── home.html
│       └── indexnew.html
│
├── Training/
│   └── HumDevIndex.ipynb
│
└── README.md


---

## Dataset

**Dataset Name:** HDI Dataset

### Input Features

- Life Expectancy
- Mean Years of Schooling
- Expected Years of Schooling
- Gross National Income (GNI) per Capita

### Output

- Predicted Human Development Index (HDI)

---

## Machine Learning Model

The project uses a Machine Learning model trained using the HDI dataset. The trained model is stored as **HDI.pkl**, and the country encoder is stored as **country_encoder.pkl**. These files are loaded by the Flask application to generate HDI predictions.

---

## Installation

Install the required Python packages:


pip install -r requirements.txt

---

## Run the Project

Start the Flask application:

python app.py


Open your browser and visit:


http://127.0.0.1:5000


---

## Future Enhancements

- Improve prediction accuracy using advanced Machine Learning algorithms.
- Add graphical visualizations for better analysis.
- Deploy the application on a cloud platform.
- Expand the dataset with more countries and recent data.
- Improve the user interface and user experience.

---

## Team

Mucharla Sweety
Gowri Nandini Puttha
Meruva Ruchitha
Paturu Malleswasri
Yashashvi Nagisettygari
