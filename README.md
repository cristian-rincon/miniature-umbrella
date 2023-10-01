# Car Info API

This is a simple API that allows you to create and retrieve information about cars.

## Requirements

To use this app, you need to have Docker and Docker Compose installed on your system.

- [Docker installation guide](https://docs.docker.com/get-docker/)
- [Docker Compose installation guide](https://docs.docker.com/compose/install/)

## Running the app

To run the app, follow these steps:

1. Clone this repository to your local machine:

```
git clone https://github.com/cristian-rincon/car-info-api.git
```

2. Change into the project directory:

```
cd car-info-api
```

3. Run the app with Docker Compose:

```
docker-compose up
```

4. Access the API in your web browser at `http://localhost`. You can use the `/docs` endpoint to access the Swagger UI and test the API.

## API endpoints

### GET /cars/{car_id}

Retrieves information about a car with the given ID.

**Parameters:**

- `car_id`: int - The ID of the car to retrieve (required)

**Response:**

- HTTP 200 OK - The car object with the given ID
- HTTP 404 Not Found - If a car with the given ID does not exist

**Example:**

```
GET /cars/1 HTTP/1.1
Host: localhost

HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 1,
    "make": "Toyota",
    "model": "Corolla",
    "year": 2010
}
```

### POST /cars/

Creates a new car with the given information.

**Parameters:**

- `make`: str - The make of the car (required)
- `model`: str - The model of the car (required)
- `year`: int - The year of the car (optional)

**Response:**

- HTTP 201 Created - The car object that was created
- HTTP 422 Unprocessable Entity - If the request data is invalid

**Example:**

```
POST /cars/ HTTP/1.1
Content-Type: application/json

{
    "make": "Toyota",
    "model": "Corolla",
    "year": 2010
}

HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 1,
    "make": "Toyota",
    "model": "Corolla",
    "year": 2010
}
```

## Updating the app

If you make changes to the app code, you can rebuild the Docker container and restart the app with the following command:

```
docker-compose up --build
```

This will rebuild the app container and start the app with your updated code.

## Stopping the app

To stop the app, press `Ctrl + C` in the terminal where you started the `docker-compose up` command. This will stop and remove the app containers, but will leave the database volume intact (so your data will not be lost).

To completely remove the app and its data, use the following command:

```
docker-compose down -v
```

This will stop and remove the app containers, and also remove the database volume. This will delete all data stored in the database.

