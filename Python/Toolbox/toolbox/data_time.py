from datetime import date, datetime


def date_to_db(data: str) -> str:
    if not data:
        return data
    return '-'.join(data.split('/')[::-1])


def str_to_date(value: str) -> date:
    if not value:
        return None
    year, mounth, day = value[0:4], value[5:7], value[8:10]
    return date(int(year), int(mounth), int(day))


def strpt_to_date(value: str) -> date:
    if not value:
        return None
    day, mounth, year = value[0:2], value[3:5], value[6:10]
    return date(int(year), int(mounth), int(day))


def data_to_ptbr(value: str) -> datetime:
    if not value:
        return ""
    year, mounth, day = value[0:4], value[5:7], value[8:10]
    dt = date(int(year), int(mounth), int(day))
    dt = datetime.strftime(dt, '%d/%m/%Y')
    return dt
