import requests
import wget
from ljhSpider.api_functions.header_api import header


def download_img_requests(url, save_path):
    response = requests.get(url, headers=header())
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
        print("图片下载完成！")
    else:
        print("无法下载图片文件。")


def download_img_by_wget(url, save_path):
    try:
        wget.download(url, save_path)
        print("图片下载完成！")
    except Exception as e:
        print("无法下载图片文件。", str(e))
