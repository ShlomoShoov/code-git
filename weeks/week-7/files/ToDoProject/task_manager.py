"""
file that manage the task list actions


"""
from pathlib import Path
import utils

TASKS_FILE_PATH = Path('tasks.txt')
DEFULT_STATUS = 'PENDING'
DEFULT_COMPLEATE_STATUS = 'complete_task'

class TaskNotFoundError(Exception):
    pass

def add_task(description:str):
    """
    adding new task to a file task
    the task contsain ->
        id : uniqe id that still not used
        status: DEFULT_STATUS
        description -> provieded as an argument

    parms:
        description: (str) the description of the task


    """

    tasks_dict = utils.load_tasks(filename=TASKS_FILE_PATH)
    task_id = utils.get_new_id(tasks_dict)
    task_status = DEFULT_STATUS
    tasks_dict[task_id] = {'id':task_id, 'status':task_status, 'desc':description}
    utils.save_tasks(filename=TASKS_FILE_PATH,
                     tasks=tasks_dict)


def complete_task(task_id:str):
    """
    change the task status and save to file to the DEFULT_COMPLEATE_STATUS

    parm:
        task_id: (str) the task id to change status for
    
    raise:
        TaskNotFoundError : in case is not found
    
    """
    tasks_dict = utils.load_tasks(filename=TASKS_FILE_PATH)
    try:
        task = tasks_dict[task_id]
    except KeyError:
        raise TaskNotFoundError
    else:
        task['status'] = DEFULT_COMPLEATE_STATUS
        utils.save_tasks(filename=TASKS_FILE_PATH,
                     tasks=tasks_dict)
        



def get_tasks()->list[dict]:
    """
    return the all tasks as list of dicts, orgenize by ids

    retutn:
        tasks: (list) a list of dicts at that format:
                {id:, status:, desc:}
    
    
    """
    tasks_dict = utils.load_tasks(filename=TASKS_FILE_PATH)
    return list (tasks_dict.values())







