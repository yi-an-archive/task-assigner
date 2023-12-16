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

	def getTask(self, week = None): 
		'''
		Get all tasks or the task for a specific week.

        Parameters:
        - week (int, optional): The week number, starting from 1. 
								If None, returns all tasks. 
	
		Returns: 
		- (list): A list of all tasks, if week is not provided. 
		- (str): The task for the specified week, if week is provided. 
		'''
		pass
	
	def setTask(self, week, task): 
		'''
		Set a task for a specific week. If the assigned task is not in the list of 
		eligible tasks, it returns an error message. 

        Parameters:
        - week (int): The week number, starting from 1. 
        - task (str): The name of the task.
		'''
		pass
	
	def getEligibleTasksList(self): 
		'''
		Get the list of eligible tasks. 
		
		Returns: 
		- (list): A list of the person's eligible tasks. 
		'''
		return self.eligibleTasks
	
	def setEligibleTasksList(self): 
		'''
		
		'''
		pass
	
	def __isEligible(self, task): 
		'''
		Check if the task is eligible for the person. 
		
		Returns: 
		- (bool): Whether this task is eligible for assignment. 
		'''
		return (task in self.eligibleTasks) 