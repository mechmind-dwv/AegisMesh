from app.models.audit import AuditReport

class AuditEngine:

    def run(self):

        return AuditReport(
            risk_score=15,
            tracked_services=[
                "browser",
                "mobile"
            ],
            recommendations=[
                "Enable MFA",
                "Review privacy settings"
            ]
        )
