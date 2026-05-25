from pathlib import Path
"""
contain the utils functions.

"""


def from_line_to_dict(line:str)-> dict:
    """
    takes a str line (which represent a task) from the task file and retutn it as a dict
    take care to remove \n or spaces

    parm:
        line: (str) a line from the task file, in that format:
            id | status | desc
    return:
        task: (dict) -> {id:, status:, desc:}
    
    
    """

    task_id, status, desc = tuple(line.strip().split('|'))
    return {'id':task_id, 'status':status, 'desc':desc}



def load_tasks(filename:Path)->dict[dict]:
    """
    load a tasks from a file and retuen them in a orderd dicts of dicts.

    parms:
        filename: (Path) the task file loction, if it doesnt exists or empty return empty dict
    
    return:
        tasks: (dict) dict of the task, at that key- value format:
            id:{id:, status:, desc:}
    
    """

    tasks = {}
    if not filename.is_file() or filename.stat().st_size == 0:
        return tasks

    with open (filename, 'r') as file:
        for line in file:
            if not line:
                continue
            task = from_line_to_dict(line)
            tasks[task['id']] = task
    return tasks


def from_dict_to_line(task_dict:dict)-> str:

    """
    takes a task in dict format and return it as a line format to save it

    parm:
        task_dict: (dict) task in that format -> {id:, status:, desc:}
    return:
        task_line: (str) task in that format ->  id | status | desc


    """
    task_id = task_dict['id']
    status = task_dict['status']
    desc = task_dict ['desc']
    return f'{task_id}|{status}|{desc}\n'


def save_tasks(filename:Path, tasks:dict):
    """
    reformat the dicts of tasks into a lines and saves it into a file thet provied,
    **note**: rewrite the file if exists.

    parms:
        filename: (Path) the file loction to save
        tasks: (dict) dict of tasks present as a dict in that format:
                id : {id:, status:, desc:}
        
    """ 
    with open(filename, 'w') as file:
        for task in tasks.values():
            task_in_line_format = from_dict_to_line(task)
            file.write(task_in_line_format)

        



def get_new_id(tasks:dict)->str:
    """
    retutn the new id avalible for task. (the next id after the max id)

    parms:
        tasks: dict of dicts it that format -> id:{id:, status:, desc:}

    
    """
    if not tasks:
        return '1'
    max_id = max(tasks.keys())
    return str(int(max_id) + 1)
