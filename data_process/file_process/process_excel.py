import pandas as pd
import json
from pandas import DataFrame


def process_line(ls):
    c = 0
    obj = {
        "website_name": ls[0],
        "website_id": ls[1],
        "website_url": ls[2],
        "website_type": ls[3],
        "country": ls[4],
        "language": ls[5],
        "module_info": []
    }
    for info in ls[6:len(ls):2]:
        if str(info) != "nan":
            m_o = {
                "module": info,
                "module_url": ls[ls.index(info) + 1]
            }
            obj['module_info'].append(m_o)
            c += 1
    return c


def process_json(path):
    out_put = []
    with open(path, "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    for obj in data:
        for module_obj in obj['module_info']:
            init_data = [obj['website_id'], obj['website_name'], 0, "", obj['website_url'], obj['website_type']]
            init_data.append(module_obj['module'])
            init_data.append(module_obj['module_url'])
            out_put.append(init_data)
            print(init_data)
            print(len(init_data))
    df = DataFrame(out_put,
                   columns=['website_id', 'website_name', 'grade', 'grade_desc', 'website_url', 'website_type',
                            'module', 'module_url'])
    df.to_excel("result.xlsx")


path = r'C:\Users\luojunhui\Desktop\中信所\颠覆性技术中心\230049 (二期）\监测源\20230625玛达新增数据源.xlsx'

data = pd.read_excel(path).values.tolist()

co = 0
for line in data:
    co += process_line(line[1:])
print(co)