import sys;
import requests;
import json;
import time;

apiDevKey           = "99edf43f-698f-4245-870f-51a5179c5e9e";
region              = "na";
baseURL             = "https://na.api.pvp.net";
getListOfMatchesURL = "/api/lol/%s/v4.1/game/ids?beginDate=%s&api_key=%s";
getMatchDataURL     = "/api/lol/%s/v2.2/match/%s?includeTimeline=true&api_key=%s";
total_requests      = 0;

def getListOfMatches_string(time, log):
  global total_requests;
  while True:
    apiMatchListRequest = requests.get(baseURL + getListOfMatchesURL % (region, str(time), apiDevKey));

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
        logFile             = open("logs/list_of_matchs_logs/urf_list_of_matchs_%s.json" % (str(time)), "wb");
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

def getMatchData_struct(id, log):
  return json.loads(getMatchData_string(id, log));

def main(argv):

  init_time = int(argv[1]);
  end_time  = int(argv[2]);
  print "Begining to log data from " + str(init_time) + " to " + str(end_time) + "\n";

  while init_time <= end_time:
    list_of_matchs = getListOfMatches_struct(init_time, True);
    for match_id in list_of_matchs:
      getMatchData_struct(match_id, True);

    init_time += 300

if __name__ == "__main__":
  main(sys.argv);