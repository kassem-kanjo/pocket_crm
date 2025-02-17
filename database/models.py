from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base


# class to define the contacts I wanna save in the database
class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)  # id of the contact
    name = Column(String, index=True)  # contact's name
    phone = Column(String, index=True)  # contact's phone number
    email = Column(String, index=True, unique=True)  # contact's email address
    rating = Column(Integer)  # rating of the connection with the person
    would_refer = Column(Boolean, default=False)  # whether I think they would refer me
    communications = relationship(
        "Communication",
        back_populates="contact",
        cascade="all, delete-orphan"
    )  # conversation history with timestamps and contact methods (video call, in person)
    
