import pgzrun, random,pyautogui
WIDTH,HEIGHT=pyautogui.size()
player=Actor("hunter.webp")
player.pos=WIDTH/2,HEIGHT-200
def draw():
    screen.blit("bg.jpg",(0,0))
    player.draw()

def update():
    if keyboard.left:
        player.x-=10
    if keyboard.right:
        player.x+=10
    if player.x <0:
        player.x=WIDTH
    if player.x>WIDTH:
        player.x=0


pgzrun.go()
