
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
		print '\n'.join(file_names) + '\nAdded to staging area'

	def commit(self, message):
		print self.run_process(['commit'] + ['-m', message ] )

	def pull(self, branch = None):
		parameter = ['pull']
		if branch:
			parameter = parameter + [ 'origin', branch ]

		print self.run_process(parameter);

	def push(self, branch):
		parameter = [ 'push', 'origin', branch ]
		print self.run_process(parameter)
