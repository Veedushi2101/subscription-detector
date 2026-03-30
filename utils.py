import re

# Clean merchant name
def clean_name(name):
    name = name.lower()
    name = re.sub(r'[^a-z ]', '', name)
    name = re.sub(r'\s+', ' ', name)
    return name.strip()


# Check if pattern is monthly
def is_monthly_pattern(dates):
    if len(dates) < 3:
        return False

    dates.sort()
    gaps = []

    for i in range(1, len(dates)):
        diff = (dates[i] - dates[i-1]).days
        gaps.append(diff)

    avg_gap = sum(gaps) / len(gaps)

    return 25 <= avg_gap <= 35