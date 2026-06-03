# to do server
**a simple api server that can handle to do list via api requests**
****

## and points and their methods

### 1. /users/
**description:**

handle the recurse of users


**methods:**
- get -> return all users meta-data
- put -> add new users (replace current if exists)
- delete -> delete all users data
- post -> add new user (get the metadata)

### 2. /users/{user_id}
**description:**

handle the recurse of specific user 

**methods:**
- get -> return all the user data
- put -> replace the user save in that recurse (replace current if exists)
- delete -> delete the user in that recurse 
- post -> changing the  user data (get dict with the new data)

### 3. /users/{user_id}/tasks
**description:**

handle the recurse of the user's all tasks 

**methods:**
- get -> return all tasks
- put -> add new tasks(replace current if exists)
- delete -> delete all tasks
- post -> add new task

### 4. /users/{user_id}/tasks/{task_id}
**description:**

handle the recurse of user's specific task

**methods:**
- get -> return the task data
- put -> add new task in that id (replace current if exists)
- delete -> delete that task
- post -> change some of the task details 

