
prompt = ""
prompt += f"\nPlan" # all the output subplans from the classic planner.
prompt += "allocation examination"
prompt += sequence_operations # the sequential/parallel checkmark from the allocation
prompt += "initial plan examination"
prompt += decompsed_plan # the initial Precondition Identifier results


prompt += "you are robot allocation expert, Your task is, based on inital plan examination and allocation examination correct the subplans. Then based on your understanding merge the subtasks together by using timed durative actions format, where parallel tasks are performed at the same time. IMPORTANT: all 'variablelocation' should be corrected to variable itself, since variable itself includes location. and result must be in PDDL plan format."


#After combining, a mini prompt module to correct the object names so that it matches to the availiable objects in the simulator.

b_prompt += objects_ai
b_prompt += "IMPORTANT: Your TASK is based on the provided pddl plan provided in the passage below and the object list above, modify and only modify the plan so that all 'variablelocation' should be corrected to variable itself, since variable itself includes location. IMPORTANT: the only parenthesis usage should be for the correct PDDL plan, no exception."
b_prompt += plan