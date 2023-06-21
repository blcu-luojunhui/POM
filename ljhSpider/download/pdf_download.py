import requests
import wget
from ljhSpider.api_functions import header


def download_pdf_requests(url, save_path):
    response = requests.get(url, headers=header())
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
        print("PDF下载完成！")
    else:
        print("无法下载PDF文件。")


def download_pdf_by_wget(url, save_path):
    try:
        wget.download(url, save_path)
        print("PDF下载完成！")
    except Exception as e:
        print("无法下载PDF文件。", str(e))
