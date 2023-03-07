
				Norman Police Incidents Summary

<h1> Author : Chandra Likhitha Chopparapu </h1>
<h3>About the Project <h3> : 
In this Project I have chosen one incident pdf that was given in this website below
<b> url <b>  : https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports
and I have extracted the data from the incidents pdf using list of lists and using sqlite3 I have inserted all the data using createdb(),populatedb() and statusdb() to get the nature of incidents and how many times each nature appears.
	
	<b> How to install Packages </b>
	
I have used pipenv to install all the packages that are required for this project
	
Packages used are
	
<ul>
	<ol> urllib </ol>
	<ol> PyPDF4 </ol>
	<ol> sqlite3 </ol>
	<ol> pytest </ol>
	<ol> re </ol>
	<ol> tempfile </ol>
	<ol> argparse</ol>
	</ul>
	
the syntax for installing some of the libraries using pipenv is 
	
<b> pipenv install <packagename> </b>
	
<h3> Project0 Python files </h3>
	
I have created a directory project0 and put these two files in that directory
1. Main.py
2. Project0.py
<h3> Main.py </h3>
	
In main.py files I have called all the 5 methods that have been used in the project0.py and run them using this command 
pipenv run python project0/main.py --incidents <url>
	
In the url we can use the url of the incident file .
	
for example we can use this url for the incident pdf : url = "https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-01_daily_incident_summary.pdf"

Using this url in the directory cs5293sp23-project0 we can run the above mentioned pipenv command.
	
<h3> Methods present in the main.py are </h3>
	
	<ul>
		
<ol> i) <b> project0.fetchincident(url) </b> : this method is used to fetch the incidents pdf and download the data using the given url </ol>
		
<ol> ii)<b> project0.extractincidents(incident_data) </b> : in this method I hace extracted the data and cleaned it and arranged into a list based on the different coloumns it has. </ol>
		
<ol> iii)<b> project0.createdb() </b> : this method created the database with the name normanpd.db </ol>
		
<ol> iv)<b> project0.populatedb() </b> :this method populates the database with the data that we have extracted from the extractincidents method and all the data will be inserted into the database into their respective columns. </ol>
		
<ol> v)<b> project0.status() </b> : this method will print the nature of the incidents and the number of times it has appeared in the data that we have pulled from the incident website of the normanpd website. </ol>
		
And all the above used methods and their body is completed in the project0.py file which is described below
		
<h3> Project.py </h3>
		
<ol > <b> fetchincidents(url) </b> : in this method we pass url as an arguement and while passing the url in the commandline it will take that url in this fetchincidents method and get the data from the incidents pdf and I checked if the method is working by giving out a print statement. </ol> 
		<ol> <b> Bugs and Assumptions </b> </ol> :
		
There are some bugs that can occur while doing this. The url cannot be extracted if there is any small change in the url. So make sure to use the correct url 
while passing the url in the command line.
		
		<ol> <b> extractincidents(incident_data) </b> </ol> : in this method I have extracted the raw data and arranged into a list where data of every column is separated into a row and those rows are placed into a list . Then I have used regex to separate each columns based on the data and time . Also I have combined the data and time into a single string and the rest of the data into separate strings based on the rest of the data. After doing this there is a list of lists that has been created to store each and every row of the incident pdf.
		
		<ol> <b> Bugs and Assumptions </b> </ol>
		
While I was extracting this data there was a issue where all the dates and time were separated for the first page but when I was appending the next page it just combined the last row of the first page and first row of the second page. I have solved this using the datetime regex which separated the dates of every page aand then used the .split() method which helped me resolve this.
		
		<ol> <b> createdb() </b> </ol> : This method uses sqlite3 package which helps to create a database with the name 'normanpd.db' create a db connection and after creating if we go out of the folder and rin a 'ls' command which lists out all the files then there will be a file created with 'normanpd.db' along with all the files.
		
		<ol > <b> populatedb() </b> </ol> : This method is used to insert data that we have extracted into a database with the name that we have created using the above method which is 'normanpd.db" and use the INSERT statement from the sql and insert the data from the extractedtext and pass into the database.
Bugs and Assumptions : while populating the db if there are some errors that we may face which is because of the errors in the data extraction part. so if we do the extractincidents part correctly then data will be inserted into the database accurately.
		
		<ol> <b> status() </b> </ol> : it prints out the number of nature of incidents and also counts everything and prints the data of the number of nature of incidents and count of the number of times it appears in the command line.
 
<h3> Pytests(Testcases) </h3>
		<ol> <b> test_fetchincidents() </b> </ol> : this method is used to check if the incidents are fetched correctly when the url is passed into the method.
		<ol> <b> test_extractincidents() </b> </ol> : this method is used to check if the the data extracted correctly is inserted into the list of lists and all the columns are also distinguishable. If this works then all the test would be passed.
<b> test_createdb() </b> : this method checks if the db name matches with the name of the db that we have passed as a url. and if it matches then the test would be passed successfully.
<b> test_populatedb() </b> : this method is used to check if the data is inserted properly and all the columns are separated properly and if this is true then the test is passed . This test checks if the data passed is correct .
<b> test_status() </b> : this tests are used to check if the nature of the incidents are printing correctly or not . And if everything is printed correctly then the test is passed .
We have to run all these tests in the main project folder .
To run the tests use this command : pipenv run python -m pytest.
If all the tests are passed it shows that All tests are passed message in the command line 
