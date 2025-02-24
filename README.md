# Bookstore Mini ERP

A minimal Enterprise Resource Planning (ERP) system for managing a bookstore's warehouse inventory. This application helps you track books, manage stock levels (add or subtract books inventory), and record details for each book.

## Features

- **Inventory Management:**  
  Manage a list of books with details such as book title, author, ISBN, quantity, and comments.
  
- **Stock Adjustments:**  
  Easily add or subtract book quantities to reflect sales or new arrivals.

- **User Association:**  
  Associate each inventory item with a user account.

- **Timestamps:**  
  Automatically track the creation and modification dates for each record.

- **Responsive UI:**  
  Built using Bootstrap for a responsive and modern design.


## Tech Stack

- **Backend:**  
  - [Django](https://www.djangoproject.com/) (Python)  
  - [Django REST Framework](https://www.django-rest-framework.org/) (to expose API endpoints)

- **Frontend:**  
  - [React](https://reactjs.org/)  
  - [Create React App](https://create-react-app.dev/) (for bootstrapping the React project)  
  - [React Bootstrap](https://react-bootstrap.github.io/) (optional, for additional UI components)

- **Database:**  
  - SQLite (default, configurable with Django settings)

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository:**

    ```bash
   git clone https://github.com/yourusername/bookstore-mini-erp.git
   cd bookstore-mini-erp
2. **Create a Virtual Environment and Install Dependencies:**
    ```bash 
    python -m venv env
    source env/bin/activate  
    # On Windows, use:
    env\Scripts\activate
    pip install -r requirements.txt