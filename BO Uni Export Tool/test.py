from collections import OrderedDict


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





class boItem:

	def __init__(self, name):
		self.name = name
		self.coreItemIdentifier = None
		self.overridableProperties = None
		self.businessName = None
		self.description = None
		self.state = None
		self.dataType = None
		self.access = None
		self.forResult = None
		self.sqlDefinition = None
		self.canBeUsedIn = None

	def setCoreItemIdentifier(self, value):
		self.coreItemIdentifier = value
	def setOverridableProperties(self, value):
		self.overridableProperties = value
	def setBusinessName(self, value):
		self.businessName = value
	def setDescription(self, value):
		self.description = value
	def setState(self, value):
		self.state = value
	def setDataType(self, value):
		self.dataType = value
	def setAccess(self, value):
		self.access = value
	def setForResult(self, value):
		self.forResult = value
	def setSqlDefinition(self, value):
		self.sqlDefinition = value
	def setCanBeUsedIn(self, value):
		self.canBeUsedIn = value

	def printAll(self):
		toPrint = [str(self.coreItemIdentifier),str(self.overridableProperties),str(self.businessName),str(self.description),str(self.state),str(self.dataType),str(self.access),str(self.forResult),str(self.sqlDefinition),str(self.canBeUsedIn)]
		print(self.name)
		print('    ' + (':'.join(toPrint)))


def countTabs(value):
	return (len(value) - len(value.lstrip())) / 4





busObj = None
#count = 0

with open('HRInfoUni.txt') as file:

	inObjLay = 0
	inDimAttr = 0
	skipNextLine = 0
	dimensionList = []

	count = 0
	for line in file:
		count=count+1

		if(skipNextLine == 1):
			# once 'Object layout' is found, skip the next (useless) line
			if(inObjLay == 1):
				skipNextLine = 0
			elif(inDimAttr == 1):
				skipNextLine = 0


		elif(skipNextLine != 1):

			if('Object layout' in line):
				inObjLay = 1
				skipNextLine = 1

			elif(inObjLay == 1 and skipNextLine != 1):
				tabs = countTabs(line)
				line = line.lstrip().rstrip('\n')

				# If there are no tabs, the Object Layout section is over
				if(tabs < 1):
					inObjLay = 0

				# If tabs is 1, the current line is the Universe name, and should be the main object folder
				elif(tabs == 1):
					busObj = boObject(line, tabs)

				if(tabs > 1):
					busObj.addObject(line, tabs)

			elif('Dimensions and Attributes' in line):
				inDimAttr = 1
				skipNextLine = 1

			elif(inDimAttr == 1 and skipNextLine != 1):
				line = line.lstrip().rstrip('\n')

				if('Dimension' in line and '-------------------------------------------------' in next(file)):
					line = line.replace('Dimension: ', '')
					newDim = boItem(line)

					li=next(file).rstrip('\n')
					if('coreItemIdentifier' in li):
						newDim.setCoreItemIdentifier(li.replace('coreItemIdentifier :','').lstrip())
						li=next(file).rstrip('\n')
					if('overridableProperties' in li):
						newDim.setOverridableProperties(li.replace('overridableProperties :','').lstrip())
						li=next(file).rstrip('\n')
					if('businessName' in li):
						newDim.setBusinessName(li.replace('businessName :','').lstrip())
						li=next(file).rstrip('\n')
					if('description' in li):
						newDim.setDescription(li.replace('description :','').lstrip())
						li=next(file).rstrip('\n')
					if(li == ''):
						li = next(file).rstrip('\n')
						if(li == ''):
							li = next(file).rstrip('\n')
					elif('state' in li):
						newDim.setState(li.replace('state :','').lstrip())
						li=next(file).rstrip('\n')
					if('dataType' in li):
						newDim.setDataType(li.replace('dataType :','').lstrip())
						li=next(file).rstrip('\n')
					if('access' in li):
						newDim.setAccess(li.replace('access :','').lstrip())
						li=next(file).rstrip('\n')
					if('forResult' in li):
						newDim.setForResult(li.replace('forResult :','').lstrip())
						li=next(file).rstrip('\n')
					if('SQL Definition' in li):
						newDim.setSqlDefinition(li.replace('SQL Definition :','').lstrip())
						li=next(file).rstrip('\n')
					if('Can be used in' in li):
						newDim.setCanBeUsedIn(li.replace('Can be used in  :','').lstrip())

#					newDim.printAll()
					dimensionList.append(newDim)

				else:
					print(str(count) + ': '+ line)

#busObj.printAll()









#
