

class boDim:

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



















#
