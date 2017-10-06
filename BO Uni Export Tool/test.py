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
		self.description = 'Empty'
		self.state = None
		self.dataType = None
		self.access = None
		self.forResult = None
		self.sqlDefinition = None
		self.canBeUsedIn = None

	def setCoreItemIdentifier(self, value):
		self.coreItemIdentifier = value if value else 'Empty'
	def getCoreItemIdentifier(self):
		return self.coreItemIdentifier
	def setOverridableProperties(self, value):
		self.overridableProperties = value if value else self.overridableProperties
	def setBusinessName(self, value):
		self.businessName = value if value else self.businessName
	def setDescription(self, value):
		self.description = value if value else self.description
	def setState(self, value):
		self.state = value if value else self.state
	def getState(self):
		return self.state
	def setDataType(self, value):
		self.dataType = value if value else self.dataType
	def setAccess(self, value):
		self.access = value if value else self.access
	def setForResult(self, value):
		self.forResult = value if value else self.forResult
	def setSqlDefinition(self, value):
		self.sqlDefinition = value if value else self.sqlDefinition
	def setCanBeUsedIn(self, value):
		self.canBeUsedIn = value if value else self.canBeUsedIn

	def printAll(self):
		toPrint = [str(self.coreItemIdentifier),str(self.overridableProperties),str(self.businessName),str(self.description),str(self.state),str(self.dataType),str(self.access),str(self.forResult),str(self.sqlDefinition),str(self.canBeUsedIn)]
		print(self.name)
		print('    ' + (':'.join(toPrint)))

	def getMissingData(self):
		#return "here "+ self.name +' : '+ str(self.coreItemIdentifier) if self.coreItemIdentifier else "heree "+ self.name
		#return (self.coreItemIdentifier if self.coreItemIdentifier else (self.overridableProperties if self.overridableProperties else (self.businessName if self.businessName else (self.description if self.description else (self.state if self.state else (self.dataType if self.dataType else (self.access if self.access else (self.forResult if self.forResult else (self.sqlDefinition if self.sqlDefinition else self.canBeUsedIn if self.canBeUsedIn else ("here "+ self.name))))))))))
		return (("here coreItemIdentifier- "+ self.coreItemIdentifier +'~'+ self.name) if not self.coreItemIdentifier else (("here overridableProperties- "+ self.overridableProperties +'~'+self.name) if not self.overridableProperties else (("here businessName- "+ self.businessName +'~'+self.name) if not self.businessName else (("here description- "+ str(self.description) +'~'+self.name) if not self.description else (("here state- "+ str(self.state) +'~'+self.name) if not self.state else (("here dataType- "+ str(self.dataType) +'~'+self.name) if not self.dataType else (("here access- "+ str(self.access) +'~'+self.name) if not self.access else (("here forResult- "+ str(self.forResult) +'~'+self.name) if not self.forResult else (("here sqlDefinition- "+ str(self.sqlDefinition) +'~'+self.name) if not self.sqlDefinition else (("here canBeUsedIn- "+ str(self.canBeUsedIn) +'~'+self.name) if not self.access else None))))))))))

def countTabs(value):
	return (len(value) - len(value.lstrip())) / 4



















busObj = None
#count = 0

with open('HRInfoUni.txt') as file:

	inObjLay = 0
	inDimAttr = 0
	skipNextLine = 0
	dimensionList = []

	errorCount = 0
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

				count=count+1
				if('Dimension' in line and '-------------------------------------------------' in next(file)):
					line = line.replace('Dimension: ', '')
					newDim = boItem(line)

					li=next(file).rstrip('\n')
					count=count+1
					if('coreItemIdentifier' in li):
						newDim.setCoreItemIdentifier(li.replace('coreItemIdentifier :','').lstrip())
						li=next(file).rstrip('\n')
						count=count+1
					if('overridableProperties' in li):
						newDim.setOverridableProperties(li.replace('overridableProperties :','').lstrip())
	#					print(str(errorCount) +' '+ li +' '+ str(newDim.getCoreItemIdentifier()))
						li=next(file).rstrip('\n')
						count=count+1
					if('businessName' in li):
						newDim.setBusinessName(li.replace('businessName :','').lstrip())
						li=next(file).rstrip('\n')
						count=count+1
					if('description' in li):
						newDim.setDescription(li.replace('description :','').lstrip())
						li=next(file).rstrip('\n')
						count=count+1
					if not li:
	#					print('here ' + str(count))
						errorCount=errorCount+1
						li = next(file).rstrip('\n')
						count=count+1
						if not li:
	#						print('here too '+ str(count))
							li = next(file).rstrip('\n')
	#						print('is ok: '+ li)
							count=count+1
					elif('state' in li):
						newDim.setState(li.replace('state :','').lstrip())
						toPrint = str(count) +' hey '+ li +'| '+ str(newDim.getState()) if not newDim.getState() else str(count) +' yay '+ li +'| '
						print(toPrint)
						li=next(file).rstrip('\n')
						count=count+1
					if('dataType' in li):
						newDim.setDataType(li.replace('dataType :','').lstrip())
						li=next(file).rstrip('\n')
						count=count+1
					if('access' in li):
						newDim.setAccess(li.replace('access :','').lstrip())
						li=next(file).rstrip('\n')
						count=count+1
					if('forResult' in li):
						newDim.setForResult(li.replace('forResult :','').lstrip())
						li=next(file).rstrip('\n')
						count=count+1
					if('SQL Definition' in li):
						newDim.setSqlDefinition(li.replace('SQL Definition :','').lstrip())
						li=next(file).rstrip('\n')
						count=count+1
					if('Can be used in' in li):
						newDim.setCanBeUsedIn(li.replace('Can be used in  :','').lstrip())

#					newDim.printAll()
					dimensionList.append(newDim)
					if newDim.getMissingData():
						print(str(count) + ': '+ str(newDim.getMissingData()))



#busObj.printAll()
print(errorCount)








#
