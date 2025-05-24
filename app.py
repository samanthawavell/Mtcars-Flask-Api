from flask import Flask, request, jsonify
import pandas as pd
import statsmodels.api as sm
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')
columns = joblib.load('columns.pkl')

@app.route('/')
def home():
    return 'Linear Regression API for mtcars is running.'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_df = pd.DataFrame([data])
        input_df = sm.add_constant(input_df, has_constant='add')
        input_df = input_df.reindex(columns=columns, fill_value=0) 
        prediction = model.predict(input_df)[0]
        return jsonify({'mpg_prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)