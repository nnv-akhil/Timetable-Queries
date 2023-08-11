from flask import Flask, render_template, request, redirect, url_for, session,jsonify
from sqlalchemy import create_engine,text
import re 
from datetime import datetime
import random
import os
from pathlib import Path
import pandas as pd
import pandas.io.sql as psql
import pickle


app = Flask(__name__,template_folder='templates',static_folder='static')

dept="cse1"
role=""

hostname="127.0.0.1"
dbname="sakila"
uname="root"
password="admin"

# engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=password))

# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'admin'
# app.config['MYSQL_DB'] = 'sakila'
# # allow_local_infile=True
# mysql = MySQL(app)

days=['Monday','Tuesday','Wednesday','Thursday','Friday']
per=[1,2,3,4,5,6,7,8,9,10]

class Dept:
    def __init__(self):      
        self.subject_classes={}
        self.subject_teachers={}
        self.teacher_tasks={}
        self.place_location={}
        self.teacher_aoi={}
        self.teachers=[]
        self.aoi=[]
        self.classes=[]
        self.places=[]
        self.subjects=[]
        self.passkey="12345"
        self.teacher_passkey={}
    # def get_passkey(self):
    #     return self.passkey
    def reg_teacher(self,teacher,table):
        pa=""
        for i in range(6):
            j=random.randint(1,3)
            if(j==1):
                k=random.randint(0,25)
                pa+=chr(97+k)
            elif(j==2):
                k=random.randint(0,25)
                pa+=chr(65+k)
            else:
                k=random.randint(0,9)
                pa+=chr(48+k)
        self.teacher_passkey[teacher]=pa
        self.teacher_tasks[teacher]=[]
        self.teacher_aoi[teacher]=[]
        self.teachers.append(teacher)
        # print("hello")
        # print(table)
        for d in days:
            for s in table[d]:
                l=list(s.split('-'))
                if(len(l)>1):
                    if l[0] not in self.subject_teachers:
                        self.subject_teachers[l[0]]=[teacher]
                    else:
                        self.subject_teachers[l[0]].append(teacher)
                    if l[0] not in self.subjects:
                        self.subjects.append(l[0])
        table['period']=per
        # table.to_sql('hello', engine, index=False)
        engine=create_engine(f"mysql+mysqldb://{uname}:{password}@{hostname}/{dbname}")
        table.to_sql(con=engine,name=teacher,if_exists='replace',index=False)
        #print(table.info())
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # table.to_csv(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{teacher}.csv',header=False,index=False)
        # cursor.execute(f'drop table if exists {teacher}')
        # cursor.execute(f'create table {teacher}(Monday varchar(100),Tuesday varchar(100),Wednesday varchar(100),Thursday varchar(100),Friday varchar(100),Period int)')
        # LOAD DATA INFIle 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/hello1.csv' INTO TABLE hello1 FIELDS TERMINATED BY "," LINES  TERMINATED BY "\n";
        # st=f"LOAD DATA INFIle 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{teacher}.csv' INTO TABLE {teacher} FIELDS TERMINATED BY "
        # st+='","'
        # st+=' LINES  TERMINATED BY "\\n"'
        # print(st)
        # table.to_sql(con=cursor, name='hello', if_exists='append')
        # psql.write_frame(table, 'hello', cursor, 'mysql')
        # cursor.execute("LOAD DATA LOCAL INFIle 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/hello.csv' INTO TABLE hello FIELDS TERMINATED BY ',' LINES  TERMINATED BY '\\n'")
        # return "hello"
        return f"{teacher} registered successfully.\n Their password is {pa}"
    def edit_teacher(self,teacher,table):
        # query=f"SELECT * FROM {teacher}"
        engine=create_engine(f"mysql+mysqldb://{uname}:{password}@{hostname}/{dbname}")
        tab=pd.read_sql(teacher,engine.connect())
        # tab=pd.read_csv(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{teacher}.csv')
        for d in days:
            for s in tab[d]:
                l=list(s.split('-'))
                if(len(l)>1):
                    self.subject_teachers[l[0]].remove(teacher)
        for d in days:
            for s in table[d]:
                l=list(s.split('-'))
                if(len(l)>1):
                    if l[0] not in self.subject_teachers:
                        self.subject_teachers[l[0]]=[teacher]
                    else:
                        self.subject_teachers[l[0]].append(teacher)
                    if l[0] not in self.subjects:
                        self.subjects.append(l[0])
        # if os.path.isfile(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{teacher}.csv'):
        #     os.remove(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{teacher}.csv')
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute(f'drop table if exists {teacher}')
        table['period']=per
        
        table.to_sql(con=engine,name=teacher,if_exists='replace',index=False)
        # table.to_csv(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{teacher}.csv',index=False)
        # cursor.execute(f'drop table if exists {teacher}')
        # cursor.execute(f'create table {teacher}(Monday varchar(100),Tuesday varchar(100),Wednesday varchar(100),Thursday varchar(100),Friday varchar(100),Period int)')
        # cursor.execute(f"LOAD DATA INFIle 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{teacher}.csv' INTO TABLE {teacher} FIELDS TERMINATED BY ',' LINES  TERMINATED BY '\n'")
        return f"{teacher}'s TimeTable updated successfully"
    def drop_teacher(self,teacher):
        del self.teacher_passkey[teacher]
        del self.teacher_tasks[teacher]
        del self.teacher_aoi[teacher]
        self.teachers.remove(teacher)
        engine=create_engine(f"mysql+mysqldb://{uname}:{password}@{hostname}/{dbname}")
        tab=pd.read_sql(teacher,engine.connect())
        # table=pd.read_csv(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{teacher}.csv')
        for d in days:
            for s in tab[d]:
                l=list(s.split('-'))
                if(len(l)>1):
                    self.subject_teachers[l[0]].remove(teacher)
        # query=text("drop table if exists hello")
        # tab=engine.execute(query)
        query=text(f"drop table if exists {teacher}")
        # engine=create_engine(f"mysql+mysqldb://{uname}:{password}@{hostname}/{dbname}")
        tab=engine.connect().execute(query)
        # tab=pd.read_sql(query,engine)
        # if os.path.isfile(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{teacher}.csv'):
        #     os.remove(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{teacher}.csv')
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute(f'drop table if exists {teacher}')
        return f"{teacher} dropped successfully"
    def reg_class(self,class_name,table):
        self.classes.append(class_name)
        for d in days:
            for s in table[d]:
                l=list(s.split('-'))
                if(len(l)>1):
                    if l[0] not in self.subject_teachers:
                        self.subject_classes[l[0]]=[class_name]
                    else:
                        self.subject_classes[l[0]].append(class_name)
                    if l[0] not in self.subjects:
                        self.subjects.append(l[0])
        table['period']=per
        engine=create_engine(f"mysql+mysqldb://{uname}:{password}@{hostname}/{dbname}")
        table.to_sql(con=engine,name=class_name,if_exists='replace',index=False)
        # table.to_csv(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{class_name}.csv',index=False)
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute(f'drop table if exists {class_name}')
        # cursor.execute(f'create table {class_name}(Monday varchar(100),Tuesday varchar(100),Wednesday varchar(100),Thursday varchar(100),Friday varchar(100),Period int)')
        # cursor.execute(f"LOAD DATA INFIle 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{class_name}.csv' INTO TABLE {class_name} FIELDS TERMINATED BY ',' LINES  TERMINATED BY '\n'")
        return f"{class_name} registered successfully"
    def edit_class(self,class_name,table):
        engine=create_engine(f"mysql+mysqldb://{uname}:{password}@{hostname}/{dbname}")
        tab=pd.read_sql(class_name,engine.connect())
        # query=f"SELECT * FROM {class_name}"
        # tab=pd.read_sql(query,engine)
        # tab=pd.read_csv(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{class_name}.csv')
        for d in days:
            for s in tab[d]:
                l=list(s.split('-'))
                if(len(l)>1):
                    self.subject_classes[l[0]].remove(class_name)
        for d in days:
            for s in table[d]:
                l=list(s.split('-'))
                if(len(l)>1):
                    if l[0] not in self.subject_teachers:
                        self.subject_classes[l[0]]=[class_name]
                    else:
                        self.subject_classes[l[0]].append(class_name)
                    if l[0] not in self.subjects:
                        self.subjects.append(l[0])
        table['period']=per
        # engine=create_engine(f"mysql+mysqldb://{uname}:{password}@{hostname}/{dbname}")
        table.to_sql(con=engine,name=class_name,if_exists='replace',index=False)
        # if os.path.isfile(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{class_name}.csv'):
        #     os.remove(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{class_name}.csv')
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute(f'drop table if exists {class_name}')
        # table['period']=per
        # table.to_csv(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{class_name}.csv',index=False)
        # cursor.execute(f'drop table if exists {class_name}')
        # cursor.execute(f'create table {class_name}(Monday varchar(100),Tuesday varchar(100),Wednesday varchar(100),Thursday varchar(100),Friday varchar(100),Period int)')
        # cursor.execute(f"LOAD DATA INFIle 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{class_name}.csv' INTO TABLE {class_name} FIELDS TERMINATED BY ',' LINES  TERMINATED BY '\n'")
        return f"{class_name}'s timetable edited successfully"
    def drop_class(self,class_name):
        engine=create_engine(f"mysql+mysqldb://{uname}:{password}@{hostname}/{dbname}")
        tab=pd.read_sql(class_name,engine.connect())
        # tab=pd.read_csv(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{class_name}.csv')
        for d in days:
            for s in tab[d]:
                l=list(s.split('-'))
                if(len(l)>1):
                    self.subject_classes[l[0]].remove(class_name)
        self.classes.remove(class_name)
        # table=pd.read_csv(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{class_name}.csv')
        # for d in days:
        #     for s in table[d]:
        #         l=list(s.split('-'))
        #         if(len(l)>1):
        #             self.subject_classes[l[0]].remove(class_name)
        # if os.path.isfile(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{class_name}.csv'):
        #     os.remove(f'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{class_name}.csv')
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute(f'drop table if exists {class_name}')
        query=text(f"drop table if exists {class_name}")
        # engine=create_engine(f"mysql+mysqldb://{uname}:{password}@{hostname}/{dbname}")
        tab=engine.connect().execute(query)
        return f"{class_name} dropped successfully"
    def get_teacher_time(self,day,hour,minute,teacher):
        m=520
        n=hour*60+minute
        n-=m
        n//=50
        n+=1
        ans=""
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if(day=='Sunday'):
            ans="Holiday yaar"
        elif(n<=0):
            ans="College not yet started yaar"
        elif(n>10):
            ans="College is over yaar!"
        elif(day=='Saturday'):
            ans="At their Cabin"
        else:
            query=text(f'SELECT {day} FROM {teacher} WHERE Period={n}').fetchall()
            # cursor.execute()
            # data = cursor.fetchall()
            engine=create_engine(f"mysql+mysqldb://{uname}:{password}@{hostname}/{dbname}")
            tab=engine.connect().execute(query).fetchall()
            # print(type(tab))
            ans='hi'
            l=list(tab[0][0].split('-'))
            if(len(l)==1):
                ans="Leisure"
            else:
                ans=f'{teacher} is at {l[2]} and teaching {l[0]} for {l[1]}'
        return ans
    def get_teacher_now(self,teacher):
        day=datetime.today().strftime("%A")
        time=datetime.now().strftime("%H:%M:%S")
        l=list(map(int,time.split(':')))
        return self.get_teacher_time(day,l[0],l[1],teacher)
    def get_classes_from_subject(self,subject):
        if subject in self.subject_classes:
            return self.subject_classes[subject]
        else:
            return []
    def get_teachers_from_subject(self,subject):
        if subject in self.subject_teachers:
            return self.subject_teachers[subject]
        else:
            return []
    def get_tasks_from_teacher(self,teacher):
        return self.teacher_tasks[teacher]
    def get_class_time(self,day,hour,minute,class_name):
        m=520
        n=hour*60+minute
        n-=m
        n//=50
        n+=1
        ans=""
        if(n>10 or day=='Sunday'):
            ans="College is over yaar!"
        elif(day=='Saturday'):
            ans="Club Activities"
        else:
            query=text(f'SELECT {day} FROM {class_name} WHERE Period={n}').fetchall()
            # cursor.execute()
            # data = cursor.fetchall()
            engine=create_engine(f"mysql+mysqldb://{uname}:{password}@{hostname}/{dbname}")
            tab=engine.connect().execute(query).fetchall()
            # print(type(tab))
            ans='hi'
            l=list(tab[0][0].split('-'))
        #     if(len(l)==1):
        #         ans="Leisure"
        #     else:
        #         ans=f'{teacher} is at {l[2]} and teaching {l[0]} for {l[1]}'
        # return ans
        #     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #     cursor.execute(f'SELECT {day} FROM {class_name} WHERE Period={str(n)}')
        #     data = cursor.fetchall()
        #     l=list(data[0][day].split())
            if(len(l)==1):
                ans="Free Period"
            else:
                ans=f'{class_name} is at {l[2]} and {l[1]} is teaching them {l[0]}'
        return ans
    def get_class_now(self,class_name):
        day=datetime.today().strftime("%A")
        time=datetime.now().strftime("%H:%M:%S")
        l=list(map(int,time.split(':')))
        return self.get_class_time(day,l[0],l[1],class_name)
    def get_teachers_from_aoi(self,a_o_i):
        l=[]
        for d in self.teacher_aoi:
            if a_o_i in self.teacher_aoi[d]:
                l.append(d)
        return l
    def add_place(self,place,loc):
        self.places.append(place)
        self.place_location[place]=loc
        return f"{place} and its location {loc} are added successfully"
    def edit_place(self,place,loc):
        self.place_location[place]=loc
        return f"{place} and its location {loc} are updated successfully"
    def del_place(self,place):
        self.places.remove(place)
        del self.place_location[place]
        return f"{place} got successfully dropped"
    def get_loc_from_place(self,place):
        return self.place_location[place]
    def get_teachers(self):
        return self.teachers
    def get_classes(self):
        return self.classes
    def get_places(self):
        return self.places
    def get_subjects(self):
        return self.subjects
    def get_aoi(self):
        return self.aoi
