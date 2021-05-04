# shop_app
## Description
This tool does the following:

- updates product prices based on the api rate of the National Bank of Poland<br />
- generates a products information report<br />

## Files

main.py - main file script<br />
backup.sql - backup database<br />
logfile.log - file with logs<br />
requirements.txt - file with used libraries<br />


## Libraries

requirements.txt:<br />
certifi==2020.12.5<br />
chardet==4.0.0<br />
idna==2.10<br />
mysql-connector==2.2.9<br />
requests==2.25.1<br />
schedule==1.1.0<br />
urllib3==1.26.4<br />
xlwt==1.3.0<br />


## Quick start
1. In the first step, create a database in MySQL Workbench called "mydb".<br />
2. Then import the backup.sql file into the database. Tables should be created and data loaded.<br />
3. Then install the necessary libraries to run the program. You can do this with:<br />
```
pip install -r requirements.txt
```
4. Now you can use the script, below for instructions on program functionality.<br />

UPDATE PRICE<br />
A) Immediately<br />
1. Run command in folder with files program:<br />
```
main.py --updateprice
```
2. The program should respond:<br />
```
03052021 19:37:06 Prices updated successfully!
```
3. The program updates product prices in USD and EUR.<br />

B) Every day<br />

1. For example if you want to update the price every day at 15:00, enter the command:<br />
```
main.py --updateprice 15:00
```
2. At the appointed time, the program should respond:<br />
```
03052021 15:00:01 Prices updated successfully!
```
You can stop the program by clicking: Ctrl+C<br /><br />
REPORT GENERATION<br />

1. Run command in folder with files program:<br />
```
main.py --generatereport
```
2. The program should respond:<br />
```
03052021 19:32:30 Report generated successfully!
```
3. An excel report with product information should be created in the program location.<br />

## Additional  information<br />
- The program generates a logfile.log file in which it saves logs from the script operation (errors and other events).<br />

## Contact<br />
mikulski.michal2@gmail.com
