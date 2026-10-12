def forecast_next(values, horizon=6):
    if not values:
        return [0.0] * horizon
    last = float(values[-1])
    return [last] * horizon

def peak_alert(values, limit):
    return [i for i, v in enumerate(values) if v > limit]

def summarize(points):
    count = len(points)
    if count == 0:
        return {
            'count': 0,
            'mean_power_kw': 0.0,
            'min_power_kw': 0.0,
            'max_power_kw': 0.0
        }
    powers = [p['power_kw'] for p in points]
    mean_power = sum(powers) / count
    min_power = min(powers)
    max_power = max(powers)
    return {
        'count': count,
        'mean_power_kw': mean_power,
        'min_power_kw': min_power,
        'max_power_kw': max_power
    }
