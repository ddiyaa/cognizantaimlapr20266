from sqlalchemy import Column, String
class FullName:
    first_name=Column(String(50), nullable=False)
    last_name=Column(String(50), nullable=False)