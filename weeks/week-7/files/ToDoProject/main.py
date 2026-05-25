"""
orginize and mange the i/u with the user as a grafic interface

"""

import task_manager

menu_options = {'1':'show your tasks'
                ,'2':'add task',
                '3': 'mark task as complate',
                '4': 'exit'}
exit_option = '4'


def show_menu():
    """
    print the menu to the user
    
    """
    display = '==========================\n'
    display +='=== To Do List Manager ===\n'
    for option_number, option_contect in menu_options.items():
        display += f'{option_number} -> {option_contect} \n'
    
    print (display)


def get_tasks_in_readable_format(tasks)-> str:
    """
    get list of tasks as dicts and return a string in that format:
        status | id | description
    
    
    """
    display = 'status | id | description \n'
    display+= '--------------------------\n'
    for task in tasks:
        status = '[✓]' + ' '*4 if task['status'] == task_manager.DEFULT_COMPLEATE_STATUS else '[ ]' + ' '*4
        task_id = task['id'] + ' ' *(4 - len(task['id'])) 
        description = task['desc']
        display += f'{status}|{task_id}|{description}\n'
    return display


def handle_show_tasks():
    """
    handle the showing all of the task to user
    """
    tasks = task_manager.get_tasks()
    if not tasks:
        print('no tasks yet :(')
        return
    
    display = get_tasks_in_readable_format(tasks)

    print(display)

    
    


def handle_add_task():
    """
    handle the prosecc of add task
    """

    desc = input('disribe your task -> ')
    task_manager.add_task(description=desc)
    print('added :)')


def handle_change_task_status():
    """
    handle the prscess of the change status

    """
    tasks = task_manager.get_tasks()
    if not tasks:
        print('no tasks yet:(')
        return
    print('pleas chooce a task and enter its id')
    print(get_tasks_in_readable_format(tasks))
    id_task = input('enter task id-> ')

    try:
        task_manager.complete_task(id_task)

    except task_manager.TaskNotFoundError:
        print(f'{id_task} -> not found')

    else:
        print('complited!')


function_option = {'1':handle_show_tasks,
                   '2':handle_add_task,
                   '3':handle_change_task_status,
                   }
def main():
    """
    mange the main menu and called the functions
    
    """
    program_running = True
    while program_running:
        show_menu()
        user_choice = input('enter your choice: ')
        if user_choice == exit_option:
            print('goodbye!')
            program_running = False
        elif user_choice in function_option:
            function_option[user_choice]()
        else:
            print(f'{user_choice} - not an option')
if __name__ == '__main__':
    main()


