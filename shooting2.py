import pgzrun, random,pyautogui

import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("shooting-game-4ac81-firebase-adminsdk-fbsvc-bb0c1c1d34.json")
if not firebase_admin._apps:

    firebase_admin.initialize_app(cred,{
        "databaseURL":
        "https://shooting-game-4ac81-default-rtdb.firebaseio.com"
    })
ref=db.reference("highscore")

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
gamestate="start"
def save_highscore(score):
    try:
        ref = db.reference("highscore")

        old = ref.get()
        print(old)
        if old is None or score > old:
            ref.set(score)
            print("Highscore Updated!")
    except Exception as e:
        print(e)
        
# get high score
def get_highscore():
    try:
        ref = db.reference("highscore")
        s=ref.get()
        print (s)
        return s
    except Exception as e:
        print (e)
        return 0

print("Highest Score:", get_highscore())
    
def draw():
    screen.blit("grave.jpg",(0,0))
    if gamestate=="start":
        screen.blit("king",(200,300))
        screen.blit("vampire",(WIDTH-300,300))
        screen.blit("treasure",(WIDTH/2,300))
        screen.draw.text("Welcome to Undead Outbreak\n  press space to start\n Move the King using up and down arrow key\n Press space to shoot\n You have 3 lives and you can collect more once you have 100 treasure score\n Protect the king from the vampires or else he loses lives\n shoot enemies to score\n collect treasure for treasure score\n NOW YOU ARE GOOD TO GO! ",center=(WIDTH/2,HEIGHT/2),fontsize=25)

    elif gamestate=="play":
        player.draw()
        for i in vampires:
            i.draw()
        for i in gems:
            i.draw()
        screen.draw.text("score->"+str(score),(50,50),fontsize=30)
        screen.draw.text("high_score->{}".format(str(high_score)),(50,100),fontsize=30)
        screen.draw.text(f"Lives->{life}",(300,50),fontsize=30)
        screen.draw.text(f"treasure->{treasure}",(WIDTH-300,50),fontsize=30)
        
    else:
        screen.draw.text("GAME OVER!\n Press space to start over.",center=(WIDTH/2,HEIGHT/2),fontsize=40)
def update():
    global score,high_score,life,treasure,gamestate
    

    if gamestate=="play":
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
                            gamestate="end"
                            save_highscore(score)
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
    global gamestate, score, life, treasure
    if key==keys.SPACE and gamestate=="play":
        gem=Actor("diamond")
        sounds.shooting.play()
        gem.pos=player.x+40,player.y-35
        gems.append(gem)
    if key==keys.SPACE and gamestate!="play":
        gamestate="play"
        score=0
        life=3
        treasure=0


def create_vampire():
    if gamestate=="play":  
        r=random.choice(characters)
        v=Actor(r)
        v.pos=WIDTH-100,random.randint(0,HEIGHT)
        vampires.append(v)

clock.schedule_interval(create_vampire,1)         








pgzrun.go()