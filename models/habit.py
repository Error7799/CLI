from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Habit(Base):
    __tablename__ = 'habits'
    id = Column(Integer, primary_key=True)
    habit_name = Column(String, nullable=False)
    frequency = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='habits')
    logs = relationship('HabitLog', back_populates='habit')
