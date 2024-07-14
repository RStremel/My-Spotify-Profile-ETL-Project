def ms_to_minutes_and_seconds(duration_ms: int) -> str:
        """
        Transform the duration of a track in milliseconds to a minute:seconds (mm:ss) format.
        """
        total_seconds = duration_ms/1000
        minutes = int(total_seconds//60)
        seconds = int(total_seconds % 60)
        duration_mm_ss =  f"{minutes:02}:{seconds:02}"
        
        return duration_mm_ss
