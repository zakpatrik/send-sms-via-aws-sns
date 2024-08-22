
# SMS via SNS

## Project Description

SMS via SNS is a simple web application written in Python using the Flask framework. The application allows users to send SMS messages using the AWS SNS (Simple Notification Service). Users can input a phone number, a message, select a Sender ID, and if the number is from the USA, they must also enter an Origination Number.

## Technologies

- **Python**: The primary programming language for the application.
- **Flask**: A web framework for Python.
- **Bootstrap**: A CSS framework for modern web design.
- **AWS SNS**: A service for sending SMS messages.
- **Docker**: Containerization of the application for easy deployment.
- **Gunicorn**: A WSGI HTTP server for running the application in a production environment.

## Prerequisites

Before setting up the application, make sure you have the following installed:

- Docker and Docker Compose
- An AWS account with permissions to use AWS SNS

## Installation and Setup

### 1. Clone the Repository

First, clone this repository to your local environment:

```bash
git clone https://github.com/zakpatrik/send-sms-via-aws-sns.git
cd send-sms-via-aws-sns
```

### 2. Environment Configuration

#### Option 1: Mounting the `.aws` Directory

Mount your `.aws` directory as a volume to give the container access to your AWS credentials:

```yaml
# docker-compose.yml
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./app:/app
      - ~/.aws:/root/.aws:ro
```

#### Option 2: Using Environment Variables

If you prefer not to use a volume, you can set AWS credentials directly in the `docker-compose.yml` file:

```yaml
# docker-compose.yml
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./app:/app
    environment:
      - AWS_ACCESS_KEY_ID=your_access_key
      - AWS_SECRET_ACCESS_KEY=your_secret_key
      - AWS_DEFAULT_REGION=your_default_region
```

### 3. Build and Run the Application

Build and run the Docker container:

```bash
docker-compose up --build
```

The application will be available at `http://localhost:5000`.

## Usage

1. Open your web browser and navigate to `http://localhost:5000`.
2. Fill in the form fields:
   - **Phone Number**: Enter the phone number including the country code.
   - **Message**: Enter the message you want to send.
   - **Sender ID**: Select a Sender ID from the dropdown (e.g., SERVERADMIN or SERVERALERT).
   - **Origination Number**: If the phone number is from the USA, enter the Origination Number.
3. Click the **Send SMS** button.

## Debugging

If you encounter any issues, check the container logs:

```bash
docker-compose logs
```

## Deployment

The application is ready for deployment in a production environment using Docker. To deploy on a server, simply transfer the Docker image and run the container.

## Contributions

If you'd like to contribute to this project, feel free to open an issue or submit a pull request.

