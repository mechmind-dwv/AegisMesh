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

        record_id = record.id

        db.close()

        return record_id

    def all(self):

        db = SessionLocal()

        records = db.query(AuditRecord).all()

        result = []

        for r in records:

            result.append({
                "id": r.id,
                "risk_score": r.risk_score,
                "tracked_services": r.tracked_services.split(","),
                "recommendations": r.recommendations.split(",")
            })

        db.close()

        return result