cse1=Dept()
cse=Dept()
ece=Dept()
eee=Dept()
mech=Dept()
civ=Dept()
chem=Dept()
it=Dept()


@app.route('/')
def home():
    return render_template('section.html')

@app.route('/send_dept',methods=['POST'])
def send_dept():
    global dept
    dept=request.form.get("q")
    dept="cse1"
    return "success"
    #print(dept)
    #return "hello"
    # return "<script>window.location.replace('/option1')</script>", 200

@app.route('/get_role_page')
def get_role_page():  
    return render_template("role.html");  
 

@app.route('/send_role',methods=['POST'])
def send_role():
    global role
    role=request.form.get("q")
    return "success"
    # print(role)

@app.route('/get_queries_page')
def get_queries_page():
    # print(role)
    # role=request.form.get("q")
    print(role)
    if(role=='student'):
        return render_template('student.html')
    elif(role=='teacher'):
        return render_template('teacher.html')
    elif(role=='admin'):
        return render_template('admin.html')
        return render_template('login.html')

# @app.route('/get_admin_page',methods=['POST'])
# def get_admin_page():
#     form_input=request.form.get('q')
#     ans=eval(f"{dept}.pass_key")
#     if(form_input==ans):
#         return render_template('admin.html')
#     else:
#         return "Password entered incorrectly"

