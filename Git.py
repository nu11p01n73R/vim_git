
from subprocess import Popen, PIPE

class Git:
	def run_process(self, parameters = []):
		process = Popen(['git'] + parameters, stdout = PIPE)
		return process.communicate()[0]
	
	def status(self):
		print self.run_process(['status'])	

git = Git()
git.status()
