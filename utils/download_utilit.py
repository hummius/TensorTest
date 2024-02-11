import os
from time import sleep
from pathlib import Path


class DownloadError(Exception):
    pass


def dir_create():
    if not os.path.exists("./downloads"):
        os.mkdir("./downloads")


def file_delete(file_name):
    if os.path.isfile(f"./downloads/{file_name}"):
        os.remove(f"./downloads/{file_name}")


def download_check(file_name, size):
    root = Path(__file__).parent.parent
    file_path = os.path.join(root, f"downloads/{file_name}")
    count = 0
    while not os.path.isfile(file_path):
        sleep(5)
        if count != 10:
            count += 1
        else:
            raise DownloadError(f"File download failed. Something goes wrong ;(")
    if round((os.path.getsize(file_path) / 1048576), 2) == size:
        return True
    else:
        return False