@app.route('/get_key')
def get_key():
    return eval(f"{dept}.pass_key")

@app.route('/get_dropdown_data', methods=['POST'])
def get_dropdown_data():
    form_input = request.form.get("q")
    #.get("q")
    if form_input == "admin-2":
        # return [1,2,3]
        return eval(f"{dept}.get_teachers()")
    elif form_input == "admin-3":
        return eval(f"{dept}.get_teachers()")
    elif form_input == "admin-5":
        return eval(f"{dept}.get_classes()")
    elif form_input == "admin-6":
        return eval(f"{dept}.get_classes()")
    elif form_input == "admin-8":
        return eval(f"{dept}.get_places()")
    elif form_input == "admin-9":
        return eval(f"{dept}.get_places()")
    elif form_input == "student-1":
        #return [1,2,3]
        return eval(f"{dept}.get_teachers()")
    elif form_input == "student-2":
        return eval(f"{dept}.get_subjects()")
    elif form_input == "student-3":
        return eval(f"{dept}.get_subjects()")
    elif form_input == "student-4":
        return eval(f"{dept}.get_teachers()")
    elif form_input == "student-5":
        return eval(f"{dept}.get_teachers()")
    elif form_input == "student-6":
        return eval(f"{dept}.get_places()")
    elif form_input == "student-7":
        return eval(f"{dept}.get_classes()")
    elif form_input == "student-8":
        return eval(f"{dept}.get_aoi()")
    else:
        return []
    # print(form_input)
    # return jsonify(result=list_data)

