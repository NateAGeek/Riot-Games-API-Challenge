import sys;
import requests;
import json;
import time;
import MySQLdb;

sqlConnection       = None;
apiDevKey           = "096de5b6-d371-41c2-a263-4db83088a4eb";
region              = "na";
baseURL             = "https://na.api.pvp.net";
getListOfMatchesURL = "/api/lol/%s/v4.1/game/ids?beginDate=%s&api_key=%s";
getMatchDataURL     = "/api/lol/%s/v2.2/match/%s?includeTimeline=true&api_key=%s";
total_requests      = 0;

def getListOfMatches_string(timestamp, log):
  global total_requests;
  while True:
    apiMatchListRequest = requests.get(baseURL + getListOfMatchesURL % (region, str(timestamp), apiDevKey));

    if apiMatchListRequest.status_code == 404 or apiMatchListRequest.status_code == 400 or apiMatchListRequest.status_code == 503:
      print "Data snag error? Code:" + apiMatchListRequest.status_code + " (waiting 10 seconds) \n"
      time.sleep(10);
    elif apiMatchListRequest.status_code == 429:
      if total_requests % 500 == 0:
        print "Made too many requests(" + str(total_requests) + ") gotta wait 10 minutes";
        time.sleep(610);
      else:
        print "Made too many requests(" + str(total_requests) + ") gotta wait 10 seconds";
        time.sleep(10);
    else:
      total_requests += 1;
      data = apiMatchListRequest.text;
    
      if log:
        print "*** Logging Match ID's for time: " + str(time) + " ***";
        logFile             = open("logs/list_of_matchs_logs/urf_list_of_matchs_%s.json" % (str(timestamp)), "wb");
        logFile.write(data);
    
      return data;

def getListOfMatches_struct(time, log):
  return json.loads(getListOfMatches_string(time, log));

def getMatchData_string(id, log):
  global total_requests;
  while True:
    apiMatchDataRequest = requests.get(baseURL + getMatchDataURL % (region, str(id), apiDevKey));

    if apiMatchDataRequest.status_code == 404 or apiMatchDataRequest.status_code == 400 or apiMatchDataRequest.status_code == 503:
      print "Data snag error? Code:" + apiMatchDataRequest.status_code + " (waiting 10 seconds) \n"
      time.sleep(10);
    elif apiMatchDataRequest.status_code == 429:
      if total_requests % 500 == 0:
        print "Made too many requests(" + str(total_requests) + ") gotta wait 10 minutes";
        time.sleep(610);
      else:
        print "Made too many requests(" + str(total_requests) + ") gotta wait 10 seconds";
        time.sleep(10);
    else:
      total_requests += 1;
      data = apiMatchDataRequest.text;
    
      if log:
        print "\t*** Logging Match ID:" + str(id) + " ***";
        logFile             = open("logs/match_data/urf_match_id_%s.json" % (str(id)), "wb");
        logFile.write(data);
    
      return data;

def getMatchData_struct(id, log, sql):

  match_json_string = getMatchData_string(id, log);
  match = json.loads(match_json_string);

  

  if sql:
    sqlConnection.query("""INSERT INTO `match` (match.match_id, match.timestamp, match.json_data) VALUES (%s, %s, '%s')""" % (match["matchId"], match["matchCreation"], json.dumps(match)));
    sqlConnection.commit();



  return match;

def loop_log_data(init_time = 1427865900, end_time = 1428018900, sql = True):

  print "Begining to log data from " + str(init_time) + " to " + str(end_time) + "\n";

  if sql:
    global sqlConnection;
    sqlConnection = MySQLdb.connect(host="localhost", user="root", passwd="", db="urf-data");

  while init_time <= end_time:
    list_of_matchs = getListOfMatches_struct(init_time, True);
    for match_id in list_of_matchs:
      match_data = getMatchData_struct(match_id, True, sql);

    init_time += 300

  sqlConnection.close();


def main(argv):

  if len(argv) > 1:
    loop_log_data(int(argv[1]), int(argv[2]));
  else:
    loop_log_data();

if __name__ == "__main__":
  main(sys.argv);