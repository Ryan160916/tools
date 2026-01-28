import os 

def search(dir_path,dir_name):
    """
    功能：可以判断这个文件指定路径下有没有。
    
    输入参数：
    dir_path:文件的路径。
    dir_name:文件的名字。
    
    输出参数：
    result:判断有没有找到指定文件。
    """
    dir_path = os.listdir(dir_path)
    
    result = ''
    for item in dir_path:
        if item == dir_name:
            result = '找到了'
    result = '没找到'
    return result

def write_file(path, text):
    """
    功能：可以在指定的文件上写东西，如果没有就会创建一个文件。

    输入参数：
    path:文件的路径。
    text:你想在文件上写的东西。
    """
    file = open(path,'a',encoding = 'utf-8')
    file.write(text)
    file.close()

def read_file(path):
    """
    功能：可以把文件读出来。

    输入参数：
    path：文件的路径。
    
    输出参数：
    lines：文件内容。
    """
    file = open(path, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    return lines


if __name__ == '__main__':
    a = 'D:/soft'
    dir_name = 'PortableApps'
    result = search(a,dir_name)
    print(result) 

    a = 'D:/work/study_python/ryan/90338.txt'
    text = '我喜欢lll'
    b = write_file(a,text)

    c = read_file(a)
    print(c)
  
  
