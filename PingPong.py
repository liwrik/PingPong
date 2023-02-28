from pygame import*

window = display.set_mode((500, 500))

timer = time.clock()

FPS = 60

window.fill(100, 200, 150)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    window.draw()

    display.update()
    timer.tick(FPS)
