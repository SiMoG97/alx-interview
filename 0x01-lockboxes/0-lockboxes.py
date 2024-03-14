#!/usr/bin/python3
"""canUnlockAll"""


def canUnlockAll(boxes):
    """checks if unlocking all boxes is possible

    Args:
        boxes (list of lists): list of locked boxes
    """
    unlocked_boxes = set([0])

    while True:
        new_unlocked_boxes = set(unlocked_boxes)

        for box in unlocked_boxes:
            for key in boxes[box]:
                if key not in new_unlocked_boxes:
                    new_unlocked_boxes.add(key)

        if len(new_unlocked_boxes) == len(unlocked_boxes):
            break

        unlocked_boxes = new_unlocked_boxes

    if len(unlocked_boxes) == len(boxes):
        return True
    else:
        return False
