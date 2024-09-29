#The template looking of prompt starts line 340, 
#lines before that are few-shot examples for filling.

# Task Description: Put an Egg in the Fridge, and place a pot containing Apple slices into the refrigerator.

# GENERAL TASK DECOMPOSITION 
# Decompose and parallel subtasks where ever possible
# Independent subtasks:
# SubTask 1: Put an Egg in the Fridge. (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject)
# SubTask 2: Prepare Apple Slices. (Skills Required: GoToObject, PickupObject, SliceObject, PutObject)
# SubTask 3: Place the Pot with Apple Slices in the Fridge. (Skills Required: GoToObject, PickupObject, PutObject, OpenObject, CloseObject)
# We can parallelize SubTask 1 and SubTask 2 because they don't depend on each other.

# action description from domain for tasks required

#Subtask 1 Put an Egg in the Fridge

# Initial condition analyze due to previous subtask:
#1. Robot not at egg location
#2. Robot not holding egg
#3. fridge is fridge, and initally closed

GoToObject: Robot goes to the egg.
Parameters: ?robot , ?egg ,
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?egg), (not (inaction ?robot))

PickupObject: Robot picks up the egg.
Parameters: ?robot , ?egg , ?location  (where egg is initially located)
Preconditions: (at-location ?egg ?location), (at ?robot ?location), (not (inaction ?robot))
Effects: (holding ?robot ?egg), (not (inaction ?robot))

GoToObject: Robot goes to the fridge.
Parameters: ?robot , ?fridge  ,
Preconditions: (not (inaction ?robot))
effects: (at ?robot ?fridge), (not (inaction ?robot))

OpenObject: Robot opens the fridge.
Parameters: ?robot , ?fridge ,
Preconditions: (not (inaction ?robot)), (at ?robot ?fridge)
Effects: (object-open ?robot ?fridge), (not (inaction ?robot))

PutObject: Robot puts the egg inside the fridge.
Parameters: ?robot  , ?egg   ?fridge   ,(location inside the fridge)
Preconditions: (holding ?robot ?egg), (at ?robot ?fridge), (not (inaction ?robot))
Effects: (at-location ?egg ?fridge), (not (holding ?robot ?egg)), (not (inaction ?robot))

CloseObject: Robot closes the fridge.
Parameters: ?robot  ?fridge 
Preconditions: (not (inaction ?robot)), (at ?robot ?fridge)
Effects: (object-close ?robot ?fridge), (not (inaction ?robot))



#Subtask 2: Prepare Apple Slices
# Initial condition analyze due to previous subtask:
#1. Robot not at apple location
#2. Robot not holding apple
#3. Robot not holding knife

GoToObject : Robot goes to the apple
Parameters: ?robot , ?Apple ,
Preconditions: (not (inaction Robot))
Effects: (at Robot Apple), (not (inaction Robot))

PickupObject (Robot, Apple, AppleLocation)
Parameters: ?robot , ?Apple , ?AppleLocation 
Preconditions: (at-location Apple AppleLocation), (at Robot AppleLocation), (not (inaction Robot))
Effects: (holding Robot Apple), (not (inaction Robot))

GoToObject (Robot, Knife)
Parameters: ?robot , ?Knife  ,
Preconditions: (not (inaction Robot))
Effects: (at Robot CuttingBoard), (not (inaction Robot))

PickupObject (Robot, Knife, KnifeLocation)
Parameters: ?robot , ?Knife , ?KnifeLocation 
Preconditions: (at-location Knife KnifeLocation), (at Robot KnifeLocation), (not (inaction Robot))
Effects: (holding Robot Knife), (not (inaction Robot))

SliceObject (Robot, Apple)
Parameters: ?robot , ?Apple,
Preconditions: (holding robot knife), (holding Robot Apple), (not (inaction Robot))
Effects: (sliced Apple), (not (inaction Robot))

GoToObject (Robot, Pot)
Parameters: ?robot , ?Pot  ,
Preconditions: (not (inaction Robot))
Effects: (at Robot Pot), (not (inaction Robot))

PutObject (Robot, AppleSlices, Pot)
Parameters: ?robot , ?AppleSlices, ?Pot
Preconditions: (holding Robot AppleSlices), (at Robot Pot), (not (inaction Robot))
Effects: (at-location AppleSlices Pot), (not (holding Robot AppleSlices)), (not (inaction Robot))


#subtask 3: Place the Pot with Apple Slices in the Fridge
# Inital condition analyze due to previous subtask:
#1. Robot at pot location
#2. Fridge is Fridge, and initally closed
#3. Robot not holding pot initally.

PickupObject (Robot, Pot, PotLocation)
Parameters: ?robot - robot, ?Apple - object ,
Preconditions: (at-location Pot PotLocation), (at Robot PotLocation), (not (inaction Robot))
Effects: (holding Robot Pot), (not (inaction Robot))

GoToObject (Robot, Fridge)
Parameters: ?robot - robot, ?Apple - object ,
Preconditions: (not (inaction Robot))
Effects: (at Robot Fridge), (not (inaction Robot))

