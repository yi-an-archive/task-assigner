"""
==========================================================
    Author: Yi An
    GNU General Public License v3.0
    Copyright (C) 2023 Yi An - All Rights Reserved
==========================================================
"""

import copy
import random

def main(): 
    
    residents = ['14', '15', '16', '17', '18', '19', '20', '21', \
                 '22', '23', '24', '25', '26', '27', '28', '29']
    
    tasks = ['Kitchen', 'Toilet&Shower', 'Corridor', 'Trash']
    
    num_week = 8    # create schedule for the next 8 weeks

    eligibleTasks = {} # tasks that can be assigned to each person
    
    for resident in residents: 
        # Initialisation: Everyone gets all tasks
        eligibleTasks[resident] = copy.deepcopy(tasks)
        
        # Exception cases: 
        ##   No need to do any task
        if resident in ['14']: 
            eligibleTasks[resident] = []
        ##   Kitchen only
        elif resident in ['15', '28', '29']: 
            eligibleTasks[resident] = ['Kitchen']
        ##   No trash
        elif resident in ['16']: 
            eligibleTasks[resident].remove('Trash')
        ##   No kitchen
        elif resident in ['20', '21']: 
            eligibleTasks[resident].remove('Kitchen')


if __name__ == "__main__": 
    main()