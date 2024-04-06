## Installation

Follow these steps to get your development environment set up:

1. Clone the repository and navigate to the directory:

   ```sh
    mkdir django-performance && cd django-performance
    python3.12 -m venv venv
    source venv/bin/activate
    git clone -b main https://github.com/amirtds/mystore
    cd mystore
   ```
2. Install requirements and dependancies

    ```sh
    python3.12 -m pip install -r requirements.txt
    ```
3. Run migration and the development server

    ```sh
    python3.12 manage.py migrate
    python3.12 manage.py runserver
    ```
4. visit [127.0.0.1:8000](https://127.0.0.1:8000)

5. create sample products

    ```bash
    python3.12 manage.py shell
    ```

    ```py
    from store.models import Category, Product

    # Create categories
    electronics = Category(name='Electronics', description='Gadgets and electronic devices.')
    books = Category(name='Books', description='Read the world.')
    clothing = Category(name='Clothing', description='Latest fashion and trends.')

    # Save categories to the database
    electronics.save()
    books.save()
    clothing.save()

    # Now let's create new Products with slugs and image URLs
    Product.objects.create(
        category=electronics,
        name='Smartphone',
        description='Latest model with high-end specs.',
        price=799.99,
        stock=30,
        available=True,
        slug='smartphone',
        image='products/iphone_14_pro_max.png'
    )

    Product.objects.create(
        category=books,
        name='Python Programming',
        description='Learn Python programming with this comprehensive guide.',
        price=39.99,
        stock=50,
        available=True,
        slug='python-programming',
        image='products/python_programming_book.png'
    )

    Product.objects.create(
        category=clothing,
        name='Jeans',
        description='Comfortable and stylish jeans for everyday wear.',
        price=49.99,
        stock=20,
        available=True,
        slug='jeans',
        image='products/jeans.png'
    )
    ```

    exit the shell and run the server again `python3.12 manage.py runserver`  and visit [127.0.0.1:8000](https://127.0.0.1:8000)
