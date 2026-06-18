class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Hour hand angle
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        
        # Minute hand angle
        minute_angle = minutes * 6
        
        # Difference
        angle = abs(hour_angle - minute_angle)
        
        # Smaller angle
        return min(angle, 360 - angle)