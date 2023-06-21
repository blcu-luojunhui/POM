import os
from ljhSpider.download import pdf_download, img_download
from datetime import datetime
import pymysql
from sshtunnel import SSHTunnelForwarder
from concurrent.futures.thread import ThreadPoolExecutor


class Mail:
    def __init__(self):
        self.server = SSHTunnelForwarder(
            ('61.160.201.138', 60022),
            ssh_password="2gKovYId7jVgVWHj",
            ssh_username="java_developer",
            remote_bind_address=("127.0.0.1", 3306),
        )
        self.server.start()
        self.host = '127.0.0.1'
        self.user = 'luojunhui'
        self.port = '3306'
        self.password = 'JFFoLGmbcb60KVYv'
        self.db = 'tech_monitor'
        self.today = datetime.today().__str__().split(" ")[0]

    def get_info_from_mysql(self):
        conn = pymysql.connect(host=self.host,
                               user=self.user,
                               password=self.password,
                               db=self.db,
                               port=self.server.local_bind_port
                               )
        sql = "SELECT news_id, image_url from articles"
        cursor = conn.cursor()
        cursor.execute(sql)
        data_list = cursor.fetchall()
        return data_list


def download(args):
    news_id = args[0]
    img_url = args[1]
    if img_url.endswith(".pdf"):
        pdf_path = os.path.join('pdf', news_id.split("-")[1], img_url.split("/")[-1])
        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
        pdf_download.download_pdf_by_wget(img_url, pdf_path)
    else:
        img_download.download_img_by_wget(img_url, os.path.join('image', news_id + ".png"))


if __name__ == "__main__":
    info_list = Mail().get_info_from_mysql()
    with ThreadPoolExecutor(max_workers=10) as Pool:
        Pool.map(download, info_list)
