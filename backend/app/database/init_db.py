from app.database.database import engine
from app.database.audit_model import AuditRecord

AuditRecord.metadata.create_all(bind=engine)

print("Database initialized")
