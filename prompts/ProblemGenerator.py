#This module includes a switch to check whether team collaboration s needed, example prompt differs slightly.
# The template starts at line 602, all lines before that are few-shot examples.



#Example 1
#Subtask examination from action perspective:
# SubTask 1: Slice the Potato

# Initial Precondition analyze due to previous subtask:
#1. Robot not at the potato
#2. Robot not holding the potato

GoToObject (Robot, Knife)
Parameters: ?robot , ?Knife  ,
Preconditions: (not (inaction Robot))
Effects: (at Robot CuttingBoard), (not (inaction Robot))

PickupObject (Robot, Knife, KnifeLocation)
Parameters: ?robot , ?Knife , ?KnifeLocation 
Preconditions: (at-location Knife KnifeLocation), (at Robot KnifeLocation), (not (inaction Robot))
Effects: (holding Robot Knife), (not (inaction Robot))

GoToObject: Robot goes to the potato.
Parameters: ?robot, ?potato
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?potato), (not (inaction ?robot))

SliceObject: Robot slices the potato.
Parameters: ?robot, ?potato
Preconditions: (holding Robot Knife), (not (inaction ?robot))
Effects: (sliced ?potato), (not (inaction ?robot))

Assigned Robots: Robot 1 and Robot 3 (as a team),
Objects Involved: Potato, Cutting Board

#Domain files content for each robot,
(define (domain robot1)
  (:requirements :strips :typing :negative-preconditions) 
  (:types robot object)
  (:predicates
    (at ?robot - robot ?object - object)
    (inaction ?robot - robot) 
    (holding ?robot - robot ?object - object)
    (at-location  ?object - object ?location - object)
    (switch-on ?robot - robot ?object - object)
    (switch-off ?robot - robot ?object - object)
    (object-open ?robot - robot ?object - object)
    (object-close ?robot - robot ?object - object)
    (break ?robot - robot ?object - object)
    (sliced ?object - object)
    (cleaned ?robot - robot ?object - object)
  )
  
  (:action GoToObject
    :parameters (?robot - robot ?object - object)
    :precondition (not (inaction ?robot))

    :effect (and 
              (at ?robot ?object)
              (forall (?another_object - object)
                (when (at ?robot ?another_object)
                  (not (at ?robot ?another_object))
                )
              )
              (not (inaction ?robot))
            )
  )

  (:action PickupObject
    :parameters (?robot - robot ?object - object ?location - object)
    :precondition (and 
                    (at-location ?object ?location)
                    (at ?robot ?location)
                    (not(inaction ?robot))
    )
    :effect (and
              (holding ?robot ?object)
              (not(inaction ?robot))
    )
  )

  (:action PutObject
    :parameters (?robot - robot ?object  - object ?location - object)
    :precondition (and 
                    (holding ?robot ?object)
                    (at ?robot ?location)
                    (not(inaction ?robot))
    )
    :effect (and
              (at-location ?object ?location)
              (not (holding ?robot ?object))
              (not(inaction ?robot))
    )
  )
  
  (:action SwitchOn
    :parameters (?robot - robot ?object - object)
    :precondition (and 
                    (not(inaction ?robot))
                    (at ?robot ?object)
    )   
    :effect (and
              (not(inaction ?robot))
              (switch-on ?robot ?object)
    ) 
  )


  (:action Switchoff
    :parameters (?robot - robot ?object - object)
    :precondition (and
                    (not(inaction ?robot))
                    (at ?robot ?object)
    )
    :effect (and
                (not(inaction ?robot))
                (switch-off ?robot ?object)
    )    
  )


  (:action OpenObject
    :parameters (?robot - robot ?object - object)
    :precondition (and
                    (not(inaction ?robot))
                    (at ?robot ?object)
    )
      
    :effect (and
                (not(inaction ?robot))
                (object-open ?robot ?object)
    )
  )


  (:action BreakObject
    :parameters (?robot - robot ?object - object)
    :precondition (and
                    (not(inaction ?robot))
                    (at ?robot ?object)
    )
    :effect (and
              (not(inaction ?robot))
              (break ?robot ?object)
    )
  )
 

  (:action CloseObject
    :parameters (?robot - robot ?object - object)
    :precondition (and
                    (not(inaction ?robot))
                    (at ?robot ?object)
    )
    :effect (and
              (not(inaction ?robot))
              (object-close ?robot ?object)
  )
  )


  (:action SliceObject
    :parameters (?robot - robot ?object - object ?location - object)
    :precondition (and 
                    (at-location ?object ?location)
                    (at ?robot ?location)
                    (not(inaction ?robot))
    )
    :effect (and
              (not(inaction ?robot))
              (sliced ?object)
    )
  )    

 (:action CleanObject
    :parameters (?robot - robot ?object - object)
    :precondition (and
                    (not(inaction ?robot))
                    (at ?robot ?object)
    )
    :effect (and
              (not(inaction ?robot))
              (cleaned ?robot ?object)
    )    
  )
)

