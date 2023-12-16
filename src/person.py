"""
==========================================================
    Author: Yi An
    GNU General Public License v3.0
    Copyright (C) 2023 Yi An - All Rights Reserved
==========================================================
"""

class Person: 
	def __init__(self, name):
		self.name = name
		# Initialise a list of all tasks assigned to the person
		self.assignedTasks = [] 
		# Initialise a list of tasks this person can do
		self.eligibleTasks = []

	def __str__(self):
		return f"Name: {self.name}"
	
	def getName(self):
		'''
		Get the person's name. 
		
		Returns: 
		- (str): The person's name.
		'''
		return self.name
	
	def setName(self, name): 
		'''
		Set the person's name. 
		
		Parameters: 
		- name (str): The person's name.
		'''
		self.name = name

	def getAllAssignedTasks(self): 
		'''
		Get all tasks assigned to the person.
	
		Returns: 
		- (list): The list of all assigned tasks. 
		'''
		if len(self.assignedTasks) == 0: 
			return None
		else: 
			return self.assignedTasks

	def getEligibleTasksList(self): 
		'''
		Get the eligible tasks. 
		
		Returns: 
		- (list): A list of the person's eligible tasks. 
		'''
		if len(self.eligibleTasks) == 0: 
			return None
		else:
			return self.eligibleTasks
	
	def setEligibleTasksList(self, eligibleTasks): 
		'''
		Set the eligible tasks. 
		
		Parameters: 
		- eligibleTasks (list): A list of the person's eligible tasks. 
		'''
		self.eligibleTasks = eligibleTasks
	
	def __isEligible(self, task): 
		'''
		Check if the task is eligible for the person. 
		
		Returns: 
		- (bool): Whether this task is eligible for assignment. 
		'''
		return (task in self.eligibleTasks) 
	
	def getTaskForTheWeek(self, week): 
		'''
		Get the task for the specified week.

        Parameters:
        - week (int): The week number, the minimum being 1. 
	
		Returns: 
		- (str): The task for the specified week. 
		'''
		pass
	
	def setTaskForTheWeek(self, week, task): 
		'''
		Set a task for the specified week. If the assigned task is not in the list of 
		eligible tasks, it returns an error message. 

        Parameters:
        - week (int): The week number, the minimum being 1. 
        - task (str): The name of the task.
		'''
		pass