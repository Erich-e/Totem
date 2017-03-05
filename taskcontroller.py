'''
Manager for creating and deleting tasks
'''

class Action():
	def __init__(self, type='', before={}, after={}):
		self.type = type
		self.before = before
		self.after = after

class TaskController():
	def __init__(self, tasks=None):
		self.actions = []
		self.tasks = tasks

	def insert_task(self, task=None, title='', description='', due_date=None):
		if(task):
			task_params = dict(title=task.title, description=task.description, due_date=task.due_date)
		else:
			task_params = dict(title=title, description=description, due_date=due_date)
		next_action = Action(type='insert', after=task_params)
		self.tasks.insert(**task_params)
		self.actions.append(next_action)

	def remove_task(self, task=None, title='', description='', due_date=None):
		if(task):
			task_params = dict(title=task.title, description=task.description, due_date=task.due_date)
		else:
			task_params = dict(title=title, description=description, due_date=due_date)
		next_action = Action(type='remove', before=task_params)
		self.tasks.remove(**task_params)
		self.actions.append(next_action)

	def edit(self, old_task=None, old_title='', old_desc='', old_dd=None, new_task=None, new_title=None, new_desc='', new_dd=''):
		if(old_task):
			old_params = dict(title=old_task.title, desc=old_task.description, due_date=old_task.due_date)
		else:
			old_params = dict(title=old_title, desc=old_desc, due_date=old_dd)
		if(new_task):
			new_params = dict(title=new_task.title, desc=new_task.description, due_date=new_task.due_date)
		else:
			new_params = dict(title=new_title, desc=new_desc, due_date=new_dd)
		next_action = Action(type='edit', before=old_params, after=new_params)
		self.tasks.remove(**old_params)
		self.tasks.insert(**new_params)
		self.actions.append(next_action)


	def undo(self):
		last_action = self.actions.pop()
		if(last_action.before):
			tasks.insert(**last_action.before)
		if(last_action.after):
			tasks.remove(**last_action.after)