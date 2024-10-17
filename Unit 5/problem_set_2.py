class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent):
		opponent.hp -= self.damage
		if opponent.hp <= 0:
			opponent.hp = 0 
			print(f'{opponent.name} fainted')
		else:
			print(f"{self.name} dealt {self.damage} damage to {opponent.name}")

# Problem 1: Battle Pokemon

# U - Understand: 
# What should occur when a Pokemon's attack reduces another Pokemon's health to zero or less?
#   The opponent's health should be set to zero and it should be indicated that they have fainted.

#P - Plan:
# 1) Define the `attack` method that accepts another `Pokemon` object as an `opponent`.
# 2) Subtract the attacking Pokemon's `damage` from the opponent's `hp`.
# 3) Check if the opponent's `hp` is 0 or less:
#    - If yes, set the `hp` to 0 and print "<opponent name> fainted".
#    - If no, print "<Pokemon name> dealt <damage> damage to <opponent name>".

#I - Implement:
pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)

# Problem 2: Convert to Linked List

# U - Understand: 
# How are elements added to a linked list?
#   Each node in a linked list points to the next node through a reference called next.

#P - Plan:
# 1) Instantiate a node with the value "Jigglypuff" and store it in `jigglypuff`.
# 2) Instantiate another node with the value "Wigglytuff" and store it in `wigglytuff`.
# 3) Set the `next` attribute of `jigglypuff` to point to `wigglytuff`, creating a link between them.

#I - Implement:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
	
	

node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next)

# Problem 3: Add First

# U - Understand: 
# What does the function return if new_node is added to an empty linked list?
# The function should return the new_node as it becomes the head of the linked list, even if the list was previously empty.

#P - Plan:
# 1) Set the `next` attribute of the `new_node` to the current `head` of the linked list.
# 2) Return `new_node`, as it is now the new head of the list.

#I - Implement:
def add_first(head, new_node):
  new_node.next = head
  return new_node 

# print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

# print(node_1.value, "->", node_1.next.value)

# Problem 4: Get Tail

# U - Understand: 
# How do we handle finding the tail in a single-node list?
    # If the list has only one node (head), that node is both the head and the tail, so we return its value.

#P - Plan:
# 1) Check if the list is empty (`head` is `None`). If it is, return `None`.
# 2) Initialize a variable `current` to `head` to start traversal.
# 3) Use a loop to navigate through the list until reaching the last node (where `current.next` is `None`).
# 4) Return the value of `current` as the value of the tail node.


#I - Implement:
def get_tail(head):
  if not head:
    return None
  current = head
  while current.next:
    current = current.next
  return current.value


# linked list: num1->num2->num3
head = num1
tail = get_tail(num1)
print(tail)


# Problem 5: Replace Node

# U - Understand: 
# What happens if the original value is not found in any node?
#   The function will traverse the entire list without making any changes, leaving the linked list unchanged


#P - Plan:
# 1) Start at the `head` of the linked list.
# 2) Traverse through the list using a loop, checking each node's value.
# 3) If a node's value matches `original`, update it to `replacement`.
# 4) Continue until all nodes have been checked (i.e., until the end of the list).


#I - Implement:

def ll_replace(head, original, replacement):
  current = head
  while current:
    if current.value == original:
      current.value = replacement
    current = current.next


num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"