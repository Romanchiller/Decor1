import datetime

def get_datetime_now():
    date_today = datetime.date.today()
    time_now = datetime.datetime.now().time()
    return date_today, time_now

def write_log(file_name, data):
    with open(file_name, 'a') as f:
        f.write(data)
    return


