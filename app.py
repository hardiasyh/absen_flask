from datetime import date
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
students=[]
attendance={}
@app.route('/')
def index():
    today=str(date.today())
    return render_template('index.html', students=students, attendance=attendance.get(today, {}), today=today)
@app.route('/add', methods=['POST'])
def add_student():
    name=request.form.get('name')
    if name: students.append(name)
    return redirect(url_for('index'))
@app.route('/absen', methods=['POST'])
def absen():
    today=str(date.today())
    attendance.setdefault(today,{})
    for s in students:
        status=request.form.get(s)
        if status: attendance[today][s]=status
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(debug=True)
