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

## IaC - Infrastructure as Code

To manage the infrastructure for this app, I used Terraform. Terraform is an open-source tool that allows you to define your infrastructure as code, and then use that code to create, modify, and destroy your infrastructure resources.

1. Install Terraform on your local machine. You can download Terraform from the official website at <https://www.terraform.io/downloads.html>.

2. Set up your cloud provider account. For example, if you're using Google Cloud Platform (GCP), you'll need to create a new project and enable the Compute Engine API. You'll also need to create and download a service account key with appropriate permissions to manage resources in your GCP account.

3. Create a directory to hold your Terraform configuration files.

4. Create a new file named `provider.tf` in the directory, and add the following code:

```terraform
provider "google" {
  credentials = "${file("path/to/your/key.json")}"
  project     = "your-project-id"
  region      = "us-central1"
}

```

This code sets the provider to `google` and specifies the GCP project ID, region, and the path to the service account key that enables Terraform to manage resources in your GCP account.

5. Add any additional `.tf` files for other resources you want to manage with Terraform (e.g. `compute.tf` to create a new virtual machine instance).

6. Initialize the Terraform project by running the command `terraform init` in the directory. This downloads and installs any necessary provider plugins for the specified provider (in this case, Google Cloud).

7. Run the command `terraform plan` to see what changes Terraform will make to your infrastructure resources, without actually creating or modifying anything.

8. If you're satisfied with the plan, run the command `terraform apply` to apply the changes to your resources.

By following these steps, you can set up Terraform to manage your cloud infrastructure easily and efficiently. Remember to always test your code thoroughly before applying any changes to your infrastructure.
