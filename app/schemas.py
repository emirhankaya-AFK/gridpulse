from pydantic import BaseModel, Field
from typing import List

class TelemetryPoint(BaseModel):
    timestamp: str
    device_id: str
    power_kw: float
    voltage_v: float = Field(default=230.0)
    current_a: float = Field(default=0.0)

class AnalyzeRequest(BaseModel):
    points: List[TelemetryPoint]
    baseline_power_kw: List[float] = Field(default_factory=list)
