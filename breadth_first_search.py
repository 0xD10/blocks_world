import sys
import time
from copy import deepcopy
from collections import deque
sys.setrecursionlimit(1000000000) 

class Node:
  def __init__(self, state, parent=None, action=None):
    self.state = state
    self.parent = parent
    self.action = action

class BFS:
  def __init__(self, initial_state, goal_state):
    self.initial_state = initial_state
    self.goal_state = goal_state
  
  def compare_states(self, current_state):
    return list(filter(None, current_state))==list(filter(None, self.goal_state))
  
  def get_children(self, node, reached):               # Usefull for all the algorithms to generate the childrens
    children = list()                                  
    temp_stack = deepcopy(node.state)
    for i in range(len(node.state)):
      if temp_stack[i]:
        temp_block = temp_stack[i].pop()
        for j in range(len(temp_stack)):
          if i!=j:
            temp_stack[j].append(temp_block)
            child_state = deepcopy(temp_stack)
            if tuple(tuple(stack) for stack in list(filter(None, child_state))) not in reached:
              if len(temp_stack[j])==1:
                move_to = "table"
              else:
                move_to = str(temp_stack[j][-2])
              if len(temp_stack[i])==0:
                moved_from = "table"
              else:
                moved_from = str(temp_stack[i][-1])
              child_node = Node(child_state, parent=node, action=f"Move ({str(temp_block)}, {moved_from}, {move_to})")
              children.append(child_node)
            temp_stack[j].pop()
        temp_stack[i].append(temp_block)
    return children

def bfs(problem, start_time):
  node = Node(problem.initial_state)
  if problem.compare_states(node.state):
    return node
  len_init_state = len(node.state)                                # Optimized BFS we check with minimum empty_stacks
  len_filter_state = len(list(filter(None, node.state)))          # the init_state if there is a solution
  node.state = list(filter(None, node.state))
  for i in range((len_init_state-len_filter_state)+1):
    if i!=0:
      node.state.append([])
    problem_init_state = tuple(tuple(stack) for stack in node.state)
    reached = {problem_init_state}
    frontier = deque([node])
    while frontier:
      if int(time.time())-start_time>=60:
        TIMEOUT()
      node = frontier.popleft()
      for child in problem.get_children(node, reached):
        state = child.state
        if problem.compare_states(state):
          return child
        state = tuple(tuple(stack) for stack in list(filter(None, state)))
        if state not in reached:
          reached.add(state)
          frontier.append(child)
  return None

def reconstruct_path(node):                              # Since we have a node that saves the parent node
  path = []                                              # we simply need the final node and then extract all the previous
  while node:                                            # nodes and actions that happened
    path.append([node.state, node.action])
    node = node.parent
  return list(reversed(path))

def main(init_state, goal_state):
  problem = BFS(init_state, goal_state)
  start_time = int(time.time())
  solution = bfs(problem, start_time)
  return reconstruct_path(solution)

def TIMEOUT():
  print("Run-time 60secs limit!\nProgram terminated!\n")
  exit(-1)