import os
import logging
from unicodedata import name
from heyoo import WhatsApp
# from dotenv import load_dotenv
from flask import Flask, request, make_response
import mysql.connector
import datetime
# Initialize Flask App
app = Flask(__name__)
# Load .env file
# load_dotenv()
id ="100406429479899"
token = "EAAFcZBbRweewBAMTqwPawsyrKhtepqsXniNeZA72Wq1F1iE7v779xT6Jy9NtNL8uL1wiab8MUsZBnalIQfqVIgzA1DNFGCu3SFSk3QOArmZBS32geN1TtiZCd0FkKhW8PUZBKuM1VAhMUeNHzllOf0Opkmv8uTDFVGKTIQDhRm9Bas4At3V52FB21oGCPhOM87E76rr4iZCUAZDZD"
messenger = WhatsApp(token=token, phone_number_id=id)
VERIFY_TOKEN = "helloworld"

# Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="clubbot"
)


# quest = 0
@app.route("/", methods=["GET", "POST"])
def hook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            logging.info("Verified webhook")
            response = make_response(request.args.get("hub.challenge"), 200)
            response.mimetype = "text/plain"
            return response
        logging.error("Webhook Verification failed")
        return "Invalid verification token"

    # Handle Webhook Subscriptions
    data = request.get_json()
    logging.info("Received webhook data: %s", data)
    changed_field = messenger.changed_field(data)

    quest = 0
    if changed_field == "messages":
       
       
        new_message = messenger.get_mobile(data)
        message_type = messenger.get_message_type(data)
        mobile = messenger.get_mobile(data)
        try:
            sname = messenger.get_name(data)
        except:
            pass
        message = messenger.get_message(data)
        greet = ["hi","Hi","hello","Hello","hey","Hey"]
        if message_type == "text":
            # if message in greet:
            mycursor = mydb.cursor()

            sql = "SELECT `id`, `number`, `name`, `seat`, `song`, `time`, `status`, `ques1`, `ques2` , `alldone`FROM `club` WHERE `number`= {}".format(mobile)

            mycursor.execute(sql)

            myresult = mycursor.fetchall()
            # last = myresult[-1]
            if myresult != []:
                res = myresult[-1]
                print(res)
                
                
                # if res[3] == 0 and res[4] == "":
                if res[7] == 0:
                    messenger.send_message("please tell your Table number",mobile)
                    mycursor = mydb.cursor()

                    sql = "UPDATE `club` SET `ques1`= {} WHERE `id` = {}".format(1,res[0])
                    # val = ("John", "Highway 21")
                    mycursor.execute(sql)
                    print("\nquest DONE \n")
                    mydb.commit()
                    mycursor = mydb.cursor()

                    sql = "SELECT `id`, `number`, `name`, `seat`, `song`, `time`, `status`, `ques1`, `ques2`, `alldone` FROM `club` WHERE `number`= {}".format(mobile)

                    mycursor.execute(sql)

                    myresult = mycursor.fetchall()
                    if myresult != []:
                        res = myresult[-1]
                        print(res)
                        print("\nnow number is ",res[-2])
                elif myresult[-1][9] == 1:
                    print("new msg")
                    mycursor = mydb.cursor()
                    time = datetime.datetime.now()
                    sql = "INSERT INTO `club`( `number`, `name`, `time`) VALUES ('"+mobile+"','"+sname+"','"+str(time)+"')"
        
                    mycursor.execute(sql)

                    mydb.commit()
                    hook()

                    

                elif res[7] == 1 and res[8] == 0:
                    mycursor = mydb.cursor()
                    sql = "UPDATE `club` SET `seat`={},`ques2`={} WHERE `id` = {}".format(int(message),1,res[0])
                    mycursor.execute(sql)
                    messenger.send_message("please tell your song name",mobile)
                    print("\nSeat added \n")
                    mydb.commit()
                    mycursor = mydb.cursor()

                    sql = "SELECT `id`, `number`, `name`, `seat`, `song`, `time`, `status`, `ques1`, `ques2` , `alldone`FROM `club` WHERE `number`= {}".format(mobile)

                    mycursor.execute(sql)

                    myresult = mycursor.fetchall()
                    if myresult != []:
                        res = myresult[-1]
                        print(res)
                        print("\nnow q2 is ",res[-1])
                
                elif res[8] == 1 and res[4] == "":
                    mycursor = mydb.cursor()
                    sql = "UPDATE `club` SET `song`='"+message+"',`alldone`=1 WHERE `id` = {}".format(res[0])
                    mycursor.execute(sql)
                    
                    
                    print("\ntable added \n")
                    mydb.commit()
                   
                   
                    mycursor = mydb.cursor()

                    sql = "SELECT `id`, `number`, `name`, `seat`, `song`, `time`, `status`, `ques1`, `ques2` FROM `club` WHERE `number`= {}".format(mobile)

                    mycursor.execute(sql)

                    myresult = mycursor.fetchall()
                    thank = "Thank you for joining us your requested song {} will be played shortly".format(message)
                    messenger.send_message(thank,mobile)
                    
                # elif res[9] == 1:
                #     song = res[4]
                    
                else:
                    print("not blank")
                data=[]
                print(message,"is blank")

            elif myresult == [] :
                print("new msg")
                mycursor = mydb.cursor()
                time = datetime.datetime.now()
                sql = "INSERT INTO `club`( `number`, `name`, `time`) VALUES ('"+mobile+"','"+sname+"','"+str(time)+"')"
      
                mycursor.execute(sql)

                mydb.commit()
                hook()


             
            # print(myresult[-1][9])

                
    return "ok"
if __name__ == "__main__":
    app.run(port=5000, debug=True)