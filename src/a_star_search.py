import time
import heapq
from copy import deepcopy

class Node:
  def __init__(self, state, parent=None, action=None, g=0, f=0, misplaced_cost=0):  # constructor for astar
    self.state = state
    self.parent = parent
    self.action = action
    self.g = g
    self.f = f
    self.misplaced_cost = misplaced_cost

  def __lt__(self, other):                
    return self.f < other.f

class A_star:
  def __init__(self, init_state, goal_state):
    self.init_state = init_state
    self.goal_state = goal_state
  
  def compare_states(self, current_state):                                             # This function check if two states are equal
    return list(filter(None, current_state))==list(filter(None, self.goal_state))      # p.e. [[],[],[],['A','B','C']] will be equal to [['A','B','C']]
  
  def calculate_f(self, node):
    node.f = node.misplaced_cost + node.g

  def calculate_misplaced(self, node):                                     # This function is the huristic used for astar and best
    filter_node = list(filter(None, node.state))                           # Checks for misplaced blocks and 
    for i, stack in enumerate(filter_node):                                # prefers a node that has more stacks with length<=1
      for j, block in enumerate(stack):                                    # Also if we find a correctly placed block
        if block != self.goal_state[0][j]:                                 # we check the blocks underneath the correct block
          node.misplaced_cost += 1 + (len(stack) - j)                      # to verify that the are also correctly placed
        else:
          for z in range(j-1, -1, -1):
            if self.goal_state[0][z]!=stack[z]: 
              node.misplaced_cost+=j-z
        if len(stack)>1:
          node.misplaced_cost+=1
  
  def generate_children(self, node, visited):                           # This function is used in all the algorithms
    children = list()                               
    temp_stack = deepcopy(node.state)
    for i in range(len(node.state)):
      if temp_stack[i]:
        temp_block = temp_stack[i].pop()
        for j in range(len(temp_stack)):
          if i!=j:
            temp_stack[j].append(temp_block)
            child_state = temp_stack
            if tuple(tuple(stack) for stack in list(filter(None, child_state))) not in visited:
              if len(temp_stack[j])==1:
                move_to = "table"
              else:
                move_to = str(temp_stack[j][-2])
              if len(temp_stack[i])==0:
                moved_from = "table"
              else:
                moved_from = str(temp_stack[i][-1])
              child_node = Node(deepcopy(child_state), parent=node, action=f"Move ({str(temp_block)}, {moved_from}, {move_to})", g=node.g+1, f=0, misplaced_cost=0)
              self.calculate_misplaced(child_node)
              self.calculate_f(child_node)
              children.append(child_node)
            temp_stack[j].pop()
        temp_stack[i].append(temp_block)
    return children

def a_star(problem, visited, start_time):
  if visited==None:
    visited = set()

  node = Node(problem.init_state)
  open_list=[]
  heapq.heappush(open_list, (0, node))
  while len(open_list)>0:
    if (int(time.time())-start_time>60):
      TIMEOUT()
    p = heapq.heappop(open_list)
    state_key = tuple(tuple(stack) for stack in list(filter(None, p[1].state)))
    if state_key not in visited:
      visited.add(state_key)
    if problem.compare_states(p[1].state):
      return p[1]
    children = problem.generate_children(p[1], visited)
    for node in children:
      if problem.compare_states(node.state):
        return node
      state_key = tuple(tuple(stack) for stack in list(filter(None, node.state)))
      if state_key not in visited:
        visited.add(state_key)
        heapq.heappush(open_list, (node.f, node))

def reconstruct_path(node):
  path = []
  while node:
    path.append([node.state, node.action])
    node = node.parent
  return list(reversed(path))    


def main(init_state, goal_state):
  problem = A_star(init_state, goal_state)
  start_time = int(time.time())
  solution_path = reconstruct_path(a_star(problem, None, start_time))
  return solution_path

def TIMEOUT():
  print("Run-time 60secs limit!\nProgram terminated!\n")
  exit(-1)