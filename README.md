# Movie Ticket Booking System

A REST API interface for booking tickets

### Assumptions :-

* A maximum of 20 tickets can be booked.
* A ticket is marked expired if there is a difference of 8 hours or more between the ticket timing and current time.
* A user can book more than 1 seat and has to provide the seat numbers too.


### Installing Libraries :-
    
    pip install -r requirements.txt


### Run the code :-
    
    export FLASK_APP=ticket.py
    flask run
   
   
### API Calls & Screenshots :-

> ***GET Request ===> http://127.0.0.1:5000/  ===>  {'msg' : 'Welcome to Ticket Booking System', 'status' : 200}***
    
    Initial Call to the API

![Home](/API_screenshots/Home.png)



> ***POST Request ===> http://127.0.0.1:5000/book ===>  {'msg' : 'Booked successfully', 'status' : 200}***
    
    To book a Ticket the user provides name, phone number, time, date, number of tickets to be booked and seat numbers. After which a ticket ID is alloted to the user. If an exception is raised the API returns with status code 400 

![Booking Ticket](/API_screenshots/Book-ticket.png)


![Database View](/API_screenshots/Database-view.png)



> ***GET Request ===> http://127.0.0.1:5000/view/<ticket_id> ===>  {'info' : ticketInfo, 'status' : 200}***
    
    To view a ticket information for the given ticket ID. If an exception is raised the API returns with status code 500

![Viewing a particular Ticket](/API_screenshots/View-ticketID.png)



> ***GET Request ===> http://127.0.0.1:5000/view ===>  {'AllTickets' : data, 'status' : 200}***
    
    To view All the tickets at a particular time. If an exception is raised the API returns with status code 500

![View all tickets](/API_screenshots/View-all-tickets.png)



> ***PUT/PATCH Request ===> http://127.0.0.1:5000/update ===>  {'msg' : 'Updated successfully', 'status' : 200}***
    
    To update the time of a booked ticket. If an exception is raised the API returns with status code 500.

![Update time of a ticket ID](/API_screenshots/Updation.png)


![Database Change after updation](/API_screenshots/After-update-db.png)



> DELETE Request ===> http://127.0.0.1:5000/delete/<name>  ===>  {'msg' : 'Deleted successfully', 'status' : 200}
    
    To delete a ticket for a given user name. If an exception is raised the API returns with status code 500.

![Delete a ticket](/API_screenshots/Deletion.png)



![Database Change after deletion](/API_screenshots/After-deletion-db.png)



> ***Expired Tickets Handling***
        
        To mark the expired tickets a background scheduling is done.

![Scheduler](/API_screenshots/Schedule-task.png)

