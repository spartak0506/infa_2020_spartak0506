from graph import *

penColor('black')
brushColor('yellow')
circle(200, 200, 150)

def circle1 (x, c, pen, brush):
    penColor(pen)
    brushColor(brush)
    circle(x, 170, c)

circle1(265, 25, 'blue', 'blue')
circle1(135, 25, 'blue', 'blue')
circle1(135, 10, 'black', 'black')
circle1(265, 10, 'black', 'black')

moveTo(162, 278)

def smile1(x, y):
    penSize(5)
    while x < 200 and y < 300:
        y += 2
        x += 4
    lineTo(x, y)
    
def smile2(x, y):  
    while y > 278 and x < 238:
        y -= 2
        x += 4 
    lineTo(x, y)
    
smile1(162, 278)
smile2(200, 300)




run()
