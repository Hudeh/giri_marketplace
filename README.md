# Giri Artisan Marketplace API

*Overview*
The Giri Artisan Marketplace API is a backend service for an artisan marketplace platform. It allows you to manage artisans, products, and orders. The API includes features like product recommendations, inventory management, filtering, sorting, and more.

## Features

- Artisan Management: Create, update, retrieve, and delete artisans.
- Product Management: Handle products with support for filtering, sorting, and search.
- Order Management: Create and view customer orders with automatic inventory updates.
- Recommendations: Suggest popular products based on order history.
- Pagination: Support for paginated responses on list endpoints.
- Basic Authentication: Secure access to API endpoints.
- Admin Interface: Manage artisans, products, and orders using Django Admin.

## Getting Started

### Prerequisites

- Python 3.x
- Virtualenv (optional but recommended)

### Installation

1. **Clone the repository:**

    ```bash
            git clone https://github.com/Hudeh/giri_marketplace.git
            cd giri_marketplace
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
        virtualenv venv
    ```

3. **Activate the virtual environment:**

    - **Windows**

    ```bash
        venv\Scripts\activate
    ```

    - **Linux/macOS**

    ```bash
        source venv/bin/activate
    ```

4. **Install dependencies:**

```bash
        pip install -r requirements.txt
```

### Database Setup

1. **Run migrations to set up the database:**

```bash
    python manage.py makemigrations
    python manage.py migrate
```

### Running the Server

```bash
python manage.py runserver
```

## API Documentation

- Authentication
    All endpoints require basic authentication. Use your Django superuser credentials or create additional users in the admin interface.

## Endpoints

1. Artisans
    - GET /api/artisans/: List all artisans.
    - POST /api/artisans/: Create a new artisan.
    - GET /api/artisans/id/: Retrieve a specific artisan.
    - PUT /api/artisans/id/: Update an artisan.
    - DELETE /api/artisans/id/: Delete an artisan.
2. Products
    - GET /api/products/: List all products (supports filtering, sorting, and search).
    - Filtering: ?price_min=10&price_max=50
    - Sorting: ?ordering=price or ?ordering=-price
    - Search: ?search=handmade
    - POST /api/products/: Create a new product.
    - GET /api/products/id/: Retrieve a specific product.
    - PUT /api/products/id/: Update a product.
    - DELETE /api/products/id/: Delete a product.
    - GET /api/products/recommendations/: Get recommended products.
3. Orders
    - GET /api/orders/: List all orders.
    - POST /api/orders/: Create a new order (inventory is automatically updated).
4. Admin Interface
    - Visit <http://127.0.0.1:8000/admin/> to access the admin panel.
    - Use your superuser credentials to log in and manage artisans, products, and orders.
5. Assumptions and Design Decisions
    - Authentication: Basic authentication is used to secure all endpoints.
    - Product Recommendations: Based on order history; the top 5 most frequently ordered products are recommended.
    - Inventory Management: Products with an inventory count of 0 cannot be ordered.
    - Filtering and Sorting: Added to the Product endpoint for better user experience.
    - Pagination: Implemented for all list endpoints to optimize performance with large datasets.
6. Ideas for Future Improvements
    - Advanced Authentication: Add token-based authentication (e.g., JWT) for better security.
    - Customer Management: Add a customer model to allow for personalized accounts and order tracking.
    - Category Support: Introduce categories for products to make browsing easier.
    - Frontend Integration: Create a React or Vue.js frontend for the platform.
    - Payment Gateway: Integrate a payment gateway to handle real transactions.
    - Inventory Alerts: Notify artisans when their inventory is low.
    - Order Reporting: Add analytics for artisans to track their sales performance.
