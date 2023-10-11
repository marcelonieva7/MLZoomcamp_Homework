import pickle

from flask import Flask
from flask import request, jsonify

CLIENT = {"job": "retired", "duration": 445, "poutcome": "success"}

with open('model1.bin', 'rb') as f_in:
  model = pickle.load(f_in)

with open('dv.bin', 'rb') as f_in:
  dv = pickle.load(f_in)

X = dv.transform([CLIENT])

score = model.predict_proba(X)[0,1]

print(f'Score = {round(score, 3)}')

app = Flask('credit_scoring')

@app.route('/predict', methods=['POST'])
def predict():
  client = request.get_json()
  X = dv.transform([client])
  score = model.predict_proba(X)[0,1]
  score = round(score, 3)

  response = {'score': score}
  return jsonify(score)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9696)