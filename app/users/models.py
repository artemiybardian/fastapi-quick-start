from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = 'Users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    
    def __str__(self):
        return f'#{self.id}: {self.name}'