(define (domain robot3)
  (:requirements :strips :typing :negative-preconditions) 
  (:types robot object)
  (:predicates
    (at ?robot - robot ?object - object)
    (inaction ?robot - robot) 
    (holding ?robot - robot ?object - object)
    (at-location  ?object - object ?location - object)
    (switch-on ?robot - robot ?object - object)
    (switch-off ?robot - robot ?object - object)
    (object-open ?robot - robot ?object - object)
    (object-close ?robot - robot ?object - object)
    (break ?robot - robot ?object - object)
    (sliced ?object - object)
    (cleaned ?robot - robot ?object - object)
  )
  
  (:action GoToObject
    :parameters (?robot - robot ?object - object)
    :precondition (not (inaction ?robot))

    :effect (and 
              (at ?robot ?object)
              (forall (?another_object - object)
                (when (at ?robot ?another_object)
                  (not (at ?robot ?another_object))
                )
              )
              (not (inaction ?robot))
            )
  )

  (:action PickupObject
    :parameters (?robot - robot ?object - object ?location - object)
    :precondition (and 
                    (at-location ?object ?location)
                    (at ?robot ?location)
                    (not(inaction ?robot))
    )
    :effect (and
              (holding ?robot ?object)
              (not(inaction ?robot))
    )
  )

  (:action PutObject
    :parameters (?robot - robot ?object  - object ?location - object)
    :precondition (and 
                    (holding ?robot ?object)
                    (at ?robot ?location)
                    (not(inaction ?robot))
    )
    :effect (and
              (at-location ?object ?location)
              (not (holding ?robot ?object))
              (not(inaction ?robot))
    )
  )
  
  (:action SwitchOn
    :parameters (?robot - robot ?object - object)
    :precondition (and 
                    (not(inaction ?robot))
                    (at ?robot ?object)
    )   
    :effect (and
              (not(inaction ?robot))
              (switch-on ?robot ?object)
    ) 
  )


  (:action Switchoff
    :parameters (?robot - robot ?object - object)
    :precondition (and
                    (not(inaction ?robot))
                    (at ?robot ?object)
    )
    :effect (and
                (not(inaction ?robot))
                (switch-off ?robot ?object)
    )    
  )


  (:action OpenObject
    :parameters (?robot - robot ?object - object)
    :precondition (and
                    (not(inaction ?robot))
                    (at ?robot ?object)
    )
      
    :effect (and
                (not(inaction ?robot))
                (object-open ?robot ?object)
    )
  )


  (:action BreakObject
    :parameters (?robot - robot ?object - object)
    :precondition (and
                    (not(inaction ?robot))
                    (at ?robot ?object)
    )
    :effect (and
              (not(inaction ?robot))
              (break ?robot ?object)
    )
  )
 

  (:action CloseObject
    :parameters (?robot - robot ?object - object)
    :precondition (and
                    (not(inaction ?robot))
                    (at ?robot ?object)
    )
    :effect (and
              (not(inaction ?robot))
              (object-close ?robot ?object)
  )
  )


  (:action SliceObject
    :parameters (?robot - robot ?object - object ?location - object)
    :precondition (and 
                    (at-location ?object ?location)
                    (at ?robot ?location)
                    (not(inaction ?robot))
    )
    :effect (and
              (not(inaction ?robot))
              (sliced ?object)
    )
  )    

 (:action CleanObject
    :parameters (?robot - robot ?object - object)
    :precondition (and
                    (not(inaction ?robot))
                    (at ?robot ?object)
    )
    :effect (and
              (not(inaction ?robot))
              (cleaned ?robot ?object)
    )    
  )
)

