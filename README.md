# Todo List Flask Application

This is a simple Todo List application built using Flask, MongoDB, and Docker. The application allows users to add and delete tasks with a title and description. The data is stored in a MongoDB database, which is managed using Docker containers.

## Project Structure

.
├── static/ <br>
│&emsp;└── css/ # Stylesheets <br>
├── templates/ <br>
│&emsp;└── index.html # Frontend HTML for the application <br>
├── application.py # Main Flask application file <br>
├── readme.md # Documentation for the project <br>
├── requirements.txt # Python dependencies <br>
├── Dockerfile # Dockerfile to build the Flask app image <br>
├── docker-compose.yaml # Docker Compose to orchestrate Flask app and MongoDB <br>
├── .gitignore # Files to ignore in Git <br>
└── .dockerignore # Files to ignore in Docker build <br>

## Prerequisites

Make sure you have the following installed:

- Git
- Docker (v19.03.0+)
- Docker Compose (v1.25.0+)

## Getting Started

### Clone the Repository

To get started, clone the repository to your local machine:

```
git clone https://github.com/TanushMM/Dockerized_ToDoList_Python.git
cd Dockerized_ToDoList_Python

```

### Build and Run with Docker Compose

You can use Docker Compose to build and run the application. Make sure you are in the project directory where the `docker-compose.yaml` file is located.

Run the following command to build and start the containers:

```
docker-compose up --build

```

This command will:

- Build the Flask application container.
- Pull the MongoDB image from Docker Hub.
- Start both the Flask app and MongoDB containers.

### Access the Application

Once the containers are up and running, you can access the application by opening your web browser and navigating to:

```
http://localhost:5000

```

### Stopping the Containers

To stop the running containers, press Ctrl+C in the terminal where the containers are running, or run:

```
docker-compose down

```

## Project Files Overview

- `application.py`: The main Python file that initializes the Flask application and handles routes for adding and deleting tasks.
- `index.html`: The template used for rendering the home page with tasks displayed in a list format.
- `Dockerfile`: The Dockerfile that specifies how to build the Flask application container.
- `docker-compose.yaml`: The Docker Compose configuration file that orchestrates the Flask and MongoDB containers.

## Customization

- If you need to change the database name or modify the port for Flask, update `application.py` and the `docker-compose.yaml` file accordingly.
- You can style the application by adding custom CSS files inside the `static/css` directory.

## Requirements

All necessary Python packages are listed in `requirements.txt`. These packages will be installed automatically when the Docker container is built.

```
Flask
pymongo
```

## Notes

- Persistence: MongoDB data will persist even after restarting the containers since it's stored in the Docker volume (todolist-volume).
- Port Mapping: The application will be available on port 5000. Ensure this port is available on your host machine.

## Conclusion

This application is a simple demonstration of using Flask with MongoDB in a Dockerized environment. Feel free to extend the functionality and customize the UI as per your needs!
