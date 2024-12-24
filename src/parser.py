import re

class parser:
  def __init__(self, file_name):
    self.file = open(file_name, "r")
    self.file.readline()
    self.file.readline()
    self.objects = []
  
  def get_objects(self):
    temp_read = self.file.readline()
    while ")" not in temp_read:
      temp_read += self.file.readline()
    self.objects = re.findall(r'[A-Z]\d|[A-Z](?!\d)', temp_read)
    return self.objects
  
  def get_initial_state(self):
    temp_read = self.file.readline()
    while "HANDEMPTY" not in temp_read:
      temp_read += self.file.readline()
    result = re.findall(r'\((\w+)((?: [\w]+)*)\)', temp_read)
    stack_init = []
    for command, args in result:
      args_list = args.strip().split()
      if command=="CLEAR":
        stack_init.append(args_list)
      elif command=="ONTABLE":
        add_value = True
        for i in range(len(stack_init)):
          if args_list[0] in stack_init[i]:
            add_value = False
            break
        if(add_value):
          stack_init.append(args_list)
      elif command=="ON":
        for i in range(len(stack_init)):
          if args_list[0] in stack_init[i]:
            stack_init[i].append(args_list[1])
        if args_list[1].split() in stack_init:
          stack_init.remove(args_list[1].split())
      elif command=="HANDEMPTY":
        break
    for i in range(len(stack_init)):
      stack_init[i] = stack_init[i][::-1]
    for i in range(len(self.objects) - len(stack_init)):
      stack_init.append([])
    return stack_init
  
  def get_goal_state(self):
    temp_read = self.file.readline()
    while "))" not in temp_read:
      temp_read += self.file.readline()
    result = re.findall(r'\((\w+)((?: [\w]+)*)\)', temp_read)
    stack_goal = []
    for command, args in result:
      args_list = args.strip().split()
      if len(stack_goal) == 0:
        stack_goal.append(args_list)
      elif command=="ON":
        for i in range(len(stack_goal)):
          if args_list[0] in stack_goal[i]:
            stack_goal[i].append(args_list[1])
      else:
        break
    for i in range(len(stack_goal)):
      stack_goal[i] = stack_goal[i][::-1]
    return stack_goal

