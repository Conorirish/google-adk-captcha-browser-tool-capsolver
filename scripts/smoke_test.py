from captcha_workflow import CaptchaWorkflow
assert CaptchaWorkflow({'owned.example'}).run('https://owned.example/demo')['status']=='ready'
print('smoke: ok')
