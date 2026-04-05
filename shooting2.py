import pgzrun, random,pyautogui
WIDTH,HEIGHT=pyautogui.size()

vampires=[]

player=Actor("hunter.webp")
player.pos=WIDTH/2,HEIGHT-200
def draw():
    screen.blit("bg.jpg",(0,0))
    player.draw()
    for i in vampires:
        i.draw()

def update():
    if keyboard.left:
        player.x-=10
    if keyboard.right:
        player.x+=10
    if player.x <0:
        player.x=WIDTH
    if player.x>WIDTH:
        player.x=0
    # create_vampire()
    for i in vampires:
        i.y+=10
        if i.y>HEIGHT:
            vampires.remove(i)
         if i.colliderect(player):
            vampires.remove(i)     

def create_vampire():
    v=Actor("vampire.png")
    v.pos=random.randint(0,WIDTH),0
    vampires.append(v)

clock.schedule_interval(create_vampire,1)    

pgzrun.go()