OpenObject (Robot, Fridge)
Parameters: ?robot - robot, ?Apple - object ,
Preconditions: (not (inaction Robot)), (at Robot Fridge)
Effects: (object-open Robot Fridge), (not (inaction Robot))

PutObject (Robot, Pot, Fridge)
Parameters: ?robot - robot, ?Apple - object ,
Preconditions: (holding Robot Pot), (at Robot Fridge), (not (inaction Robot))
Effects: (at-location Pot Fridge), (not (holding Robot Pot)), (not (inaction Robot))

CloseObject (Robot, Fridge)
Parameters: ?robot - robot, ?Apple - object ,
Preconditions: (not (inaction Robot)), (at Robot Fridge)
Effects: (object-close Robot Fridge), (not (inaction Robot))

# Task Put an Egg in the Fridge, and place a pot containing Apple slices into the refrigerator is done.






# Task Description: Make a sandwich with sliced lettuce, sliced tomato, sliced bread and serve it on a washed plate.

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Slice the Lettuce, Tomato, and Bread. (Skills Required: GoToObject, PickupObject, SliceObject, PutObject)
# SubTask 2: Wash the Plate. (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff)
# SubTask 3: Assemble the Sandwich. (Skills Required: GoToObject, PickupObject, PutObject)
# We can parallelize SubTask 1 and SubTask 2 because they don't depend on each other.

# action description from domain for tasks required
#Subtask 1: Prepare Lettuce Slices

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding lettuce.
# 2. Robot not at lettuce location.

GoToObject (Robot, Knife)
Parameters: ?robot , ?Knife  ,
Preconditions: (not (inaction Robot))
Effects: (at Robot CuttingBoard), (not (inaction Robot))

PickupObject (Robot, Knife, KnifeLocation)
Parameters: ?robot , ?Knife , ?KnifeLocation 
Preconditions: (at-location Knife KnifeLocation), (at Robot KnifeLocation), (not (inaction Robot))
Effects: (holding Robot Knife), (not (inaction Robot))

GoToObject: Robot goes to the lettuce.
Parameters: ?robot, ?lettuce
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?lettuce), (not (inaction ?robot))

SliceObject: Robot slices the lettuce.
Parameters: ?robot, ?lettuce
Preconditions: (holding robot knife), (holding ?robot ?lettuce), (not (inaction ?robot))
Effects: (sliced ?lettuce), (not (inaction ?robot))

#Subtask 2: Prepare Tomato Slices

# Initial Precondition analyze due to previous subtask:
#1. Robot not holding tomate
#2. Robot not at tomate location
#3. Robot not holding knife

GoToObject (Robot, Knife)
Parameters: ?robot , ?Knife  ,
Preconditions: (not (inaction Robot))
Effects: (at Robot CuttingBoard), (not (inaction Robot))

PickupObject (Robot, Knife, KnifeLocation)
Parameters: ?robot , ?Knife , ?KnifeLocation 
Preconditions: (at-location Knife KnifeLocation), (at Robot KnifeLocation), (not (inaction Robot))
Effects: (holding Robot Knife), (not (inaction Robot))

GoToObject: Robot goes to the tomato.
Parameters: ?robot, ?tomato
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?tomato), (not (inaction ?robot))

SliceObject: Robot slices the tomato.
Parameters: ?robot, ?tomato
Preconditions: (holding robot knife), (holding ?robot ?tomato), (not (inaction ?robot))
Effects: (sliced ?tomato), (not (inaction ?robot))

#Subtask 3: Prepare Bread Slices

#1. Robot not holding bread
#2. Robot not at  bread location.


GoToObject (Robot, Knife)
Parameters: ?robot , ?Knife  ,
Preconditions: (not (inaction Robot))
Effects: (at Robot CuttingBoard), (not (inaction Robot))

PickupObject (Robot, Knife, KnifeLocation)
Parameters: ?robot , ?Knife , ?KnifeLocation 
Preconditions: (at-location Knife KnifeLocation), (at Robot KnifeLocation), (not (inaction Robot))
Effects: (holding Robot Knife), (not (inaction Robot))

GoToObject: Robot goes to the bread.
Parameters: ?robot, ?bread
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?bread), (not (inaction ?robot))

SliceObject: Robot slices the bread.
Parameters: ?robot, ?bread
Preconditions: (holding robot knife), (holding ?robot ?bread), (not (inaction ?robot))
Effects: (sliced ?bread), (not (inaction ?robot))

#Subtask 4: Wash Plate

#1. Robot not holding plate
#2. Robot not at plate location

GoToObject: Robot goes to the plate.
Parameters: ?robot, ?plate
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?plate), (not (inaction ?robot))

PickupObject: Robot picks up the plate.
Parameters: ?robot, ?plate, ?location (where plate is initially located)
Preconditions: (at-location ?plate ?location), (at ?robot ?location), (not (inaction ?robot))
Effects: (holding ?robot ?plate), (not (inaction ?robot))

