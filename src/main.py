"""
==========================================================
    Author: Yi An
    GNU General Public License v3.0
    Copyright (C) 2023 Yi An - All Rights Reserved
==========================================================
"""

from person import Person
from resident import Resident

def main(): 
    p1 = Person("X") 
    print(p1)
    print(p1.getName())
    p1.setName("Y")
    print(p1.getName())
    
    r1 = Resident("Z", 20)
    print(r1)

if __name__ == "__main__": 
    main()