@app.route('/admin-form1', methods=['POST'])
def admin_form1():
    teacher_name = request.form.get("teacher_name")
    #.get("teacher_name")
    #username = request.form.get("username")
    
    csv_file = request.files['csv_data']
    csv_f=pd.read_csv(csv_file)
    # .decode('utf-8')
    #print(csv_f.columns)
    # print(teacher_name)
    # print(username)
    # print(csv_file)
    # return "hello"
    return eval(f"{dept}.reg_teacher(teacher_name,csv_f)")
    # ans=
    # return jsonify(result=ans)
    #return "Data received successfully"

@app.route('/admin-form2', methods=['POST'])
def admin_form2() :
    teacher_name = request.form.get("teacher_name")
    return eval(f"{dept}.drop_teacher(teacher_name)")
    #print(teacher_name)
    #return jsonify(result=ans)

@app.route('/admin-form3', methods=['POST'])
def admin_form3():
    teacher_name = request.form.get("teacher_name")
    csv_data = request.form.get("csv_data")
    return eval(f"{dept}.edit_teacher(teacher_name,csv_data)")
    # print(teacher_name)
    # print(csv_data)
    #return jsonify(result=ans)

@app.route('/admin-form4', methods=['POST'])
def admin_form4():
    class_name = request.form.get("class_name")
    csv_data = request.form.get("csv_data")
    return exec(f"{dept}.reg_class(class_name,csv_data)")
    # print(class_name)
    # print(csv_data)
    #return jsonify(result=ans)

