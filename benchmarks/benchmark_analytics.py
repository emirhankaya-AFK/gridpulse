import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import json, time
from app.analytics import forecast_next, peak_alert, summarize

def _data():
    return [float(i) for i in range(1000)]

def _bench(fn, data, iters=100):
    times = []
    for _ in range(iters):
        t0 = time.perf_counter()
        if fn is peak_alert:
            fn(data, 900.0)
        elif fn is summarize:
            fn([{'power_kw': x} for x in data])
        else:
            fn(data)
        times.append((time.perf_counter() - t0) * 1000)
    total = sum(times)
    mean = total / iters
    srt = sorted(times)
    p95 = srt[int(0.95 * iters) - 1] if iters else 0.0
    return {
        "operation": fn.__name__,
        "iterations": iters,
        "total_ms": round(total, 3),
        "mean_ms": round(mean, 3),
        "p95_ms": round(p95, 3)
    }

if __name__ == "__main__":
    d = _data()
    out = [_bench(forecast_next, d), _bench(peak_alert, d), _bench(summarize, d)]
    print(json.dumps(out, indent=2))

