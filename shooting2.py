import pgzrun, random,pyautogui
WIDTH,HEIGHT=pyautogui.size()
player=Actor("king.png")
player.pos=100,HEIGHT/2
characters=["dracula","mummy","skeleton","zombie", "vampire","treasure"]
vampires=[]
speed=5
gems=[]
score=0
life=3
high_score=0
treasure=0

def draw():
    screen.blit("grave.jpg",(0,0))

    player.draw()
    for i in vampires:
        i.draw()
    for i in gems:
        i.draw()
    screen.draw.text("score->"+str(score),(50,50),fontsize=30)
    screen.draw.text("high_score->{}".format(str(high_score)),(50,100),fontsize=30)
    screen.draw.text(f"Lives->{life}",(300,50),fontsize=30)
    screen.draw.text(f"treasure->{treasure}",(WIDTH-300,50),fontsize=30)
def update():
    global score,high_score,life,treasure
    if keyboard.up:
        player.y-=10
    if keyboard.down:
        player.y+=10
    if player.y <0:
        player.y=HEIGHT
    if player.y>HEIGHT:
        player.y=0
    if treasure>100:
        treasure-=100
        life+=1
    if score>high_score:
        high_score=score    
        

    for i in gems:
        i.x+=speed
        if i.x>WIDTH:
            gems.remove(i)
    for i in vampires:
            i.x-=speed
            if i.x<0:
                vampires.remove(i)
            if i.colliderect(player):
                if i.image=="treasure":
                    treasure+=10
                else:
                    if life>0:
                        life-=1
                    else:
                        print("Game Over")
                vampires.remove(i)
                continue
            for g in gems:
                if g.colliderect(i):
                    if i.image=="treasure":
                        treasure+=10
                    else:
                        score+=10    
                    vampires.remove(i)
                    gems.remove(g)

def on_key_down(key):
    if key==keys.SPACE:
        gem=Actor("diamond")
        gem.pos=player.x+40,player.y-35
        gems.append(gem)



def create_vampire():
    r=random.choice(characters)
    v=Actor(r)
    v.pos=WIDTH-100,random.randint(0,HEIGHT)
    vampires.append(v)

clock.schedule_interval(create_vampire,1)         


pgzrun.go()
