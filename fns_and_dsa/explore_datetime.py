import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)
    
    
    
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date_time = datetime.datetime.now()
    
    future_date = current_date_time + timedelta(days=number_of_days)
    
    
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")
    
calculate_future_date()
    