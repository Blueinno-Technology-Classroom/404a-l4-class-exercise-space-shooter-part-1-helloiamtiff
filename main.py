import pgzrun
import random

WIDTH = 1024
HEIGHT = 768

player = Actor("playership2_blue")
player.pos = (WIDTH/2, HEIGHT/2)

enemies = []
lasers = []
elasers = []

def update():

    if random.randint(0, 100)<5:
        enemy = Actor("enemygreen5")
        enemy.x = random.randint(0, WIDTH)
        enemies.append(enemy)

    for e in enemies:
        if random.randint(0, 100)<20:
            elaser = Actor('laserred07')
            elaser.pos = e.pos
            elasers.append(elaser)

    if keyboard.space:
        laser = Actor('laserblue01')
        laser.pos = player.pos
        lasers.append(laser)

    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5

    if player.left <= 0:
        player.left =0
    if player.right >= WIDTH:
        player.right = WIDTH
    if player.top <= 0:
        player.top =0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT

    for l in lasers:
        l.y -= 5
        if l.bottom < 0:
            lasers.remove(l)
            continue 
    for e in enemies:
            if l.colliderect(e):
                lasers.remove(l)
                enemies.remove(e)
    for el in elasers:
        el.y+=5
        if el.top > HEIGHT:
            elasers.remove(el)
            continue

    

def draw():
    screen.clear()

    for l in lasers:
        l.draw()

    for el in elasers:
        el.draw()

    player.draw()

    for e in enemies:
        e.draw()

pgzrun.go()