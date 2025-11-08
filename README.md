# Business Review API

A Flask-based REST API for managing businesses and reviews with JWT authentication, built with MongoDB backend and Angular frontend.

## Project Structure

```
idk/
├── app.py                  # Main Flask application
├── globals.py             # Database configuration and global variables
├── decorators.py          # JWT authentication decorator
├── blueprint/
│   ├── auth/
│   │   └── auth.py       # Authentication endpoints
│   ├── businesses/
│   │   └── businesses.py # Business CRUD operations
│   └── reviews/
│       └── reviews.py    # Review management
└── front_end/
    └── bizFE/            # Angular frontend application
```

## Features

- **Authentication**: JWT-based authentication with token blacklisting
- **Business Management**: Create, read, update, and delete businesses
- **Review System**: Add and manage reviews for businesses
- **Pagination**: Support for paginated business listings
- **MongoDB Integration**: NoSQL database for data persistence
- **Angular Frontend**: Modern SSR-enabled Angular application

## Tech Stack

### Backend
- **Flask**: Python web framework
- **MongoDB**: NoSQL database
- **PyMongo**: MongoDB driver for Python
- **JWT**: JSON Web Tokens for authentication
- **bcrypt**: Password hashing

### Frontend
- **Angular 20**: Modern web framework
- **TypeScript**: Type-safe JavaScript
- **SSR**: Server-Side Rendering enabled
- **Zoneless**: Modern Angular architecture

## Prerequisites

- Python 3.x
- MongoDB (running on localhost:27017)
- Node.js 20+ or 22+ (LTS version)
- npm 10+

## Installation

### Backend Setup

1. Install Python dependencies:
```bash
pip install flask pymongo bcrypt pyjwt
```

2. Start MongoDB:
```bash
# Make sure MongoDB is running on localhost:27017
```

3. Run the Flask application:
```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000`

### Frontend Setup

1. Navigate to the Angular project:
```bash
cd front_end/bizFE
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
ng serve
```

The Angular app will be available at `http://localhost:4200`

## API Endpoints

### Authentication

- **POST** `/login` - User login (returns JWT token)
  - Requires Basic Auth (username/password)
  - Returns: `{"token": "jwt_token"}`

### Businesses

- **GET** `/businesses` - Get all businesses (paginated)
  - Query params: `page` (default: 1), `size` (default: 10)
  
- **GET** `/businesses/<biz_id>` - Get specific business by ID

- **POST** `/businesses` - Create new business
  - Required fields: `name`, `town`, `rating`
  
- **PUT** `/businesses/<biz_id>` - Update business
  - Optional fields: `name`, `town`, `rating`
  
- **DELETE** `/businesses/<biz_id>` - Delete business

### Reviews

- **POST** `/businesses/<biz_id>/reviews` - Add review to business
  - Required fields: `username`, `comments`, `star` (1-5)

## Authentication

The API uses JWT tokens for authentication. Include the token in request headers:

```
x-access-token: your_jwt_token_here
```

Tokens expire after 30 minutes and can be blacklisted for logout functionality.

## Database Schema

### Users Collection
```javascript
{
  "username": "string",
  "password": "hashed_password",
  "admin": boolean
}
```

### Businesses Collection
```javascript
{
  "_id": ObjectId,
  "name": "string",
  "town": "string",
  "rating": number,
  "reviews": [
    {
      "_id": ObjectId,
      "username": "string",
      "comments": "string",
      "star": number (1-5)
    }
  ]
}
```

### Blacklist Collection
```javascript
{
  "token": "jwt_token_string"
}
```

## Configuration

Edit `globals.py` to configure:
- MongoDB connection string
- Secret key for JWT signing
- Database name

```python
SECRET_KEY = "mysecret"  # Change this in production!
Client = MongoClient("mongodb://localhost:27017/")
db = Client.Business
```

## Security Notes

⚠️ **Important**: 
- Change the `SECRET_KEY` in production
- Use environment variables for sensitive data
- Enable HTTPS in production
- Implement rate limiting
- Add input validation and sanitization

## Development

The application runs in debug mode by default. To run in production:

```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

## Known Issues

- Missing `Blueprint` import in `businesses.py` and `reviews.py`
- Typo: `bsuinesses` instead of `businesses` in variable names
- Inconsistent error handling across endpoints
- Missing logout endpoint implementation
- Review endpoint uses `@app.route` instead of `@reviews_bp.route`

## Future Enhancements

- [ ] Add user registration endpoint
- [ ] Implement logout functionality with token blacklisting
- [ ] Add input validation middleware
- [ ] Implement role-based access control (RBAC)
- [ ] Add API documentation (Swagger/OpenAPI)
- [ ] Add unit tests
- [ ] Implement rating calculation based on reviews
- [ ] Add search and filter functionality for businesses

## License

This project is for educational purposes.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
