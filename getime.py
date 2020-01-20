import time


def get_current_time():
    time_stamp = time.time()  # 当前时间的时间戳
    local_time = time.localtime(time_stamp)  #
    str_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(time_stamp, "\n", local_time, "\n", str_time)


if __name__ == "__main__":
    get_current_time()