import requests
import os


intelligence_dict = {}


def get_intelligence(hero_name):
    url = "https://superheroapi.com/api/2619421814940190/search/" + hero_name
    response = requests.get(url)
    for hero in response.json()["results"]:
        if hero["name"] == hero_name:
            intelligence = hero["powerstats"]["intelligence"]
            intelligence_dict[hero_name] = int(intelligence)


get_intelligence("Hulk")
get_intelligence("Captain America")
get_intelligence("Spider-man")
get_intelligence("Thanos")

v = list(intelligence_dict.values())
k = list(intelligence_dict.keys())
print(f"Наибольший интерллект у персонажа {k[v.index(max(v))]} - {v[v.index(max(v))]} пунктов")


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        file_list = []
        for i in os.walk(self.file_path):
            file_list.append(i)
            for address, dirs, files in file_list:
                for elem in files:
                    get_url = f"https://cloud-api.yandex.net/v1/disk/resources/upload?path={elem}"
                    headers = {"Authorization": "OAuth TOKEN"}
                    response = requests.get(get_url, headers=headers)
                    put_url = response.json()["href"]
                    with open(os.path.join(address, elem), "rb") as f:
                        requests.put(put_url, files={"file": f})
                    print(f'файл {elem} успешно загружен')
        return print("Все файлы загружены")


if __name__ == '__main__':
    uploader = YaUploader('C:\\Users\\user\\Desktop\\HomeAssistant')
    result = uploader.upload()