from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import CollisionTraverser
from panda3d.core import CollisionHandlerPusher
from panda3d.core import CollisionSphere, CollisionNode
from panda3d.core import CollisionTube
from panda3d.core import WindowProperties
from panda3d.core import Plane, Point3

## control ralph
from panda3d.core import Vec4, Vec3

FRICTION = 150.0

class Game(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)

		#setup window size
		properties = WindowProperties()
		properties.setSize(1000,750)
		self.win.requestProperties(properties)
		self.win.setClearColor((0, 0, 1, 1))

		#setting task manger
		self.updateTask = taskMgr.add(self.update,'update') #check event and change position

		#disable mouse
		self.disableMouse()

		#load ralph model
		self.ralph = Actor('Models/ralph',
							{'run':'Models/ralph-run',
							 'walk':'Models/ralph-walk'})
		self.ralph.reparentTo(render) #Load ralph to current program
		self.ralph.setScale(0.8) #set scale
		self.ralph.setPos(0,10,0) #position (x,y,z)
		self.ralph.setH(180)

		self.cTrav = CollisionTraverser()
		self.pusher = CollisionHandlerPusher()

		colliderNode = CollisionNode("ralph")
		colliderNode.addSolid(CollisionSphere(0, 0, 0, 0.8))
		collider = self.ralph.attachNewNode(colliderNode)
		collider.show()

		base.pusher.addCollider(collider, self.ralph)
		base.cTrav.addCollider(collider, self.pusher)
		self.pusher.setHorizontal(True)

		wallSolid = CollisionTube(-4.0, 0, 0, 10, 0, 0, 1)
		wallNode = CollisionNode("wall")
		wallNode.addSolid(wallSolid)
		wall = render.attachNewNode(wallNode)
		wall.setY(8.0)

		#wall.show()

		#start animation
		#self.ralph.loop('walk')

		#setting camera
		self.camera.setP(-20)
		self.camera.setPos(self.ralph.getX(),self.ralph.getY()-20, 10)

		#load box model
		self.box = loader.loadModel('Models/box')
		self.box.setScale(0.8)
		self.box.setPos(0,7,0)
		self.box.setH(45)
		self.box.reparentTo(render)

		
		#keyboard State
		self.keyMap = {
			'up':False,
			'down':False,
			'lefe':False,
			'right':False
		}

		#Check keyboard Event
		self.accept('w',self.CheckKeyboard,['up',True])
		self.accept('w-up',self.CheckKeyboard,['up',False])
		self.accept('s',self.CheckKeyboard,['down',True])
		self.accept('s-up',self.CheckKeyboard,['down',False])
		self.accept('a',self.CheckKeyboard,['lefe',True])
		self.accept('a-up',self.CheckKeyboard,['lefe',False])
		self.accept('d',self.CheckKeyboard,['right',True])
		self.accept('d-up',self.CheckKeyboard,['right',False])

		self.count = 0

		self.isMoving = False #Stop when we run main.py

	def CheckKeyboard(self, controlName, controlState):
		self.keyMap[controlName] = controlState
		print('Key: ',controlName, 'State: ',controlState)
		print('-----')
		print(self.keyMap)

	def update(self,task):

		def Running():
			if self.isMoving == False:
				self.ralph.loop('walk')
				self.isMoving = True

		#setup clock
		dt = globalClock.getDt() #check time
		print('DT',dt)
		print('count: ',self.count)
		self.count += 1 #self.count = self.count + 1

		speed = 20 

		if self.keyMap['up'] == True:
			self.ralph.setPos(self.ralph.getPos() + Vec3(0, speed*dt, 0))
			Running()
			self.ralph.setH(180)
		if self.keyMap['down'] == True:
			self.ralph.setPos(self.ralph.getPos() + Vec3(0, -speed*dt, 0))
			Running()
			self.ralph.setH(360)	
		if self.keyMap['lefe'] == True:
			self.ralph.setPos(self.ralph.getPos() + Vec3(-speed*dt, 0, 0))
			Running()
			self.ralph.setH(-90)
			self.camera.setX(self.camera, -speed * dt)
		if self.keyMap['right'] == True:
			self.ralph.setPos(self.ralph.getPos() + Vec3(speed * dt, 0, 0))
			Running()
			self.ralph.setH(90)
			self.camera.setX(self.camera, speed * dt)

		if self.keyMap['up'] == False and self.keyMap['down'] == False and self.keyMap['lefe'] == False and self.keyMap['right'] == False:
			if self.isMoving == True:
				self.ralph.stop()
				self.ralph.pose('walk',6)
				self.isMoving = False

		#set camera follow ralph
		camvec = self.ralph.getPos() - self.camera.getPos()
		print('CAMVEC',camvec)
		camvec.setZ(0)
		camdist = camvec.length()
		camvec.normalize()
		if camdist > 10.0:
			self.camera.setPos(self.camera.getPos() + camvec * (camdist - 20))
			camdist = 10.0
		if camdist < 5.0:
			self.camera.setPos(self.camera.getPos() - camvec * (5 - camdist))
			camdist = 5.0  

		return task.cont	
game = Game()
game.run()