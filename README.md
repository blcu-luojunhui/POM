# POM Project

### crawl multi methods of info from the internet and process them with different tools


### 目录结构
- data_process/
    - cv/
        - image_peocess.py
    - nlps/
- ljhSpider/
    - items.py
    - middlewares.py
    - pipelines.py
    - settings.py
    - __init__.py
    - api_functions/
        - es_api.py
        - header_api.py
        - mongo_api.py
        - mysql_api.py
        - openai_api.py
        - proxy_api.py
        - redis_api.py
        - tools_api.py
    - download/
        - img_download.py
        - pdf_download.py
        - video_download.py
    - get_html_info/
        - by_drissionpage.py
        - by_selenium.py
        - stealth.min.js
    - parse/
        - parse_detail.py
        - url_list_search.py
    - spiders/
        - crawl_anything.py
        - __init__.py


