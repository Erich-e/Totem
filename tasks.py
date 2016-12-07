'''
Sorted storage for ToDo tasks.
'''
import os
import json
import datetime

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
		if root:
			self.size = 1
		else:
			self.size = 0

	def __iter__(self):
		return self

	def next(self):
		if not self.root.next():
			raise StopIteration
		else:
			t = self.root.data
			self.remove(t)
			return t

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

	def to_json(self):
		data = []
		cur = self.root
		while cur:
			cur_data = cur.data
			data.append(dict(title=cur_data.title, description=cur_data.description, due_date=cur_data.due_date.isoformat()))
			cur = cur.next
		return data

def read(filename=""):
	fpath = os.path.dirname(os.path.abspath(__file__)) + filename
	if not os.path.isfile(fpath):
		return task_list()
	else:
		tlist = task_list()
		with open(fpath) as f:
			data = json.load(f)
		for e in data:
			t = task(title=e["title"], description=e["description"], due_date=datetime.datetime.strptime(e["due_date"], "%Y-%m-%d").date())
			tlist.insert(t)
		return tlist

def write(filename="", tlist=None):
	if tlist:
		data = tlist.to_json()
		fpath = os.path.dirname(os.path.abspath(__file__)) + filemane
		with open(fpath, "w+") as f:
			json.dump(data, f)
