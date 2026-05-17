from kafka import KafkaConsumer

import json

from anomaly_detector import detect_anomaly

from database import (
    save_transaction,
    save_anomaly
)

consumer = KafkaConsumer(
    'transactions',

    bootstrap_servers='localhost:9092',

    auto_offset_reset='earliest',

    enable_auto_commit=True,

    group_id='sales-group',

    value_deserializer=lambda x:
    json.loads(x.decode('utf-8'))
)


def process_transaction(transaction):

    save_transaction(transaction)

    is_anomaly, reason = detect_anomaly(transaction)

    if is_anomaly:

        save_anomaly(
            transaction['transaction_id'],
            transaction['amount'],
            reason
        )

        print(f'ANOMALY DETECTED: {reason}')


print('Consumer started...')


for message in consumer:

    transaction = message.value

    print(f'Received: {transaction}')

    process_transaction(transaction)