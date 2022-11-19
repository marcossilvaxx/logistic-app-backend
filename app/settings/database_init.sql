CREATE TABLE public.companies (
    id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE public.customers (
    id VARCHAR(255) NOT NULL,
    login VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    company_id INTEGER,
    credit_cards VARCHAR(255)
);

CREATE TABLE public.deliveries (
    id INTEGER NOT NULL,
    delivered_quantity INTEGER NOT NULL,
    order_item_id INTEGER
);

CREATE TABLE public.order_items (
    id INTEGER NOT NULL,
    product VARCHAR(255) NOT NULL,
    price_per_unit DECIMAL,
    quantity INTEGER NOT NULL,
    order_id INTEGER
);

CREATE TABLE public.orders (
    id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE,
    customer_id VARCHAR(255)
);

ALTER TABLE public.companies
    ADD CONSTRAINT companies_pkey PRIMARY KEY (id);

ALTER TABLE public.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (id);

ALTER TABLE public.deliveries
    ADD CONSTRAINT deliveries_pkey PRIMARY KEY (id);

ALTER TABLE public.order_items
    ADD CONSTRAINT order_items_pkey PRIMARY KEY (id);

ALTER TABLE public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);

ALTER TABLE public.customers
    ADD CONSTRAINT customers_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(id);

ALTER TABLE public.deliveries
    ADD CONSTRAINT deliveries_order_item_id_fkey FOREIGN KEY (order_item_id) REFERENCES public.order_items(id);

ALTER TABLE public.order_items
    ADD CONSTRAINT order_items_order_id_fkey FOREIGN KEY (order_id) REFERENCES public.orders(id);

ALTER TABLE public.orders
    ADD CONSTRAINT orders_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(id);