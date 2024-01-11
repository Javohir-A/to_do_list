#Gets information from file and puts into list of dicts
def process_file(file_path):
    tasks_type = {}

    with open(file_path, 'r') as read_file:
        for line in read_file:
            parts = line.split(":")
            x_id = parts[0].strip()
            task = parts[1].strip() if len(parts) > 1 else None

            if x_id and x_id not in tasks_type:
                tasks_type[x_id] = {'tasks': []}

            if task is not None:
                tasks_type[x_id]['tasks'].append(task)

    return tasks_type


def process_task_file(file_path):
    with open(file_path,"r") as read_file:
        content = read_file.read().split('\n')
        tasks_type = []
        IDs = []
        [IDs.append((x.split(":")[0]).strip()) for x in content if (x.split(":")[0]).strip() not in IDs and x!='']
        for i, x in enumerate(IDs):
            tasks_type.append(dict())
            tasks_type[i][x] = [x.split(':')[1] for x in content if IDs[i] == (x.split(":")[0]).strip()]

    return tasks_type

def send_list_for_view(file_path, id):
    file_path1 = file_path
    content = process_file(file_path1)
    
    user_task_list = content[str(id)]['tasks']
    print(user_task_list)  
    return user_task_list

