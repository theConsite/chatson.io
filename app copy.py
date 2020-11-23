from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from threading import Thread
import sqlite3
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'


def send_mess(user_number, chat, key, mess_counter_current):
    conn = sqlite3.connect('sqlite.db')
    c = conn.cursor()
    mess_counter_current = str(int(mess_counter_current)+1)
    c.execute("INSERT INTO chat_table ( user_number,   chat,  [key],  mess_counter    )  VALUES (" +
              user_number+", '"+chat+"', '"+key+"',   "+mess_counter_current+"    );")
    # rows = c.fetchall()
    # # print(rows)
    # tab=[]
    # for row in rows:
    #     tab.append(row)
    conn.commit()
    conn.close()
    return mess_counter_current


def get_mess(user_number, key, mess_counter_current):
    conn = sqlite3.connect('sqlite.db')
    c = conn.cursor()
    # print("SELECT user_number,chat,key,mess_counter FROM chat_table  where user_number = "+user_number+" and  key='"+key+"' and mess_counter >= "+mess_counter_current+" ;")
    c.execute("SELECT user_number,chat,key,mess_counter FROM chat_table  where  key='" +
              key+"' and mess_counter >= "+mess_counter_current+" ;")
    rows = c.fetchall()
    # print(rows)
    tab = []
    for row in rows:
        tab.append(row)
    conn.commit()
    conn.close()
    return tab


def prepare_mess(messeges):
    for i in messeges:
        dic_to_add = {"user": list(i)[:-2][0], "mess": list(i)[:-2][1]}
        session["messgeges"].append(dic_to_add)
# def check_new_mess():
#     while True:
#         messeges=get_mess(user,key,str(session["mess_counter_current"]))
#         prepare_mess(messeges)
#         try:
#             max_mess_counter=messeges[-1][-1]
#             if max_mess_counter > session["mess_counter_current"]:
#                 session["mess_counter_current"]=max_mess_counter
#                 return render_template('chat.html',messeges=session["messgeges"])
#         except:
#             pass


@app.route('/chat', methods=['GET', 'POST'])
def sessions():
    if request.method == 'GET':
        messeges = get_mess(session["user"], session["key"], str(
            session["mess_counter_current"]))
        try:
            max_mess_counter = messeges[-1][-1]
            if max_mess_counter > session["mess_counter_current"]:
                session["mess_counter_current"] = max_mess_counter
        except:
            pass
        print("get")
    if request.method == 'POST':
        print("Post")
        chat_mess = request.form.get('chat_mess')
        # user_number chat, key
        # if new mess
        # get new mess
        messeges = get_mess(session["user"], session["key"], str(
            session["mess_counter_current"]))
        try:
            max_mess_counter = messeges[-1][-1]
            if max_mess_counter > session["mess_counter_current"]:
                session["mess_counter_current"] = max_mess_counter
        except:
            pass
        # send mess
        send_mess(session["user"], chat_mess, session["key"],
                  str(session["mess_counter_current"]))
        messeges = get_mess(session["user"], session["key"], str(
            session["mess_counter_current"]))
        session["mess_counter_current"] += 1
        # prepare_mess(messeges)
    return render_template('chat.html')


@app.route('/chat_check', methods=['GET', 'POST'])
def check_chat():
    messeges = get_mess(session["user"], session["key"], str(
        session["mess_counter_current"]))
    prepare_mess(messeges)
    try:
        max_mess_counter = messeges[-1][-1]
        if max_mess_counter > session["mess_counter_current"]:
            session["mess_counter_current"] = max_mess_counter
    except:
        pass
    return jsonify(session["messgeges"])
