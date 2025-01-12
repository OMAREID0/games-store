# Games API

Welcome to the Games API! This project provides a RESTful API for accessing and managing game data. Whether you're a developer looking to integrate game information into your application or a gamer wanting to explore game details, this API is designed to meet your needs.

# Digram
[Game API Diagram](./games%20store%20api%20(1).png)

## Features

- Retrieve a list of all games
- Get detailed information about a specific game
- Create, update, and delete game entries
- Search for games by various criteria

# Endpoints

Here are the 14 endpoints available in the Games API:

## User
1. GET /api/user/ - Retrieve a list of registered user and if he authorized or not.
2. POST /api/user/login - Authenticate a user by providing their credentials (username and password). If the credentials are valid, the server will return a token for session management.
3. POST /api/user/register - Create a new user account. This endpoint requires user details such as username, password, and email. Upon successful registration, a  token may be returned.
4. POST /api/user/logout - Log out the currently authenticated user. This endpoint invalidates the user's session token, ensuring that the user is logged out securely.

## Category
4. GET api/category - Retrieve a list of all product categories.
5. POST api/category/add - Add a new category to the system. This endpoint requires details about the category (e.g., name and description) and is typically restricted to administrators.
6. GET api/category/{name} - Retrieve detailed information about a specific category by its name. This can include a list of products within that category and other relevant details.
7. GET api/category/{id} - Retrieve detailed information about a specific category using its unique identifier (ID). This endpoint is useful for fetching category details programmatically.

## Products
8. GET api/product - Retrieve a list of all products available in the system.
9. GET api/product/{id} - Retrieve detailed information about a specific product using its unique identifier (ID). This includes product specifications, pricing, and availability.
10. GET api/product/{name} - Retrieve detailed information about a specific product using its name. This endpoint is useful for searching products by their names.
11. GET api/product/{category} - Retrieve a list of products that belong to a specific category. This endpoint allows users to filter products based on their interests.
12. POST GET api/product/add - Add a new product to the system. This endpoint requires product details such as name, description, price, and category.

## Order
13. GET api/order - Retrieve a list of all orders.
14. POST api/order/add - Create a new order.
15. GET api/order/{order_number} - Retrieve a specific order by order_number.


## Authentication

This API does not require authentication for accessing the endpoints. However, you can implement authentication using JWT or any other method as per your requirements.

## Error Handling

The API returns standard HTTP status codes to indicate the success or failure of requests. Common error responses include:

- 404 Not Found - The requested resource could not be found.
- 400 Bad Request - The request was invalid or cannot be served.
- 500 Internal Server Error - An unexpected error occurred on the server.

## Contributing

Contributions are welcome! If you have suggestions for improvements