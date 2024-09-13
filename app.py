from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__, template_folder='templates2')  # Specify the custom template folder

# Load the model
model_file = open('model.pkl', 'rb')
model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form (expecting 30 features)
        input_data = [float(request.form[f'input{i}']) for i in range(30)]
        input_data = np.array([input_data])

        # Make prediction using the model
        prediction = model.predict(input_data)

        # Return the result to the HTML template
        result = "fraudulent" if prediction[0] == 1 else "non-fraudulent"
        return render_template('index.html', prediction_text=f'Transaction is predicted to be {result}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
