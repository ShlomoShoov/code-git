# Exercise 4 Write a script that:
# 1. Gets all posts from jsonplaceholder (GET /posts)
# 2. Gets all users from jsonplaceholder (GET /users)
# 3. For each post, adds the author's name (match userId)
# 4. Prints a formatted list: "Post title" by Author Name


import requests
posts_url = 'https://jsonplaceholder.typicode.com/posts'
users_url = 'https://jsonplaceholder.typicode.com/users'

def get_data(url:str)->list[dict]:
    response = requests.get(url)
    if response.status_code == 200:
        print (f'get data from {url}')
        return response.json()
    else:
        print(f'error get data from {url} -> code {response.status_code}')
        return  []
    
posts = get_data(posts_url)
users = get_data(users_url)

mapped_users = {}
for post in posts:
    user_id = post["userId"]
    for user in users:
        if user["id"] == user_id:
            mapped_users[user_id] = user['name']
            break
    else:
        mapped_users[user_id] = 'unknown'

for post in posts:
    author = mapped_users.get(post['userId'], 'unknown')
    print (f"{author} :\n title: {post['title']}\n")