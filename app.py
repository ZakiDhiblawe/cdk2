from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the CKD model
with open('Kidney.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the gender model (example: heuristic based on hemoglobin)
def predict_gender(hemo):
    return 1 if hemo >= 14.0 else 0  # Assuming threshold for male/female

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        sg = float(data['sg'])
        htn = int(data['htn'])
        hemo = float(data['hemo'])
        dm = int(data['dm'])
        al = int(data['al'])
        appet = int(data['appet'])
        rc = float(data['rc'])
        pc = int(data['pc'])

        # Create a numpy array for prediction
        input_features = np.array([[sg, htn, hemo, dm, al, appet, rc, pc]])

        # Get the prediction and probability for CKD
        ckd_prediction = model.predict(input_features)[0]
        ckd_probabilities = model.predict_proba(input_features)[0]  # Probabilities for both classes

        # Probability of CKD (class 1)
        ckd_probability = float(ckd_probabilities[1])  # Convert to native Python type

        # Predict gender based on heuristics
        gender_prediction = predict_gender(hemo)

        # Return the prediction, probability, and gender prediction as JSON
        return jsonify({
            'prediction': int(ckd_prediction),  # Convert to native Python type
            'probability': ckd_probability,
            'gender_prediction': int(gender_prediction)  # Convert to native Python type
        })
    except Exception as e:
        # Print the error for debugging
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
