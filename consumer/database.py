from sqlalchemy import create_engine

import pandas as pd

engine = create_engine(
    'postgresql://admin:admin@localhost:5432/sales_db'
)


def save_transaction(transaction):

    df = pd.DataFrame([transaction])

    df.to_sql(
        'transactions',
        engine,
        if_exists='append',
        index=False
    )


def save_anomaly(transaction_id, amount, reason):

    anomaly = pd.DataFrame([
        {
            'transaction_id': transaction_id,
            'amount': amount,
            'anomaly_reason': reason,
            'detected_at': pd.Timestamp.now()
        }
    ])

    anomaly.to_sql(
        'anomalies',
        engine,
        if_exists='append',
        index=False
    )