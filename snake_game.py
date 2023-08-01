#imports
from tkinter import *
import random
import pygame

#main code I learnt from Bro Code on youtube

    #Snake Game
    #settings
game_width = 600
game_height = 600
speed = 100
space_size = 30
body_part = 3
snake_color = ('blue')
food_color = ('yellow')
backgound = 'black'

    #MAIN CODE GOES HERE
    #I learnt this code from BRO CODE channel on YOUTUBE
    #Snake class
class Snake:
        def __init__(self):
            self.body_size = body_part
            self.coordinates = []
            self.squares = []

            for i in range(0, body_part):
                self.coordinates.append([0,0])
            
            for x,y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color, tag='snake')
                self.squares.append(square)

    #Food class
    
class Food:
        def __init__(self):
            x = random.randint(0, (game_width/space_size)-1)*space_size
            y = random.randint(0, (game_height/space_size)-1)*space_size
            self.coordinates = [x,y]

            canvas.create_oval(x, y, x + space_size, y +space_size, fill=food_color, tag='food')
    #next turn
def next_turn(snake, food):
        x, y = snake.coordinates[0]
        if direction == 'up':
            y -= space_size
        elif direction == 'down':
            y += space_size
        elif direction == 'left':
            x-= space_size
        elif direction == 'right':
            x += space_size
        snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y , x+space_size, y+space_size, fill=snake_color)
        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            global score
            score += 1
            label.config(text=f'Score: {score}')
            canvas.delete('food')
            food = Food()
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]
        
        if check_collision(snake):
            game_over()

        else:
            window.after(speed, next_turn, snake, food)

    #change direction
def change_direction(new_direction):
        global direction

        if new_direction == 'left':
            if direction != 'right':
                direction = new_direction
        elif new_direction == 'right':
            if direction != 'left':
                direction = new_direction
        elif new_direction == 'up':
            if direction != 'down':
                direction = new_direction
        elif new_direction == 'down':
            if direction != 'up':
                direction = new_direction

    #check collision
def check_collision(snake):
        x,y = snake.coordinates[0]

        if x < 0 or x >= game_width:
            return True
        
        elif y < 0 or y >= game_height:
            return True
        
        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                print('game over')
                return True
        return False  
    
    #game over 
def game_over():
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                        font=('IranNastaliq', 50), text='GAME OVER', fill='red', tag='game over')
window = Tk()
window.title('Snake Game')
window.resizable(False, False)

pygame.mixer.init()
pygame.mixer.music.load('C:\\Users\\shahr\\OneDrive\\Desktop\\main\\124.mp3')
pygame.mixer.music.play(loops=0)

score = 0
direction = 'down'
canvas = Canvas(window, bg=backgound, height=game_height, width=game_width)
canvas.pack()
    
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<Up>', lambda event: change_direction('up'))
snake = Snake()
food = Food()

next_turn(snake, food)

name = Label(window, text='Made by MHA 2023', font=('Comis Sans M', 11))
name.pack()
label = Label(window, text=f'Score: {score}', font=('consola', 45))
label.pack()

window.mainloop()
