from app.database.database import Base
from app.database.database import engine

from app.database.audit_model import AuditRecord
from app.database.user_model import User

Base.metadata.create_all(bind=engine)

print("Database initialized")
