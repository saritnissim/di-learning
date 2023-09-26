CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE,
    customer_name VARCHAR
);


CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES product_orders(order_id),
    item_name VARCHAR,
);


CREATE FUNCTION calculate_order_total(order_id INT)
RETURNS NUMERIC(10, 2) AS $$
DECLARE
    total NUMERIC(10, 2) := 0;
BEGIN
    SELECT SUM(price * quantity)
    INTO total
    FROM items
    WHERE items.order_id = calculate_order_total.order_id;
    
    RETURN total;
END;
$$ LANGUAGE plpgsql;