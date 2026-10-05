import csv
with open ("login_data.csv",'w' , newline ='') as file:
    made = csv.writer(file)
    made.writerow(['name','Course','score'])
    made.writerow(['Glory','Cybersecurity',85])
    made.writerow(['John','Networking',72])
    made.writerow(['Sarah','Cybersecurity',91])+




import csv
with open ("students.csv","r", newline = "") as document:
    read = csv.reader(document)

    next(read)
    for row in read:
        if row[1] == 'Cybersecurity':

           print(f'{row[0]} - {row[1]} - {row[2]}') 