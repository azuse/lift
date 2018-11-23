import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.OUT)
#方向正，低电平正转，高电平反转
GPIO.setup(31,GPIO.OUT)
#脱机正，低电平工作，高电平脱机
GPIO.setup(33,GPIO.OUT)
GPIO.output(33,GPIO.LOW)
time.sleep(2)
#GPIO.setup(等下再接线的LED1,GPIO.OUT)
#GPIO.setup(等下再接线的LED2,GPIO.OUT)
#GPIO.setup(等下再接线的LED3,GPIO.OUT)
#GPIO.setup(等下再接线的LED4,GPIO.OUT)
#GPIO.setup(等下再接线的LED5,GPIO.OUT)
#GPIO.setup(等下再接线的LED6,GPIO.OUT)
#GPIO.setup(等下再接线的LED7,GPIO.OUT)
#GPIO.setup(等下再接线的LED8,GPIO.OUT)
#在目标楼层亮起灯，作为执行成功的反馈
#认为整个行程为40cm，划分8个拟似楼层，5cm为一个拟似楼层
#认为整个状态下移动匀速，即移动相同距离的时间相同
GPIO.output(31,GPIO.HIGH)
time.sleep(2)
GPIO.output(31,GPIO.LOW)
time.sleep(2)
GPIO.output(29,GPIO.LOW)
time.sleep(2)
GPIO.output(29,GPIO.HIGH)
#开机初始化为脱机状态，维持原位置
#b = 1
#电梯初始在一楼
#c = 0
#初始化步数

#while True:
    #a = 0
    #a = a + input()
    #读入目标楼层数
    #认为当前（调试前第一次）拟似电梯轿厢（滑块）的位置为一楼
    #if a = 0:
        #GPIO.output(等下再接线的脱机正,GPIO.HIGH)
        #当没有输入时，丝杆电机脱机状态
    #else:
        #GPIO.output(等下再接线的LEDa,GPIO.HIGH)
        #亮起目标楼层的LED灯
        #b = b
        #b作为一个寄存器，存放前一个状态
        #c = a - b
        #c为前后状态的差值，即电梯移动步数
        #if c > 0:
            #当有输入时，丝杆电机工作状态
            #后按的人的目标楼层数比前一个大，即电梯需要向上移动，正转
            #GPIO.output(等下再接的方向正,GPIO.LOW)
            #time.sleep(c*等下测一下跑5cm要几秒)
            #正转c个单位秒数
            #GPIO.output(等下再接的脱机正,GPIO.HIGH)
            #到达目标楼层，脱机，停止工作
            #GPIO.output(等下再接线的LEDa,GPIO.LOW)
            #到达目标楼层，目标楼层灯灭
            #b = a
            #更新寄存器状态
            #time.sleep(0.01)
        #elif c < 0:
            #当有输入时，丝杆电机工作状态
            #后按的人的目标楼层数比前一个小，即电梯需要向下移动，反转
            #GPIO.output(等下再接的方向正,GPIO.HIGH)
            #time.sleep(c*等下测一下跑5cm要几秒)
            #反转c个单位秒数
            #GPIO.output(等下再接的脱机正,GPIO.HIGH)
            #到达目标楼层，脱机，停止工作
            #GPIO.output(等下再接线的LEDa,GPIO.LOW)
            #到达目标楼层，目标楼层灯灭
            #b = a
            #更新寄存器状态
            #time.sleep(0.01)
    

GPIO.cleanup()
