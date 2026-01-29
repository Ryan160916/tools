def taifeng(number):
    '''
    功能：判断台风等级
    number:台风等级
    '''
    yujing = ''
    if number > 17:
        yujing = '超顶台风'
    elif number == 17:
        yujing = '超强台风'
    elif number == 16:
        yujing = '超强台风'
    elif number == 15:
        yujing = '强台风'
    elif number == 14:
        yujing = '强台风'
    elif number == 13:
        yujing = '台风'
    elif number == 12:
        yujing = '台风'
    elif number == 11:
        yujing = '强热带风暴' 
    elif number == 10:
        yujing = '强热带风暴'     
    elif number == 9:
        yujing = '热带风暴'
    elif number == 8:
        yujing = '热带风暴' 
    elif number == 7:
        yujing = '热带低压'
    elif number == 6:
        yujing = '热带低压'
    elif number == 5:
        yujing = '热带扰动'
    elif number == 4:
        yujing = '热带扰动'
    else:
        yujing = '输入不正确'   
    
    return yujing 

def baoyu(a):
    '''
    功能：判断暴雨等级
    a:降雨量
    '''
    yujing = ''
    if a > 250:
        yujing ='特大暴雨'
    elif a > 200 and a < 250:
        yujing ='大暴雨'
    elif a > 50 and a <= 200:
        yujing ='暴雨'
    elif a > 30 and a <= 50:
        yujing ='大雨'
    elif a > 10 and a <= 30:
        yujing ='中雨'
    elif a > 5 and a <= 10:
        yujing ='小雨'
    else:
        yujing ='输入不正确'  

    return yujing 
     
def qiya(b):
    '''
    功能：判断台风的气压
    b:气压
    '''
    yujing = ''
    if b == b:
        yujing = str(b)+'百帕'
    else:
        yujing ='输入不正确'

    return yujing 


def taifengyujing(number,a):
    '''
    功能：判断台风预警级别
    number:台风级别
    a:降雨量
    '''
    yujing = ''
    if number > 17:
        yujing ='台风红色预警'
    elif number == 17:
        yujing ='台风红色预警'
    elif number == 16:
        yujing ='台风红色预警'
    elif number == 15:
        yujing ='台风红色预警'
    elif number == 14:
        yujing ='台风红色预警'
    elif number == 13 and a >= 200:
        yujing ='台风红色预警'
    elif number == 13:
        yujing ='台风橙色预警' 
    elif number == 12 and a >= 200:
        yujing ='台风红色预警'
    elif number == 12:
        yujing ='台风橙色预警' 
    elif number == 11:
        yujing ='台风黄色预警'  
    elif number == 10:
        yujing ='台风黄色预警'      
    elif number == 9:
        yujing ='台风蓝色预警'
    elif number == 8:
        yujing ='台风蓝色预警'   
    elif number == 7:
        yujing ='台风白色预警'
    elif number == 6:
        yujing ='台风白色预警'
    
    return yujing 

def baoyu_yujing(a):
    '''
    功能：判断暴雨预警
    a:降水量
    '''
    yujing=''
    if a > 250 or a == 250 :
        yujing ='暴雨红色预警'
    elif a > 200 and a < 250:
        yujing ='暴雨橙色预警'
    elif a > 50 and a < 200:
        yujing = '暴雨黄色预警'
    elif a > 30 and a < 50:
        yujing = '暴雨蓝色预警'
        
    return yujing


def dafeng_yujing(number):
    '''
    功能：判断大风预警
    number:台风等级
    '''
    yujing = ''
    if number > 17:
        yujing = '大风红色预警'
    elif number == 17:
        yujing='大风红色预警'
    elif number == 16:
        yujing='大风红色预警'
    elif number == 15:
        yujing='大风橙色预警'
    elif number == 14:
        yujing='大风黄色预警'
    elif number == 13:
        yujing='大风黄色预警'
    elif number == 12:
        yujing='大风蓝色预警' 
    elif number == 11:
        yujing='大风蓝色预警'  
    elif number == 10:
        yujing='大风蓝色预警'      
    elif number == 9:
        yujing='大风蓝色预警'
    elif number == 8:
        yujing='大风蓝色预警'  
        
    return yujing 

def leiyudafeng_yujing(number):
    '''
    功能：判断雷雨大风预警
    number:台风等级
    '''
    yujing = ''
    if number > 17:
        yujing ='雷雨大风红色预警'
    elif number == 17:
        yujing ='雷雨大风橙色预警'
    elif number == 16:
        yujing ='雷雨大风橙色预警'
    elif number == 15:
        yujing ='雷雨大风黄色预警'
    elif number == 14:
        yujing ='雷雨大风黄色预警'
    elif number == 13:
        yujing ='雷雨大风黄色预警'
    elif number == 12:
        yujing ='雷雨大风蓝色预警'
    elif number == 11:
        yujing ='雷雨大风蓝色预警'
    
    return yujing 


def taifeng_jibie_he_yujing(number,a,b):
    tf_str = taifeng(number)
    tf_yujing=taifengyujing(number,a)
    df_yujing=dafeng_yujing(number)
    lydf_yujing=leiyudafeng_yujing(number)
    baoyu_=baoyu(a)
    by_yujing=baoyu_yujing(a)
    tf_qiya=qiya(b)
    print('你输入的台风级别:', number, '级','，降雨量:', a, '气压:', b)
    print(tf_str)    
    print(baoyu_)
    print(tf_qiya)
    
    print('='*10,'配置的预警如下:', '='*10)
    print(tf_yujing)
    print(df_yujing)
    print(lydf_yujing)
    print(by_yujing)
    print('='*50)

if __name__ == '__main__':
    '''
    这个程序可以把台风的数字的等级转化成文字的台风等级，把暴雨的降雨量转化成等级，把气压显示，还会把这些台风的数据
    配置一些预警信号。
    '''
    number=int(input('输入你的台风等级:'))
    a=int(input('输入你的台风降水量:'))
    b=int(input('输入你的台风气压:'))
    taifeng_jibie_he_yujing(number,a,b)
    