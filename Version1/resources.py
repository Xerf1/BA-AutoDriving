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

center_image(car_image)