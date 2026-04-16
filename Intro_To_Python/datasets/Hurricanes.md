# Hurricane fatalities and gender of names

Data used in CENSORED analysis of the effect of name gender on hurricane fatalities. Note that hurricanes Katrina (2005) and Audrey (1957) were removed from the data.

## Files

- `Hurricanes.csv` — per-hurricane records of fatalities, storm severity, and name femininity ratings

## Variables

| Column | Description |
|--------|-------------|
| `name` | Given name of hurricane |
| `year` | Year of hurricane |
| `deaths` | Number of deaths |
| `category` | Severity code for storm |
| `min_pressure` | Minimum pressure, a measure of storm strength (lower = stronger) |
| `damage_norm` | Normalized estimate of damage in dollars |
| `female` | Indicator variable for female name |
| `femininity` | 1–11 scale from totally masculine (1) to totally feminine (11). Average of 9 rater scores. |
