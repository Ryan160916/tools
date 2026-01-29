def write(path,text):
    file = open(path,'a',encoding='utf-8')
    file.write(text)
    file.close()

a = 'D:/work/study_python/ryan/90339.txt'
text = '我喜欢11'
b = write(a,text)

def read(path):
    file = open(path,'r',encoding='utf-8')
    texts = file.readlines()
    file.close()
    return texts

a = 'D:/work/study_python/ryan/fs.py'    
c = read(a)
print(c)





    