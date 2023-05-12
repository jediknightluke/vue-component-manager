# Vue Component Manager

This project consists of a Django backend and a Vue.js frontend that work together to manage and display chess components. The project is organized into two main directories, `django_app` and `vue_app`.

## Project Structure

/vue-component-manager
/django_app
/vue_app

### Django App (API)

The `django_app` directory contains the Django project that serves as the API for the Vue.js frontend. It is responsible for managing the database and handling all server-side logic.

#### Requirements

- Python 3.x
- Django 4.x
- PostgreSQL
- Django Rest Framework
- Python-dotenv

### Vue App (Frontend)

The `vue_app` directory contains the Vue.js project that serves as the frontend for the application. It interacts with the Django API to fetch, display, and manage chess components.

#### Requirements

- Node.js
- Vue.js
- Axios
- Vue Router
- Vuetify

## Getting Started

1. Clone the repository.

```bash
git clone https://github.com/jediknightluke/vue-component-manager.git
Create .env files for both the Django and Vue projects with appropriate settings (see .env.example files in each directory).
Navigate to the project root directory and build the Docker images.
bash
Copy code
cd vue-component-manager
docker-compose build
Start the Docker containers.
bash
Copy code
docker-compose up
Now, the Django API should be running at http://localhost:2550/ and the Vue frontend should be running at http://localhost:8081/.
```
