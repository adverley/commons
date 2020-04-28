import datetime


def get_timestamp_human_readable():
    now = datetime.datetime.now()
    now_str = now.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    return now_str


def get_timestamp():
    now = datetime.datetime.now()
    now_str = now.strftime("%d-%m-%Y_%Hh%Mm%Ss")
    return now_str


if __name__ == '__main__':
    print(get_timestamp())
