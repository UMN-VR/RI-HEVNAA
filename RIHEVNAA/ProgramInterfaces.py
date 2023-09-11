import os

def llm_repo_feedback(question, logger):
    # Execute 'llm_repo_feedback_V0.py' with command line arguments: --prompt=question

    # use python 3.10.12 to run script

    #prepare command to be run in terminal
    command = "python3.10 programs/llm_repo_feedback_V0.py --prompt='" + question + "'"

    #run command in terminal
    #os.system(command)
    #run and save output to logger
    logger.info(f"Running command: {command}")
    output = os.popen(command).read()
    logger.info(f"Output: {output}")
    return output