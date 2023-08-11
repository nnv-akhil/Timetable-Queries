# from sqlalchemy import create_engine,text
# import pandas as pd

# hostname="127.0.0.1"
# dbname="sakila"
# uname="root"
# password="admin"

# # engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=password))
# engine=create_engine(f"mysql+mysqldb://{uname}:{password}@{hostname}/{dbname}").connect()

# # c = engine.raw_connection()
# # cursor = c.cursor()
# # connection = engine.connect()
# # 
# # query='SELECT  FROM hello where period=1'
# query=text('select Monday,Tuesday from hello where Period=1')
# tab=engine.execute(query)
# # print(list(tab.keys()))
# res=tab.fetchall()
# print(type(res[0][0]))
# # tab=pd.read_sql('hello',engine)
# # print(tab[tab.columns[0]])
# # query=text("drop table if exists hello")
# # tab=engine.execute(query)
# # print(tab)


import pickle

class temp:
    def __init__(self):      
        self.l=[0]
    def res(self):
        return self.l
    def change(self):
        self.l=[1,2]
a=temp()

# print(a.res())
f = open('store.pckl', 'wb')
pickle.dump(a, f)
f.close()


f = open('store.pckl', 'rb')
obj = pickle.load(f)
print(obj.l)
obj.change()
f.close()


# f = open('store.pckl', 'wb')
# pickle.dump(obj, f)
# f.close()

# f = open('store.pckl', 'rb')
# x = pickle.load(f)
# print(x.l)
