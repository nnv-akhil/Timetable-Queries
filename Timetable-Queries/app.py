from pathlib import Path

from flask import *

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def home():
    return render_template('admin.html')

@app.route('/get_dropdown_data', methods=['POST'])
def get_dropdown_data():
    form_input = request.form.get("q")
    if form_input == "admin-2":
        list_data = {'q':teachers}
    elif form_input == "admin-3":
        list_data = {'q':teachers}
    elif form_input == "admin-5":
        list_data = {'q': classes}
    elif form_input == "admin-6":
        list_data = {'q': classes}
    elif form_input == "admin-8":
        list_data = {'q': places}
    elif form_input == "admin-9":
        list_data = {'q': places}
    else:
        list_data = {}
    print(form_input)
    return jsonify(result=list_data)

@app.route('/admin-form1', methods=['POST'])
def form1():
    teacher_name = request.form.get("teacher_name")
    username = request.form.get("username")
    csv_file = request.form.get("csv_data")
    
    print(teacher_name)
    print(username)
    print(csv_file)
    return "Data received successfully"

@app.route('/admin-form2', methods=['POST'])
def form2() :
    teacher_name = request.form.get("teacher_name")

    print(teacher_name)
    return "Data received successfully"

@app.route('/admin-form3', methods=['POST'])
def form3():
    teacher_name = request.form.get("teacher_name")
    csv_data = request.form.get("csv_data")

    print(teacher_name)
    print(csv_data)
    return "Data received successfully"

@app.route('/admin-form4', methods=['POST'])
def form4():
    class_name = request.form.get("class_name")
    csv_data = request.form.get("csv_data")

    print(class_name)
    print(csv_data)
    return "Data received successfully"

@app.route('/admin-form5', methods=['POST'])
def form5():
    class_name = request.form.get("class_name")

    print(class_name)
    return "Data received successfully"

@app.route('/admin-form6', methods=['POST'])
def form6():
    class_name = request.form.get("class_name")
    csv_data = request.form.get("csv_data")

    print(class_name)
    print(csv_data)
    return "Data received successfully"

@app.route('/admin-form7', methods=['POST'])
def form7():
    place_name = request.form.get("place_name")
    location_name = request.form.get("location_name")

    print(place_name)
    print(location_name)
    return "Data received successfully"

@app.route('/admin-form8', methods=['POST'])
def form8():
    place_name = request.form.get("place_name")

    print(place_name)
    return "Data received successfully"

@app.route('/admin-form9', methods=['POST'])
def form9():
    place_name = request.form.get("place_name")
    location_name = request.form.get("location_name")

    print(place_name)
    print(location_name)
    return "Data received successfully"

if __name__ == '__main__':
    app.run(debug=True)
