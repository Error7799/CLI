from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

# Import models
from .user import User
from .habit import Habit
from .habit_log import HabitLog

# Database connection
engine = create_engine('sqlite:///habit_tracker.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
