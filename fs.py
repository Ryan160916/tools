import os

def search(dir_path,dir_name):
    dir_path = os.listdir(dir_path)
    
    for item in dir_path:
        if item == dir_name:
            return '找到了'
    return '没找到'


if __name__ == '__main__':
    a = 'D:/soft'
    dir_name = 'PortableApps'
    result = search(a,dir_name)
    print(result)  
  