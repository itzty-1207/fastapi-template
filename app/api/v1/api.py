#!/usr/bin/python3

# from fastapi import APIRouter
# from app.api.v1.endpoints import items, users

# api_router = APIRouter()

# api_router.include_router(items.router)
# api_router.include_router(users.router)

print("Hello World!")

def is_valid_identifier(name):
  try:
    exec(f"{name} = None")
    return True
  except:
    return False

print(is_valid_identifier("2var"))

item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three

print(total)

x = 10
print(type(x))
print(isinstance(x, int))