import pickle

from flask import Flask
from flask import request, jsonify

with open('model2.bin', 'rb') as f_in:
  model = pickle.load(f_in)

with open('dv.bin', 'rb') as f_in:
  dv = pickle.load(f_in)

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