from datetime import datetime

# Program: Format dates to the Campus Terms

def get_term(date_str):
    date = datetime.strptime(date_str, "%m/%d/%Y")
    year = date.year
    
    # Define the start and end dates for each term
    spring_start = datetime(year, 1, 15)
    spring_end = datetime(year, 5, 20)
    summer_start = datetime(year, 5, 21)
    summer_end = datetime(year, 8, 20)
    fall_start = datetime(year, 8, 21)
    fall_end = datetime(year, 12, 20)
    winter_start = datetime(year, 12, 21)
    winter_end = datetime(year + 1, 1, 15)
    
    # Check which term the date falls into and return the corresponding term
    if spring_start <= date <= spring_end:
        return f"Spring {year}"
    elif summer_start <= date <= summer_end:
        return f"Summer {year}"
    elif fall_start <= date <= fall_end:
        return f"Fall {year}"
    elif winter_start <= date or date <= winter_end:  # Adjusted condition for winter term
        return f"Winter {year}"
    else:
        return "Unknown term"

# Read input dates from a text file
input_file = "input_dates.txt"
with open(input_file, "r") as file:
    dates = [line.strip() for line in file]

# Output the corresponding term for each date
for date in dates:
    print(get_term(date))
