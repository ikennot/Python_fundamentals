from TaskService import TaskService


service = TaskService()
def show_tasks(list_tasks):
    count = 0;
    for x in list_tasks:
        print(count,x.description);
        count+=1;


choose = 0; 
while choose != 5:
    print('WELCOME TO TODO-LIST CLI')
    print('1. Add task')
    print('2. Update task info')
    print('3. Read all task')
    print('4. Delete task')
    print('5. Exit')
    choose = int(input('choose [1 - 5] : '))
    match choose:
        case 1:
            print('Add new task')
            taskEntry = input('Enter a new task : ')
            service.add_task(taskEntry)
        case 2:
            print('Update task info')
            list_tasks = service.get_all_task();
            show_tasks(list_tasks)

            num = int (input('Enter the number of task to be update : '));
            if num < 0 or  num >= len(list_tasks):
                print('invalid number');
            else:
                new_value = input('Update task info : ');
                service.update_task(num,new_value);
        case 3:
            print('Read all task')
            list_tasks = service.get_all_task();
            show_tasks(list_tasks);         
        case 4:
            print('Delete task');
            list_tasks = service.get_all_task();
            show_tasks(list_tasks);
            del_num = int(input('input number to delete '));
            if del_num < 0 or  del_num >= len(list_tasks):
                print('invalid tasks');
            else:
                service.delete_task(del_num);

        case 5:
            print('Exiting...')
        case _:
            print('Invalid choice')
