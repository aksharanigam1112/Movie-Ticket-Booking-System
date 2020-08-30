from flask import Flask,jsonify,request,Response
from bson.json_util import dumps
import json
import random
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/akshara"
app.config["DEBUG"] = True
mongo = PyMongo(app)
ticket = mongo.db.tickets

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
    return jsonify({'msg' : 'Welcome to Ticket Booking System'}),200

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
            return jsonify({'msg' : 'booked successfully'}),200
        else:
            return jsonify({'msg':'More than 20 tickets cannot be booked'}),200

    except Exception as e :
        return jsonify({'msg' : str(e)}),500

# API for Updating the time of a ticket
@app.route('/update',methods=['POST'])
def update_time():
    data = json.loads(request.get_data())
    try :
        name = data['name']
        new_time = data['time']

        ticket.find_one_and_update({'name': name},{'$set' : {'time' : new_time}})
        return jsonify({'msg':'updated successfully'}),200

    except Exception as e:
        return jsonify({'msg' : str(e)}),500

# API for deleting a particular ticket
@app.route('/delete/name',methods=['POST'])
def delete(name):
    try :
        ticket.delete_one({'name':name})
        return jsonify({'msg':'deleted successfully'}),200

    except Exception as e:
        return  jsonify({'msg' : str(e)}),500

# API to view ticket information of a user
@app.route('/view/<ticket_id>',methods=['GET'])
def viewUserTicket(ticket_id):
    try :
        ticketInfo = ticket.find_one({'ticketID' : int(ticket_id)},{'_id' : 0})
        return jsonify({'info' : ticketInfo}),200

    except Exception as e:
        return jsonify({'msg' : str(e)}),500

# API to view all the booked tickets
@app.route('/view',methods=['GET'])
def viewAllTickets():
    try :
        data = []
        tickets = ticket.find({},{'_id':0,'ticketID':0})
        for t in tickets :
            data.append(t)
        return jsonify({'AllTickets' : data}),200

    except Exception as e :
        return jsonify({'msg':str(e)}),500

# API to remove all the expired tickets
@app.route('/expired',methods=['GET'])
def removeExpired():
    pass

if __name__ == "__main__":
    app.run() 