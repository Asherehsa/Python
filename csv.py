from csv import reader

with open ('C:\Users\Asher\Documents\Spring 2014\Python\bent.csv', 'rb') as csvfile:

    rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for col in row:
            print '%-8s: %s' % (header[colnum], col)
            colnum += 1
    rownum += 1

ifile.close()