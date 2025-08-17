#This is code that I had written in Thonny in 2022

from designer import *
from random import randint

'''
This changes the color of the background to
a shade of blue to make it look like the sky.
'''
set_window_color("cornflowerblue")

'''
This dictionary holds the names and types
of variables that will be used in the following
functions.
'''
World = {'bird': DesignerObject,
         'bird speed': int,
         'pipes': [DesignerObject],
         'pipe speed': int,
         'time': int,
         'timer': DesignerObject,
         'sun': DesignerObject,
         'sun speed': int,
         'cloud': DesignerObject,
         'cloud speed': int
         }
'''
Global Args:
    world (World): the dictionary that the game variables
                    are stored in
'''

BIRD_SPEED = -5
PIPE_SPEED = -5
SUN_SPEED = -0.475
CLOUD_SPEED = -1

def create_world() -> World:
    '''
This calls the variables defined in the World
dictionary to create the Flappy Hummingbird world.

    Returns:
        World: creates the game world.
'''
    return {'bird': create_bird(),
            'bird speed': BIRD_SPEED,
            'pipes': [],
            'pipe speed': PIPE_SPEED,
            'time': 0,
            'timer': text('black', ''),
            'sun': create_sun(),
            'sun speed': SUN_SPEED,
            'cloud': create_cloud(),
            'cloud speed': CLOUD_SPEED
            }

def create_bird() -> DesignerObject:
    '''
This function scales down an image of a hummingbird
downloaded from the internet to fit our game world
and assigns it to the bird variable.

    Returns:
        DesignerObject: The image of a hummingbird
'''
    bird = image("Hummingbird.png")
    bird['scale'] = .15
    change_x(bird, -90)
    return bird
    
def create_pipe() -> DesignerObject:
    '''
This function creates an object meant to
resemble a pipe and sets its x and y coordinates.
It also changes the pipe's y coordinates and width by
random chance using the randint function.

    Returns:
        DesignerObject: The image of a pipe
'''
    random_chance = randint(1, 10) == 1
    pipe = rectangle("black", 100, 370)
    pipe['scale'] = .70
    set_x(pipe, 790)
    set_y(pipe, 530)
    if random_chance:
        set_y(pipe, 130)
    return pipe

def create_sun() -> DesignerObject:
    '''
This function creates an object meant
to look like the sun in the background.

    Returns:
        DesignerObject: The image of a sun
'''
    sun = circle("yellow", 40)
    change_xy(sun, 360, -170)
    return sun

def create_cloud() -> DesignerObject:
    '''
This function creates multiple objects
and groups them together to look like a cloud.

    Returns:
        DesignerObject: The image of a cloud
'''
    puff_cloud = circle("white", 20, -300, 80) 
    puff_cloud_2 = change_xy(circle("white", 20), -290, 85)
    puff_cloud_3 = change_xy(circle("white", 20), -315, 90)
    puff_cloud_4 = change_xy(circle("white", 20), -320, 75)
    cloud = group(puff_cloud, puff_cloud_2, puff_cloud_3, puff_cloud_4)
    set_x(cloud, 750)
    set_y(cloud, 120)
    return cloud

def make_pipes(world):
    '''
This function takes the previously defined pipe
variable and stores it in a lit of pipes in order
to generate multiple pipes in the world by random
chance.
'''
    world['pipes'].append(create_pipe())

def move_cloud(world):
    '''
This function moves the cloud left
at the rate of the cloud speed variable.
'''
    world['cloud']['x'] += world['cloud speed']
        
def move_sun(world):
    '''
This function moves the sun left at the rate
of the sun speed variable which has been set
to match the amount of time that it takes
for the player to win the game.
'''
    world['sun']['x'] += world['sun speed']
            
def move_bird(world):
    '''
This function moves the hummingbird down towards
the bottom of the screen by the value of the bird
speed variable.
'''
    world['bird']['y'] += world['bird speed']
    
def move_pipes(world):
    '''
This function moves the pipes left towards the bird
at the rate of the pipe speed variable.
'''
    
    for pipe in world['pipes']:
        pipe['x'] += world['pipe speed']

def change_bird_speed(world):
    '''
This function creates a gravity effect on the speed
at which the bird falls by increasing the bird's speed
at every update.
'''
    world['bird speed'] = world['bird speed'] + 0.2
    
def go_up(world):
    '''
This function causes the bird to move upward
at the bird speed.
'''
    world['bird speed'] = BIRD_SPEED
    world['bird']['change_y'] = True
    
def change_y(world, key: str):
    '''
This function activates the go_up function
when the space bar is pressed.
'''
    if key == 'space':
        go_up(world)
    else:
        go_up(world)
        
def count_time(world):
    '''
This function increases the time variable
every second that the player continues to play.
'''
    world['time'] = world['time'] + 0.02
        
def update_timer(world):
    '''
This function updates the text on the screen
showing the player the amount of time that they
have been playing.
'''
    world['timer']['text'] = "Time: " + str(int(world['time']))

def call_pipes(world):
    '''
This function causes pipes to spawn in the game
every five seconds.
'''
    if "5" in world['timer']['text'] or "0" in world['timer']['text']:
        make_pipes(world)
        
def player_win(world):
    '''
This function pauses the game and
defines the text that
will be shown to the player when they
win the game.
'''
    world['timer']['text'] = "GREAT JOB! YOU WIN!"
    pause()
    
def flash_game_over(world):
    '''
This function pauses the game
and defines the text that
will be shown to the player if they
lose the game.
'''
    world['timer']['text'] = "OOPS! TRY AGAIN!"
    pause()
    
def collide_bird_world(world):
    '''
This function causes the player to
lose the game by calling the
flash_game_over function when they
collide with a pipe or the top or
bottom of the screen.
'''
    for pipe in world['pipes']:
        if colliding(pipe, world['bird']):
            return flash_game_over(world)
    if colliding(world['bird'], 310, 600):
        return flash_game_over(world)
    if colliding(world['bird'], 310, 0):
        return flash_game_over(world)
    
def you_won(world):
    '''
This function causes the player
to win the game by calling the
player_win function when the sun
reaches the left side of the screen
(when they reach a minute of play time).
'''
    if int(world['time']) == 60:
        return player_win(world)
    
when('starting', create_world)
when('updating', move_bird)
when('updating', move_sun)
when('updating', change_bird_speed)
when('typing', change_y)
when('clicking', change_y)
when('updating', call_pipes)
when('updating', move_pipes)
when('updating', move_cloud)
when('updating', count_time)
when('updating', count_time)
when('updating', update_timer)
when('updating', collide_bird_world)
when('updating', you_won)
start()