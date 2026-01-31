import streamlit as st
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import WebBaseLoader

# loader = CSVLoader('D:/work/study_python/ryan/files/Historical_Tropical_Storm_V3.csv',encoding='utf-8')
# documents = loader.load()
# st.write(documents)

# loader2 = PyPDFLoader('D:/work/study_python/ryan/files/wiki-中国历史.pdf')
# documents2 = loader2.load()
# pages = []
# for item in documents2:
#     pages.append(item.page_content)
# st.write(str(pages))

loader3 = Docx2txtLoader('D:/work/study_python/ryan/files/我的好朋友.docx')
documents3 = loader3.load()
pages = []
for item in documents3:
    pages.append(item.page_content)
#st.write(str(pages))


web_urls = ('https://www.bilibili.com/video/BV1YAhQzcEeH','https://space.bilibili.com/374392541')
loader = WebBaseLoader(web_urls)
documents4 = loader.load()
pages = []
for item in documents4:
    pages.append(item.page_content)
#st.write(str(pages))

path = 'D:/work/study_python/ryan/files/金风科技肯德基.txt'
file = open(path,'r',encoding='utf-8')
lines = file.readlines()
file.close()
st.write(str(lines))


