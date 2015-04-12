import sys;
import requests;
import json;
import time;
import MySQLdb;
import MySQLdb.cursors

sqlCursor           = None;
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
        print "*** Logging Match ID's for time: " + str(timestamp) + " ***";
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
    print "\t\t --Beginging To SQL Log Data id:%s--" %(str(id));
    sql_log_match(match);
    print "\t\t --Logged To SQL Log Data id:%s--" %(str(id));

  return match;

def slq_log_bans(bans_data, match_id):
  sqlCursor.execute("""SELECT MAX(ban_id) FROM `bans`""");

  number_of_bansid = sqlCursor.fetchall();

  bid = 0;

  if number_of_bansid[0]["MAX(ban_id)"] is not None:
    bid = int(number_of_bansid[0]["MAX(ban_id)"]) + 1;

  for value in bans_data:
    sqlCursor.execute("""INSERT INTO `bans`(pickTurn, championId, match_id, ban_id) VALUES (%s, %s, %s, %s)""" % (str(value["pickTurn"]), str(value["championId"]), str(match_id), str(bid)));
    sqlConnection.commit();

  return bid;

def sql_log_teams(teams_data, match_id):
  delta = 0;
  for team in teams_data:
    bans_id = slq_log_bans(team["bans"], match_id);
    sqlCursor.execute("""INSERT INTO `team`(firstDragon, bans_id, firstInhibitor, baronKills, winner, firstBaron, firstBlood, teamId, firstTower, vilemawKills, inhibitorKills, towerKills, dominionVictoryScore, dragonKills, match_id, delta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" % (str(team["firstDragon"]), str(bans_id), str(team["firstInhibitor"]), str(team["baronKills"]), str(team["winner"]), str(team["firstBaron"]), str(team["firstBlood"]), str(team["teamId"]), str(team["firstTower"]), str(team["vilemawKills"]), str(team["inhibitorKills"]), str(team["towerKills"]), str(team["dominionVictoryScore"]), str(team["dragonKills"]), str(match_id), str(delta)));
    team_id = sqlCursor.lastrowid;
    sqlCursor.execute("""UPDATE `bans` SET team_id = %s WHERE ban_id = %s""" % (str(team_id), bans_id));
    sqlConnection.commit();
    delta += 1;

def sql_log_runes_id(runes, match_id):

  sqlCursor.execute("""SELECT MAX(runes_id) FROM `runes`""");

  number_of_runesid = sqlCursor.fetchall();

  rid = 0;

  if number_of_runesid[0]["MAX(runes_id)"] is not None:
    rid = int(number_of_runesid[0]["MAX(runes_id)"]) + 1;

  delta = 0;

  for rune in runes:
    sqlCursor.execute("""INSERT INTO `runes`(runeId, match_id, rank, delta, runes_id) VALUES (%s, %s, %s, %s, %s)""" % (str(rune["runeId"]), str(match_id), str(rune["rank"]), str(delta), str(rid)));
    sqlConnection.commit();
    delta += 1;

  return rid;

def sql_log_masteries_id(masteries, match_id):

  sqlCursor.execute("""SELECT MAX(masteries_id) FROM `masteries`""");

  number_of_masteriesid = sqlCursor.fetchall();

  mid = 0;

  if number_of_masteriesid[0]["MAX(masteries_id)"] is not None:
    mid = int(number_of_masteriesid[0]["MAX(masteries_id)"]) + 1;

  delta = 0;

  for mastery in masteries:
    sqlCursor.execute("""INSERT INTO `masteries`(masteryId, match_id, rank, masteries_id) VALUES (%s, %s, %s, %s)""" % (str(mastery["masteryId"]), str(match_id), str(mastery["rank"]), str(mid)));
    sqlConnection.commit();
    delta += 1;

  return mid;


def sql_log_csDiffPerMinDeltas(csDiffPerMinDeltas, match_id):

  sqlCursor.execute("""INSERT INTO `csDiffPerMinDeltas`(zeroToTen, match_id, tenToTwenty) VALUES(%s, %s, %s)""" % (str(csDiffPerMinDeltas["zeroToTen"]), str(match_id), str(csDiffPerMinDeltas["tenToTwenty"])));
  sqlConnection.commit();

  return sqlCursor.lastrowid;

def sql_log_goldPerMinDeltas(goldPerMinDeltas, match_id):

  sqlCursor.execute("""INSERT INTO `goldPerMinDeltas`(zeroToTen, tenToTwenty, match_id) VALUES(%s, %s, %s)""" % (str(goldPerMinDeltas["zeroToTen"]), str(goldPerMinDeltas["tenToTwenty"]), str(match_id)));
  sqlConnection.commit();

  return sqlCursor.lastrowid;

def sql_log_xpDiffPerMinDeltas(xpDiffPerMinDeltas, match_id):

  sqlCursor.execute("""INSERT INTO `xpDiffPerMinDeltas`(zeroToTen, tenToTwenty, match_id) VALUES(%s, %s, %s)""" % (str(xpDiffPerMinDeltas["zeroToTen"]), str(xpDiffPerMinDeltas["tenToTwenty"]), str(match_id)));
  sqlConnection.commit();

  return sqlCursor.lastrowid;

def sql_log_creepsPerMinDeltas(creepsPerMinDeltas, match_id):

  sqlCursor.execute("""INSERT INTO `creepsPerMinDeltas`(zeroToTen, tenToTwenty, match_id) VALUES(%s, %s, %s)""" % (str(creepsPerMinDeltas["zeroToTen"]), str(creepsPerMinDeltas["tenToTwenty"]), str(match_id)));
  sqlConnection.commit();

  return sqlCursor.lastrowid;

def sql_log_xpPerMinDeltas(xpPerMinDeltas, match_id):

  sqlCursor.execute("""INSERT INTO `xpPerMinDeltas`(zeroToTen, tenToTwenty, match_id) VALUES(%s, %s, %s)""" % (str(xpPerMinDeltas["zeroToTen"]), str(xpPerMinDeltas["tenToTwenty"]), str(match_id)));
  sqlConnection.commit();

  return sqlCursor.lastrowid;

def sql_log_damageTakenDiffPerMinDeltas(damageTakenDiffPerMinDeltas, match_id):

  sqlCursor.execute("""INSERT INTO `damageTakenDiffPerMinDeltas`(zeroToTen, tenToTwenty, match_id) VALUES(%s, %s, %s)""" % (str(damageTakenDiffPerMinDeltas["zeroToTen"]), str(damageTakenDiffPerMinDeltas["tenToTwenty"]), str(match_id)));
  sqlConnection.commit();

  return sqlCursor.lastrowid;

def sql_log_damageTakenPerMinDeltas(damageTakenPerMinDeltas, match_id):

  sqlCursor.execute("""INSERT INTO `damageTakenPerMinDeltas`(zeroToTen, tenToTwenty, match_id) VALUES(%s, %s, %s)""" % (str(damageTakenPerMinDeltas["zeroToTen"]), str(damageTakenPerMinDeltas["tenToTwenty"]), str(match_id)));
  sqlConnection.commit();

  return sqlCursor.lastrowid;

def sql_log_participant_timeline_id(timeline, match_id):
  if not 'csDiffPerMinDeltas' in timeline:
    timeline["csDiffPerMinDeltas"] = {'zeroToTen':0, 'tenToTwenty':0};
  if not 'goldPerMinDeltas' in timeline:
    timeline["goldPerMinDeltas"] = {'zeroToTen':0, 'tenToTwenty':0};
  if not 'xpDiffPerMinDeltas' in timeline:
    timeline["xpDiffPerMinDeltas"] = {'zeroToTen':0, 'tenToTwenty':0};
  if not 'creepsPerMinDeltas' in timeline:
    timeline["creepsPerMinDeltas"] = {'zeroToTen':0, 'tenToTwenty':0};
  if not 'xpPerMinDeltas' in timeline:
    timeline["xpPerMinDeltas"] = {'zeroToTen':0, 'tenToTwenty':0};
  if not 'damageTakenDiffPerMinDeltas' in timeline:
    timeline["damageTakenDiffPerMinDeltas"] = {'zeroToTen':0, 'tenToTwenty':0};
  if not 'damageTakenPerMinDeltas' in timeline:
    timeline["damageTakenPerMinDeltas"] = {'zeroToTen':0, 'tenToTwenty':0};
  if not 'zeroToTen' in timeline['csDiffPerMinDeltas']:
    timeline["csDiffPerMinDeltas"]['zeroToTen'] = 0;
  if not 'zeroToTen' in timeline['goldPerMinDeltas']:
    timeline["goldPerMinDeltas"]['zeroToTen'] = 0;
  if not 'zeroToTen' in timeline['xpDiffPerMinDeltas']:
    timeline["xpDiffPerMinDeltas"]['zeroToTen'] = 0;
  if not 'zeroToTen' in timeline['creepsPerMinDeltas']:
    timeline["creepsPerMinDeltas"]['zeroToTen'] = 0;
  if not 'zeroToTen' in timeline['xpPerMinDeltas']:
    timeline["xpPerMinDeltas"]['zeroToTen'] = 0;
  if not 'zeroToTen' in timeline['damageTakenDiffPerMinDeltas']:
    timeline["damageTakenDiffPerMinDeltas"]['zeroToTen'] = 0;
  if not 'zeroToTen' in timeline['damageTakenPerMinDeltas']:
    timeline["damageTakenPerMinDeltas"]['zeroToTen'] = 0;
  if not 'tenToTwenty' in timeline['csDiffPerMinDeltas']:
    timeline["csDiffPerMinDeltas"]['tenToTwenty'] = 0;
  if not 'tenToTwenty' in timeline['goldPerMinDeltas']:
    timeline["goldPerMinDeltas"]['tenToTwenty'] = 0;
  if not 'tenToTwenty' in timeline['xpDiffPerMinDeltas']:
    timeline["xpDiffPerMinDeltas"]['tenToTwenty'] = 0;
  if not 'tenToTwenty' in timeline['creepsPerMinDeltas']:
    timeline["creepsPerMinDeltas"]['tenToTwenty'] = 0;
  if not 'tenToTwenty' in timeline['xpPerMinDeltas']:
    timeline["xpPerMinDeltas"]['tenToTwenty'] = 0;
  if not 'tenToTwenty' in timeline['damageTakenDiffPerMinDeltas']:
    timeline["damageTakenDiffPerMinDeltas"]['tenToTwenty'] = 0;
  if not 'tenToTwenty' in timeline['damageTakenPerMinDeltas']:
    timeline["damageTakenPerMinDeltas"]['tenToTwenty'] = 0;
  

  csid        = sql_log_csDiffPerMinDeltas(timeline["csDiffPerMinDeltas"], match_id);
  goldid      = sql_log_goldPerMinDeltas(timeline["goldPerMinDeltas"], match_id);
  xpdifid     = sql_log_xpDiffPerMinDeltas(timeline["xpDiffPerMinDeltas"], match_id);
  crepsid     = sql_log_creepsPerMinDeltas(timeline["creepsPerMinDeltas"], match_id);
  xpperminid  = sql_log_xpPerMinDeltas(timeline["xpPerMinDeltas"], match_id);
  damtkndifid = sql_log_damageTakenDiffPerMinDeltas(timeline["damageTakenDiffPerMinDeltas"], match_id);
  damtknpmid  = sql_log_damageTakenPerMinDeltas(timeline["damageTakenPerMinDeltas"], match_id);

  sqlCursor.execute("""INSERT INTO `participant_timeline`(lane, match_id, role, csDiffPerMinDeltas_id, goldPerMinDeltas_id, xpDiffPerMinDeltas_id, creepsPerMinDeltas_id, xpPerMinDeltas_id, damageTakenDiffPerMinDeltas_id, damageTakenPerMinDeltas_id) VALUES ('%s', %s, '%s', %s, %s, %s, %s, %s, %s, %s)""" % (str(timeline["lane"]), str(match_id), str(timeline["role"]), str(csid), str(goldid), str(xpdifid), str(crepsid), str(xpperminid), str(damtkndifid), str(damtknpmid)));
  sqlConnection.commit();

  timeline_id = sqlCursor.lastrowid;

  sqlCursor.execute("""UPDATE `csDiffPerMinDeltas` SET timeline_id = %s WHERE id = %s""" % (str(timeline_id), str(csid)));
  sqlCursor.execute("""UPDATE `goldPerMinDeltas` SET timeline_id = %s WHERE id = %s""" % (str(timeline_id), str(goldid)));
  sqlCursor.execute("""UPDATE `xpDiffPerMinDeltas` SET timeline_id = %s WHERE id = %s""" % (str(timeline_id), str(xpdifid)));
  sqlCursor.execute("""UPDATE `creepsPerMinDeltas` SET timeline_id = %s WHERE id = %s""" % (str(timeline_id), str(crepsid)));
  sqlCursor.execute("""UPDATE `xpPerMinDeltas` SET timeline_id = %s WHERE id = %s""" % (str(timeline_id), str(xpperminid)));
  sqlCursor.execute("""UPDATE `damageTakenDiffPerMinDeltas` SET timeline_id = %s WHERE id = %s""" % (str(timeline_id), str(damtkndifid)));
  sqlCursor.execute("""UPDATE `damageTakenPerMinDeltas` SET timeline_id = %s WHERE id = %s""" % (str(timeline_id), str(damtknpmid)));
  sqlConnection.commit();

  return timeline_id;

def sql_log_stats_id(stats, match_id):

  sqlCursor.execute("""INSERT INTO `stats`(neutralMinionsKilledTeamJungle, totalPlayerScore, unrealKills, objectivePlayerScore, totalDamageDealt, magicDamageDealtToChampions, match_id, largestMultiKill, largestKillingSpree, item1, quadraKills, magicDamageTaken, towerKills, totalTimeCrowdControlDealt, wardsKilled, firstTowerAssist, firstBloodAssist, firstTowerKill, item2, item3, item0, winner, item6, wardsPlaced, item4, item5, minionsKilled, doubleKills, tripleKills, neutralMinionsKilledEnemyJungle, goldEarned, magicDamageDealt, kills, largestCriticalStrike, firstInhibitorKill, trueDamageTaken, firstBloodKill, assists, deaths, neutralMinionsKilled, combatPlayerScore, visionWardsBoughtInGame, physicalDamageDealtToChampions, goldSpent, trueDamageDealt, trueDamageDealtToChampions, champLevel, pentaKills, firstInhibitorAssist, totalHeal, physicalDamageDealt, sightWardsBoughtInGame, totalDamageDealtToChampions, totalUnitsHealed, inhibitorKills, totalScoreRank, totalDamageTaken, killingSprees, physicalDamageTaken) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" % (str(stats["neutralMinionsKilledTeamJungle"]), str(stats["totalPlayerScore"]), str(stats["unrealKills"]), str(stats["objectivePlayerScore"]), str(stats["totalDamageDealt"]), str(stats["magicDamageDealtToChampions"]), str(match_id), str(stats["largestMultiKill"]), str(stats["largestKillingSpree"]), str(stats["item1"]), str(stats["quadraKills"]), str(stats["magicDamageTaken"]), str(stats["towerKills"]), str(stats["totalTimeCrowdControlDealt"]), str(stats["wardsKilled"]), str(stats["firstTowerAssist"]), str(stats["firstBloodAssist"]), str(stats["firstTowerKill"]), str(stats["item2"]), str(stats["item3"]), str(stats["item0"]), str(stats["winner"]), str(stats["item6"]), str(stats["wardsPlaced"]), str(stats["item4"]), str(stats["item5"]), str(stats["minionsKilled"]), str(stats["doubleKills"]), str(stats["tripleKills"]), str(stats["neutralMinionsKilledEnemyJungle"]), str(stats["goldEarned"]), str(stats["magicDamageDealt"]), str(stats["kills"]), str(stats["largestCriticalStrike"]), str(stats["firstInhibitorKill"]), str(stats["trueDamageTaken"]), str(stats["firstBloodKill"]), str(stats["assists"]), str(stats["deaths"]), str(stats["neutralMinionsKilled"]), str(stats["combatPlayerScore"]), str(stats["visionWardsBoughtInGame"]), str(stats["physicalDamageDealtToChampions"]), str(stats["goldSpent"]), str(stats["trueDamageDealt"]), str(stats["trueDamageDealtToChampions"]), str(stats["champLevel"]), str(stats["pentaKills"]), str(stats["firstInhibitorAssist"]), str(stats["totalHeal"]), str(stats["physicalDamageDealt"]), str(stats["sightWardsBoughtInGame"]), str(stats["totalDamageDealtToChampions"]), str(stats["totalUnitsHealed"]), str(stats["inhibitorKills"]), str(stats["totalScoreRank"]), str(stats["totalDamageTaken"]), str(stats["killingSprees"]), str(stats["physicalDamageTaken"])));
  sqlConnection.commit();

  return sqlCursor.lastrowid;


def sql_log_participant(participant_data, match_id, delta):
  if not "runes" in participant_data:
    participant_data["runes"] = {};
  if not "masteries" in participant_data:
    participant_data["masteries"] = {};
  if not "timeline" in participant_data:
    participant_data["timeline"] = {};
  if not "stats" in participant_data:
    participant_data["stats"] = {};

  runes_id     = sql_log_runes_id(participant_data["runes"], match_id);
  masteries_id = sql_log_masteries_id(participant_data["masteries"], match_id);
  timeline_id  = sql_log_participant_timeline_id(participant_data["timeline"], match_id);
  stats_id     = sql_log_stats_id(participant_data["stats"], match_id);

  sqlCursor.execute("""INSERT INTO `participant`(spell1Id, championId, participantId, runes_id, highestAchievedSeasonTier, teamId, spell2Id, masteries_id, timeline_id, stats_id, match_id, delta) VALUES (%s, %s, %s, %s, '%s', %s, %s, %s, %s, %s, %s, %s) \n""" % (str(participant_data["spell1Id"]), str(participant_data["championId"]), str(participant_data["participantId"]), str(runes_id), str(participant_data["highestAchievedSeasonTier"]), str(participant_data["teamId"]), str(participant_data["spell2Id"]), str(masteries_id), str(timeline_id), str(stats_id), str(match_id), str(delta)));
  sqlConnection.commit();

  participant_id = sqlCursor.lastrowid;


  sqlCursor.execute("""UPDATE `runes` SET participant_id = %s WHERE runes_id = %s """ % (str(participant_id), str(runes_id)));
  sqlCursor.execute("""UPDATE `masteries` SET participant_id = %s WHERE masteries_id = %s """ % (str(participant_id), str(masteries_id)));
  sqlCursor.execute("""UPDATE `participant_timeline` SET participant_id = %s WHERE id = %s """ % (str(participant_id), str(runes_id)));
  sqlCursor.execute("""UPDATE `stats` SET participant_id = %s WHERE id = %s """ % (str(participant_id), str(stats_id)));
  sqlConnection.commit();

  return participant_id;

def sql_log_participants(participants_data, match_id):
  delta = 0;
  for participant in participants_data:
    participant_id = sql_log_participant(participant, match_id, delta);
    delta += 1;

def sql_log_position(position, match_id):
  sqlCursor.execute("""INSERT INTO `position`(x, y, match_id) VALUES (%s, %s, %s)""" % (str(position["x"]), str(position["y"]), str(match_id)));
  sqlConnection.commit();
  return sqlCursor.lastrowid;

def sql_log_match_timeline(timeline, match_id):

  delta = 0;
  for frame in timeline["frames"]:

    sqlCursor.execute("""SELECT MAX(match_timeline_id) FROM `match_timeline_frames`""");
  
    number_of_match_timeline = sqlCursor.fetchall();
  
    mtid = 0;
  
    if number_of_match_timeline[0]["MAX(match_timeline_id)"] is not None:
      mtid = int(number_of_match_timeline[0]["MAX(match_timeline_id)"]) + 1;
  
    sqlCursor.execute("""INSERT INTO `match_timeline`(match_id, match_timeline_frames_id, frameInterval, delta) VALUES (%s, %s, %s, %s)""" %(str(match_id), str(mtid), str(timeline["frameInterval"]), str(delta)));
    sqlConnection.commit();
  
    frame_delta = 0;
    for participantFrame_id in frame["participantFrames"]:
      participantFrame = frame["participantFrames"][participantFrame_id];
      if not "position" in participantFrame:
        participantFrame["position"] = {'x': -1, 'y': -1};
      pid = sql_log_position(participantFrame["position"], match_id);
      sqlCursor.execute("""INSERT INTO `match_timeline_frames`(totalGold, teamScore, participantId, level, currentGold, minionsKilled, dominionScore, match_timeline_id, position_id, xp, jungleMinionsKilled, match_id, delta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" % (str(participantFrame["totalGold"]), str(participantFrame["teamScore"]), str(participantFrame["participantId"]), str(participantFrame["level"]), str(participantFrame["currentGold"]), str(participantFrame["minionsKilled"]), str(participantFrame["dominionScore"]), str(mtid), str(pid), str(participantFrame["xp"]), str(participantFrame["jungleMinionsKilled"]), str(match_id), str(frame_delta)));
      mfid = sqlCursor.lastrowid;
      sqlConnection.commit();
      sqlCursor.execute("""UPDATE `position` SET match_timeline_frame_id = %s WHERE id = %s""" % (str(mfid), str(pid)));
      sqlConnection.commit();
      frame_delta += 1;
    delta += 1;

def sql_log_match(data):

  sql_log_teams(data["teams"], data["matchId"]);
  sql_log_participants(data["participants"], data["matchId"]);
  sql_log_match_timeline(data["timeline"], data["matchId"]);

  sqlCursor.execute("""INSERT INTO `match`(queueType, matchVersion, platformId, season, region, matchId, mapId, matchCreation, matchMode, matchDuration, matchType) VALUES ('%s', '%s', '%s', '%s', '%s', %s, %s, %s, '%s', %s, '%s')""" % (str(data["queueType"]), str(data["matchVersion"]), str(data["platformId"]), str(data["season"]), str(data["region"]), str(data["matchId"]), str(data["mapId"]), str(data["matchCreation"]), str(data["matchMode"]), str(data["matchDuration"]), str(data["matchType"])));
  sqlConnection.commit();


def match_jsonData_string_to_sqlData(json_data_string):
  data = json.loads(json_data_string);

  sql_log_match(data);


  return "";

def loop_log_data_to_sql():
  return "";


def loop_old_data_to_sql():
  global sqlConnection;
  global sqlCursor;
  sqlConnection = MySQLdb.connect(host="localhost", user="root", passwd="", db="urf-data", cursorclass=MySQLdb.cursors.SSDictCursor);  
  sqlCursor     = sqlConnection.cursor();

  index = 4000;

  while True:

    sqlCursor.execute("""SELECT `match_old`.json_data, `match_old`.match_id FROM `match_old` LIMIT %s, %s""" % (str(index), str(index+10)));
    rows = sqlCursor.fetchall();

    for row in rows:
      # match_jsonData_string_to_sqlData(row["json_data"]);

      print "Logged Match ID: %s; LIMIT %s, %s" % (row["match_id"], str(index), str(index+10)); 

    if len(rows) < 10:
      break;

    index = index + 10;

  sqlCursor.close();
  sqlConnection.close();  

def loop_log_data(init_time = 1427865900, end_time = 1428018900, sql = True):

  print "Begining to log data from " + str(init_time) + " to " + str(end_time) + "\n";

  if sql:
    global sqlConnection;
    global sqlCursor;
    sqlConnection = MySQLdb.connect(host="localhost", user="root", passwd="", db="urf-data",  cursorclass=MySQLdb.cursors.SSDictCursor);
    sqlCursor     = sqlConnection.cursor();

  while init_time <= end_time:
    list_of_matchs = getListOfMatches_struct(init_time, False);
    for match_id in list_of_matchs:
      match_data = getMatchData_struct(match_id, False, sql);

    init_time += 300

  if sql:
    sqlCursor.close();
    sqlConnection.close();


def main(argv):
  # loop_old_data_to_sql();


  if len(argv) > 1:
    loop_log_data(int(argv[1]), int(argv[2]));
  else:
    loop_log_data();

if __name__ == "__main__":
  main(sys.argv);