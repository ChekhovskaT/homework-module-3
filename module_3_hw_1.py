from datetime import datetime

def get_days_from_today(date):
    try:
        # Converting a string to a datetime object
        datetime_obj = datetime.strptime(date, '%Y-%m-%d').date()

        # Getting the current date
        current_date = datetime.today().date()

        # Calculation of the difference in days
        date_difference = current_date - datetime_obj

        # Return the number od days as an integer
        return date_difference.days
    
    except ValueError:
        #return a message if an incorrect date format was entered
        print("Incorrect format! Use 'YYYY-MM-DD'")
        return None
    
# Examples
print(get_days_from_today('2020-10-09'))
print(get_days_from_today('2027-01-15'))
print(get_days_from_today('14.03.2024'))