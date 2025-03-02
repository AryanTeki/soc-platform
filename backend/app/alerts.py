class Alert:
    def __init__(self, alert_id, message, severity='low'):
        self.alert_id = alert_id
        self.message = message
        self.severity = severity
        self.status = 'new'

    def acknowledge(self):
        self.status = 'acknowledged'

    def resolve(self):
        self.status = 'resolved'

# Additional alert management functions can be added here.
