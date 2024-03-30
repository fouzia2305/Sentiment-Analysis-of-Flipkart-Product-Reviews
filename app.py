from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/prediction', methods=[ 'POST'])
def prediction():
   
    review = request.form['review']
    if not review:
        text = "Please enter a review."
        return render_template('home.html', text=text)
    
    model = joblib.load("model/logistic_regression.pkl")
    prediction = model.predict([review])[0]
    sentiment = "Positive" if prediction == 1 else "Negative"
    return render_template('prediction.html', prediction=sentiment)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)