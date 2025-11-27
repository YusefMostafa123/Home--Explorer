from pathlib import Path

# Constants for later use
MILES_PER_DEG = 69.0
RADIUS_MILES = 0.6
MILES_PER_DEGREE = 69.0
RADIUS_DEG = RADIUS_MILES / MILES_PER_DEGREE
RADIUS_SQ = RADIUS_DEG * RADIUS_DEG
LOW_MAX_CRIMES = 166
MEDIUM_MAX_CRIMES = 625
ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "home_explorer.db"

# Given: # of Total Crimes
# Returns: String of relative crime rate
def crime_severity_label(total_crimes: int) -> str:
    """Map total crimes to Low / Medium / High."""
    if total_crimes <= 166:
        return "Low"
    elif total_crimes <= 625:
        return "Medium"
    else:
        return "High"
    

