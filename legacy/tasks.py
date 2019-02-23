'''
Sorted storage for ToDo tasks.
'''
import os
import json
import datetime

class Task():
	def __init__(self, title="", description="", due_date=None):
		self.title = title
		self.description = description
		self.due_date = due_date

	def date_str(self):
		return self.due_date.strftime("%a, %b %d")

	def __eq__(self, other):
		return (self.title == other.title) and (self.description == other.description) \
			and (self.due_date == other.due_date)

	def __ne__(self, other):
		return not self.__eq__(other)

class TaskNode():
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def set_next(self, node):
		self.next = node

class TaskList():
	def __init__(self, root=None):
		self.root = root
		if root:
			self.size = 1
		else:
			self.size = 0

	def __iter__(self):
		self.iter_tmp = self.root
		self.iter_tmp_size = self.size
		return self

	def next(self):
		if not self.root:
			self.root = self.iter_tmp
			self.size = self.iter_tmp_size
			raise StopIteration
		else:
			t = self.root.data
			self.remove(t)
			return t

	def insert(self, new_task=None, title="", description="", due_date=None):
		self.size += 1
		if not new_task:
			new_task = Task(title=title, description=description, due_date=due_date)
		if not self.root or self.root.data.due_date > new_task.due_date:
			self.root = TaskNode(data=new_task, next=self.root)
		else:
			cur = self.root
			while cur.next and cur.next.data.due_date <= new_task.due_date:
				cur = cur.next
			cur.next = TaskNode(data=new_task, next=cur.next)

	def remove(self, old_task=None, title="", description="", due_date=None):
		if self.size == 0:
			return
		self.size -= 1
		if not old_task:
			old_task = Task(title=title, description=description, due_date=due_date)
		if self.root.data == old_task:
			self.root = self.root.next
		else:
			cur = self.root
			while cur.next and cur.next.data != old_task:
				cur = cur.next
			if cur:
				cur.next = cur.next.next

	def search(self, val=None, param=None):
		cur = self.root
		while cur:
			if getattr(cur.data, param, None) == param:
				return cur.data
		return None

	def access(self, index=0):
		if not self.root or index < 0:
			raise IndexError
		else:
			cur = self.root
			while index > 0:
				index -= 1
				cur = cur.next
			return cur.data

	def to_json(self):
		data = []
		cur = self.root
		while cur:
			cur_data = cur.data
			data.append(dict(title=cur_data.title, description=cur_data.description, due_date=cur_data.due_date.isoformat()))
			cur = cur.next
		return data

def t_read(filename=""):
	fpath = os.path.dirname(os.path.abspath(__file__)) + '/' + filename
	if not os.path.isfile(fpath):
		return TaskList()
	else:
		tlist = TaskList()
		with open(fpath) as f:
			try:
				data = json.load(f)
			except:
				raise
		for e in data:
			date_obj = datetime.datetime.strptime(e["due_date"], "%Y-%m-%d").date()
			t = Task(title=e["title"],
				description=e["description"],
				due_date=date_obj)
			tlist.insert(t)
		return tlist

def t_write(filename="", tlist=None):
	if tlist:
		data = tlist.to_json()
		fpath = os.path.dirname(os.path.abspath(__file__)) + '/' + filename
		with open(fpath, "w+") as f:
			json.dump(data, f)