@app.route('/admin-form5', methods=['POST'])
def admin_form5():
    class_name = request.form.get("class_name")
    return exec(f"{dept}.drop_class(class_name)")
    #print(class_name)
    #return jsonify(result=ans)

@app.route('/admin-form6', methods=['POST'])
def admin_form6():
    class_name = request.form.get("class_name")
    csv_data = request.form.get("csv_data")
    return exec(f"{dept}.edit_class(class_name,csv_data)")
    # print(class_name)
    # print(csv_data)
    #return "Data received successfully"

@app.route('/admin-form7', methods=['POST'])
def admin_form7():
    place_name = request.form.get("place_name")
    location_name = request.form.get("location_name")
    return exec(f"{dept}.add_place(place_name,location_name)")
    # print(place_name)
    # print(location_name)
    # return "Data received successfully"

@app.route('/admin-form8', methods=['POST'])
def admin_form8():
    place_name = request.form.get("place_name")
    return eval(f"{dept}.del_place(place_name)")
    # print(place_name)
    # return "Data received successfully"

@app.route('/admin-form9', methods=['POST'])
def admin_form9():
    place_name = request.form.get("place_name")
    location_name = request.form.get("location_name")
    return exec(f"{dept}.edit_place(place_name,location_name)")
    # print(place_name)
    # print(location_name)
    # return "Data received successfully"

@app.route('/student-form1', methods=['POST'])
def student_form1():
    teacher_name = request.form.get("teacher_name")
    #.get("teacher_name")
    #username = request.form.get("username")
    #csv_file = request.form.get("csv_data")
    
    # print(teacher_name)
    # print(username)
    # print(csv_file)
    # return "hello"
    return eval(f"{dept}.get_teacher_now(teacher_name)")
    # ans=
    # return jsonify(result=ans)
    #return "Data received successfully"

@app.route('/student-form2', methods=['POST'])
def student_form2() :
    subject_name = request.form.get("subject_name")
    return exec(f"{dept}.get_classes_from_subject(subject_name)")
    #print(teacher_name)
    #return jsonify(result=ans)

@app.route('/student-form3', methods=['POST'])
def student_form3():
    subject_name = request.form.get("subject_name")
    return eval(f"{dept}.get_teachers_from_subject(subject_name)")
    # print(teacher_name)
    # print(csv_data)
    #return jsonify(result=ans)

@app.route('/student-form4', methods=['POST'])
def student_form4():
    teacher_name = request.form.get("teacher_name")
    return exec(f"{dept}.get_tasks_from_teacher(teacher_name)")
    # print(class_name)
    # print(csv_data)
    #return jsonify(result=ans)

@app.route('/student-form5', methods=['POST'])
def student_form5():
    class_name = request.form.get("class_name")
    return exec(f"{dept}.drop_class(class_name)")
    #print(class_name)
    #return jsonify(result=ans)

@app.route('/student-form6', methods=['POST'])
def student_form6():
    place_name = request.form.get("place_name")
    return exec(f"{dept}.get_loc_from_place(place_name)")
    # print(class_name)
    # print(csv_data)
    #return "Data received successfully"

@app.route('/student-form7', methods=['POST'])
def student_form7():
    class_name = request.form.get("class_name")
    # location_name = request.form.get("location_name")
    return exec(f"{dept}.get_class_now(class_name)")
    # print(place_name)
    # print(location_name)
    # return "Data received successfully"

@app.route('/student-form8', methods=['POST'])
def student_form8():
    aoi = request.form.get("aoi")
    return eval(f"{dept}.get_teachers_from_aoi(aoi)")

if __name__ == '__main__':
    app.run(debug=True)
