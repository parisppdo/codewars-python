def race(vA, vB, g):
    from datetime import timedelta
    from math import floor
    # Explore the case tortoise A is faster
    if vA >= vB:
        return None
    else:
        # Calculate the asked time in seconds
        seconds = (g / (vB - vA)) * 3600
        # Transform seconds into hours, minuites, seconds
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        # Round down the results
        hours = floor(hours)
        minutes = floor(minutes)
        seconds = floor(seconds)
        return [hours, minutes, seconds]