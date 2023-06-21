import re
import spacy
from keybert import KeyBERT
from zhkeybert import KeyBERT as KB
from zhkeybert import extract_kws_zh


# 清洗字符串-把字符中的特殊字符和“nan”字符去掉， 把字符中的双引号改为单引号
def clean_str(text):
    text = str(text)
    # 判断空字符串
    if text == "nan" or len(text.strip()) == 0:
        return ""
    else:
        # 去除html符号
        html_clean = re.compile("<.*?>")
        text = re.sub(html_clean, "", text)
        # 去除特殊符号
        special_clean = re.compile("[^\w\s]]")
        text = re.sub(special_clean, "", text)
        return text.replace("'", '"')


# 获取关键词
class KeysExtract:
    def __init__(self, language):
        if language == "中文":
            self.model = KB(model="paraphrase-multilingual-MiniLM-L12-v2")
        else:
            self.model = KeyBERT(model="all-mpnet-base-v2")

    def get(self, text, language):
        # 先清洗
        text_after_clean = clean_str(text)
        if language == "中文":
            keywords = extract_kws_zh(text_after_clean, self.model, diversity=0.8, top_n=5)
            key_list = list(dict(keywords).keys())
            return key_list
        else:
            keywords = self.model.extract_keywords(
                text_after_clean, keyphrase_ngram_range=(1, 3), stop_words="english", use_mmr=True, diversity=0.8, top_n=5
            )
            keys_list = list(dict(keywords).keys())
            return keys_list


# NER获取文本中的命名实体
class NER:
    def __init__(self, language):
        if language == "中文":
            self.ner = spacy.load("zh_core_web_trg")
        else:
            self.ner = spacy.load("en_core_trf")

    def get(self, text):
        per_list = set()
        org_list = set()
        # 先清洗
        text_after_clean = clean_str(text)
        doc = self.ner(text_after_clean)
        for i in doc.ents:
            if i.label_ == "PERSON":
                per_list.add(str(i))
            if i.label_ == "ORG":
                org_list.add(str(i))
        return per_list, org_list


