from kafka import KafkaProducer
from faker import Faker

import json
import time
import random

from datetime import datetime

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = [
    'Laptop',
    'Phone',
    'Keyboard',
    'Monitor',
    'Mouse'
]

categories = [
    'Electronics',
    'Accessories'
]


def generate_transaction():

    return {

        'transaction_id': fake.uuid4(),

        'customer_id': fake.uuid4(),

        'product_name': random.choice(products),

        'category': random.choice(categories),

        'amount': round(random.uniform(50, 15000), 2),

        'city': fake.city(),

        'transaction_time': datetime.now().isoformat()
    }


def send_transaction(transaction):

    producer.send(
        'transactions',
        value=transaction
    )


while True:

    transaction = generate_transaction()

    send_transaction(transaction)

    print(f'Sent: {transaction}')

    time.sleep(1)