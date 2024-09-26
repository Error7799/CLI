from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date
from . import Base

class HabitLog(Base):
    __tablename__ = 'habit_logs'
    id = Column(Integer, primary_key=True)
    date_completed = Column(Date, default=date.today)
    habit_id = Column(Integer, ForeignKey('habits.id'))
    habit = relationship('Habit', back_populates='logs')
