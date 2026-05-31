from app.database.database import SessionLocal
from app.database.audit_model import AuditRecord

class AuditRepository:

    def save(self, report):

        db = SessionLocal()

        record = AuditRecord(
            risk_score=report.risk_score,
            tracked_services=",".join(report.tracked_services),
            recommendations=",".join(report.recommendations)
        )

        db.add(record)
        db.commit()

        db.refresh(record)

        db.close()

        return record.id
