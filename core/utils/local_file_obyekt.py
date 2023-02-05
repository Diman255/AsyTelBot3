import json



def local_file_obyect_save(local_user_id, local_user_obyect):
    local_user_id = str(local_user_id)
    with open('local_user.json', 'r+') as f:
        local_user = json.load(f)

    local_user[local_user_id] = local_user_obyect

    with open('local_user.json', 'w+') as f:
        json.dump(local_user, f)

    print(local_user)



def local_file_obyect_load():

    with open('local_user.json', 'r') as f:
        local_user_load = json.load(f)

    return local_user_load


