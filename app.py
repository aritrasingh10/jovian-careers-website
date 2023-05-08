from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 100000
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 150000
  },
  {
    'id': 3,
    'title': 'Data Engineer',
    'location': 'Remote',
  },
  {
    'id': 4,
    'title': 'Marketing Analyst',
    'location': 'Kolkata, India',
    'salary': 50000
  },
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=8443)
