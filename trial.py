from pydantic import BaseModel

class UserBase1():#input
    username:str

user = UserBase1(username=1)

print(user.username)