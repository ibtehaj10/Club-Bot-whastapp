# req libraries
import streamlit as st
import time
import mysql.connector
import webbrowser
from streamlit_autorefresh import st_autorefresh
import random

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
# db connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="clubbot"
)

# functions 
def get_all():
    mycursor = mydb.cursor()
    sql = "SELECT `id`, `number`, `name`, `seat`, `song`, `time`, `status`, `ques1`, `ques2` , `alldone`FROM `club` WHERE  `status` = 0"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def get_by_seat(seatno):
    mycursor = mydb.cursor()
    sql = "SELECT `id`, `number`, `name`, `seat`, `song`, `time`, `status`, `ques1`, `ques2` , `alldone`FROM `club` WHERE `seat` = {} and `status` = 0".format(seatno)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def search(song):
        rep = song.replace(" ", "+")
        url = "https://www.youtube.com/results?search_query={}".format(rep)
        # st.markdown(body=song)
        webbrowser.open_new_tab(url)

def dele(sid):
            mycursor = mydb.cursor()
            sql = "UPDATE `club` SET `status`=1 WHERE `id` = {}".format(sid)
            mycursor.execute(sql)
            mydb.commit()
            st_autorefresh()
        
def get_random():
    all = get_all()
    random.shuffle(all)
    return all

# elements
options = [i for i in range(0,23)]

table  = st.sidebar.selectbox('Check Song request according to Table Number',options)
contain = st.container()
contain.write("Recording According to Table Number")
col,col1, col2, col3,col4,col5 = contain.columns(6)
col.header("Sno")
col1.header("Name")
col2.header("Song")
col3.header("Table")
col4.header("Play")
col5.header("Played")
x = 0

if table == 0:
    myresult = get_all()
else:
    myresult = get_by_seat(table)

btn = st.sidebar.button('Generate random')
if btn:
    myresult = get_random()

for i in range(len(myresult)):
    sname = myresult[i][2]
    song = myresult[i][4]
    table = myresult[i][3]
    col.write(str(i+1))
    col1.write(sname)
    col2.write(song)
    col3.write(str(table))
    # unsafe_allow_html=True
    x+= 1
    btncol4 = col4.button('search',key="a"+str(x))
    if btncol4:
        search(song)
    x+= 1
    btncol5 = col5.button('mark as played',key="a"+str(x))
    if btncol5:
        dele(myresult[i][0])
