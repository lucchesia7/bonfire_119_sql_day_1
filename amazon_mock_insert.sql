INSERT INTO customer(
    customer_id,
    first_name,
    last_name,
    address,
    billing_info
)VALUES(
    2,
    'Alex',
    'Lucchesi',
    '123 Main Street, Seattle, WA 98007',
    '4242-4242-4242-4242 623 05/30'
);

-- Insert statement for brand data
INSERT INTO brand(
    seller_id,
    brand_name,
    contact_number,
    address
)VALUES(
    1,
    'Coding Temple Trading Company',
    '773-555-4490',
    '222 W Ontario Street, Chicago, IL'
);

-- Insert statement for the inventory data
INSERT INTO inventory(
    upc,
    product_amount
)VALUES(
    1,
    20.00
);

-- Insert statement for the product data
INSERT INTO product(
    iten_id,
    amount,
    prod_name,
    seller_id,
    upc
)VALUES(
    1,
    20.00,
    'Python 101',
    1,
    1
);

-- Insert statement for the orders data
INSERT INTO orders(
    order_id,
    sub_total,
    total_cost,
    upc
)VALUES(
    1,
    40.00,
    43.50,
    1
);

-- Insert statement for the cart data
INSERT INTO cart(
    cart_id,
    customer_id,
    order_id
)VALUES(
    1,
    1,
    1
);