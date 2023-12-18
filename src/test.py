"""
==========================================================
    Author: Yi An
    GNU General Public License v3.0
    Copyright (C) 2023 Yi An - All Rights Reserved
==========================================================
"""

import copy
import random

def haveEnoughPeople(people_per_task, task_counters, task = None): 
    '''
    Determines if all tasks have or a specific task has enough people. 
    
    Parameters: 
    - task_counters (dict): How many people have been assigned to each task. 
    - people_per_task (dict): Number of people needed for each task. 
    - task (str, optional): Name of a specific task. 
    '''
    if (task == None): 
        for t in task_counters.keys(): 
            if task_counters[t] < people_per_task[t]: 
                return False
    elif task_counters[task] < people_per_task[task]: 
            return False
    
    return True

residents = ['14', '15', '16', '17', '18', '19', '20', '21', \
                '22', '23', '24', '25', '26', '27', '28', '29']
    
tasks = ['Kitchen', 'Toilet&Shower', 'Corridor', 'Trash']
    
num_week = 8    # create schedule for the next 8 weeks

eligible_tasks = {'14': [], '15': ['Kitchen'], '16': ['Kitchen', 'Toilet&Shower', 'Corridor'], \
                '17': ['Kitchen', 'Toilet&Shower', 'Corridor', 'Trash'], \
                '18': ['Kitchen', 'Toilet&Shower', 'Corridor', 'Trash'], \
                '19': ['Kitchen', 'Toilet&Shower', 'Corridor', 'Trash'], \
                '20': ['Toilet&Shower', 'Corridor', 'Trash'], '21': ['Toilet&Shower', 'Corridor', 'Trash'], \
                '22': ['Kitchen', 'Toilet&Shower', 'Corridor', 'Trash'], \
                '23': ['Kitchen', 'Toilet&Shower', 'Corridor', 'Trash'], \
                '24': ['Kitchen', 'Toilet&Shower', 'Corridor', 'Trash'], \
                '25': ['Kitchen', 'Toilet&Shower', 'Corridor', 'Trash'], \
                '26': ['Kitchen', 'Toilet&Shower', 'Corridor', 'Trash'], \
                '27': ['Kitchen', 'Toilet&Shower', 'Corridor', 'Trash'], \
                '28': ['Kitchen'], '29': ['Kitchen']}

# Initialise the assignment history for residents and tasks
res_assign_hist = {resident: [] for resident in residents}
task_assign_hist = {task: [] for task in tasks}

# Initialise task counters
task_counters = {task: 0 for task in tasks}
people_per_task = {'Kitchen': 2, 'Toilet&Shower': 3, 'Corridor': 1, 'Trash': 1}

# ######## Assign tasks for the given number of weeks ########
for week in range(1, 2):
    print(f"----- Week {week} -----")
    
    # Shuffle the list of people to ensure randomness
    residents_copy = copy.deepcopy(residents)
    random.shuffle(residents_copy)

    # Assign tasks to residents
    for resident in residents_copy: 

        print(resident)
            
        # Skip if there are no eligible tasks
        if not eligible_tasks[resident]:
            print('case 1')
            continue
        
        # Assign no task if all tasks already have enough people
        elif haveEnoughPeople(people_per_task, task_counters): 
            assigned_task = '-'
            print('case 2')
       
        else: 
            print('case 3')
            # Randomly choose a task from the eligible tasks
            assigned_task = random.choice(eligible_tasks[resident])
            
            while haveEnoughPeople(people_per_task, task_counters, task = assigned_task): 
                assigned_task = random.choice(eligible_tasks[resident])
            
            print(f"{resident}: {assigned_task}")
            
            # Update task counter
            task_counters[assigned_task] += 1
            
        print(assigned_task)
        print('---------\n')
            
