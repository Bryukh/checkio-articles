Hello everyone,

Last couple of times when we’ve talked about Game Development with Python or about GameDev for Android Using Python, we’ve received great responce from our and other related communities.

So now we starting our small series of articles dedicated to more practical usage of Python in GameDev.

Today we will build a very(i mean it) simple platform game using Python game framework PyGame, and in the next article, we will try to port it to Android! Please, note that author of this article is learning together with CheckiO players, other part of CiO team is dealing with waaayy more cooler stuff!

So what’s a “platform game” game exactly? According to Wiki it’s a “ideo game which involves guiding an avatar to jump between suspended platforms, over obstacles, or both to advance the game. These challenges are known as jumping puzzles or freerunning. The player controls the jumps to avoid letting the avatar fall from platforms or miss necessary jumps. ”

Classical example of platform game is Nintendo’s famous “Mario”, so we wil try to build something similar to it.

Let’s start with the basics: 

####**Installation**
You can find installation instructions on the [official PyGame page](http://www.pygame.org/download.shtml)  as well as prebuilt
 executables for whole variety of Operating Systems. 

It wasn't that hard, isn't it?

####**Getting Started**

So now we have PyGame installed, let’s start with importing it into our future project!
Simply start your favourite IDE (check out [previous article about IDE’s](http://www.checkio.org/blog/choosing-best-python-ide/) for Python) and paste this code into newly created main.py, see details in comments in the code!

Code:

    # Importing PyGame library
    import pygame
    from pygame import *
     
    #Declaring variables
    window_width = 800 #Width of game windows
    window_height = 640 # height
    screen = (window_width, window_height) #Grouping W and H into a single variable 
    bg_color = "#FFFFFF" #setting background color
     
    def main(): #main function start
        pygame.init() # PyGame initialization (all pygame projects requires this)  
        window = pygame.display.set_mode(screen) #Let’s create a window
        pygame.display.set_caption("Platform Game") # Windows title
        bg = Surface((window_width,window_height)) # Creating a visible surface to use as background 
        bg.fill(Color(bg_color)) #and fill it with bg_color color (white)    
        while True: # Main Game cycle, ‘True’ means it will run without stop forever
            for event in pygame.event.get(): # Handling quit event
                if event.type == QUIT:
                    raise SystemExit("QUIT") # raise SystemExit, "QUIT" for Py 2.7
            window.blit(bg, (0,0))      # We need to redraw screen each cycle iteration
            pygame.display.update()     # drawing everything after each iteration
     
     
    if __name__ == "__main__":
        main() #executing main function


Woah, it’s starting to get hot in here, isn’t it?

*Keep in mind:*
The game will be launched in the cycle (while True), each iteration it is necessary to redraw the background, platforms, monsters, messages, etc. It is important to note that the drawing is a sequence, for example, if the hero is drawn firtst, and then we fill the background, the character won’t be seen.

Once you will run above code, you will see a window filled with white color



####**Level construction**

Let’s draw a level on existing surface!

How we will do this? We’re choosing the easiest way, we will create a two-dimensional array of m by n. Each cell (m, n) will be a rectangle. Rectangle can contain something or may be empty. 

Let’s add some more constants:

    platform_width = 32
    platform_height = 32
    platform_color = "#000000"

And a level structure to the ’main’ function :

    map = [
           "-------------------------",
           "                        -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-                       -",
           "-------------------------"]

And to the main cycle we’re adding a level parser, to convert above drawing into playable level

    x=y=0 # coordinates
      for row in map: # whole row
          for col in row: # each symbol
              if col == "-":
                  #creating a block, filling it with color and drawing it
                  platform = Surface((platform_width,platform_height))
                  platform.fill(Color(platform_color)) 
                  screen.blit(pf,(x,y))
     
              x += platform_width #positioning blocks width
           y += platform_height    #same for height
           x = 0                   #on each row, start from 0


So what we’re doing here is we sorting out the two-dimensional level array, and if there is a symbol "-", then the coordinates `(x * platform_width, y * platform_height)`, where x, y - is the  index in the array of level.

####**Character**

Bold blocks on the background are boring. We need our character that will run and jump on the platforms we’ve just built.

So it’s time for some object oriented programming!
We will create a class for our hero! For convenience, we will keep our character as a separate file player.py

    from pygame import *
    
    move_speed = 7
    width = 22
    height = 32
    color =  "#111111"
    
    
    class Player(sprite.Sprite):
        def __init__(self, x, y):
            sprite.Sprite.__init__(self)
            self.xvel = 0    # movement speed, 0 is standing still position
            self.startX = x  # initial charecter spawn position
            self.startY = y  # same for y spawn position
            self.image = Surface((width,height))
            self.image.fill(Color(color))  # setting charecter color 
            self.rect = Rect(x, y, width, height) # rectangular charecter
    
        def update(self,  left, right):
            if left:
                self.xvel = -MOVE_SPEED  # left = x- n
     
            if right:
                self.xvel = MOVE_SPEED  # right = x + n
             
            if not(left or right): # standing still, when not walking
                self.xvel = 0
    
            self.rect.x += self.xvel # moving our position on xvel 
       
        def draw(self, screen): # drawing charecter
            screen.blit(self.image, (self.rect.x,self.rect.y))

What so interesting and what to look for in this code?

Let's start with the fact that we create a new class inheriting from another class pygame.sprite.Sprite, thereby we inherit all the characteristics of a sprite.
Sprite, according to wiki is a moving the bitmap. It has a number of useful methods and properties.

In `self.rect = Rect(x, y, width, height)` line, we are creating borders of our rectangular character. Using this rectangle we will not only move hero, but also will check(later) it on a collision with other objects. 

`update(self, left, right))` method is used to describe the behavior of the object. It overrides the parent update(* args) → None. It may be called in groups of sprites.

`draw(self, screen)` method is used to display the character on the screen. We will lated remove this method to use more convinient way to display the character.

Before defining the level, let’s add our hero and variables to move it.

    hero = Player(55,55) # creating a hero on x and y coordinates
    left = right = False    # standing still by default :)

Also, let’s add some code to move our charecter at the ‘event’ section of our code.

    if e.type == KEYDOWN and e.key == K_LEFT:
       left = True
    if e.type == KEYDOWN and e.key == K_RIGHT:
       right = True
    
    if e.type == KEYUP and e.key == K_RIGHT:
       right = False
    if e.type == KEYUP and e.key == K_LEFT:
        left = False

Everything is pretty much self explanatory in this code, if not, please, ask in the comment section

Now, it’s time to finally move and draw our charecter! According to drawing rules, you’ll need to add this after backgroud and platform drawing

    hero.update(left, right)  # movement
    hero.draw(screen)  # charecter drawing

But, if you launch your code, you’ll see that our hero moves too quickly, let’s add a restriction in the number of frames per second. To do this, after determining the level add a timer

    timer = pygame.time.Clock()

And to make it work, we will add it’s parameters to our main cycle 

    timer.tick(60)

As you may see, if you launch your code, your hero is stuck in the air, to fix this, let’s add some gravity and ability to jump! It’s kinda boring, but result is totally worth it!

To do so, let’s open our old friend player.py and add a little magic there!

What in real life makes jumps possible? Of course it’s gravity!. Now converting those values into the code,:

    jump_power = 10
    gravity = 0.35 # Force, that will drag player down

And  voi-là, we now have gravity in our game!

Now setting vertical movement speed and a check if we’re standing on the floor, cause we can jump only from the floor. All this goes to _init_ method!

    self.yvel = 0 
    self.GroundCheck = False 
    
    Now let’s add new argument to our existing method
    def update(self, left, right, up):
    if up:
    	   if self.GroundCheck: # Jump, only when on floor 
       	    self.yvel = -jump_power

Now, right before self.rect.x += self.xvel  string, add: 

    if not self.GroundCheck:
        self.yvel +=  gravity

    self.GroundCheck = False; # We don’t know when we’re on the ground
    self.rect.y += self.yvel

Now, let’s forbid our player to fly! After left = right = False line, let’s add:

    up = false

Again, this code is pretty much self explanatory.

To end flying question, let’s add some more event checks!

    if e.type == KEYDOWN and e.key == K_UP:
           up = True
    
    if e.type == KEYUP and e.key == K_UP:
           up = False

And to ‘update’ method, add argument named ‘up’

####**Final Chapter: Jumping, Movement**

How do you know that we are on the ground or other hard surface? The answer is obvious - to check if rectangle(hero) crosses with platforms!

Firstly, we will need to change how platforms are generating ;)

To make our code more readable and clear, let’s split each important part of the code to a different files, same as we did with player.py, but now, create platforms.py and move platform creation code there:

    platform_width = 32
    platform_height = 32
    platform_color = "#000000"

Then, create class, that inherits from  from pygame.sprite.Sprite

    class Platform (sprite.Sprite):
        def __init __ (self, x, y):
            sprite.Sprite .__ init __ (self)
            self.image = Surface ((platform_width, platform_height))
            self.image.fill (Color (platform_color))
            self.rect = Rect (x, y, platform_width, platform_height)

Nothing new here, i think, so let’s move on

In addition, we will need to change some parts of main file. Just right befor level array let’s add:

    entities = pygame.sprite.Group () # All objects
    platforms = [] # Platforms, that we will bounce of
    entities.add(charecter)

We will will use Sprites Group entities  to display all the elements of this group.
An array of platforms will be used to test for intersection with the platform.

Remember this tricky part?

    if col == "-":
       pf = Surface((platform_width, platform_height))
       pf.fill(Color (platform_color))
       screen.blit(pf, (x, y))


Now, we will replace it with more readable

    if col == "-":
       platform = Platform(x, y)
       entities.add(platform)
       platforms.append(platform)

What we did is we created an instance of Platform class, and added it to the ‘entities’ group of sprites and ‘platforms’ array.’entities’ part is to ease up blocks display logic, and ‘platforms’ part is to check intersection with the player.

Next, move all of the level generation code from the cycle and replace charecter display part

    charecter.draw (screen) 

with

    entities.draw (screen) # display everything


If you’ll run the code, you will see that nothing changed, becase we’re not checking for intersections with our charecter! Let’s fix it!

Getting back to player.py. We can now remove draw method, *wohoo*! But we will need new method, *boo*!, let’s name it ‘collide’

    def collide (self, xvel, yvel, platforms):
            for p in platforms:
                if sprite.collide_rect (self, p): # if there’s collision with player
    
                    if xvel> 0: # if moves right
                        self.rect.right = p.rect.left # Not move to the right
    
                    if xvel <0 # same for left
                        self.rect.left = p.rect.right # 
    
                    if yvel> 0:  # if falling down
                        self.rect.bottom = p.rect.top # do not fall down
                        self.GroundCheck  = True # if standing on something solid
                        self.yvel = 0 # falling velocity stops
    
                    if yvel <0 # if moves up
                        self.rect.top = p.rect.bottom # do not move up
                        self.yvel = 0 # jump energy disappears

In this method, we’re checking the intersection of the coordinates of the hero and platforms, if any, above described the logic activates.

Well, to make things work, we will need to call this method.
Change the number of arguments for update method once again, it now should look like this:

    update(self,left,right,up,platforms)

*Tip: Do not forget to change method call in the main file.*

And some finishing touches:

    self.rect.y += self.yvel
    self.rect.x += self.xvel 

Replace with:

    self.rect.y += self.yvel
    self.collide(0, self.yvel, platforms)
    self.rect.x += self.xvel # transfer their position on xvel
    self.collide(self.xvel, 0, platforms)

If the hero moved vertically, we check the intersection of the vertical, moved horizontally and again, checked at the intersection of the horizontal.
Let’s run our game and see what we’ve acieved!

#####***P.S***
That’s all folks, it was a tough one, but it’s your first game!

In the next part of this article, we will try to add Android support and maybe some graphics!

Write your questions and feedback in the comment section, and CheckiO team will do the best we can to help you!
