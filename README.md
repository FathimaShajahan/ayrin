Ayrin Fashion Store - eCommerce Website
Overview
Ayrin Fashion Store is a dynamic eCommerce web application developed to offer a seamless online shopping experience. The platform includes various features such as product categorization, pagination, shopping cart functionality, and an efficient search system. Additionally, the website comes with a user-friendly Admin Panel for managing products, categories, and orders.

Features
1. Admin Panel
Manage products (add, edit, delete)
Handle product categories
Monitor and update customer orders
Secure login for admins
2. Product Categorization
Organize products into various categories
Filter products based on categories
3. Pagination
Efficiently display products across multiple pages
Enhance website performance
4. Shopping Cart Functionality
Add/remove items to/from cart
View and update quantities in the cart
Track total prices before checkout
5. Efficient Search System
Search for products by name, category, or description
Instant search results display
Technologies Used
Frontend:
HTML: Structure of web pages
CSS: Styling and layout design
JavaScript: Interactivity and dynamic content
Backend:
Python (Django): Core backend development and functionality implementation
Database:
MySQL: Storing product, user, and order information
Version Control:
Git: Code versioning and collaboration
Installation
Clone the repository

bash
Copy code
git clone https://github.com/yourusername/ayrin-fashion-store.git
Navigate to the project directory

bash
Copy code
cd ayrin-fashion-store
Install required dependencies

bash
Copy code
pip install -r requirements.txt
Set up the database
Configure the database in the settings.py file and run migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the development server

bash
Copy code
python manage.py runserver
Access the site locally
Open your browser and go to http://127.0.0.1:8000/

Admin Access
To access the admin panel, create a superuser using the following command:

bash
Copy code
python manage.py createsuperuser
Then, log in at http://127.0.0.1:8000/admin/

Contributing
Feel free to contribute to this project by submitting a pull request or reporting issues. Make sure to follow the contribution guidelines.

License
This project is licensed under the MIT License - see the LICENSE file for details.

