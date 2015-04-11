import json;
import sys;
import MySQLdb;
import requests;
import MySQLdb.cursors

sqlCursor           = None;
sqlConnection       = None;

def json2SQLTable(json_data, tablename):

  json_data["match_id"] = 0;

  query = "CREATE TABLE IF NOT EXISTS `%s`(id BIGINT NOT NULL AUTO_INCREMENT, PRIMARY KEY (id)" % (tablename);

  for (key, value) in json_data.items():
    #print "key "+str(key)+" has type = "+str(type(value));
    if type(value) is dict:
      value[tablename+"_id"] = 0;
      json2SQLTable(value, key);
      query += ",%s %s" % (str(key+"_id"), "BIGINT"); 
    elif type(value) is list:
      value[0][tablename+"_id"] = 0;
      json2SQLTable(value[0], key);
      query += ",%s %s" % (str(key+"_id"), "BIGINT"); 
    else:
      query += ",%s %s" % (str(key), getEqSQLType(value));

  print query;

  query += ");"

  sqlConnection.query(query);


def setDBStruct(champJSONData):
  json2SQLTable(champJSONData["data"]["Aatrox"], 'champion');


def pushDataIntoDBStruct(champDict):
  for champ in champDict:



def main(argv):
  global sqlConnection;
  global sqlCursor;
  sqlConnection = MySQLdb.connect(host="localhost", user="root", passwd="", db="urf-data", cursorclass=MySQLdb.cursors.SSDictCursor);  
  sqlCursor     = sqlConnection.cursor();

  rData = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=all&api_key=096de5b6-d371-41c2-a263-4db83088a4eb");

  champJSONData = json.loads(rData.text);

  setDBStruct(champJSONData);

  pushDataIntoDBStruct(champJSONData["data"]);


if __name__ == "main":
  main(sys.argv);
