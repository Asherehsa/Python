import sys
import MySQLdb as mdb
import csv
import time
import datetime
import pprint

# Script Start time
startMicroTime = time.time()



############################################
###############FILE SETTINGS################
############################################
filename = 'file.csv'
############################################

# Connect to the DB
try:
    con = mdb.connect(host, username, password, database)
    
except _mysql.Error, e:
  
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)
		

with con:
	cur = con.cursor()
	insertStatement = "INSERT IGNORE INTO `yourdrea_stuller`.`sku` (`sku`) VALUES (%s);"
	
# get count of rows in table.
cur.execute("SELECT COUNT(*) FROM `sku`")
oldCount = cur.fetchone()


with open(filename, 'rb') as f:
	reader = csv.reader(f)
	totalRows = len(list(reader))
	print 'The file has', totalRows, 'records.'
	f.seek(0)
	rowCount = f.tell()
	for row in reader:
		cur.execute(insertStatement, row)
		rowCount +=1
		progress = float(rowCount) / (totalRows)
		progress *= 100
		progress = round(progress, 2)
#		print progress
		sys.stdout.write("Completed: %d%%   \r" % (progress))
		
sys.stdout.flush()	
	
# get count of rows in table.
cur.execute("SELECT COUNT(*) FROM `sku`")
totalCount = cur.fetchone()
# close the cursor
cur.close()
# close the DB connection.
con.close()

print 'The DB has', totalCount[0], 'records.'
addedRecords = int(totalCount[0]) - int(oldCount[0])
print 'We added', addedRecords, 'new records.' 

# Script End time
endMicroTime = time.time()
totalExecuteTime = endMicroTime - startMicroTime

# Print time to execute
print 'This took', totalExecuteTime, 'seconds to execute.'

exit()