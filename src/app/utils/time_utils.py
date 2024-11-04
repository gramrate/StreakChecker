import datetime


def get_time():
    return datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S")


def substr_time(date1: str, date2: str):
    d1 = datetime.datetime.strptime(date1, "%Y/%m/%d-%H:%M:%S")
    d2 = datetime.datetime.strptime(date2, "%Y/%m/%d-%H:%M:%S")
    res = abs(d1 - d2)
    return res


def check_session_time(time1: str, time2: str):
    s_time = substr_time(time1, time2)
    return s_time <= datetime.timedelta(hours=24)


def check_streak_time_into(time1: str, time2: str):
    s_time = substr_time(time1, time2)
    return datetime.timedelta(hours=24) <= s_time <= datetime.timedelta(hours=48)

def check_streak_time_over(time1: str, time2: str):
    s_time = substr_time(time1, time2)
    return s_time > datetime.timedelta(hours=48)
