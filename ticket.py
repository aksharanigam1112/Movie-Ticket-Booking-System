from flask import Flask,jsonify,request
from datetime import datetime
import json
from flask_pymongo import PyMongo
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/akshara"
app.config["DEBUG"] = True
mongo = PyMongo(app)
ticket = mongo.db.tickets

sched = BackgroundScheduler(daemon=True)

@sched.scheduled_job('interval', minutes=60)
def removeExpired():

    curr_time_hrs = datetime.now().strftime("%H")
    curr_time_mins = datetime.now().strftime("%M")
    tkts = ticket.find({})

    for t in tkts :
        time_booked_hrs = t['time'].split(':')[0]
        time_booked_mins = t['time'].split(':')[1]
        diff = 0

        if(curr_time_mins < time_booked_mins) :
            curr_time_mins+=60
            curr_time_hrs-=1
            diff += (float(curr_time_mins)-float(time_booked_mins))/60

        diff += float(curr_time_hrs) - float(time_booked_hrs)

        if(diff >= 8):
            ticket.delete_one({'name':t['name']})


def checkTicketCount(t=0):
    tickets = ticket.find({})
    count=t
    for i in tickets:
        count+=i['tickets']

    if(count>20):
        return False
    else:
        return True

# Initial API call
@app.route('/',methods=['GET'])
def home():
    return jsonify({'msg' : 'Welcome to Ticket Booking System',
                    'status' : 200}),200

# API for Booking a ticket
@app.route('/book',methods=['POST'])
def book():
    data = json.loads(request.get_data())
    try :
        count = 0
        ticket_data = ticket.find({})

        for i in ticket_data:
            count = i['ticketID']

        data['ticketID'] = count+1
        flag = checkTicketCount(int(data['tickets']))

        if(flag==True):
            ticket.insert(data)
            return jsonify({'msg' : 'Booked successfully',
                            'status' : 200 }),200
        else:
            return jsonify({'msg':'More than 20 tickets cannot be booked',
                           'status' : 400}),400

    except Exception as e :
        return jsonify({'msg' : str(e),
                        'status' : 500}),500

# API for Updating the time of a ticket
@app.route('/update',methods=['PUT','PATCH'])
def update_time():
    data = json.loads(request.get_data())
    try :
        name = data['name']
        new_time = data['time']

        ticket.find_one_and_update({'name': name},{'$set' : {'time' : new_time}})
        return jsonify({'msg':'Updated successfully',
                        'status':200}),200

    except Exception as e:
        return jsonify({'msg' : str(e),
                        'status':500}),500

# API for deleting a particular ticket
@app.route('/delete/<name>',methods=['DELETE'])
def delete(name):
    try :
        ticket.delete_one({'name':name})
        return jsonify({'msg':'Deleted successfully',
                        'status' : 200}),200

    except Exception as e:
        return  jsonify({'msg' : str(e),
                         'status':500}),500

# API to view ticket information of a user
@app.route('/view/<ticket_id>',methods=['GET'])
def viewUserTicket(ticket_id):
    try :
        ticketInfo = ticket.find_one({'ticketID' : int(ticket_id)},{'_id' : 0})
        return jsonify({'info' : ticketInfo,
                        'status':200}),200

    except Exception as e:
        return jsonify({'msg' : str(e),
                        'status':500}),500

# API to view all the booked tickets
@app.route('/view',methods=['GET'])
def viewAllTickets():
    try :
        data = []
        tickets = ticket.find({},{'_id':0,'ticketID':0})
        for t in tickets :
            data.append(t)
        return jsonify({'AllTickets' : data,
                        'status':200}),200

    except Exception as e :
        return jsonify({'msg':str(e),
                        'status':500}),500

sched.start()
if __name__ == "__main__":
    app.run()