GoToObject: Robot goes to the sink.
Parameters: ?robot, ?sink
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?sink), (not (inaction ?robot))

CleanObject: Robot cleans the plate.
Parameters: ?robot, ?plate
Preconditions: (at ?robot ?sink), (holding ?robot ?plate), (not (inaction ?robot))
Effects: (cleaned ?robot ?plate), (not (inaction ?robot))

#Subtask 5: Assemble Sandwich on Plate

#1. Robot not holding bread, lettuce, or tomato
#2. Robot holding plate
#3. Robot not at bread, lettuce, or tomato location

GoToObject: Robot goes to the sliced bread.
Parameters: ?robot, ?bread
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?bread), (not (inaction ?robot))

PickupObject: Robot picks up the sliced bread.
Parameters: ?robot, ?bread, ?cuttingBoard
Preconditions: (at-location ?bread ?cuttingBoard), (at ?robot ?cuttingBoard), (not (inaction ?robot))
Effects: (holding ?robot ?bread), (not (inaction ?robot))

GoToObject: Robot goes to the plate.
Parameters: ?robot, ?plate
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?plate), (not (inaction ?robot))

PutObject: Robot places the sliced bread on the plate.
Parameters: ?robot, ?bread, ?plate
Preconditions: (holding ?robot ?bread), (at ?robot ?plate), (not (inaction ?robot))
Effects: (at-location ?bread ?plate), (not (holding ?robot ?bread)), (not (inaction ?robot))

GoToObject: Robot goes to the lettuce.
Parameters: ?robot, ?lettuce
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?lettuce), (not (inaction ?robot))

PickupObject: Robot picks up the sliced lettuce.
Parameters: ?robot, ?lettuce, ?cuttingBoard
Preconditions: (at-location ?lettuce ?cuttingBoard), (at ?robot ?cuttingBoard), (not (inaction ?robot))
Effects: (holding ?robot ?lettuce), (not (inaction ?robot))

GoToObject: Robot goes to the plate.
Parameters: ?robot, ?plate
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?plate), (not (inaction ?robot))

PutObject: Robot places the sliced lettuce on the bread.
Parameters: ?robot, ?lettuce, ?plate
Preconditions: (holding ?robot ?lettuce), (at ?robot ?plate), (not (inaction ?robot))
Effects: (at-location ?lettuce ?plate), (not (holding ?robot ?lettuce)), (not (inaction ?robot))

GoToObject: Robot goes to the sliced tomato.
Parameters: ?robot, ?tomato
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?tomato), (not (inacti

PickupObject: Robot picks up the sliced tomato.
Parameters: ?robot, ?tomato, ?cuttingBoard
Preconditions: (at-location ?tomato ?cuttingBoard), (at ?robot ?cuttingBoard), (not (inaction ?robot))
Effects: (holding ?robot ?tomato), (not (inaction ?robot))

GoToObject: Robot goes to the plate.
Parameters: ?robot, ?plate
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?plate), (not (inaction ?robot))

PutObject: Robot places the sliced tomato on the lettuce.
Parameters: ?robot, ?tomato, ?plate
Preconditions: (holding ?robot ?tomato), (at ?robot ?plate), (not (inaction ?robot))
Effects: (at-location ?tomato ?plate), (not (holding ?robot ?tomato)), (not (inaction ?robot))

GoToObject: Robot goes to another sliced bread.
Parameters: ?robot, ?bread
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?bread), (not (inaction ?robot))

PickupObject: Robot picks up another sliced bread.
Parameters: ?robot, ?bread, ?cuttingBoard
Preconditions: (at-location ?bread ?cuttingBoard), (at ?robot ?cuttingBoard), (not (inaction ?robot))
Effects: (holding ?robot ?bread), (not (inaction ?robot))

GoToObject: Robot goes to the plate.
Parameters: ?robot, ?plate
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?plate), (not (inaction ?robot))

PutObject: Robot places the sliced bread on the sandwich.
Parameters: ?robot, ?bread, ?plate
Preconditions: (holding ?robot ?bread), (at ?robot ?plate), (not (inaction ?robot))
Effects: (at-location ?bread ?plate), (not (holding ?robot ?bread)), (not (inaction ?robot))

# Task Make a sandwich with sliced lettuce, sliced tomato, sliced bread and serve it on a washed plate is done.


#The actual Prompt Template:

# prepare train decompostion demonstration for ai2thor samples
    allaction_pddldomain = open(os.getcwd() + "/resources/allactionrobot.pddl","r")
    prompt = f"from pddl domain file with all possible actions: " +"\n" + allaction_pddldomain.read()
    objects_ai = f"\n\nobjects = {get_ai2_thor_objects(args.floor_plan)}"
    prompt += objects_ai
    prompt +=  decompose_prompt #the above examples
    
    prompt += "robot initaite 'as not inaction robot' (which defaults location too)\n\n" + decompose_prompt
    prompt += "# GENERAL TASK DECOMPOSITION \n Decompose and parallel subtasks where ever possible."

