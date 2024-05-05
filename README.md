# Vendor Management System

## Introduction
The Vendor Management System is a Django-based application designed to manage vendor profiles, track purchase orders, and evaluate vendor performance metrics.

## Prerequisites
Before you begin, ensure you have the following installed on your machine:
- Python 3.x
- Django
- Django REST Framework
- [Add any additional dependencies here]

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/pranavpk-672/Vendor-Management-System-API.git

Navigate to the project directory:

cd vendor-management-system
Install Python dependencies using pip:

Apply database migrations:

python manage.py migrate

Running the Server
To start the Django development server, run the following command:

python manage.py runserver
By default, the server will start at http://127.0.0.1:8000/.

API Endpoints : 

Vendor Profile Management:
-POST /api/vendors/: Create a new vendor.
-GET /api/vendors/: List all vendors.
-GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
-PUT /api/vendors/{vendor_id}/: Update a vendor's details.
-DELETE /api/vendors/{vendor_id}/: Delete a vendor.

-Purchase Order Tracking:
-POST /api/purchase_orders/: Create a purchase order.
-GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
-GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
-PUT /api/purchase_orders/{po_id}/: Update a purchase order.
-DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

-Vendor Performance Evaluation:
-GET /api/vendors/{vendor_id}/performance/: Retrieve a vendor's performance metrics.
