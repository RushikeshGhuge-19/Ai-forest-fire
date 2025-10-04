def predict_fire_occurrence(temperature, humidity, wind_speed, rainfall):
    """
    Simple rule-based fire risk prediction.
    Returns 1 if high fire risk, 0 if low fire risk.
    """
    # High fire risk conditions:
    # - High temperature (> 30°C)
    # - Low humidity (< 40%)
    # - High wind speed (> 20 km/h)
    # - Low rainfall (< 5mm)
    
    risk_score = 0
    
    if temperature > 30:
        risk_score += 1
    if humidity < 40:
        risk_score += 1
    if wind_speed > 20:
        risk_score += 1
    if rainfall < 5:
        risk_score += 1
    
    # If 3 or more risk factors, predict fire occurrence
    return 1 if risk_score >= 3 else 0  