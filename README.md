# StreamGuard — Real-Time Sales Analytics & Anomaly Detection

## Overview

StreamGuard is a real-time sales analytics platform designed to simulate modern streaming architectures used in e-commerce and fintech environments.
The project demonstrates how transaction data can be processed continuously using Apache Kafka, analyzed in real time, stored in PostgreSQL, and visualized in Power BI dashboards.

The system generates live transaction events, streams them through Kafka topics, processes them with Python consumers, detects suspicious transactions, and stores analytical data for further business intelligence reporting.

This project presents a complete end-to-end data engineering and BI pipeline focused on real-time analytics and anomaly detection.


# Business Problem

Modern e-commerce platforms generate thousands of transactions every minute. Traditional batch-processing systems are often unable to detect suspicious activities quickly enough, which may lead to financial losses, delayed reactions, and limited operational visibility.

Businesses require systems capable of:

* monitoring sales activity in real time,
* detecting unusual transactions instantly,
* identifying high-risk operations,
* supporting operational and strategic decision-making through live dashboards.

This project addresses these challenges by implementing a streaming-based architecture for real-time transaction processing and anomaly detection.


# Project Goals

The main objectives of the project are:

* build a real-time streaming pipeline using Apache Kafka,
* simulate live transaction processing,
* implement anomaly/fraud detection logic,
* store processed data in PostgreSQL,
* visualize business metrics in Power BI,
* demonstrate a modern data engineering workflow.


# System Architecture

```text id="u8x4wr"
Producer → Apache Kafka → Consumer → PostgreSQL → Power BI
```

### Components

| Component         | Description                            |
| ----------------- | -------------------------------------- |
| Producer          | Generates and streams transaction data |
| Apache Kafka      | Handles real-time event streaming      |
| Consumer          | Processes incoming transactions        |
| Anomaly Detection | Detects suspicious transactions        |
| PostgreSQL        | Stores analytical and anomaly data     |
| Power BI          | Visualizes KPIs and business insights  |


# Technologies Used

| Technology   | Purpose                                |
| ------------ | -------------------------------------- |
| Python       | Data generation and processing         |
| Apache Kafka | Real-time event streaming              |
| PostgreSQL   | Data storage                           |
| Docker       | Containerization and environment setup |
| Power BI     | Business intelligence dashboards       |
| Pandas       | Data transformation                    |
| Faker        | Synthetic data generation              |
| SQLAlchemy   | Database connection layer              |


# Key Features

* Real-time transaction streaming
* Kafka Producer & Consumer architecture
* Online anomaly detection
* PostgreSQL integration
* Business Intelligence dashboarding
* Fraud monitoring simulation
* Scalable event-driven architecture
* Dockerized environment


# Real-Time Anomaly Detection

The project includes a simple fraud/anomaly detection mechanism.
Transactions exceeding a defined threshold are automatically classified as anomalies and stored separately for monitoring and investigation purposes.

Example anomaly conditions:

* unusually high transaction amounts,
* suspicious sales patterns,
* abnormal purchasing behavior.

This simulates real-world fraud detection systems used in financial services and e-commerce platforms.


# Power BI Dashboard

The dashboard provides real-time analytical insights, including:

* total number of transactions,
* total sales value,
* anomaly/fraud count,
* sales trends over time,
* top-selling products,
* geographic sales distribution,
* suspicious transaction monitoring.

The dashboard enables near real-time business monitoring and operational analytics.


# Example Use Case

The system simulates a company operating an online sales platform that requires continuous transaction monitoring and fraud detection.

Potential business applications include:

* e-commerce platforms,
* fintech systems,
* payment gateways,
* banking analytics,
* operational monitoring systems.


# Repository Structure

```text id="x1m7zp"
real-time-sales-analytics/
│
├── producer/
│   └── producer.py
│
├── consumer/
│   ├── consumer.py
│   ├── anomaly_detector.py
│   └── database.py
│
├── sql/
│   └── init.sql
│
├── dashboard/
│   └── dashboard.pbix
│
├── images/
│   ├── dashboard.png
│   └── architecture.png
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```


# How to Run the Project

## 1. Start Docker containers

```bash id="a4q2vn"
docker-compose up -d
```


## 2. Run Kafka Producer

```bash id="d7v5xp"
cd producer
python producer.py
```


## 3. Run Kafka Consumer

```bash id="g1m8wr"
cd consumer
python consumer.py
```


## 4. Open Power BI Dashboard

Connect Power BI to PostgreSQL using:

```text id="j4q2zn"
Server: localhost
Database: sales_db
Username: admin
Password: admin
```


# Future Improvements

Potential future enhancements:

* Machine Learning anomaly detection,
* Spark Streaming integration,
* automated alerting system,
* Grafana dashboards,
* REST API integration,
* Kubernetes deployment,
* cloud deployment (Azure/AWS/GCP),
* advanced fraud scoring models.
