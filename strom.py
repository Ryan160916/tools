import storm_utils 

class Strom():
    def __init__(self,level,str_name,str_speed,qiya):
        self.level = level
        self.name = str_name
        self.speed = str_speed
        self.qiya = qiya
        
    def update_wind(self,sudu):
        self.speed = sudu

    def destroy(self):
        return '此次台风摧毁了牙买加西南部地区。'
    
    def __str__(self):
        return str(self.level) + self.name  + self.speed + str(self.qiya)

    def taifeng_jibie_he_yujing(self,number,a,b):
        storm_utils.taifeng_jibie_he_yujing(number,a,b)

    def leiyudafeng_yujing(number):
        storm_utils.leiyudafeng_yujing(number)

    
if __name__ == '__main__':
    meilisha = Strom(19,'梅丽莎','82m/s',892)
    print(meilisha)

    number = int(input('请输入你的台风等级：'))
    a = int(input('请输入你的台风降水：'))
    b = int(input('请输入你的台风气压'))
    meilisha.taifeng_jibie_he_yujing(number,a,b)







        

    


        

