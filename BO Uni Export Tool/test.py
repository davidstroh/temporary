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
		self.listOfValues = None
		self.canBeUsedIn = None

		self.previousAttr = None


	def setPrevAttr(self, prev):
		self.previousAttr = prev
	def getPrevAttr(self):
		return self.previousAttr

	def setAttr(self, type, value):
		value = value.replace(type + ' :','').lstrip()

		if('coreItemIdentifier' in type):
			self.coreItemIdentifier = value if value else 'Empty'
			self.previousAttr = 'coreItemIdentifier'
		elif('overridableProperties' in type):
			self.overridableProperties = value if value else self.overridableProperties
			self.previousAttr = 'overridableProperties'
		elif('businessName' in type):
			self.businessName = value if value else self.businessName
			self.previousAttr = 'businessName'
		elif('description' in type):
			self.description = value if value else ''
			self.previousAttr = 'description'
		elif('state' in type):
			self.state = value if value else self.state
			self.previousAttr = 'state'
		elif('dataType' in type):
			self.dataType = value if value else self.dataType
			self.previousAttr = 'dataType'
		elif('access' in type):
			self.access = value if value else self.access
			self.previousAttr = 'access'
		elif('forResult' in type):
			self.forResult = value if value else self.forResult
			self.previousAttr = 'forResult'
		elif('SQL Definition' in type):
			self.sqlDefinition = value if value else self.sqlDefinition
			self.previousAttr = 'SQL Definition'
		elif('Can be used in' in type):
			self.canBeUsedIn = value if value else self.canBeUsedIn
			self.previousAttr = 'Can be used in'

		self.previousAttr = type


	def getCoreItemIdentifier(self):
		return self.coreItemIdentifier
	def getOverridableProperties(self):
		return self.overridableProperties
	def getState(self):
		return self.state


	def appendAttribute(self, type, value):
		if('coreItemIdentifier' in type):
			self.coreItemIdentifier += value
		elif('overridableProperties' in type):
			self.overridableProperties += value
		elif('businessName' in type):
			self.businessName += value
		elif('description' in type):
			self.description += value
		elif('state' in type):
			self.state += value
		elif('dataType' in type):
			self.dataType += value
		elif('access' in type):
			self.access += value
		elif('forResult' in type):
			self.forResult += value
		elif('SQL Definition' in type):
			self.sqlDefinition  += value
		elif('Can be used in' in type):
			self.canBeUsedIn += value


	def printAll(self):
		toPrint = [str(self.coreItemIdentifier),str(self.overridableProperties),str(self.businessName),str(self.description),str(self.state),str(self.dataType),str(self.access),str(self.forResult),str(self.sqlDefinition),str(self.canBeUsedIn)]
		print(self.name)
		print('    ' + (':'.join(toPrint)))

















def countTabs(value):
	return (len(value) - len(value.lstrip())) / 4







busObj = None
#count = 0

with open('HRInfoUni.txt') as file:

	inObjLayGroup = 0 # indicates whether current parsed line is within the Object Layout Section
	inDimAttrGroup = 0 # indicates whether current parsed line is within the Dimensions and Attributes Section
	inIndiDimGroup = 0 # indicates whether current parsed line is within an individual dimension grouping
	isBlankLine = 0 # indicates whether the parsed line is blank to be used in the next iteration
	prevLine = None
	skipNextLine = 0
	dimensionList = []

	errorCount = 0
	count = 0
	for line in file:
		count=count+1

		if(skipNextLine == 1):
			# once 'Object layout' is found, skip the next (useless) line
			if(inObjLayGroup == 1):
				skipNextLine = 0
			elif(inDimAttrGroup == 1):
				skipNextLine = 0


		elif(skipNextLine != 1):

			if('Object layout' in line):
				inObjLayGroup = 1
				skipNextLine = 1

			elif(inObjLayGroup == 1 and skipNextLine != 1):
				tabs = countTabs(line)
				line = line.lstrip().rstrip('\n')

				# If there are no tabs, the Object Layout section is over
				if(tabs < 1):
					inObjLayGroup = 0

				# If tabs is 1, the current line is the Universe name, and should be the main object folder
				elif(tabs == 1):
					busObj = boObject(line, tabs)

				if(tabs > 1):
					busObj.addObject(line, tabs)


			elif('Dimensions and Attributes' in line):
				inDimAttrGroup = 1
				skipNextLine = 1

			elif(inDimAttrGroup == 1 and skipNextLine != 1):
				tabs = countTabs(line)
				line = line.lstrip().rstrip('\n')

				count=count+1
				if(inIndiDimGroup == 0 and 'Dimension' in line and '-------------------------------------------------' in next(file)):
					inIndiDimGroup = 1
					line = line.replace('Dimension: ', '')
					newDim = boItem(line)
					prevLine = next(file).lstrip().rstrip('\n')
					count = count+1

				elif(inIndiDimGroup == 1):

					if('coreItemIdentifier' in line):
						newDim.setAttr('coreItemIdentifier', line)
					elif('overridableProperties' in line):
						newDim.setAttr('overridableProperties', line)
					elif('businessName' in line):
						newDim.setAttr('businessName', line)
					elif('description' in line):
						newDim.setAttr('description', line)
					elif('state' in line):
						newDim.setAttr('state', line)
					elif('dataType' in line):
						newDim.setAttr('dataType', line)
					elif('access' in line):
						newDim.setAttr('access', line)
					elif('forResult' in line):
						newDim.setAttr('forResult', line)
					elif('SQL Definition' in line):
						newDim.setAttr('SQL Definition', line)
					elif('List of Values' in line):
						newDim.setAttr('List of Values', line)
					elif('Can be used in' in line):
						newDim.setAttr('Can be used in', line)

					elif(line and not tabs):
						#print('RIGHT HERE MOTHERFUCKER')
						newDim.appendAttribute(newDim.getPrevAttr(), line)

					elif not line:
						inIndiDimGroup = 0
						dimensionList.append(newDim)
					else:
						print(line)




#busObj.printAll()
print(len(dimensionList))








#
