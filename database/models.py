from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base
import datetime

# Class defining the contacts that I want to save in my database
class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)  # Primary key for this contact
    name = Column(String, index=True)  # The contact's name
    phone = Column(String, index=True)  # The contact's phone number
    email = Column(String, index=True, unique=True)  # The contact's email address
    would_refer = Column(Boolean, default=False)  # Indicates if I believe they would refer me

    # New fields that I've added:
    company = Column(String, nullable=True)  # The company they work for
    job_title = Column(String, nullable=True)  # Their job title/role
    linkedin_url = Column(String, nullable=True, unique=True)  # Their LinkedIn profile (unique)
    last_contacted = Column(DateTime, nullable=True)  # The last time I contacted them
    follow_up_date = Column(DateTime, nullable=True)  # When I plan to follow up with them
    notes = Column(Text, nullable=True)  # Extra details that I've recorded about the contact
    relationship_strength = Column(Integer, nullable=True)  # A 1-10 scale of how strong our connection is
    met_at = Column(String, nullable=True)  # Where I met the contact

    communications = relationship(
        "Communication",
        back_populates="contact",
        cascade="all, delete-orphan"
    )  # History of our conversations (e.g., video call, in-person)
    
# class that defines all the communications between me and the contact 
class Communication(Base):
    __tablename__ = "communications"

    id = Column(Integer, primary_key=True, index=True)  # unique id for each communication
    contact_id = Column(Integer, ForeignKey("contacts.id"))  # link to a contact
    method = Column(String, index=True)  # e.g., email, call, in-person
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)  # when the conversation happened
    notes = Column(String, nullable=True)  # extra details about the conversation

    contact = relationship("Contact", back_populates="communications")  # link back to the contact

    
