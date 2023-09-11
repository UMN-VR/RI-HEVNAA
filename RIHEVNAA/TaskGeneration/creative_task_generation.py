from RIHEVNAA.ProgramInterfaces import llm_repo_feedback

# Example JSON of Tasks

# {
#     "task_name": {
#         "task_description": "Task 1", "type": "EXECUTE.PY", "program": "llm_repo_feedback", "memory": "{"args": "--prompt \"Help me draft a new Task\""}"     


def create_task(logger, RAM, Accelerators):
        # Generate a new task
        # Add the new task to the task queue
        # Set the HCPU state to running
        prompt ="""
        Help me draft a new Task

        Here is an example of a task:
        {
            "task_name": {
                "task_description": "Task 1", "type": "EXECUTE.PY", "program": "llm_repo_feedback", "memory": "{"args": "--prompt \"Help me draft a new Task\"" }} 
        }

        Now pick a something to do at random, and then write a task for it.

        RESPOND WITH ONLY THE JSON OF THE TASK

        """

        #logger.info(f"prompt: {prompt}")

        answer = llm_repo_feedback(prompt, logger)

        return answer