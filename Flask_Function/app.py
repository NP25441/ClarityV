from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Clarity V</h1>"

@app.route('/type')
def type():
    return "ชนิดของรถ"

@app.route('/license')
def license():
    return "หลายเลขทะเบียน"

@app.route('/city')
def city():
    return "จังหวัด"

@app.route('/color')
def color():
    return "สีของรถ"

@app.route('/time_in')
def time_in():
    return "ช่วงเวลาgเข้า"

@app.route('/time_out')
def time_out():
    return "ช่วงเวลาออก"

@app.route('/date')
def date():
    return "วันที่"

if __name__ == '__main__':
    app.run(debug=True)