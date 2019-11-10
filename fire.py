from graphics import *
import random
#     420 pixels
f = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      
def main():
    win=GraphWin("x",350,120)
    win.setBackground('black')

    for t in range(10):
        for i in range(len(f)):
            if int(i) < 35:
                f[i] = random.randrange(0, stop=100, step=99)
            else:
                f[i] =  int(( f[i-35] + f[i-36] + f[i-34] ) / 3) - 10
                if f[i] <= 10: f[i] = 0

            if i in range(0,36):
                yy, xx = 1,i
            elif i in range(36,71):
                yy, xx = 2, i - 35
            elif i in range(71,106):
                yy, xx = 3, i - 70
            elif i in range(106,141):
                yy, xx = 4, i - 105
            elif i in range(141,176):
                yy, xx = 5, i - 140
            elif i in range(176,211):
                yy, xx = 6, i - 175
            elif i in range(211,246):
                yy, xx = 7, i - 210
            elif i in range(246,281):
                yy, xx = 8, i - 245
            elif i in range(281,316):
                yy, xx = 9, i - 280
            elif i in range(316,351):
                yy, xx = 10, i - 315
            elif i in range(351,386):
                yy, xx = 11, i - 350
            elif i in range(386,421):
                yy, xx = 12, i - 420
            pt = Circle(Point(xx * 10, yy * 10), 5)
            pt.setFill(hex(f[i]))
            pt.draw(win)
           # label = Text(Point(xx * 10, yy * 10), f[i])
           # label.setFill('white')
           # label.setSize(5)
           # label.draw(win)

        time.sleep(.75)
        print(t)
            
        
        
        
   
       # win.close()



def hex(r):
    return "#{:02d}{:02d}{:02d}".format(r,0,0) 

def fire():
    win = GraphWin("Fire", 35, 12)
    win.setBackground('black')
    win.getMouse()
    win.close()

main()

