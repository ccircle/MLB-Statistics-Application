#!/usr/bin/env python
#----------------------------------------------------------------------
# createMyMLBTables.py
# Cody Circle
# CS230 9:00AM
# 12/07/2015
#----------------------------------------------------------------------

import sys
import csv
import sqlite3 as sqlite

#----------------------------------------------------------------------

def createTable(dbCursor, tableName):

    """ creates the playersHitting, playersPitching, mlbTeams, myTeamHitters, and myTeamPitchers tables
    that will be used to make up the schema of my database

    :param dbCursor: database cursor
    :param tableName: table to insert into
    """

    if tableName == 'playersHitting':
        dbCursor.execute('''CREATE TABLE playersHitting
                            (playerHittingID INT PRIMARY KEY, playerName VARCHAR(50), playerMLBTeam CHAR(3), gamesPlayed INT,
                            ab INT, runs INT, hits INT, doubles INT, triples INT, homeruns INT, rbi INT, sb INT, bb INT, so INT, ba DECIMAL(4,3),
                            obp DECIMAL(4,3), slg DECIMAL(4,3), ops DECIMAL(4,3),
                            FOREIGN KEY (playerMLBTeam) REFERENCES mlbTeams(teamID));''')

    elif tableName == 'playersPitching':
        dbCursor.execute('''CREATE TABLE playersPitching
                            (playerPitchingID INT PRIMARY KEY, playerName VARCHAR(50), playerMLBTeam CHAR(3),
                            wins INT, losses INT, winLossPercent DECIMAL(4,3), era DECIMAL(4,3), gamesPlayed INT, gamesStarted INT,
                            cg INT, shutouts INT, saves INT, ip DECIMAL(4,2), walks INT, strikeouts INT, whip DECIMAL(4,3),
                            FOREIGN KEY (playerMLBTeam) REFERENCES mlbTeams(teamID));''')

    elif tableName == 'mlbTeams':
        dbCursor.execute('''CREATE TABLE mlbTeams
                            (teamID CHAR(3) PRIMARY KEY, teamName INT);''')

    elif tableName == 'myTeamHitters':
        dbCursor.execute('''CREATE TABLE myTeamHitters
                            (userID VARCHAR(50), playerHittingID INT,
                            FOREIGN KEY (playerHittingID) REFERENCES playersHitting(playerHittingID));''')

    elif tableName == 'myTeamPitchers':
        dbCursor.execute('''CREATE TABLE myTeamPitchers
                            (userID	VARCHAR(50), playerPitchingID INT,
	                        FOREIGN KEY (playerPitchingID) REFERENCES playersPitching(playerPitchingID));''')

#----------------------------------------------------------------------

def insert(dbCursor, tableName, data):

    """inserts a row into the table

    :param dbCursor: database cursor
    :param tableName: table to insert into
    :param data: list of statistics to enter into the table
    """

    newData = []
    placeHolders = []

    for value in data:
        newData.append(value)
        placeHolders.append('?')
    placeHolders = ','.join(placeHolders)

    # modify the command based on which table entering into
    if tableName == 'playersHitting':
        cmd = 'insert into {} (playerHittingID, playerName, playerMLBTeam, gamesPlayed, ab, runs, hits, doubles, triples, homeruns, rbi, sb, bb, so, ba, obp, slg, ops) values({});'.format(tableName, placeHolders)

    elif tableName == 'playersPitching':
        cmd = 'insert into {} (playerPitchingID, playerName, playerMLBTeam, wins, losses, winLossPercent, era, gamesPlayed, gamesStarted, cg, shutouts, saves, ip, walks, strikeouts, whip) values({});'.format(tableName, placeHolders)

    elif tableName == 'mlbTeams':
        cmd = 'insert into {} (teamID, teamName) values({});'.format(tableName, placeHolders)

    elif tableName == 'myTeamHitters':
        cmd = 'insert into {} (userID, playerHittingID) values({});'.format(tableName, placeHolders)

    elif tableName == 'myTeamPitchers':
        cmd = 'insert into {} (userID, playerPitchingID) values({});'.format(tableName, placeHolders)

    dbCursor.execute(cmd, newData)

#----------------------------------------------------------------------

def main(argv):

    print(argv)
    if len(argv) < 2:
        dbName = input('enter sqlite database name: ')
    else:
        dbName =  argv[1]

    if len(argv) < 3:
        fileName = input('enter CSV filename: ')
    else:
        fileName = argv[2]

    if len(argv) < 4:
        tableName = input('enter table name: ')
    else:
        tableName = argv[3]

    reader = csv.reader(open(fileName), delimiter=",", quotechar="'")
    # get the first line of CSV file
    header = next(reader)
    print(header)

    # connect to the created database given by user and create desired table
    dbConnection = sqlite.connect(dbName)
    dbCursor = dbConnection.cursor()
    createTable(dbCursor, tableName)

    # for each line in the CSV file grab the data to insert into the table
    for line in reader:
        d = []
        for data in line:
            d.append(data)
        if d != []:
            insert(dbCursor, tableName, d)


    dbConnection.commit()

    dbCursor.close()
    dbConnection.close()

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
