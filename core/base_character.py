from stats import Stats
from equipment import Equipment
from inventory import Inventory


class BaseCharacter():
	def __init__(self, position, name="Unnamed", inventory=Inventory(), equipment=Equipment(), stats=Stats()):
		self.stats = stats
		self.name = name
		self.position = position
		self.inventory = inventory
		self.equipment = equipment
		
	def move_to(self, position):
		self.position = position
		
	def move(self, delta_position):
		self.position += delta_position
		
	def get_stats(self):
		return self.equipment.sum_stats()
		
	def __str__(self):
		return "[%s] (%s) %s <%s>" % (type(self),
								self.name,
								str(self.stats),
								str(self.position))