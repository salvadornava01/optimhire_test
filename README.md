# Technical Challenge

The following are the instructions for running the project. This project runs requires python 3.9.

## Installation

Use the package manager [pipenv](https://pypi.org/project/pipenv/) to install the project, and configure environment vars:

```bash
pipenv install

export DEBUG=true
export DJANGO_SETTINGS_MODULE=optimhiretest.settings
export PYTHONUNBUFFERED=1
```

## Usage

Activate virtual environment:

```bash
pipenv shell
```
Then go to src folder, and run the project via manage.py runserver command:

```bash
python manage.py runserver
```

The API is now running on Port 8000 at localhost.

## Resources

You can test the API using postman, you can import it from the project or run it directly from: [here](https://www.postman.com/warped-crater-215855/workspace/optimhire/request/12574810-e7e95582-f00d-4438-b6e0-d6b303a818d6)

You'll find 7 requests inside the collection:


### Create a Room

Create a room with N capacity
```json
POST /api/room/

body

{
    "capacity": 46
}
```

### Retrieve Rooms

List all created rooms
```
GET /api/room/
```

### POST Event

List all public events
```json
POST /api/room/{room-id}/event/

path params: "room-id" id of the room where the event is going to be created

body

{
    "date": "2022-08-27",
    "type": "public"
}

```


### Retrieve Public Events

List all public events
```
GET /api/room/event
```


### Book a Place

Create a booking for a place in a public event
```json
POST /api/room/{room-id}/event/{event-id}/book/?customer_id={customer-id}

path params: 

"room-id" the id of the room
"event-id" the id of the event

query-params:
"customer-id" an identifier for a customer

body

{
    "requested_capacity": 300
}

```
### Retrieve all Booked Places
List all booked places
```json
GET /api/room/event/book/
```

### Cancel a Booked Place
Cancel a Place that's already booked
```json
DELETE /api/room/event/book/{book-id}/?customer_id={customer-id}
```

