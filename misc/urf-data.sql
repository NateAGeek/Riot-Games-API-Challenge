-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 11, 2015 at 07:50 PM
-- Server version: 5.6.21
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `urf-data`
--

-- --------------------------------------------------------

--
-- Table structure for table `bans`
--

CREATE TABLE IF NOT EXISTS `bans` (
`id` bigint(20) NOT NULL,
  `pickTurn` int(11) DEFAULT NULL,
  `championId` int(11) DEFAULT NULL,
  `team_id` int(11) DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `ban_id` bigint(20) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=44340 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `creepsPerMinDeltas`
--

CREATE TABLE IF NOT EXISTS `creepsPerMinDeltas` (
`id` bigint(20) NOT NULL,
  `timeline_id` int(11) DEFAULT NULL,
  `zeroToTen` float DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `tenToTwenty` float DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=74434 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `csDiffPerMinDeltas`
--

CREATE TABLE IF NOT EXISTS `csDiffPerMinDeltas` (
`id` bigint(20) NOT NULL,
  `timeline_id` int(11) DEFAULT NULL,
  `zeroToTen` float DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `tenToTwenty` float DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=74434 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `damageTakenDiffPerMinDeltas`
--

CREATE TABLE IF NOT EXISTS `damageTakenDiffPerMinDeltas` (
`id` bigint(20) NOT NULL,
  `timeline_id` int(11) DEFAULT NULL,
  `zeroToTen` float DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `tenToTwenty` float DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=74434 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `damageTakenPerMinDeltas`
--

CREATE TABLE IF NOT EXISTS `damageTakenPerMinDeltas` (
`id` bigint(20) NOT NULL,
  `timeline_id` int(11) DEFAULT NULL,
  `zeroToTen` float DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `tenToTwenty` float DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=74434 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `goldPerMinDeltas`
--

CREATE TABLE IF NOT EXISTS `goldPerMinDeltas` (
`id` bigint(20) NOT NULL,
  `timeline_id` int(11) DEFAULT NULL,
  `zeroToTen` float DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `tenToTwenty` float DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=74434 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `masteries`
--

CREATE TABLE IF NOT EXISTS `masteries` (
`id` bigint(20) NOT NULL,
  `masteryId` int(11) DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `rank` int(11) DEFAULT NULL,
  `participant_id` int(11) DEFAULT NULL,
  `masteries_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1127806 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `match`
--

CREATE TABLE IF NOT EXISTS `match` (
`id` bigint(20) NOT NULL,
  `queueType` text NOT NULL,
  `matchVersion` text NOT NULL,
  `platformId` text NOT NULL,
  `season` text NOT NULL,
  `region` text NOT NULL,
  `matchId` bigint(20) NOT NULL,
  `mapId` bigint(20) NOT NULL,
  `matchCreation` bigint(20) NOT NULL,
  `matchMode` text NOT NULL,
  `matchDuration` bigint(20) NOT NULL,
  `matchType` text NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=7442 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `match_old`
--

CREATE TABLE IF NOT EXISTS `match_old` (
`id` bigint(20) NOT NULL,
  `match_id` int(11) NOT NULL,
  `timestamp` bigint(20) NOT NULL,
  `json_data` longtext NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=7268 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `match_timeline`
--

CREATE TABLE IF NOT EXISTS `match_timeline` (
`id` bigint(20) NOT NULL,
  `match_id` int(11) DEFAULT NULL,
  `match_timeline_frames_id` bigint(20) DEFAULT NULL,
  `frameInterval` int(11) DEFAULT NULL,
  `delta` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=227839 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `match_timeline_frames`
--

CREATE TABLE IF NOT EXISTS `match_timeline_frames` (
`id` bigint(20) NOT NULL,
  `totalGold` int(11) DEFAULT NULL,
  `teamScore` int(11) DEFAULT NULL,
  `participantId` int(11) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `currentGold` int(11) DEFAULT NULL,
  `minionsKilled` int(11) DEFAULT NULL,
  `dominionScore` int(11) DEFAULT NULL,
  `match_timeline_id` int(11) DEFAULT NULL,
  `position_id` bigint(20) DEFAULT NULL,
  `xp` int(11) DEFAULT NULL,
  `jungleMinionsKilled` int(11) DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `delta` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2278381 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `participant`
--

CREATE TABLE IF NOT EXISTS `participant` (
`id` bigint(20) NOT NULL,
  `spell1Id` int(11) DEFAULT NULL,
  `championId` int(11) DEFAULT NULL,
  `participantId` int(11) DEFAULT NULL,
  `runes_id` bigint(20) DEFAULT NULL,
  `highestAchievedSeasonTier` text,
  `teamId` int(11) DEFAULT NULL,
  `spell2Id` int(11) DEFAULT NULL,
  `masteries_id` bigint(20) DEFAULT NULL,
  `timeline_id` bigint(20) DEFAULT NULL,
  `stats_id` bigint(20) DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `delta` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=74434 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `participant_timeline`
--

CREATE TABLE IF NOT EXISTS `participant_timeline` (
`id` bigint(20) NOT NULL,
  `lane` text,
  `match_id` int(11) DEFAULT NULL,
  `csDiffPerMinDeltas_id` bigint(20) DEFAULT NULL,
  `goldPerMinDeltas_id` bigint(20) DEFAULT NULL,
  `xpDiffPerMinDeltas_id` bigint(20) DEFAULT NULL,
  `creepsPerMinDeltas_id` bigint(20) DEFAULT NULL,
  `xpPerMinDeltas_id` bigint(20) DEFAULT NULL,
  `role` text,
  `participant_id` int(11) DEFAULT NULL,
  `damageTakenDiffPerMinDeltas_id` bigint(20) DEFAULT NULL,
  `damageTakenPerMinDeltas_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=74434 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `position`
--

CREATE TABLE IF NOT EXISTS `position` (
`id` bigint(20) NOT NULL,
  `y` int(11) DEFAULT NULL,
  `x` int(11) DEFAULT NULL,
  `match_timeline_frame_id` int(11) DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2278381 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `runes`
--

CREATE TABLE IF NOT EXISTS `runes` (
`id` bigint(20) NOT NULL,
  `runeId` int(11) DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `rank` int(11) DEFAULT NULL,
  `participant_id` int(11) DEFAULT NULL,
  `delta` int(11) NOT NULL,
  `runes_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=370075 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `stats`
--

CREATE TABLE IF NOT EXISTS `stats` (
`id` bigint(20) NOT NULL,
  `neutralMinionsKilledTeamJungle` int(11) DEFAULT NULL,
  `totalPlayerScore` int(11) DEFAULT NULL,
  `unrealKills` int(11) DEFAULT NULL,
  `objectivePlayerScore` int(11) DEFAULT NULL,
  `totalDamageDealt` int(11) DEFAULT NULL,
  `magicDamageDealtToChampions` int(11) DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `largestMultiKill` int(11) DEFAULT NULL,
  `largestKillingSpree` int(11) DEFAULT NULL,
  `item1` int(11) DEFAULT NULL,
  `quadraKills` int(11) DEFAULT NULL,
  `magicDamageTaken` int(11) DEFAULT NULL,
  `towerKills` int(11) DEFAULT NULL,
  `totalTimeCrowdControlDealt` int(11) DEFAULT NULL,
  `wardsKilled` int(11) DEFAULT NULL,
  `firstTowerAssist` tinyint(1) DEFAULT NULL,
  `firstBloodAssist` tinyint(1) DEFAULT NULL,
  `firstTowerKill` tinyint(1) DEFAULT NULL,
  `item2` int(11) DEFAULT NULL,
  `item3` int(11) DEFAULT NULL,
  `item0` int(11) DEFAULT NULL,
  `winner` tinyint(1) DEFAULT NULL,
  `item6` int(11) DEFAULT NULL,
  `wardsPlaced` int(11) DEFAULT NULL,
  `item4` int(11) DEFAULT NULL,
  `item5` int(11) DEFAULT NULL,
  `minionsKilled` int(11) DEFAULT NULL,
  `doubleKills` int(11) DEFAULT NULL,
  `tripleKills` int(11) DEFAULT NULL,
  `neutralMinionsKilledEnemyJungle` int(11) DEFAULT NULL,
  `goldEarned` int(11) DEFAULT NULL,
  `magicDamageDealt` int(11) DEFAULT NULL,
  `kills` int(11) DEFAULT NULL,
  `largestCriticalStrike` int(11) DEFAULT NULL,
  `firstInhibitorKill` tinyint(1) DEFAULT NULL,
  `trueDamageTaken` int(11) DEFAULT NULL,
  `firstBloodKill` tinyint(1) DEFAULT NULL,
  `assists` int(11) DEFAULT NULL,
  `deaths` int(11) DEFAULT NULL,
  `neutralMinionsKilled` int(11) DEFAULT NULL,
  `combatPlayerScore` int(11) DEFAULT NULL,
  `participant_id` int(11) DEFAULT NULL,
  `visionWardsBoughtInGame` int(11) DEFAULT NULL,
  `physicalDamageDealtToChampions` int(11) DEFAULT NULL,
  `goldSpent` int(11) DEFAULT NULL,
  `trueDamageDealt` int(11) DEFAULT NULL,
  `trueDamageDealtToChampions` int(11) DEFAULT NULL,
  `champLevel` int(11) DEFAULT NULL,
  `pentaKills` int(11) DEFAULT NULL,
  `firstInhibitorAssist` tinyint(1) DEFAULT NULL,
  `totalHeal` int(11) DEFAULT NULL,
  `physicalDamageDealt` int(11) DEFAULT NULL,
  `sightWardsBoughtInGame` int(11) DEFAULT NULL,
  `totalDamageDealtToChampions` int(11) DEFAULT NULL,
  `totalUnitsHealed` int(11) DEFAULT NULL,
  `inhibitorKills` int(11) DEFAULT NULL,
  `totalScoreRank` int(11) DEFAULT NULL,
  `totalDamageTaken` int(11) DEFAULT NULL,
  `killingSprees` int(11) DEFAULT NULL,
  `physicalDamageTaken` int(11) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=74434 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `team`
--

CREATE TABLE IF NOT EXISTS `team` (
`id` bigint(20) NOT NULL,
  `firstDragon` tinyint(1) DEFAULT NULL,
  `bans_id` bigint(20) DEFAULT NULL,
  `firstInhibitor` tinyint(1) DEFAULT NULL,
  `baronKills` int(11) DEFAULT NULL,
  `winner` tinyint(1) DEFAULT NULL,
  `firstBaron` tinyint(1) DEFAULT NULL,
  `firstBlood` tinyint(1) DEFAULT NULL,
  `teamId` int(11) DEFAULT NULL,
  `firstTower` tinyint(1) DEFAULT NULL,
  `vilemawKills` int(11) DEFAULT NULL,
  `inhibitorKills` int(11) DEFAULT NULL,
  `towerKills` int(11) DEFAULT NULL,
  `dominionVictoryScore` int(11) DEFAULT NULL,
  `dragonKills` int(11) DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `delta` tinyint(4) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=14889 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `xpDiffPerMinDeltas`
--

CREATE TABLE IF NOT EXISTS `xpDiffPerMinDeltas` (
`id` bigint(20) NOT NULL,
  `timeline_id` int(11) DEFAULT NULL,
  `zeroToTen` float DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `tenToTwenty` float DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=74434 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `xpPerMinDeltas`
--

CREATE TABLE IF NOT EXISTS `xpPerMinDeltas` (
`id` bigint(20) NOT NULL,
  `timeline_id` int(11) DEFAULT NULL,
  `zeroToTen` float DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  `tenToTwenty` float DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=74434 DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bans`
--
ALTER TABLE `bans`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `creepsPerMinDeltas`
--
ALTER TABLE `creepsPerMinDeltas`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `csDiffPerMinDeltas`
--
ALTER TABLE `csDiffPerMinDeltas`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `damageTakenDiffPerMinDeltas`
--
ALTER TABLE `damageTakenDiffPerMinDeltas`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `damageTakenPerMinDeltas`
--
ALTER TABLE `damageTakenPerMinDeltas`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `goldPerMinDeltas`
--
ALTER TABLE `goldPerMinDeltas`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `masteries`
--
ALTER TABLE `masteries`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `match`
--
ALTER TABLE `match`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `match_old`
--
ALTER TABLE `match_old`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `match_timeline`
--
ALTER TABLE `match_timeline`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `match_timeline_frames`
--
ALTER TABLE `match_timeline_frames`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `participant`
--
ALTER TABLE `participant`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `participant_timeline`
--
ALTER TABLE `participant_timeline`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `position`
--
ALTER TABLE `position`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `runes`
--
ALTER TABLE `runes`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stats`
--
ALTER TABLE `stats`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `team`
--
ALTER TABLE `team`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `xpDiffPerMinDeltas`
--
ALTER TABLE `xpDiffPerMinDeltas`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `xpPerMinDeltas`
--
ALTER TABLE `xpPerMinDeltas`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bans`
--
ALTER TABLE `bans`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=44340;
--
-- AUTO_INCREMENT for table `creepsPerMinDeltas`
--
ALTER TABLE `creepsPerMinDeltas`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=74434;
--
-- AUTO_INCREMENT for table `csDiffPerMinDeltas`
--
ALTER TABLE `csDiffPerMinDeltas`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=74434;
--
-- AUTO_INCREMENT for table `damageTakenDiffPerMinDeltas`
--
ALTER TABLE `damageTakenDiffPerMinDeltas`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=74434;
--
-- AUTO_INCREMENT for table `damageTakenPerMinDeltas`
--
ALTER TABLE `damageTakenPerMinDeltas`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=74434;
--
-- AUTO_INCREMENT for table `goldPerMinDeltas`
--
ALTER TABLE `goldPerMinDeltas`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=74434;
--
-- AUTO_INCREMENT for table `masteries`
--
ALTER TABLE `masteries`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1127806;
--
-- AUTO_INCREMENT for table `match`
--
ALTER TABLE `match`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=7442;
--
-- AUTO_INCREMENT for table `match_old`
--
ALTER TABLE `match_old`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=7268;
--
-- AUTO_INCREMENT for table `match_timeline`
--
ALTER TABLE `match_timeline`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=227839;
--
-- AUTO_INCREMENT for table `match_timeline_frames`
--
ALTER TABLE `match_timeline_frames`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2278381;
--
-- AUTO_INCREMENT for table `participant`
--
ALTER TABLE `participant`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=74434;
--
-- AUTO_INCREMENT for table `participant_timeline`
--
ALTER TABLE `participant_timeline`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=74434;
--
-- AUTO_INCREMENT for table `position`
--
ALTER TABLE `position`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2278381;
--
-- AUTO_INCREMENT for table `runes`
--
ALTER TABLE `runes`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=370075;
--
-- AUTO_INCREMENT for table `stats`
--
ALTER TABLE `stats`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=74434;
--
-- AUTO_INCREMENT for table `team`
--
ALTER TABLE `team`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=14889;
--
-- AUTO_INCREMENT for table `xpDiffPerMinDeltas`
--
ALTER TABLE `xpDiffPerMinDeltas`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=74434;
--
-- AUTO_INCREMENT for table `xpPerMinDeltas`
--
ALTER TABLE `xpPerMinDeltas`
MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=74434;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
