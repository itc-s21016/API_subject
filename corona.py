import json

import requests


def get_npatients(uri_head, date, item):
    prefName = item
    url = f"{url_head}Covid19JapanAll?dataName={prefName}&date={date}"
    res = requests.get(url)
    values = json.loads(res.text)
    values_npatients = values["itemList"][0]["npatients"]

    return values_npatients


def read_file(file):
    data = open(file)
    data_read = data.read()
    return data_read


def get_date_from_input():
    print("[*]日付のフォーマットはyyyymmddです")
    print("[*]2020年4月22日から有効です")
    date = input("[*]日付を入力:")
    return date


if __name__ == "__main__":
    prefectures = "./prefectures.txt"
    prefectures_data = read_file(prefectures)
    date = get_date_from_input()
    url_head = "https://opendata.corona.go.jp/api/"
    prefectures_list = prefectures_data.split("\n")
    prefectures_list.pop()
    for item in prefectures_list:
        npatients = get_npatients(url_head, date, item)
        print(f"{item}の感染者数は: {npatients}")
