# Giri Artisan Marketplace API

*Overview*
The Giri Artisan Marketplace API is a backend service for an artisan marketplace platform. It allows you to manage artisans, products, and orders. The API includes features like product recommendations, inventory management, filtering, sorting, and more.

## Features

    1. Artisan Management: Create, update, retrieve, and delete artisans.
    2. Product Management: Handle products with support for filtering, sorting, and search.
    3. Order Management: Create and view customer orders with automatic inventory updates.
    4. Recommendations: Suggest popular products based on order history.
    5. Pagination: Support for paginated responses on list endpoints.
    6. Basic Authentication: Secure access to API endpoints.
    7. Admin Interface: Manage artisans, products, and orders using Django Admin.

## Setup Instructions

    1. Prerequisites
        Python 3.9+
        PostgreSQL installed and running
        Virtual environment tool (e.g., venv or virtualenv)

## Clone Repo

    ```bash
    git clone https://github.com/Hudeh/giri_marketplace.git
    cd giri_marketplace
    ```

## Virtual Environment

    Create a virtual environment and activate it. On macOS and Linux, run these commands:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

    On Windows, run these commands:

    ```bash
    python -m venv env
    env\Scripts\activate
    ```

## Install Dependencies

    With the virtual environment configured, install the Temporal SDK:

    ```bash
    python -m pip install -r requirements.xtx
    ```

## Apply Migrations

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Create a Superuser

    ```bash
    python manage.py createsuperuser
    ```

## Run the Server

    ```bash
    python manage.py runserver
    ```
    The API will be available at: <http://127.0.0.1:8000/api/>

## API Documentation

    Authentication
    All endpoints require basic authentication. Use your Django superuser credentials or create additional users in the admin interface.

## Endpoints

1. Artisans
    GET /api/artisans/: List all artisans.
    POST /api/artisans/: Create a new artisan.
    GET /api/artisans/id/: Retrieve a specific artisan.
    PUT /api/artisans/id/: Update an artisan.
    DELETE /api/artisans/id/: Delete an artisan.
2. Products
    GET /api/products/: List all products (supports filtering, sorting, and search).
    Filtering: ?price_min=10&price_max=50
    Sorting: ?ordering=price or ?ordering=-price
    Search: ?search=handmade
    POST /api/products/: Create a new product.
    GET /api/products/id/: Retrieve a specific product.
    PUT /api/products/id/: Update a product.
    DELETE /api/products/id/: Delete a product.
    GET /api/products/recommendations/: Get recommended products.
3. Orders
    GET /api/orders/: List all orders.
    POST /api/orders/: Create a new order (inventory is automatically updated).
4. Admin Interface
    Visit <http://127.0.0.1:8000/admin/> to access the admin panel.
    Use your superuser credentials to log in and manage artisans, products, and orders.
5. Assumptions and Design Decisions
    Authentication: Basic authentication is used to secure all endpoints.
    Product Recommendations: Based on order history; the top 5 most frequently ordered products are recommended.
    Inventory Management: Products with an inventory count of 0 cannot be ordered.
    Filtering and Sorting: Added to the Product endpoint for better user experience.
    Pagination: Implemented for all list endpoints to optimize performance with large datasets.
6. Ideas for Future Improvements
    Advanced Authentication: Add token-based authentication (e.g., JWT) for better security.
    Customer Management: Add a customer model to allow for personalized accounts and order tracking.
    Category Support: Introduce categories for products to make browsing easier.
    Frontend Integration: Create a React or Vue.js frontend for the platform.
    Payment Gateway: Integrate a payment gateway to handle real transactions.
    Inventory Alerts: Notify artisans when their inventory is low.
    Order Reporting: Add analytics for artisans to track their sales performance.
