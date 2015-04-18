# Riot-Games-API-Challenge
Installation:
  ***Please note: I plan to have a live demo on my website [http://riotapichall.nateageek.net](http://riotapichall.nateageek.net)***

Database(Test on MySQL):
  *First generate the database called urf-data, the tables structures is located at /misc/urf-data.sql
  *Config the username and password of the query user, /main/util/dbHandler.php (Default = username:root password:’’)
  *To get data run the python script, /misc/quick-logger/log_match_URF_NA.py, please note if the database credentials are different from the default, username:’root’ password:’’, they can be changed in the loop_log_data function. 
  *Script can take in arguments of startbucket time and endbucket time. If no arguments passed, goes through all the data available within the eight hour span(1427865900->1428018900).
  *Finally, add the api key to the /main/util/StaticData.php, the variable is $api_key, as a string.
  


Created by NateAGeek, North America, IL 