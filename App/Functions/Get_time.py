from datetime import datetime 

def get_time():
    date_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    
    return date_time