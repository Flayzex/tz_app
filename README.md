## Installation

Before getting started, make sure you have the following tools installed:

- [Docker](https://www.docker.com/get-started)

## Running the project

1. Clone the repository to your computer:

    ```bash
    git clone https://github.com/Flayzex/tz_app.git
    ```

2. Navigate to the project folder:

    ```bash
    cd tz_app
    ```

3. Run Docker Compose to build and start the containers:

    ```bash
    docker-compose up
    ```

    This command will create and launch Django and PostgreSQL containers. Ensure that port 8000 on your computer is available.

4. Open your web browser and go to:

    ```
    http://localhost:8000/
    ```

    You should now see the running blog.

## Stopping the container

To stop the container, execute the following command in the terminal:

```bash
docker-compose down
