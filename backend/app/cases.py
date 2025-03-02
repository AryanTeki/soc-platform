class Case:
    def __init__(self, case_id, description, status='open'):
        self.case_id = case_id
        self.description = description
        self.status = status

    def close_case(self):
        self.status = 'closed'

    def reopen_case(self):
        self.status = 'open'

# Additional case management functions can be added here.
