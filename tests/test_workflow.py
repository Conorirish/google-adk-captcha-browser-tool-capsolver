import unittest
from captcha_workflow import CaptchaWorkflow
class TestWorkflow(unittest.TestCase):
 def test_ready(self): self.assertEqual(CaptchaWorkflow({'owned.example'}).run('https://owned.example/demo')['status'],'ready')
 def test_allowlist(self): self.assertEqual(CaptchaWorkflow({'owned.example'}).run('https://other.example/demo')['stop_reason'],'target_not_allowlisted')
 def test_budget(self): self.assertEqual(CaptchaWorkflow({'owned.example'},0).run('https://owned.example/demo')['stop_reason'],'resume_budget_exhausted')
if __name__=='__main__': unittest.main()
