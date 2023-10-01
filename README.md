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

## Metrics and Monitoring

1. Here are three additional metrics that are critical for understanding the health and performance of an end-to-end system:
    - Error Rate: This metric indicates the percentage of requests that are resulting in errors. A high error rate can indicate issues with application logic or third-party services, and can impact user experience and revenue.
    - Response Time: This metric measures the time it takes for the application to respond to a given request. A high response time can lead to slow or unresponsive applications and negatively impact user experience.
    - Throughput: This metric measures the number of requests that the application is processing per unit time. High throughput is a good indicator of the scalability of the application, but can also indicate potential bottlenecks in the system.

2. A visualization tool like Grafana can be utilized to display these metrics. Grafana is an open-source visualizing tool that supports a wide range of data sources, including many cloud-based metrics and logging services. The metrics can be displayed over time using a line graph, with a separate line for each metric. This can help identify trends in the system's health and performance. For example, a trend of increasing error rates could indicate a problem that needs to be addressed.

3. To implement Grafana in the cloud, the tool would need to be configured to collect metrics from different sources, such as custom application metrics, CloudWatch metrics, Log metrics, or Prometheus metrics. Integrating it with traditional systems like VMs requires manual configuration and integration, while container-based systems like Kubernetes can dynamically integrate with monitoring tools like Grafana using service discovery and label selectors.

4. When scaling the system to 50 similar systems, a metric like cross-system error rate and latency could be added to the visualization. This helps identify if there are common issues manifesting in multiple systems. Additionally, visualization methods like heat maps, histograms, and scatter plots could be used to identify anomalies and correlations between metrics across the multiple systems.

5. A limitation that we might face is the overhead required to collect and store metrics at scale. Metrics can be resource-intensive and require significant storage and processing power to collect data across multiple systems. One approach to address this issue is to integrate metrics collection and analysis into the application code, which can reduce network overhead by avoiding a separate service call for metrics. Additionally, configuring selective sampling of metrics can help mitigate the scalability issue. However, selectively sampling metrics may lead to incomplete data collection and potential false decisions.

## Next steps

This app is a simple example of how to build a REST API with Python and FastAPI. It can be used as a starting point for building more complex applications. Here are some ideas for how to extend this app:

1. Deploy the application to a development environment. This will allow you to test the application in an environment that is isolated from your production environment. You can use a tool like Docker Compose to create a local development environment, or deploy the application to a cloud-based development environment like Google Cloud Shell or AWS Cloud9.

2. Add automated functional and integration tests to your CI/CD pipeline. These tests will ensure that the API endpoints are working as expected, and can help catch issues before they reach production.

3. Set up a staging environment. This will allow you to test your application in an environment that is more production-like than your development environment, but still isolated from production. You can use a tool like Terraform to create a staging environment that matches your production environment as closely as possible.

4. Implement continuous deployment to your staging environment. This will allow you to deploy changes to your staging environment automatically whenever tests pass in your CI/CD pipeline.

5. Use a tool like Istio or Cloud Endpoints to manage traffic to and from your application. These tools add features like traffic routing, load balancing, and API gateway functionality.

6. Monitor your application's logs and metrics to identify any issues quickly. This can be done using a tool like Stackdriver or Elasticsearch/Kibana.

7. When you're ready to deploy to production, create a new production environment that is identical to your staging environment. Use a tool like Terraform to create the environment, and run your CI/CD pipeline to deploy the latest code changes automatically.

8. Set up alerting and monitoring for your production environment to ensure you're quickly notified of any issues that arise.

By following these steps, you can deploy your Car Info API app with confidence, knowing that it has been thoroughly tested and monitored at each stage of the deployment process.
