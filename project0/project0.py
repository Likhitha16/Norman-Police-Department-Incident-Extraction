import urllib.request
import  PyPDF4
import tempfile
import re
import sqlite3

def fetchincidents(url):
    print('Fetching incidents in process')
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    return data
def extractincidents(incident_data):
    temporary = tempfile.TemporaryFile()
    temporary.write(incident_data)
    temporary.seek(0)
    temporary.read()

    # Load the temporary file into a PdfFileReader object
    pdf_reader = PyPDF4.PdfFileReader(temporary)

    # Get the number of pages in the PDF file
    pages = pdf_reader.getNumPages()

    # Extract text from the first page
    page1 = pdf_reader.getPage(0).extractText()

    # Remove unwanted strings from the text
    page1 = page1.replace("NORMAN POLICE DEPARTMENT","").replace("Daily Incident Summary (Public)","")
    #extracting data from all the pages
    for i in range(pages):
        page1 = page1 + pdf_reader.pages[i].extractText().replace("\n ","n" )
    #    print(len(page1))    
        pattern = pattern = r'(\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{1,2})\n(.*?)\n(.*?)\n(.*?)\n(.*?)\n(.*?)'
        data_list = re.findall(pattern, page1, re.DOTALL)
        insert_list = []
        for data in data_list:
        
    # Combine the lines into a single string
        
            row = [data[0], data[1], data[2], data[3], data[4]]
            #print(row)
            insert_list.append(row)
    #exception which handles any extra column that is present in the pdf 
    if(len(row)) > 5:
        row.pop()
    return insert_list        

   #initialize an empty list to store the data

def createdb():
    con = sqlite3.connect('normanpd.db')
    cursor = con.cursor()
    print("connection created successfully")
    cursor.execute('''DROP TABLE if exists incidents''')
    cursor.execute('''CREATE TABLE if not exists incidents (incident_time TEXT, incident_number TEXT, incident_location TEXT,nature TEXT,incident_ori TEXT)''')
    cursor.execute('''SELECT * FROM incidents''')
    test = cursor.fetchall()
    #print(test)
    con.commit()
    con.close()
    return 'normanpd.db'
def populatedb(db,incidents):
    con = sqlite3.connect('normanpd.db')
    cursor = con.cursor()
# Extract the individual components
#incident_date, incident_time, incident_number, incident_location, incident_nature, incident_ori = components[0], components[1], components[2], ' '.join(components[3:-2]), components[-2], components[-1]
    cursor.executemany('''INSERT INTO  incidents(incident_time,incident_number,incident_location,nature,incident_ori)  VALUES(?,?,?,?,?)''',incidents)
    con.commit()
    con.close()
def status():
    con = sqlite3.connect('normanpd.db')
    cursor = con.cursor()
    print("a list of the nature of incidents and the number of times they have occurred")
    query = cursor.execute('''SELECT nature || '|' || COUNT(*) as incident_count 
    FROM incidents 
    GROUP BY nature 
    ORDER BY COUNT(*) DESC, nature ASC;''')
    test1 = query.fetchall()
    for row in test1:
        print(row[0])
    con.commit()
    con.close()
