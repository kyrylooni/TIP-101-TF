# Problem 1: Detect Circular Linked List

#U - Understand:
# What if the linked list only contains one node?
#   If the single node points to itself, the function should return True; otherwise, it should return False.
# What if the linked list is empty?
#   An empty list is not circular by definition so the function should return False.

# HAPPY CASE
# Input: A list where the last node points back to the first node (e.g., num1 -> num2 -> num3 -> num1)
# Output: True
# Explanation: The tail node points back to the head, forming a circular linked list.

# EDGE CASE
# Input: A single node that does not point to itself (e.g., num1)
# Output: False
# Explanation: The single node points to None, indicating it is not a circular linked list.

#M - Match:
# Traversing from head to tail and checking if tail points back to head. A circular linked list should not have any node pointing to None.


#P - Plan:

# 1) Start at the head.
# 2) If the list is empty, return False.
# 3) Traverse through the list. If any node points back to the head, return True.
# 4) If the end of the list is reached (i.e., current.next is None), return False.


#I - Implement:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
    if not head:
        return False  # An empty list is not circular by definition
    
    current = head
    while current.next:
        current = current.next
        if current.next == head:
            return True  # Found that tail points back to head

    return False

# num1 -> num2 -> num3 -> num1
num1 = Node(1, Node(2, Node(3, Node(1))))
print(is_circular(num1))

# var1 -> var2 -> var3
var1 = Node(1, Node(2, Node(3)))
print(is_circular(var1))
#R - Review:

      
# E- Evaluate:

# Problem 2: Find Last Node in a Linked List Cycle:

#U - Understand:

# What if the linked list has no cycle?
#   Return None as there is no last node in the cycle.

    # HAPPY CASE
    # Input: A list with a cycle (e.g., 1 -> 2 -> 3 -> 4 -> 5 -> 2)
    # Output: Node with value 5 (last node before the cycle starts again at node 2)
    # Explanation: The cycle occurs starting at node 2 and ends at node 5 which points back to node 2.

    # EDGE CASE
    # Input: A list with no cycle (e.g., 1 -> 2 -> 3 -> 4 -> 5)
    # Output: None
    # Explanation: There is no cycle in the list so there is no "last node in the cycle".


#M - Match:
    # For problems involving cycles in linked lists, the Floyd’s Cycle Detection Algorithm is typically employed to find the presence of a cycle and the starting node of the cycle.

#P - Plan:

# 1) Use two pointers (slow and fast) to detect a cycle using Floyd's algorithm.
# 2) If a cycle is detected, reset one pointer to head and find the starting node of the cycle.
# 3) Traverse the cycle to find the last node before it starts again.


#I - Implement:
def find_last_node_in_cycle(head):
    if not head or not head.next:
        return None

    slow = fast = head
    has_cycle = False

    # Phase 1: Detecting the cycle using the Floyd's Cycle Detection Algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    # If there's no cycle, return None
    if not has_cycle:
        return None

    # Phase 2: Identifying the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Find the last node in the cycle
    cycle_start = slow
    last_node = cycle_start
    while last_node.next != cycle_start:
        last_node = last_node.next

    return last_node



#R - Review:

# Trace through the code with a known cycle to confirm detection and correct identification of the last node.

      
# E- Evaluate:

# Time Complexity: O(N) where N is the number of nodes. Both detection and finding the last node require traversal but do not exceed linear time.
# Space Complexity: O(1) as the space used does not scale with the size of the input.


# Problem 3: Partition List Around Value:

#U - Understand:
# What if the linked list is empty?
#   Return None as there are no nodes to partition.

# HAPPY CASE
# Input: List = 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1, val = 5
# Output: 3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10
# Explanation: All nodes with values less than 5 come before nodes with values 5 or greater.

# EDGE CASE
# Input: List = 2 -> 1 -> 3, val = 4
# Output: 2 -> 1 -> 3
# Explanation: All node values are less than 4, so the list remains unchanged.

#M - Match:
# For partitioning problems, consider strategies such as the two-pointer technique where one pointer builds the "less than" list and another builds the "greater than or equal to" list.


#P - Plan:
# 1) Initialize two new linked list heads: one for elements less than 'val' and one for elements greater or equal.
# 2) Traverse through the original list, appending elements to the appropriate new list.
# 3) Finally, merge the two lists by connecting the tail of the 'less' list to the head of the 'greater' list.
# 4) Ensure the 'greater' list ends with a null to avoid cycles.


#I - Implement:
def partition(head, val):
    # Create two temp heads to start the less and greater lists
    less_head = Node(0)
    greater_head = Node(0)
    
    # These pointers will be used to add nodes to the less and greater lists
    less = less_head
    greater = greater_head
    
    # Traverse the original list
    current = head
    while current:
        if current.value < val:
            less.next = current
            less = less.next
        else:
            greater.next = current
            greater = greater.next
        
        current = current.next
    
    # Important: end the greater list to prevent cycles
    greater.next = None
    
    # Attach the end of the less list to the start of the greater list
    # Important: Skip the temp head
    less.next = greater_head.next
    
    return less_head.next


#R - Review:

# Test with the happy case to ensure proper partitioning.
# Test with an edge case where all elements are less than the partition value to confirm no change in list structure.

      
# E- Evaluate:

# Time Complexity: O(N) because we need to traverse the list once.
# Space Complexity: O(1) because we only use existing nodes without allocating new space except for the two temp head nodes.