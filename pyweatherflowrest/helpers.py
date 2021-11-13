"""Helper Class for Weatherflow Rest module."""

class Conversions:
    """Converts values from metric."""

    async def wind_speed_imperial(self, value) -> float:
        """Returns miles per hour from m/s"""
        if value is None:
            return None
        return round(value * 2.236936292, 1)

    async def pressure_imperial(self, value) -> float:
        """Returns inHg from mb/hPa"""
        if value is None:
            return None
        return round(value * 0.029530, 1)
