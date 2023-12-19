"""
==========================================================
    Author: Yi An
    GNU General Public License v3.0
    Copyright (C) 2023 Yi An - All Rights Reserved
==========================================================
"""

import copy
import random

def haveEnoughPeople(people_per_task, task_counters, assigned_task = None): 
    '''
    Determines if all tasks have or a specific task has enough people. 
    
    Parameters: 
    - task_counters (dict): How many people have been assigned to each task. 
    - people_per_task (dict): Number of people needed for each task. 
    - assigned_task (str, optional): Name of a specific task. 
    
    Returns: 
    - (bool): Whether there are enough people for all tasks / a specific task. 
    '''
    # Case 1: Check for all tasks
    if (assigned_task is None): 
        for task in task_counters.keys(): 
            if task_counters[task] < people_per_task[task]: 
                return False
    # Case 2: Check for one specific task    
    elif task_counters[assigned_task] < people_per_task[assigned_task]: 
        return False

    return True

residents = ['14', '15', '16', '17', '18', '19', '20', '21', \
                '22', '23', '24', '25', '26', '27', '28', '29']
    
tasks = ['Kitchen', 'Toilet&Shower', 'Corridor', 'Trash']
    
num_week = 3    # create schedule for the next 3 weeks

eligible_tasks = {} # tasks that can be assigned to each person
    
# Add content to eligible tasks list
# key: resident, value: a list of tasks the resident can do
for resident in residents: 
    # Initialisation: Everyone gets all tasks
    eligible_tasks[resident] = copy.deepcopy(tasks)
        
    # Exception cases: 
    ##   No need to do any task
    if resident in ['14']: 
        eligible_tasks[resident] = []
    ##   Kitchen only
    elif resident in ['15', '28', '29']: 
        eligible_tasks[resident] = ['Kitchen']
    ##   No trash
    elif resident in ['16']: 
        eligible_tasks[resident].remove('Trash')
    ##   No kitchen
    elif resident in ['20', '21']: 
        eligible_tasks[resident].remove('Kitchen')

# Initialise the assignment history 
res_assign_hist = {resident: [] for resident in residents} # for residents
task_assign_hist = {task: [] for task in tasks}            # for tasks

# Initialise task counters
task_counters = {task: 0 for task in tasks}
people_per_task = {'Kitchen': 2, 'Toilet&Shower': 3, 'Corridor': 1, 'Trash': 1}

# ######## Assign tasks for the given number of weeks ########
for week in range(1, num_week + 1):
    print(f"----- Week {week} -----")
    
    # Shuffle the list of people to ensure randomness
    residents_copy = copy.deepcopy(residents)
    random.shuffle(residents_copy)

    # #### Assign tasks to residents ####
    for resident in residents_copy: 
            
        # Skip if there are no eligible tasks
        if not eligible_tasks[resident]:
            continue
        
        # Assign no task if all tasks already have enough people
        elif haveEnoughPeople(people_per_task, task_counters): 
            assigned_task = '-'
       
        else: 
            # Randomly choose a task from the eligible tasks
            assigned_task = random.choice(eligible_tasks[resident])
            
            while haveEnoughPeople(people_per_task, task_counters, assigned_task): 
                assigned_task = random.choice(eligible_tasks[resident])
            
            print(f"{resident}: {assigned_task}")
            
            # Update task counter
            task_counters[assigned_task] += 1
            
            # Update assignment history for the task
            task_assign_hist[assigned_task].append(resident)
            
        # Update assignment history for the resident
        res_assign_hist[resident].append(assigned_task)
        
    # #### End assignment in one week ####

    # Reset task counters for the next week
    task_counters = {task: 0 for task in tasks}
    print()
    
# ######## End overall assignment ########

# Print the final assignment for each resident
print("----- Final Assignment History for Each Resident -----")
for resident, tasks_assigned in res_assign_hist.items():
    print(f"Resident {resident}: {tasks_assigned}")

print()

# Print the final assignment for each task
print("----- Final Assignment History for Each Task -----")
for task, residents_assigned in task_assign_hist.items():
    print(f"{task}: {residents_assigned}")
