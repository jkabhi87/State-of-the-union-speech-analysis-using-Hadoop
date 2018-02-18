import string
import os

def rempuncandlower(filename):
	with open(filename,"r") as myfile:
		filedata=myfile.read()
		filedata = filedata.translate(None,string.punctuation)
#		dir_path = os.path.join(self.feed, self.address)  # will return 'feed/address'
#		os.mkdir('../generated')                             # create directory [current_path]/feed/address
		output = open(filename+"_1.txt", 'w')
		output.write(filedata.lower())
#		print(filedata.lower())
		output.close()
	myfile.close()

for f in os.listdir('/Users/abhishek/Desktop/HW1/'):
	rempuncandlower(f)
