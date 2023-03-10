from flask import Flask, request
from joblib import load
# import sklearn

app = Flask(__name__)

filename = "iris_clf.joblib"

model = load(filename)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/predict')
def predict():
    data = [
        request.args.get('sepallength', type=float),
        request.args.get('sepalwidth', type=float),
        request.args.get('petallength', type=float),
        request.args.get('petalwidth', type=float)
    ]
    prediction = model.predict([data])[0]
    return str(prediction)

# /predict?sepallength=1.0&sepalwidth=1.0&petallength=1.0&petalwidth=1.0

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# # some time later...

# # load the model from disk
# loaded_model = joblib.load(filename)
# result = loaded_model.score(X_test, y_test)
# print(result)