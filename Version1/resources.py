<<<<<<< HEAD
import pyglet 
pyglet.resource.path = ['../Resources']
pyglet.resource.reindex()

car_image = pyglet.resource.image("car.png")
car_image.width = 50
car_image.height = 25

def center_image(image):
	"""Sets an image's anchor point to its center"""
	image.anchor_x = image.width/2
	image.anchor_y = image.height/2

=======
import pyglet 
pyglet.resource.path = ['../Resources']
pyglet.resource.reindex()

car_image = pyglet.resource.image("car.png")
car_image.width = 50
car_image.height = 25

def center_image(image):
	"""Sets an image's anchor point to its center"""
	image.anchor_x = image.width/2
	image.anchor_y = image.height/2

>>>>>>> 0e13d0c6f304902f2074cab7ccbea29ca4280fb4
center_image(car_image)