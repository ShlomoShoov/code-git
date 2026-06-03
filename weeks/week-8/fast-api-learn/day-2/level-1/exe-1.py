# Exercise 1 :Write a script that calls https://jsonplaceholder.typicode.com/users/1 
# and prints:
# Name: Leanne Graham
# Email: Sincere@april.biz
# City: Gwenborough

import requests 

response = requests.get('https://jsonplaceholder.typicode.com/users/1')

if response.status_code == 200:
    keys = ['name', 'email']
    data = response.json()
    for key in keys:
        print(f"{key}:{data.get(key,'unknown')}")
    print(f"city: {data.get('address',{}).get('city','unknown')}")
    

else:
    print(f'there was a problem reaching the data, status code: {response.status_code}')


# https://jsonplaceholder.typicode.com/posts 
# - print how many posts exist in total.

response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    print(f'\n\nthe count of ports is {len(response.json())} ')

else:
    print(f'there was a problem reaching the data, status code: {response.status_code}')


# https://jsonplaceholder.typicode.com/posts?userId=2
#  print the title of each post by user 2.

response = requests.get('https://jsonplaceholder.typicode.com/posts?userId=2')

if response.status_code == 200:
    posts  = response.json()
    for post in posts:
        print(post['title'])

else:
    print(f'there was a problem reaching the data, status code: {response.status_code}')


# Exercise 2 Write a function safe_get(url) that:
# - Makes a GET request to the URL
# - Returns the parsed JSON if status is 200
# - Returns None if status is 404
# - Raises an Exception with the status code for any other status

import requests 


def safe_get(url:str):
    response = requests(url=url)
    status_code  = response.status_code
    if status_code == 200:
        return response.json()
    elif status_code == 404:
        return None
    else:
        raise ValueError(f'error: status code- {status_code}')
    
    