:: ----------------------------- Begin Header -----------------------------------
:: Name of the batch file : training-batch.bat
::
:: Purpose : Automate the pulling of data from the server and run the R scripts that clean data
::
:: Input  :  
::
:: Output : Updated datasets
::          Updated reports
::
::
:: Authors : Moses Otieno
::
::
:: Contact Email : mosotieno25@gmail.com
::
::
:: First version : 15 October 2024
::
::
:: Reviewed :
::
:: ----------------------------- End Header--------------------------------------


echo "Downloading and preparing project data..."

:: Change the directory appropriately

D:
cd "D:\InterestingTasks\data-mngmt\scripts"


:: Run the python script to pull the data from the server

python "download_data.py"

:: Wait the download

timeout /t 3  /nobreak  

Rscript "master.R"



