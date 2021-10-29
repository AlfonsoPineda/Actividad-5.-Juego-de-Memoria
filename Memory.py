from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
taps=0 
turned_cards = 0


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    global taps
    taps +=1 # Contabilizando los taps

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        global turned_cards
        turned_cards += 1

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 26, y + 4) 
        color(tiles[mark]*7, 255-tiles[mark]*3, 200-tiles[mark]*5) 
        write(tiles[mark], align="center", font=('Arial', 30, 'normal')) 


    goto(0,210) 
    write (taps,font=("Arial",20)) 
    update()
    if turned_cards==32: 
        up()
        goto(0, 0)
        color('green')
        write("GANASTE",  align="center", font=("Arial", 20, "bold")) 
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
colormode(255)
addshape(car)
hideturtle()
tracer(False)
addshape(car)
onscreenclick(tap)
draw()
done()