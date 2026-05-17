CREATE TABLE transactions (
    transaction_id VARCHAR(50),
    customer_id VARCHAR(50),
    product_name VARCHAR(100),
    category VARCHAR(50),
    amount FLOAT,
    city VARCHAR(50),
    transaction_time TIMESTAMP
);

CREATE TABLE anomalies (
    transaction_id VARCHAR(50),
    amount FLOAT,
    anomaly_reason VARCHAR(255),
    detected_at TIMESTAMP
);