'''
Sorted storage for ToDo tasks.
'''

class task():
	def __init__(self, title="", description="", due_date=None):
		self.title = title
		self.description = description
		self.due_date = due_date

class task_node():
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def set_next(self, node):
		self.next = node

class task_list():
	def __init__(self, root=None):
		self.root = root
		self.size = 0

	def get_size(self):
		return self.size

	def insert(self, task=None):
		self.size += 1
		if not self.root or self.root.data.date > task.date:
			self.root = task_node(data=task, next=self.root)
		else:
			cur = self.root
			while cur.next and cur.data.date <= task.date:
				cur = cur.next
			cur.next = task_node(date=task, next=cur.next)

	def remove(self, task=None):
		self.size -= 1
		if self.root == task:
			self.root = self.root.next
		cur = self.root
		while cur.next and cur.next.data != task:
			cur = cur.next
		if cur:
			cur.next = cur.next.next

	def search(self, val=None, param=None):
		cur = self.root
		while cur:
			if getattr(cur.data, param, None) == param:
				return cur.data
		return None

