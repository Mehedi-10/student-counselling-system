
# SCS: API

This README will guide you through setting up the Django REST Framework project locally and navigating to Swagger UI to explore the available APIs.

## Requirements

- Python (3.8 or later)
- Django (3.x or later)
- Django REST Framework
- drf-yasg (for Swagger UI)

## Initial Setup

1. **Clone the Repository**
   - Clone this repository to your local machine using:
     ```
     git clone <repository-url>
     ```
   - Navigate into the project directory:
     ```
     cd <project-directory>
     ```

2. **Create a Virtual Environment**
   - For Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - For macOS and Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**
   - Install the required Python packages using:
     ```
     pip install -r requirements.txt
     ```

4. **Database Setup**
   - Migrate the database to prepare the schema:
     ```
     python manage.py migrate
     ```

5. **Create a Superuser**
   - Create an admin user for accessing the Django admin panel:
     ```
     python manage.py createsuperuser
     ```
   - Follow the prompts to create the user.

## Running the Project

- Start the Django development server:
  ```
  python manage.py runserver
  ```
- The server will start running on http://127.0.0.1:8000 by default.

## Accessing Swagger UI

- To explore the API with Swagger UI, navigate to:
  ```
  http://127.0.0.1:8000/swagger/
  ```
- This page will display all the available API endpoints with their details. You can expand each endpoint to see request and response formats and even try out the API calls directly from the browser.

## Using the API

- **Authentication**: To use endpoints that require authentication, you must first obtain a token via the login endpoint. Use the provided credentials to log in through the Swagger UI.
- **Endpoints**: Each endpoint can be tested directly from Swagger by filling in the required fields and executing the requests.
- **Responses**: The responses, including data and potential error messages, will be displayed directly in the Swagger UI.

## Additional Resources

- **Django Documentation**: https://www.djangoproject.com/
- **Django REST Framework Documentation**: https://www.django-rest-framework.org/
- **drf-yasg Documentation**: https://drf-yasg.readthedocs.io/en/stable/

Feel free to contact the backend team if you encounter any issues or have questions regarding the API functionalities.

---

This README provides a comprehensive guide for a frontend developer to set up the DRF project locally, run it, and use Swagger UI to interact with the API, helping them understand and utilize the endpoints effectively for frontend development.