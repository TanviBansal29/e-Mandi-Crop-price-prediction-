import pickle
from flask import Flask, request, jsonify
import pandas as pd

# commodity = 'Cotton'
# variety = 'Desi'
# marketName = 'Jhabua'

# marketName_pkl = pickle.load(open('encoders_exp/market.pkl', 'rb'))
# marketName_encoded = marketName_pkl.transform([marketName])
# commodity_pkl = pickle.load(open('encoders_exp/commodity.pkl', 'rb'))
# commodity_encoded = marketName_pkl.transform([commodity])
# variety_pkl = pickle.load(open('encoders_exp/variety.pkl', 'rb'))
# variety_encoded = marketName_pkl.transform([variety])

# model = pickle.load(open('models_exp/model.pkl', 'rb'))

# model.predict()

app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle classifier
        # model = pickle.load(open('model1.pkl', 'rb'))
        
        # Get values through input bars
        marketName = request.form['marketInput']
        commodityName = request.form["commodityInput"]
        
        # Put inputs to dataframe
        # X = pd.DataFrame([[height, weight]], columns = ["Height", "Weight"])
        
        # Get prediction
        # prediction = model.predict(X)[0]
        
    else:
        prediction = "asd"
        
    return jsonify(marketName)

if __name__ == '__main__':
    app.run(port=5000, debug=True)