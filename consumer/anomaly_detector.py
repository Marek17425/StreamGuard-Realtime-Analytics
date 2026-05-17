def detect_anomaly(transaction):

    if transaction['amount'] > 10000:

        return True, 'Transaction amount above 10000'

    return False, ''