#based on the objects availiable for potential usage below."
objects = [{'name': 'SaltShaker', 'mass': 1.0}, {'name': 'SoapBottle', 'mass': 5.0}, {'name': 'Bowl', 'mass': 3.0}, {'name': 'CounterTop', 'mass': 2}, {'name': 'Drawer', 'mass': 5}, {'name': 'Vase', 'mass': 1}, {'name': 'Lettuce', 'mass': 5}, {'name': 'Plate', 'mass': 5}, {'name': 'Potato', 'mass': 2}, {'name': 'Pan', 'mass': 5}, {'name': 'Window', 'mass': 4}, {'name': 'Fridge', 'mass': 4}, {'name': 'Sink', 'mass': 5}, {'name': 'Stool', 'mass': 6}, {'name': 'DiningTable', 'mass': 6}, {'name': 'HousePlant', 'mass': 2}, {'name': 'Chair', 'mass': 6}, {'name': 'Cup', 'mass': 3}, {'name': 'Shelf', 'mass': 6}, {'name': 'StoveKnob', 'mass': 3}, {'name': 'ButterKnife', 'mass': 6}, {'name': 'Bread', 'mass': 2}, {'name': 'DishSponge', 'mass': 4}, {'name': 'Floor', 'mass': 4}, {'name': 'PepperShaker', 'mass': 2}, {'name': 'Spatula', 'mass': 2}, {'name': 'StoveBurner', 'mass': 4}, {'name': 'Statue', 'mass': 1}, {'name': 'Kettle', 'mass': 2}, {'name': 'Apple', 'mass': 4}, {'name': 'WineBottle', 'mass': 5}, {'name': 'Knife', 'mass': 6}, {'name': 'GarbageCan', 'mass': 5}, {'name': 'Microwave', 'mass': 5}, {'name': 'LightSwitch', 'mass': 6}, {'name': 'Pot', 'mass': 2}, {'name': 'Egg', 'mass': 3}, {'name': 'Mug', 'mass': 2}, {'name': 'CoffeeMachine', 'mass': 6}, {'name': 'Faucet', 'mass': 6}, {'name': 'Tomato', 'mass': 4}, {'name': 'Spoon', 'mass': 2}, {'name': 'Fork', 'mass': 4.8}, {'name': 'Toaster', 'mass': 1}, {'name': 'Book', 'mass': 6}, {'name': 'SinkBasin', 'mass': 6}, {'name': 'Cabinet', 'mass': 1}, {'name': 'ShelvingUnit', 'mass': 3}]

#Task description: Extractout the problem file. Step by step, based on the objects potential useful availiable above, the domain file precondition, actions and subtask examination. Note that the robot initate as not inaction is enough(the statement includes robot location)
#IMPORTANT, strictly follow the structure ,stop parsing after the Problem file is completed.
#To extract pit the problem file for the given domain and task of slicing a potato, we need to follow these steps:
#Let's start by defining the objects and their initial states based on the provided list and task description.
#Step 1: Identify Objects and Initial State for each robot based on their avaliable action


#Initial States:

    at-location potato counterTop
    inaction robot1
    inaction robot3
    at robot 1 starting
    at robot 3 starting
    (not holding robot 1 potato)

#Step 2: Define Goals

Goals:
    pickup knife and go to potato for robot1 that has pickup and put object action.

    sliced potato for robot3 that has sliced object

#Problem files Extraction:

pddl

(define (problem grabknifeandgotopotato_problem)
  (:domain robot1)
  (:objects
    robot1 - robot
    potato - object
    knife- object
    counterTop - object
    initiallocation -object
  )

  (:init
    (at robot1 initiallocation)
    (at-location knife counterTop)
    (at-location potato counterTop)
    (inaction robot1)
    (not(holding robot1 potato))

  )
  (:goal
    (and
      (at robot1 potato)
      (holding robot1 knife)
    )
  )
)

pddl

(define (problem slicepotatoatBoard)
  (:domain robot3)
  (:objects
    robot3 - robot
    potato - object
    startinglocation -object
  )
  (:init
    (at robot3 startinglocation)
    (at-location potato cuttingBoard)
    (not(holding robot1 potato))

  )
  (:goal
      (sliced potato)
    
  )
)


#Problem file Extraction is done
#IMPORTANT stop extracting after seeing Problem file extraction is done.

#Example 2

#Subtask Examination from Action Perspective:
#SubTask 2: Clean the CounterTop
# Initial Precondition analyze due to previous subtask:

#Robot not at the CounterTop.
#Robot not holding a cleaning tool (e.g., DishSponge).

GoToObject: Robot goes to the CounterTop.
Parameters: ?robot - robot, ?counterTop - object
Preconditions: (not (inaction ?robot))
Effects: (at ?robot ?counterTop), (not (inaction ?robot))

PickupObject: Robot picks up the DishSponge.
Parameters: ?robot, ?dishSponge, ?location (where DishSponge is initially located)
Preconditions: (at-location ?dishSponge ?location), (at ?robot ?location), (not (inaction ?robot))
Effects: (holding ?robot ?dishSponge), (not (inaction ?robot))

CleanObject: Robot cleans the CounterTop.
Parameters: ?robot, ?dishSponge, ?counterTop
Preconditions: (at ?robot ?counterTop), (holding ?robot ?dishSponge), (not (inaction ?robot))
Effects: (cleaned ?robot ?counterTop), (not (inaction ?robot))

