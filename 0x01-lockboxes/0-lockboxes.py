#!/usr/bin/python3
"""Lockboxes"""

def canUnlockAll(boxes):
    """
        Check if all boxes can be opened
        start with the fist box, unlocked automatically
        check all keys we have 
        take the last key
        if the key has not been used to open a box
        add new key from opened box

    """
    n = len(boxes)
    unlocked = set([0])
    keys = [0]

    while keys:
        current_key = keys.pop()
        for new_key in boxes[current_key]:
            if new_key not in unlocked and new_key < n:
                unlocked.add(new_key)
                keys.append(new_key) 

    return len(unlocked) == n            
