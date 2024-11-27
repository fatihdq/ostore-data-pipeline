CREATE TABLE products (
	product_id VARCHAR(255) PRIMARY KEY,
	product_category_name VARCHAR(255),
	product_name_lenght	INT,
	product_description_lenght INT,
	product_photos_qty INT,
	product_weight_g INT, 
	product_length_cm INT,
	product_height_cm INT,
	product_width_cm INT
);

CREATE TABLE customers (
    customer_id VARCHAR(255) PRIMARY KEY,
    customer_unique_id VARCHAR(255),
    customer_zip_code_prefix INT,
    customer_city VARCHAR(255),
    customer_state VARCHAR(255)
);

CREATE TABLE geolocations (
    geolocation_zip_code_prefix VARCHAR(255) PRIMARY KEY,
    geolocation_lat FLOAT,
    geolocation_lng FLOAT,
    geolocation_city VARCHAR(255),
    geolocation_state VARCHAR(255)
);

CREATE TABLE sellers (
    seller_id VARCHAR(255) PRIMARY KEY,
    seller_zip_code_prefix VARCHAR(255),
    seller_city VARCHAR(255),
    seller_state VARCHAR(255)
);

CREATE TABLE orders (
    order_id VARCHAR(255) PRIMARY KEY,
    customer_id VARCHAR(255),
    order_status VARCHAR(255),
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP,
    CONSTRAINT fk_customer_order FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_payments (
    order_id VARCHAR(255) NOT NULL,
    payment_sequential INT NULL,
    payment_type VARCHAR(255),
    payment_installments INT,
    payment_value FLOAT,
    CONSTRAINT pk_order_payment PRIMARY KEY (order_id,payment_sequential),
    CONSTRAINT fk_order_op FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE order_items (
    order_id VARCHAR(255),
    order_item_id VARCHAR(255),
    product_id VARCHAR(255),
    seller_id VARCHAR(255),
    shipping_limit_date TIMESTAMP,
    price FLOAT,
    freight_value FLOAT,
    CONSTRAINT pk_order_items PRIMARY KEY (order_id,order_item_id),
    CONSTRAINT fk_order_oi FOREIGN KEY (order_id) REFERENCES orders(order_id),
    CONSTRAINT fk_product_oi FOREIGN KEY (product_id) REFERENCES products(product_id),
    CONSTRAINT fk_seller_oi FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)
);

CREATE TABLE order_reviews (
    review_id VARCHAR(255),
    order_id VARCHAR(255),
    review_score INT,
    review_comment_title VARCHAR(255),
    review_comment_message VARCHAR(255),
    review_creation_date TIMESTAMP,
    review_answer_timestamp TIMESTAMP,
    CONSTRAINT pk_order_reviews PRIMARY KEY (review_id,order_id),
    CONSTRAINT fk_order_or FOREIGN KEY (order_id) REFERENCES orders(order_id)
);