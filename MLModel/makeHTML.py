


class treenode:
	def __init__(self,name,type_):
		self.name = name
		self.type_ = type_
		self.children = []
	def append(self,key,type_):
		self.children.append(treenode(key,type_))

class Tree:
	def __init__(self,mapping=[],key='null'):
		if mapping == []:
			self.root = treenode('!DOCTYPE',1)
		else:
			self.root = treenode('!DOCTYPE',1)
			current = self.root
			for tag in mapping[:-1]:
				current.append(tag,1)
				current = current.children[0]
			current.append(mapping[-1],2)
			current = current.children[0]
			current.append(key,0)
	def merge(self, othertree):
		current1 = self.root
		prev = self.root
		current2 = othertree.root
		while current2.type_!=0:
			if current2.name=='!DOCTYPE' and current1.name=='!DOCTYPE' and len(current1.children)==0:
				current2 = current2.children[0]
				while current2.type_!=0:
					current1.append(current2.name, current2.type_)
					current1 = current1.children[0]
					current2 = current2.children[0]
				current1.append(current2.name, current2.type_)
			elif current1.name==current2.name and current1.type_==1:
				prev = current1
				current1 = current1.children[0]
				current2 = current2.children[0]
				for each in prev.children:
					if each.name==current2.name:
						current1 = each
			else:
				current1 = prev
				while current2.type_!=0:
					current1.append(current2.name, current2.type_)
					current1 = current1.children[len(current1.children)-1]
					current2 = current2.children[0]
				current1.append(current2.name, current2.type_)
	def print__(self):
		current = self.root
		indent = ''
		self.printtree(current,indent)

	def printtree(self,current,indent):
		if current.type_!=0:
			print(indent+"<"+current.name+">")
		else:
			print(indent+current.name)
		for each in current.children:
			self.printtree(each,indent+' ')
		if current.type_!=0:
			print(indent+"</"+current.name+">")
		

class HTMLmaker:
	def __init__(self, mappings):
		self.dictionary = mappings
		self.tree = Tree()
	def createTree(self):
		for key in self.dictionary:
			temp = Tree(key[1],key[0])
			self.tree.merge(temp)
		return self.tree
	def print_(self):
		self.tree.print__()

