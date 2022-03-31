from datetime import date, timedelta



def twodigit(_str):
    if len(_str) < 2:
        return "0" + _str
    return _str

def datetime(_date, _time):
    _date = date.today() + timedelta(days=_date - 1)  

    res = "\'" + str(_date.year) + "-" + twodigit(str(_date.month)) + "-" + twodigit(str(_date.day)) + " " + twodigit(str(_time * 2)) + ":00:00" + "\'"
    return res




print(datetime(2, 2))