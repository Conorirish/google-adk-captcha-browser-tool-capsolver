from urllib.parse import urlparse

class CaptchaWorkflow:
    def __init__(self, allowed_hosts, max_resume_attempts=1):
        self.allowed_hosts=set(allowed_hosts); self.max_resume_attempts=max_resume_attempts
    def run(self, url, observation='challenge_detected'):
        if urlparse(url).hostname not in self.allowed_hosts:
            return {'status':'stopped','stop_reason':'target_not_allowlisted'}
        if observation == 'challenge_detected' and self.max_resume_attempts < 1:
            return {'status':'stopped','stop_reason':'resume_budget_exhausted'}
        return {'status':'ready','result':'mock-observation','stop_reason':None}
