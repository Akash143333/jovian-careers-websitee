from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'Data-analyst',
  'location': 'Bengaluru,India',
  'salary': 'Rs. 15,00000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi,India',
  'salary': 'Rs 15,00000'
}, {
  'id': 3,
  'title': 'Front end Engineer',
  'location': 'Remote',
  'salary': 'Rs. 14,00000'
}, {
  'id': 4,
  'title': 'Backend Emgineer',
  'location': 'San francisko',
  'salary': '$120,000'
}]


@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs=JOBS, company_name='jovian')


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)