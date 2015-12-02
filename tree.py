class bintree:
	def __init__ (self,rootobj):
		self.key=rootobj
		self.rightchild = None
		self.leftchild = None
	def insertleft(self,newnode):
		if self.leftchild == None:
			self.leftchild=bintree(newnode)
		else:
			t=bintree(newnode)
			t.leftchild=self.leftchild
			self.leftchild=t
	def insertright(self,newnode):
		if self.rightchild == None:
			self.rightchild = bintree(newnode)
		else:
			t=bintree(newnode)
			t.self.rightchild=self.rightchild
			self.rightchild=t
	def getrightchild(self):
		return self.rightchild
	def getleftchild(self):
		return self.leftchild
	def setrootval(self,obj):
		self.key=obj
	def getrootval(self):
		return self.key
	def __str__(self):
		return self.key

class Node:
	def __init__(self,identifier):
		self.__identifier=identifier
		self.__children=[]
	@property
	def children(self):
		return self.__children
	def addchildren(self,identifier,parent=name):
		self.__children.append(identifier)

(_ROOT, _DEPTH, _BREADTH) = range(3)

class tree:
	def __init__(self):
		self.__nodes={}
	@property
	def addnode(self,identifier,parent=None):
		node=Node(identifier)
		self(identifier)=node
		if parent is not None:
			self[parent].addnode[identifier]
		return node
	def display(self,identifier,depth=_ROOT):
		children=self[identifier].children
		if depth==_ROOT:
			print ("{0}".format(identifier))
		else:
			print "\t"*depth, "{0}".format(identifier)
		depth+=1
		for child in children:
			self.display(child,depth)
	def __getitem__(self):
		return self.__nodes[key]
