
# cleaner code:

def filter_users_by_age_and_activity(users_data:list[list[str|float]])->list:
    name_index = 0
    age_index = 1
    activiti_index = 2
    

    filterd_users_names = []

    for user_data in users_data:
        is_active = user_data[activiti_index] == 'active'
        is_adolt = user_data[age_index] >= 18

        if is_active and is_adolt:
            user_name = user_data[name_index]
            filterd_users_names.append(user_name)

    return filterd_users_names
        
    
