# E-Commerce Database
Database design practice for the LS181 interview

## Scenario:

- Imagine you're designing a database for a large scale e-commerce platform. How would you structure the database to handle prodducts, categories, users, orders, and reviews? Consider the relationships between these entities and explain how you would implement them using foreign keys. How would you ensure referential integrity? Discuss trade-offs of your design choices.

### Design

- First we need to identify the entities that will be present in our database.

1. Products
2. Categories
3. Users
4. Orders
5. Reviews

- Now we need to identify the relationships between these entities on a conceptual level and if they are required or not. This will help us determine the cardinality and modality on either side of the relationships between the entities. Using the word "may" means the relationship (modality) is not required. Using "do not" indicates relationship (modality) is not allowed. 

1. Products may have many categories but must have at least 1, may have many orders, and may have many reviews. 
2. Categories may belong to many products. Categories do not relate to Users, Orders, and Reviews
3. Users may have many Orders. May have many Reviews. Users do not relate to Categories and Products
4. An order must relate to only one User. An order must have at least one Product but can have many products. An order does not relate to Categories.
5. A review may have only one user but does not have to have a user. A review must have one and only one product. Reviews do not relate to categories or orders.

- Now that we have broken down the relationships and described their cardinality and modality, lets break down more of the logical aspects, focusing on the primary and foreign keys. Here are the proposed tables:

~~~SQL
CREATE TABLE products (id serial PRIMARY KEY, name text NOT NULL, description text, price numeric(6, 2) NOT NULL);

CREATE TABLE categories (id serial PRIMARY KEY, name text NOT NULL UNIQUE);

CREATE TABLE products_categories (id serial PRIMARY KEY, product_id integer NOT NULL REFERENCES products (id) ON DELETE CASCADE, category_id integer NOT NULL REFERENCES categories (id) ON DELETE SET NULL);

CREATE TABLE users (id serial PRIMARY KEY, username text NOT NULL UNIQUE, date_joined date NOT NULL DEFAULT NOW());

CREATE TABLE orders (id serial PRIMARY KEY, user_id integer NOT NULL REFERENCES users (id) ON DELETE RESTRICT);

CREATE TABLE orders_products (id serial PRIMARY KEY, order_id integer NOT NULL REFERENCES orders (id), product_id integer NOT NULL REFERENCES products (id));

Create TABLE reviews (id serial PRIMARY KEY, stars integer NOT NULL, description text, user_id integer DEFAULT 000 REFERENCES users (id) CHECK UNIQUE (id, user_id) ON DELETE SET DEFAULT, product_id integer REFERENCES products (id) CHECK UNIQUE (id, product_id) ON DELETE CASCADE);
~~~

- Design choices
  - It is SQL design convention that each relation should have an "id" column serving as a surrogate key
  - Treat Categories as a separate entity instead of grouping them in as a category with Products
  - To not relate categories to Orders
  - Do not require Reviews to have Users to support anonymous reviews, Provide ON DELETE clauses in Reviews to support referential integrity and to support deletion of products and users.
  - Reviews only belong to one product at a time
  - Product names may contain duplicates, the id's will be used to uniquely identify products
  - The kind of information an Order needs must be present in the products table, will keep the products table schema simple until at a future point we know more about the products and their information our system might need.
  - Category names should be unique to prevent future grouping conflictions
  - Both product_id and category_id in products_categories must not be UNIQUE because both can have many relationships
  - `ON DELETE SET NULL` clause for the category_id in products_categories because we don't want to get rid of that product's category because products must have a category. So if we delete that category and an associated product is only related to that one category, the foreign key will automatically set to `NULL` and we can go back in and either re-associate the product to a category or create a new category for it. Another choice could be to have a default "General" category as well.
  - Restrict the deletion of a user if they have an active order

- How I address each anomaly:
  - Update anomaly: relationships utilize surrogate keys to maintain referential integrity and common fields that are updated such as names or descriptions are not relevant to the relationships
  - Insertion anomaly: People are able to leave reviews on products without having to be registered users, preventing an insertion anomaly of reviews needing user_id's. 
  - Deletion anomaly: various `ON DELETE` clauses are used to maintian referential integrity when we need to perform actions such as deleting users, products, and categories.
  - The decision to separate an order's product id's into its own join table was made to provide for better normalization in the relatinship. If orders just contained a list of product_id's it would require every order to be manually updated with a new product_id.

- Improvement:
  - Need to add a quantity column to orders_products
  - Use triggers or default categories to enforce products needing to have a category

- Scalability:
  - Use of separate tables for independent scaling of entities
  - Use of junction tables to avoid embedding arrays or complex structures within other tables
  - Tables support various indexing if we wanted to implement that
- Efficiency:
  - use of join tables for efficient queries to find all products in a specific category
  - Support of indexing can increase this as well
  - Direct foreign key from reviews to product table to support retrieval
  

