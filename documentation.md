### Overview
Our Django backend manages user authentication through a custom token-based system. This system supports two types of users: students and teachers. The frontend needs to handle registration, login, and subsequent authenticated requests to the server.

### Registration
**Endpoint:** `/register/`
- **Method:** POST
- **Data Required:**
  - `email`: User's email (must be unique)
  - `password`: User's password
  - `confirm_password`: Confirmation of the password
  - `user_type`: Either "student" or "teacher"
- **Success Response:** 
  - **Code:** 201 (Created)
  - **Content:** `{'message': 'User registered successfully'}`
- **Error Response:** 
  - **Code:** 400 (Bad Request)
  - **Content:** Error message explaining what went wrong (e.g., "Passwords do not match")
  
**Example Payload:**
```json
{
  "email": "user@example.com",
  "password": "securepassword123",
  "confirm_password": "securepassword123",
  "user_type": "student"
}
```

### Login
**Endpoint:** `/login/`
- **Method:** POST
- **Data Required:**
  - `email`: User's email
  - `password`: User's password
- **Success Response:**
  - **Code:** 200 (OK)
  - **Content:** 
    - `token`: Authentication token to be used for subsequent requests
    - `expires_in`: Token expiration time in seconds
    - `user_type`: Indicates whether the user is a "student" or "teacher"
- **Error Response:**
  - **Code:** 401 (Unauthorized)
  - **Content:** `{'error': 'Invalid credentials'}`

**Example Payload:**
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

### Accessing Protected Routes (e.g., Home Page)
**Endpoint:** `/home/`
- **Method:** GET
- **Headers Required:**
  - `Authorization`: "Token <user_token_here>"
- **Success Response:**
  - **Code:** 200 (OK)
  - **Content:** `{'message': 'Welcome, [Teacher/Student] <email>!'}`
- **Error Response:**
  - **Code:** 401 (Unauthorized)
  - **Content:** Depending on the error, it may indicate that the token is missing, invalid, or expired.

### Recommendations for Frontend Development
- **Handle Authentication State:** Ensure the frontend maintains the user's authentication state, storing the token securely (e.g., in sessionStorage) and sending it with each request to protected endpoints.
- **Manage Token Expiry:** Implement logic to handle token expiration effectively. This could involve prompting the user to log in again or automatically refreshing the token if your backend supports it.
- **Security Considerations:** Ensure all communications with the backend are performed over HTTPS to secure data in transit. Do not store sensitive information in local storage.
- **Error Handling:** Implement robust error handling to provide clear feedback to the user for different scenarios like network issues, login failures, or data validation errors.

This summary outlines the key interactions the frontend needs to manage and provides enough detail to ensure that the frontend and backend can be integrated smoothly.