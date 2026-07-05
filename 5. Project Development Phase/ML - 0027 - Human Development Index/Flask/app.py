# Import required libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

# Load the saved HDI prediction model and the Country label encoder
model = pickle.load(open('HDI.pkl', 'rb'))
country_encoder = pickle.load(open('country_encoder.pkl', 'rb'))

# Sorted list of countries for the dropdown (built from the encoder's known classes)
COUNTRY_LIST = sorted(country_encoder.classes_)


def get_hdi_category(score):
    """Map a predicted HDI score to its official UNDP category band."""
    if score >= 0.800:
        return "Very High HDI"
    elif score >= 0.700:
        return "High HDI"
    elif score >= 0.550:
        return "Medium HDI"
    else:
        return "Low HDI"


# Home route - renders the introduction page
@app.route('/')
def home():
    return render_template('home.html')


# Prediction page - shows the form (GET) and handles submission (POST)
@app.route('/predict', methods=['GET'])
def show_form():
    return render_template('indexnew.html', countries=COUNTRY_LIST)


@app.route('/predict', methods=['POST'])
def predict():
    # 1. Country -> encode using the same LabelEncoder used during training
    country_name = request.form.get('country')
    country_encoded = country_encoder.transform([country_name])[0]

    # 2. Remaining numeric inputs from the form
    life_expectancy = float(request.form.get('life_expectancy'))
    mean_schooling = float(request.form.get('mean_schooling'))
    expected_schooling = float(request.form.get('expected_schooling'))
    gni = float(request.form.get('gni'))

    # 3. Build the feature vector in the SAME column order used during training:
    #    [Country, Life_Expectancy, Mean_Years_of_Schooling, Expected_Years_of_Schooling, GNI_Per_Capita]
    input_features = [country_encoded, life_expectancy, mean_schooling, expected_schooling, gni]
    final_features = [np.array(input_features)]

    # 4. Predict and round for readability
    prediction = model.predict(final_features)
    score = round(float(prediction[0]), 2)
    category = get_hdi_category(score)

    return render_template(
        'indexnew.html',
        countries=COUNTRY_LIST,
        prediction_text=f'{category}  {score}'
    )


if __name__ == '__main__':
    app.run(debug=True)
