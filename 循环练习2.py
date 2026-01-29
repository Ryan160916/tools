
def my_print_2(list1):
    '''
    输入参数：list1。
    功能：可以循环判断一下列表里的值是否是偶数，是偶数就打印。
    '''
    '''
    1.1 先创建一个函数,开头要是def。然后给函数取一个名字,不要重复。再增加一个list1列表,取好名字后，再把它放在一个括号里，别忘了加冒号。
    
    1.2 然后就进入了循环，写一个for，然后再添加一个item变量，写一个in，把刚刚添加的list1列表放到后面，再加上冒号。这样做可以把list1里的东
    西循环放到item变量里。
    '''
    for item in list1:
        #1.3 然后套上刚刚添加的item变量把它除以2，这样做可以让它判断它是否是偶数。
        if item % 2 == 0:
        #1.4 然后打印一下item变量，这样做可以把判断好的东西都打印一下，打印不是用打印机来打印，是显示在屏幕上。  
            print(item)
'''
1.5 总结：函数写完后要加冒号，写完for也要加冒号。写for循环开头要加for。写好循环拿列表里的值的变量后，要加in。循环拿列表里的值的变量尽量把
名字写成item。for循环的for必须写在函数下面的四个空格下面，也可以直接敲Tab，但是不要混用Tab和四个空格。在python中想运行代码可以直接点小箭
头，也可以右键点击Run Python，然后再点击Run Python fine in Terminal。
'''

def my_print_3(list2):
    '''
    输入参数：list2。
    功能：可以
    '''

    length = len(list2)
    index = 0
    while index < length:
        if list2[index] % 2 == 0:
            print(list2[index])     
        index = index + 1
        

if __name__ == '__main__':
    print('=====================================') 
    print('                                     ')
    print('        现在开始学习for循环            ')
    print('                                     ') 
    print('=====================================')
    list2=[12,14,84,33]        
    a = my_print_2(list2)        
    print('=======================================') 
    print('                                       ')
    print('        现在开始学习while循环            ')
    print('                                       ') 
    print('=======================================')
    list2=[12,14,84,33]        
    a = my_print_3(list2)               



