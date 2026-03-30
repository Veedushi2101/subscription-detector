from collections import defaultdict
from utils import clean_name, is_monthly_pattern

def detect_subscriptions(transactions):
    grouped = defaultdict(list)

    for txn in transactions:
        clean_desc = clean_name(txn['description'])

        # Allow small variation in amount
        amount_bucket = round(txn['amount'])

        key = (clean_desc, amount_bucket)
        grouped[key].append(txn)

    subscriptions = []

    for (desc, amount), txns in grouped.items():
        dates = [t['date'] for t in txns]

        if is_monthly_pattern(dates):
            confidence = min(1.0, len(txns) / 3)

            subscriptions.append({
                'name': desc,
                'amount': amount,
                'occurrences': len(txns),
                'confidence': round(confidence, 2)
            })

    return subscriptions