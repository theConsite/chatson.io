from flask import Flask, render_template,request,session,redirect,url_for,jsonify
import sqlite3
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'

def send_mess(user_number,chat, key,mess_counter_current):
    conn = sqlite3.connect('sqlite.db')
    c = conn.cursor()
    mess_counter_current=str(int(mess_counter_current)+1)
    to_execute=(user_number,chat,key,mess_counter_current)
    c.execute("INSERT INTO chat_table ( user_number,   chat,  [key],  mess_counter    )  VALUES (?, ?, ?,?    );",to_execute )

    conn.commit()
    conn.close()
    return mess_counter_current
def get_mess(user_number,key,mess_counter_current):
    conn = sqlite3.connect('sqlite.db')
    c = conn.cursor()
    key=(key,)
    c.execute("SELECT user_number,chat,key,mess_counter FROM chat_table  where  key=?;",key)
    rows = c.fetchall()
    tab=[]
    for row in rows:
        tab.append(row)
    conn.commit()
    conn.close()
    return tab

def prepare_mess(messeges):
    for i in messeges:
        dic_to_add={"user":list(i)[:-2][0],"mess":list(i)[:-2][1]}
        session["messgeges"].append(dic_to_add)

@app.route('/enter', methods=['GET', 'POST'])
def init():
    if request.method =="POST": 
        session["key"]=request.form.get("key_id")
        if session["key"][-1] == "2":
            session["user"]="2"
            session["key"]=session["key"][:-1]+"1"
        else:
            session["user"]="1"
        session["mess_counter_current"]=1
        session["messgeges"]=[]
    return  render_template("enter.html")



@app.route('/chat', methods=["GET",'POST'])
def sessions():
    if request.method =="POST": 
        print("Post")
        chat_mess=request.form.get('chat_mess')
        if chat_mess =="":
            return render_template('chat.html',error="You can't send blank mess!")
        else:
            # send mess
            send_mess(session["user"],chat_mess,session["key"],str(session["mess_counter_current"]))
            # messeges=get_mess(session["user"],session["key"],str(session["mess_counter_current"]))
            session["mess_counter_current"]+=1
            # prepare_mess(messeges)
        
    return render_template('chat.html')

@app.route('/chat_check', methods=['GET', 'POST'])
def check_chat():
        messeges=get_mess(session["user"],session["key"],str(session["mess_counter_current"]))
        prepare_mess(messeges)
        return jsonify(session["messgeges"])