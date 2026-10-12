# GridPulse — Energy Intelligence MVP

**Status: MVP completed — synthetic-data evaluation only.**

GridPulse analyzes electrical telemetry, summarizes power demand, produces a simple short-horizon forecast, and flags peak-demand points through a FastAPI service.

## Run

```bash
python -m pip install -e ".[test]"
uvicorn app.main:app --reload
pytest -q
```

Endpoints: `GET /health`, `POST /analyze`.

## Türkçe

GridPulse elektrik telemetrisi için güç tüketimi özeti, kısa vadeli tahmin ve tepe talep uyarısı sunan bir FastAPI MVP’sidir. Değerlendirmeler sentetik veriyle yapılır; üretim sistemi değildir.

## Deutsch

GridPulse ist ein FastAPI-MVP zur Analyse elektrischer Telemetrie mit Lastzusammenfassung, Kurzzeitprognose und Spitzenlastwarnung. Die Auswertung verwendet synthetische Daten und ist kein Produktionssystem.
