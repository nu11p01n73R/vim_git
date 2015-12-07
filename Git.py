
from subprocess import Popen, PIPE

class Git:
	def run_process(self, parameters = []):
		process = Popen(['git'] + parameters, stdout = PIPE)
		return process.communicate()[0]
	
	def status(self):
		print self.run_process(['status'])	

	def add(self, file_names = []):
		if file_names == []:
			file_names = ['.']
		self.run_process(['add'] + file_names)

git = Git()
#git.status()
git.add(['Git.py'])