Assigned Robots: Robot 2 and Robot 4 (as a team)
Objects Involved: CounterTop, DishSponge

#Domain Files Content for Each Robot:
(define (domain robot2)
  (:requirements :strips :typing :negative-preconditions) 
  (:types robot object)
  (:predicates
    (at ?robot - robot ?object - object)
    (inaction ?robot - robot) 
    (holding ?robot - robot ?object - object)
    (at-location ?object - object ?location - object)
    (cleaned ?robot - robot ?object - object)
  )
  
  (:action GoToObject
    :parameters (?robot - robot ?object - object)
    :precondition (not (inaction ?robot))
    :effect (and 
              (at ?robot ?object)
              (forall (?another_object - object)
                (when (at ?robot ?another_object)
                  (not (at ?robot ?another_object))
                )
              )
              (not (inaction ?robot))
            )
  )

  (:action PickupObject
    :parameters (?robot - robot ?object - object ?location - object)
    :precondition (and 
                    (at-location ?object ?location)
                    (at ?robot ?location)
                    (not (inaction ?robot))
    )
    :effect (and
              (holding ?robot ?object)
              (not (inaction ?robot))
    )
  )

  (:action CleanObject
    :parameters (?robot - robot ?object - object)
    :precondition (and
                    (at ?robot ?object)
                    (holding ?robot ?object)
                    (not (inaction ?robot))
    )
    :effect (and
              (cleaned ?robot ?object)
              (not (inaction ?robot))
    )    
  )
)

(define (domain robot4)
  (:requirements :strips :typing :negative-preconditions) 
  (:types robot object)
  (:predicates
    (at ?robot - robot ?object - object)
    (inaction ?robot - robot) 
    (holding ?robot - robot ?object - object)
    (at-location ?object - object ?location - object)
    (cleaned ?robot - robot ?object - object)
  )
  
  (:action GoToObject
    :parameters (?robot - robot ?object - object)
    :precondition (not (inaction ?robot))
    :effect (and 
              (at ?robot ?object)
              (forall (?another_object - object)
                (when (at ?robot ?another_object)
                  (not (at ?robot ?another_object))
                )
              )
              (not (inaction ?robot))
            )
  )

  (:action PickupObject
    :parameters (?robot - robot ?object - object ?location - object)
    :precondition (and 
                    (at-location ?object ?location)
                    (at ?robot ?location)
                    (not (inaction ?robot))
    )
    :effect (and
              (holding ?robot ?object)
              (not (inaction ?robot))
    )
  )

  (:action CleanObject
    :parameters (?robot - robot ?object - object)
    :precondition (and
                    (at ?robot ?object)
                    (holding ?robot ?object)
                    (not (inaction ?robot))
    )
    :effect (and
              (cleaned ?robot ?object)
              (not (inaction ?robot))
    )    
  )
)

#Problem File Extraction:
(define (problem cleancountertop_problem)
  (:domain robot2)
  (:objects
    robot2 - robot
    dishSponge - object
    counterTop - object
    storageArea - object
  )
  (:init
    (at robot2 storageArea)
    (at-location dishSponge storageArea)
    (inaction robot2)
    (not(holding robot2 dishSponge))
  )
  (:goal
    (and
      (cleaned robot2 counterTop)
      (not (holding robot2 dishSponge))
    )
  )
)

(define (problem cleancountertop_problem)
  (:domain robot4)
  (:objects
    robot4 - robot
    dishSponge - object
    counterTop - object
    storageArea - object
  )
  (:init
    (at robot4 storageArea)
    (at-location dishSponge storageArea)
    (inaction robot4)
    (not(holding robot4 dishSponge))
  )
  (:goal
    (and
      (cleaned robot4 counterTop)
      (not (holding robot4 dishSponge))
    )
  )
)


#Problem file Extraction is done
#IMPORTANT stop extracting after seeing Problem file extracttion is done.

#The Prompt Template:
prompt += problem_examplecontent #The above few-shot example content, slightly differ for single robots.
prompt = "Strictly follow the structure and finish the tasks like example"
prompt += "\nSubtask examination from action perspective:"
prompt += subtask #The summary of Precondition Identifier +Allocation, looks similiar to line 7-35.
prompt +="\nDomain file content:"
prompt += domain_content #the corresponding assigned robot number is the name of domain, each robot has its individual domain.
prompt +="\n based on the objects availiable below."
prompt += objects_ai #the objects availiable in the environment.
prompt += "Task description: extract out the problem files, based on the above objects , the precondition, actions and subtask examination."
prompt += "#IMPORTANT, strictly follow the structure ,stop generate after the Problem file generation is done."