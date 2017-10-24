class boObject:
	count = 0

	def __init__(self, name, tabs):
		# Initializzes the data
		self.name = name
		self.tabs = tabs
		boObject.count = boObject.count+1

	def appendItem(self, value, tabs):
		if not self.isFolder():
			self.children = []
		self.children.append(boObject(value, tabs))


	def addObject(self, value, currTab):
		if(currTab == self.tabs + 1):
			self.appendItem(value, currTab)
#			print(':'.join([value, str(currTab)]) )

		elif(currTab > self.tabs + 1):
			if not self.isFolder():
				print('ERROR @'+str(boObject.count)+': '+ self.name+': '+value)
				return
			self.children[-1].addObject(value, currTab)


	def isFolder(self):
#		print(self.name + ' ' + str(hasattr(self, 'children')))
		return hasattr(self, 'children')

	def getLatest(self):
		return self.children[-1]

	def printAll(self):
		print (('    ' * int(self.tabs)) + self.name)
		if(self.isFolder()):
#			print('fold: '+ self.name)
			for child in self.children:
				child.printAll()





#
