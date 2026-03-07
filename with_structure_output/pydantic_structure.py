from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str
    
student = {"name":"vikas singh" , "age": 25 , "email": "vikas.singh@example.com"}

new_student = User(**student)

print(new_student)