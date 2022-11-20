CREATE TABLE IF NOT EXISTS companies (
    id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    CONSTRAINT companies_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS customers (
    id VARCHAR(255) NOT NULL,
    login VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    company_id INTEGER,
    credit_cards VARCHAR(255),
    CONSTRAINT customers_pkey PRIMARY KEY (id),
    CONSTRAINT customers_company_id_fkey FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE,
    customer_id VARCHAR(255),
    CONSTRAINT orders_pkey PRIMARY KEY (id),
    CONSTRAINT orders_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER NOT NULL,
    product VARCHAR(255) NOT NULL,
    price_per_unit DECIMAL,
    quantity INTEGER NOT NULL,
    order_id INTEGER,
    CONSTRAINT order_items_pkey PRIMARY KEY (id),
    CONSTRAINT order_items_order_id_fkey FOREIGN KEY (order_id) REFERENCES orders(id)
);

CREATE TABLE IF NOT EXISTS deliveries (
    id INTEGER NOT NULL,
    delivered_quantity INTEGER NOT NULL,
    order_item_id INTEGER,
    CONSTRAINT deliveries_pkey PRIMARY KEY (id),
    CONSTRAINT deliveries_order_item_id_fkey FOREIGN KEY (order_item_id) REFERENCES order_items(id)
);
