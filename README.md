# Movie Ticket Booking System

A REST API interface for booking tickets

### Assumptions :-

* A maximum of 20 tickets can be booked.
* A ticket is marked expired if there is a difference of 8 hours or more between the ticket timing and current time.
* A user can book more than 1 seat and has to provide the seat numbers too.

### API Calls & Screenshots :-

> ***GET Request ===> http://127.0.0.1:5000/  ===>  {'msg' : 'Welcome to Ticket Booking System', 'status' : 200}***


![Home](/API_screenshots/Home.png)



> ***POST Request ===> http://127.0.0.1:5000/book ===>  {'msg' : 'Booked successfully', 'status' : 200}***


![Booking Ticket](/API_screenshots/Book-ticket.png)


![Database View](/API_screenshots/Database-view.png)



> ***GET Request ===> http://127.0.0.1:5000/view/<ticket_id> ===>  {'info' : ticketInfo, 'status' : 200}***


![Viewing a particular Ticket](/API_screenshots/View-ticketID.png)



> ***GET Request ===> http://127.0.0.1:5000/view ===>  {'AllTickets' : data, 'status' : 200}***


![View all tickets](/API_screenshots/View-all-tickets.png)



> ***PUT/PATCH Request ===> http://127.0.0.1:5000/update ===>  {'msg' : 'Updated successfully', 'status' : 200}***


![Update time of a ticket ID](/API_screenshots/Updation.png)


![Database Change after updation](/API_screenshots/After-update-db.png)



> ***DELETE Request ===> http://127.0.0.1:5000/delete/<name>  ===>  {'msg' : 'Deleted successfully', 'status' : 200}


![Delete a ticket](/API_screenshots/Deletion.png)



![Database Change after deletion](/API_screenshots/After-deletion-db.png)

