# FastAPI Grocery List

## Description
The FastAPI Grocery List project is a web application built using the FastAPI framework. It allows users to manage a grocery list with various functionalities such as adding items, listing items, updating item quantities, and deleting items. The application is designed to be fast, efficient, and easy to use, leveraging the capabilities of FastAPI for handling HTTP requests and responses.

## Features
- **Add Items:** Users can add new items to the grocery list with a specified quantity.
- **List Items:** Users can view all items in the grocery list or retrieve details of a specific item by its ID.
- **Update Quantity:** Users can update the quantity of a specific item in the grocery list.
- **Remove Quantity:** Users can remove a specified quantity of an item, and if the quantity becomes zero or less, the item is deleted.
- **Delete Items:** Users can delete specific items from the grocery list by their ID.

## Technologies Used
- **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.6+.
- **Pydantic:** Used for data validation and settings management using Python type annotations.
- **Uvicorn:** A lightning-fast ASGI server for serving the FastAPI application.

## Setup Instructions
1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd <your-repo-directory>
