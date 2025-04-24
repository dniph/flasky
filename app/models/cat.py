from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Cat(db.Model):    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)    
    name: Mapped[str]
    color: Mapped[str]
    personality: Mapped[str]




# class Cat:
#     def __init__(self, id, name, color, personality):
#         self.id = id 
#         self.name = name
#         self.color = color
#         self.personality = personality

# cats = [
#     Cat(1, "Luna", "grey", "calm"),
#     Cat(2, "Ash", "orange", "cool")
# ] 