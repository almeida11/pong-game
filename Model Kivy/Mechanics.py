from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Line, Ellipse
import random

class Paddle():

    def __init__(self, velocity):
        self.velocity = velocity
        self.position = [0,0]
        self.size = [0,0]

    def setup(self, position,size):
        self.position = [position[0], position[1]-size[1]/2]
        self.size = size
        self.on_position()

    def move(self, direction):
        if(self.position[1]-self.velocity<0 and direction==-1):
            return
        elif(self.position[1]+self.size[1]+self.velocity>self.parent.size[1] and direction==1):
            return
        self.position[1] += direction*self.velocity
        self.on_position()

    def on_position(self):
        self.parent.Canvas.redraw()

class Ball():

    def __init__(self):
        self.velocity = self.get_velocity()
        self.position = [0,0]
        self.size = [0,0]

    def setup(self, position, radius):
        self.position = position
        self.radius = radius
        self.on_position()
        self.p1 = self.parent.PaddleLeft 
        self.p2 = self.parent.PaddleRight

    def move(self, time):
        paddle_hit = 0

        if((self.position[0]==self.radius+self.p1.size[0] and self.position[1]<self.p1.position[1]+self.p1.size[1] and self.position[1]>self.p1.position[1]) or (self.position[0]+self.radius==self.parent.size[0]-self.p2.size[0] and self.position[1]<self.p2.position[1]+self.p2.size[1] and self.position[1]>self.p2.position[1])):
            self.velocity[0] *= -1
            self.position[0] = self.velocity[0]+self.position[0]
            self.position[1] = self.velocity[1]+self.position[1]
            paddle_hit = 1
        elif(self.position[0]-self.radius+self.velocity[0]<self.p1.size[0] and self.position[0]>self.p1.size[0]+self.radius):
            self.position[0] = self.radius+self.p1.size[0]
            self.position[1] = self.velocity[1]+self.position[1]
            paddle_hit = 1
        elif(self.position[0]+self.velocity[0]+self.radius>self.parent.size[0]-self.p2.size[0] and self.position[0]<self.parent.size[0]-self.p2.size[0]-self.radius):
            self.position[0] = self.parent.size[0]-self.radius-self.p2.size[0]
            self.position[1] = self.velocity[1]+self.position[1]
            paddle_hit = 1

        if paddle_hit:
            self.on_position()
            return

        #horizontal movement
        if((self.position[0]-self.radius==0) or (self.position[0]+self.radius==self.parent.size[0])):
            self.velocity[0] *= -1
            self.position[0] = self.velocity[0]+self.position[0]
            if self.velocity[0]>0 :
                self.parent.score(1)
            else :
                self.parent.score(0)
            self.velocity = self.get_velocity(self.velocity)
        elif(self.position[0]-self.radius+self.velocity[0]<0):
            self.position[0] = self.radius
        elif(self.position[0]+self.velocity[0]+self.radius>self.parent.size[0]):
            self.position[0] = self.parent.size[0]-self.radius
        else:
            self.position[0] = self.velocity[0]+self.position[0]

        #general vertical movement
        if((self.position[1]-self.radius==0) or (self.position[1]+self.radius==self.parent.size[1])):
            self.velocity[1] *= -1
            self.position[1] = self.velocity[1]+self.position[1]
        elif(self.position[1]-self.radius+self.velocity[1]<0):
            self.position[1] = self.radius
        elif(self.position[1]+self.velocity[1]+self.radius>self.parent.size[1]):
            self.position[1] = self.parent.size[1]-self.radius
        else:
            self.position[1] = self.velocity[1]+self.position[1]

        self.on_position()
        return

    def on_position(self):
        self.parent.Canvas.redraw()

    def get_velocity(self, current=None):
        x = [3,3.5,4,4.5,5,5.5,6,6.5,7]
        m = [1,-1]
        if not current:
            return ([random.choice(x)*random.choice(m), random.choice(x)*random.choice(m)])
        vel = [0,0]
        if current[0]<0:
            vel[0] = random.choice(x)*-1
        else:
            vel[0] = random.choice(x)*1
        if current[1]<0:
            vel[1] = random.choice(x)*-1
        else:
            vel[1] = random.choice(x)*1
        return vel

class Canvas(Widget):
    def __init__(self, **kwargs):
        super(Canvas, self).__init__(**kwargs)

    def setup(self, size):
        self.p1 = self.parent.PaddleLeft 
        self.p2 = self.parent.PaddleRight
        self.b = self.parent.Ball
        self.sx, self.sy = size

    def redraw(self):
        with self.canvas :
            self.canvas.clear()
            Line(points = [1,1,1,self.sy-1,self.sx-1,self.sy-1, self.sx-1,1,1,1], width = 2)
            Rectangle(pos = self.p1.position , size=self.p1.size)
            Rectangle(pos = self.p2.position , size=self.p2.size)
            Ellipse(pos = [self.b.position[0]-self.b.radius, self.b.position[1]-self.b.radius], size = (2*self.b.radius, 2*self.b.radius))