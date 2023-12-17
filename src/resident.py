"""
==========================================================
    Author: Yi An
    GNU General Public License v3.0
    Copyright (C) 2023 Yi An - All Rights Reserved
==========================================================
"""

from person import Person

class Resident(Person): 
	def __init__(self, name, room):
		super().__init__(name)
		self.room = room # room number, an integer

	def __str__(self):
		return f"Room {self.room}: {self.name}"
	
	def getRoom(self):
		'''
		Get the person's room number. 
		
		Returns: 
		- (int): The person's room number.
		'''
		return self.room
	
	def setRoom(self, room): 
		'''
		Set the person's room number. 
		
		Parameters: 
		- room (int): The person's room number.
		'''
		self.room = room
		