import csv
import sys
import os

class Filter:

	def __init__(self): #constructor
		self.filename = raw_input("Which file would you like to filter?\n")
		self.success = False #success bool

	def openFile(self):
		if os.path.exists ('./%s' % (self.filename)) and os.access(self.filename, os.R_OK): #checks path and file permissions
			self.csvfile = open(self.filename, 'r') #open input file
			self.reader = csv.reader(self.csvfile) #read in entire file
			try:
				self.header = next(self.reader) #checks if second line exits
				if (len(self.header) != 6): #checks number of columns
					sys.exit("%s does not have a valid number of columns." % (self.filename))
				self.success = True
			except:
				sys.exit("%s does not have any data." % (self.filename))
		elif os.path.exists ('./%s' % (self.filename)) == False:  
			sys.exit("File %s does not exist." % (self.filename)) 
		else:
			sys.exit("File %s has protected read permissions." % (self.filename))

	def createFiles(self):
		if (self.header[0] == 'id' and self.header[1] == 'title' and self.header[2]  == 'privacy' and 
			self.header[3] == 'total_plays' and self.header[4] == 'total_comments' and self.header[5] == 'total_likes'): #check header titles
			self.valid = open('valid.csv', 'w') #create valid
			self.invalid = open('invalid.csv', 'w') #craete invalid
		else:
			sys.exit("%s does not have a valid header titles." % (self.filename))

 	def check(self, privacy, title, likes, plays):
 		if privacy == 'anybody' and len(title) < 30 and int(likes) > 10 and int(plays) > 200:
 			return True #conditions are true
 		else:
 			return False # conditions are false

 	def writeValid(self):
 		self.valid.write("%s\n" % str(self.row[0])) #write in valid

 	def writeInvalid(self):
 		self.invalid.write("%s\n" % str(self.row[0])) #write in invalid

 	def runFilter(self):
 		try:
	 		for self.row in self.reader: #iterate through input file
	 			if (self.check(self.row[2], self.row[1], self.row[5], self.row[3])): #check conditions
	 				self.writeValid() #write in valid file
	 			else:
	 				self.writeInvalid() #write in invlaid file
	 	except:
			sys.exit('Error caught in file %s on line %d.' % (self.filename, self.reader.line_num))

 	def __del__(self): #destructor 
 		if self.success == True:
 			print "File %s has been filtered." % (self.filename)
 		else:
 			print "File %s could not be filtered." % (self.filename)

Vimeo = Filter() #create instance 
Vimeo.openFile() #open input file
Vimeo.createFiles() #create output files 
Vimeo.runFilter()
del Vimeo #destoy instance
