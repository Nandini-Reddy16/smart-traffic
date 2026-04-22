import random

def analyze_traffic():
    results = []

    for i in range(3):
        traffic_time = random.randint(2, 15)

        if traffic_time < 5:
            level = "LOW"
        elif traffic_time < 10:
            level = "MEDIUM"
        else:
            level = "HIGH"

        results.append(f"Road {i+1}: {traffic_time} mins ({level})")

    return "\n".join(results)