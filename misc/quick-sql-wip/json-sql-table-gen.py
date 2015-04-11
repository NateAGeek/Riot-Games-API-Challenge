import json;
import sys;
import MySQLdb;

sqlConnection = None;
database      = "urf-data";

json_string = """{"match_timeline":{"match_timeline_frames":{"participant_frame":{"participantId":3,"position":{"x":351,"y":293},"currentGold":475,"totalGold":475,"level":1,"xp":0,"minionsKilled":0,"jungleMinionsKilled":0,"dominionScore":0,"teamScore":0},"timestamp":0},"frameInterval":60000}}""";

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

def getEqSQLType(type_val):

  if type(type_val) is int:
    return "INT";
  elif type(type_val) is str or type(type_val) is unicode:
    return "TEXT";
  elif type(type_val) is bool:
    return "BOOLEAN";
  elif type(type_val) is float:
    return "FLOAT";

  return "NULL";

def main(argv):
  global sqlConnection;
  sqlConnection = MySQLdb.connect(host="localhost", user="root", passwd="", db="urf-data");
  p_data = json.loads(json_string);

  json2SQLTable(p_data, 'match_timeline');
  sqlConnection.close();


if __name__ == "__main__":
  main(sys.argv);