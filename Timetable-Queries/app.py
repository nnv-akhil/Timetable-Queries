from flask import *
from pathlib import Path

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/') 
def home():
    return render_template('admin.html')

@app.route('/get_dropdown_data', methods=['POST'])
def get_dropdown_data():
    form_input = request.form.get("q")
    if form_input == "1":
        list_data = {'teacher': '10', 'user': '100'}
    elif form_input == "2":
        list_data = {'teacher': '20', 'user': '200'}
    elif form_input == "3":
        list_data = {'teacher': '30', 'user': '300'}
    elif form_input == "4":
        list_data = {'teacher': '40', 'user': '400'}
    elif form_input == "5":
        list_data = {'teacher': '50', 'user': '500'}
    elif form_input == "6":
        list_data = {'teacher': '60', 'user': '600'}
    else:
        list_data = {} 
    print(form_input)
    return jsonify(result=list_data)

@app.route('/form1', methods=['POST'])
def form1():
    teacher_name = request.form.get("teacher_name")
    username = request.form.get("username")
    csv_file = request.form.get("csv_data")
    
    print(teacher_name)
    print(username)
    print(csv_file)
    return "Data received successfully"

@app.route('/form2', methods=['POST'])
def form2() :
    teacher_name = request.form.get("teacher_name")

    print(teacher_name)
    return "Data received successfully"

@app.route('/form3', methods=['POST'])
def form3():
    teacher_name = request.form.get("teacher_name")
    csv_data = request.form.get("csv_data")

    print(teacher_name)
    print(csv_data)
    return "Data received successfully"

@app.route('/form4', methods=['POST'])
def form4():
    class_name = request.form.get("class_name")
    csv_data = request.form.get("csv_data")

    print(class_name)
    print(csv_data)
    return "Data received successfully"

@app.route('/form5', methods=['POST'])
def form5():
    class_name = request.form.get("class_name")

    print(class_name)
    return "Data received successfully"

@app.route('/form6', methods=['POST'])
def form6():
    class_name = request.form.get("class_name")
    csv_data = request.form.get("csv_data")

    print(class_name)
    print(csv_data)
    return "Data received successfully"

@app.route('/form7', methods=['POST'])
def form7():
    place_name = request.form.get("place_name")
    location_name = request.form.get("location_name")

    print(place_name)
    print(location_name)
    return "Data received successfully"

@app.route('/form8', methods=['POST'])
def form8():
    place_name = request.form.get("place_name")

    print(place_name)
    return "Data received successfully"

@app.route('/form9', methods=['POST'])
def form9():
    place_name = request.form.get("place_name")
    location_name = request.form.get("location_name")

    print(place_name)
    print(location_name)
    return "Data received successfully"

if __name__ == '__main__':
    app.run(debug=True)
