class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Alert:
    def __init__(self, alert_id, message, severity='low'):
        self.alert_id = alert_id
        self.message = message
        self.severity = severity
        self.status = 'new'

class Case:
    def __init__(self, case_id, description, status='open'):
        self.case_id = case_id
        self.description = description
        self.status = status

# Additional models can be added here.
