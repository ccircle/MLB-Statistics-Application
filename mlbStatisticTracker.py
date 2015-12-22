#!/usr/bin/env python
#-----------------------------------------------------------------------------------------------------------------------
# myMLBStatTracker.py
# Cody Circle
# CS230 9:00AM
# 12/07/2015
#-----------------------------------------------------------------------------------------------------------------------
import sys
import csv
import sqlite3 as sqlite
#-----------------------------------------------------------------------------------------------------------------------

def viewPlayerStats(dbCursor):

    """Presents the user a menu that allows them to choose to view individual hitting and pitching
    stats by providing the player they want to find more about (eg Joey Votto). Also allows the user
    to choose to view hitting and pitching stats by providing a team name (eg Cincinnati Reds)."""

    while(True):
        print()
        print("1 Search individual player hitting statistics")
        print("2 Search individual player pitching statistics")
        print("3 Search individual hitting statistics for a specific team")
        print("4 Search individual pitching statistics for a specific team")
        print("5 Go to main menu")
        print()

        try:
            mainOption = eval(input("Enter your choice: "))
            optionList = [1, 2, 3, 4, 5]
            # user entered a number that is not an option, don't allow
            if mainOption not in optionList:
                print("\nInvalid input, try again.\n")
            #-----------------------------------------------------------------------------------------------------------
            # user wants to return to the main menu
            elif mainOption == 5:
                return
            #-----------------------------------------------------------------------------------------------------------
            # view individual player hitting statistics
            elif mainOption == 1:
                try:
                    # enter player's first and last name spelled correctly
                    playerHittingName = input("Enter player's name: ")
                    # select the corresponding stats for the desired player and display them
                    dbCursor.execute('select playerHittingID, playerName, playerMLBTeam, gamesPlayed, ab, runs, hits, doubles, triples, homeruns, rbi, sb, bb, so, ba, obp, slg, ops from playersHitting where playerName=?;', (playerHittingName,))
                    for playerHittingID, playerName, playerMLBTeam, gamesPlayed, ab, runs, hits, doubles, triples, homeruns, rbi, sb, bb, so, ba, obp, slg, ops in dbCursor:
                        printHittingData(playerName, playerMLBTeam, gamesPlayed, ab, runs, hits, doubles, triples, homeruns, rbi, sb, bb, so, ba, obp, slg, ops)

                    input("Click enter to continue...")

                except SyntaxError:
                    print("\nThis player's statistics were not found, try again.\n")
            #-----------------------------------------------------------------------------------------------------------
            # view individual player pitching statistics
            elif mainOption == 2:
                try:
                    # enter player's first and last name spelled correctly
                    playerPitchingName = input("Enter player's name: ")
                    # select the corresponding stats for the desired player and display them
                    dbCursor.execute('select playerPitchingID,playerName,playerMLBTeam,wins,losses,winLossPercent,era,gamesPlayed,gamesStarted,cg,shutouts,saves,ip,walks,strikeouts,whip from playersPitching where playerName=?;', (playerPitchingName,))
                    for playerPitchingID,playerName,playerMLBTeam,wins,losses,winLossPercent,era,gamesPlayed,gamesStarted,cg,shutouts,saves,ip,walks,strikeouts,whip in dbCursor:
                        printPitchingData(playerName, playerMLBTeam, wins, losses, winLossPercent, era, gamesPlayed, gamesStarted, cg, shutouts, saves, ip, walks, strikeouts, whip)

                    input("Click enter to continue...")

                except SyntaxError:
                    print("\nThis player's statistics were not found, try again.\n")
            #-----------------------------------------------------------------------------------------------------------
            # view an entire team's hitting statistics player by player
            elif mainOption == 3:
                try:
                    # enter full team name spelled correctly
                    teamName = input("Enter a team's name: ")
                    # select the corresponding stats for the desired team for all players on that team
                    dbCursor.execute('select playerHittingID, playerName, playerMLBTeam, gamesPlayed, ab, runs, hits, doubles, triples, homeruns, rbi, sb, bb, so, ba, obp, slg, ops from playersHitting where playerMLBTeam=(select teamID from mlbTeams where teamName=?);', (teamName,))
                    for playerHittingID, playerName, playerMLBTeam, gamesPlayed, ab, runs, hits, doubles, triples, homeruns, rbi, sb, bb, so, ba, obp, slg, ops in dbCursor:
                        printHittingData(playerName, playerMLBTeam, gamesPlayed, ab, runs, hits, doubles, triples, homeruns, rbi, sb, bb, so, ba, obp, slg, ops)

                    input("Click enter to continue...")

                except SyntaxError:
                    print("\nThis player's statistics were not found, try again.\n")
            #-----------------------------------------------------------------------------------------------------------
            # view an entire team's pitching statistics player by player
            elif mainOption == 4:
                try:
                    # enter full team name spelled correctly
                    teamName = input("Enter a team's name: ")
                    # select the corresponding stats for the desired team for all players on that team
                    dbCursor.execute('select playerPitchingID,playerName,playerMLBTeam,wins,losses,winLossPercent,era,gamesPlayed,gamesStarted,cg,shutouts,saves,ip,walks,strikeouts,whip from playersPitching where playerMLBTeam=(select teamID from mlbTeams where teamName=?);', (teamName,))
                    for playerPitchingID,playerName,playerMLBTeam,wins,losses,winLossPercent,era,gamesPlayed,gamesStarted,cg,shutouts,saves,ip,walks,strikeouts,whip in dbCursor:
                        printPitchingData(playerName, playerMLBTeam, wins, losses, winLossPercent, era, gamesPlayed, gamesStarted, cg, shutouts, saves, ip, walks, strikeouts, whip)

                    input("Click enter to continue...")

                except SyntaxError:
                    print("\nThis player's statistics were not found, try again.\n")
            #-----------------------------------------------------------------------------------------------------------

        # handle other bad input by the user when they choose an option like entering a word
        except NameError:
            print("\nInvalid input, try again.\n")
        except SyntaxError:
            print("\nInvalid input, try again.\n")

#-----------------------------------------------------------------------------------------------------------------------

def printHittingData(playerName, playerMLBTeam, gamesPlayed, ab, runs, hits, doubles, triples, homeruns, rbi, sb, bb, so, ba, obp, slg, ops):

    """Prints the different hitting stats for a player line by line in the form of a key pair (stat: value)"""

    print()
    print(playerName)
    print("Team: ", playerMLBTeam)
    print("Games Played: ", gamesPlayed)
    print("At-Bats: ", ab)
    print("Runs: ", runs)
    print("Hits: ", hits)
    print("Doubles: ", doubles)
    print("Triples: ", triples)
    print("Homeruns: ", homeruns)
    print("RBI: ", rbi)
    print("Stolen Bases: ", sb)
    print("Walks: ", bb)
    print("Strikeouts: ", so)
    print("Batting Average: {0:1.3f}".format(ba))
    print("On-Base Percentage: {0:1.3f}".format(obp))
    print("Slugging Percentage: {0:1.3f}".format(slg))
    print("On-Base Plus Slugging Percentage: {0:1.3f}".format(ops))
    print()

#-----------------------------------------------------------------------------------------------------------------------

def printPitchingData(playerName, playerMLBTeam, wins, losses, winLossPercent, era, gamesPlayed, gamesStarted, cg, shutouts, saves, ip, walks, strikeouts, whip):

    """Prints the different pitching stats for a player line by line in the form of a key pair (stat: value)"""

    print()
    print(playerName)
    print("Team: ", playerMLBTeam)
    print("Wins: ", wins)
    print("Losses: ", losses)
    print("Win-Loss Percentage: {0:1.3f}".format(winLossPercent))
    print("ERA: {0:.2f}".format(era))
    print("Games Played: ", gamesPlayed)
    print("Games Started: ", gamesStarted)
    print("Complete Games: ", cg)
    print("Shutouts: ", shutouts)
    print("Saves: ", saves)
    print("Innings Pitched: {0:.2f}".format(ip))
    print("Walks: ", walks)
    print("Strikeouts: ", strikeouts)
    print("WHIP: {0:1.3f}".format(whip))
    print()

#-----------------------------------------------------------------------------------------------------------------------

def viewStatLeaders(dbCursor):

    """Presents a user with a menu that gives them options to view different hitting statistic
    leaders or different pitching statistic leaders"""

    while(True):
        print()
        print("1 View hitting statistic leaders")
        print("2 View pitching statistic leaders")
        print("3 Go to main menu")
        print()

        try:
            mainOption = eval(input("Enter your choice: "))
            optionList = [1, 2, 3]
            # user entered a number that is not an option, don't allow
            if mainOption not in optionList:
                print("\nInvalid input, try again.\n")
            #-----------------------------------------------------------------------------------------------------------
            # user chose option to return to the main menu
            elif mainOption == 3:
                return
            #-----------------------------------------------------------------------------------------------------------
            # user chose to be able to view hitting stats leaderboards
            elif mainOption == 1:
                viewHittingStatLeaders(dbCursor)
            #-----------------------------------------------------------------------------------------------------------
            # user chose to be able to view pitching stats leaderboards
            elif mainOption == 2:
                viewPitchingStatLeaders(dbCursor)
            #-----------------------------------------------------------------------------------------------------------

        # handle other bad input by user like entering a word for their option
        except NameError:
            print("\nInvalid input, try again.\n")
        except SyntaxError:
            print("\nInvalid input, try again.\n")

#-----------------------------------------------------------------------------------------------------------------------

def viewHittingStatLeaders(dbCursor):

    """Presents user with options to view 12 different hitting statistics leaderboards
    and presents them with their desired leaderboard. The leaderboards include the top
    20 players in each category"""

    while(True):
        print()
        print("Leaderboards for Hitting Statistics")
        print("1 Runs leaderboard")
        print("2 Hits leaderboard")
        print("3 Doubles leaderboard")
        print("4 Triples leaderboard")
        print("5 Homeruns leaderboard")
        print("6 RBI leaderboard")
        print("7 Stolen Bases leaderboard")
        print("8 Walks leaderboard")
        print("9 Batting Average leaderboard")
        print("10 On-Base Percentage leaderboard")
        print("11 Slugging Percentage leaderboard")
        print("12 On-Base Plus Slugging Percentage leaderboard")
        print("13 Go back to leader's menu")
        print()

        try:
            mainOption = eval(input("Enter your choice: "))
            print()

            # user choice was a number not part of list so don't allow
            optionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            if mainOption not in optionList:
                print("\nInvalid input, try again.\n")
            #-----------------------------------------------------------------------------------------------
            # user chose option 13 which will return them to the leaderboards main menu
            elif mainOption == 13:
                return
            #-----------------------------------------------------------------------------------------------

            # for each of the 12 hitting stats leaderboards, print the player's order, name and stat for the top 20
            # DESC order to get highest results first since leaders are wanted
            # make user hit enter before continuing

            elif mainOption == 1:
                dbCursor.execute('select playerName, runs from playersHitting order by runs DESC limit 20;')
                order = 1
                print("{:5} {:25} {:8}".format('Order', 'Name', 'Runs'))
                for playerName, runs in dbCursor:
                    print("{:5} {:25} {:3}".format(order, playerName, runs))
                    order += 1
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 2:
                dbCursor.execute('select playerName, hits from playersHitting order by hits DESC limit 20;')
                order = 1
                print("{:5} {:25} {:8}".format('Order', 'Name', 'Hits'))
                for playerName, hits in dbCursor:
                    print("{:5} {:25} {:3}".format(order, playerName, hits))
                    order += 1
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 3:
                dbCursor.execute('select playerName, doubles from playersHitting order by doubles DESC limit 20;')
                order = 1
                print("{:5} {:25} {:8}".format('Order', 'Name', 'Doubles'))
                for playerName, doubles in dbCursor:
                    print("{:5} {:25} {:2}".format(order, playerName, doubles))
                    order += 1
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 4:
                dbCursor.execute('select playerName, triples from playersHitting order by triples DESC limit 20;')
                order = 1
                print("{:5} {:25} {:8}".format('Order', 'Name', 'Triples'))
                for playerName, triples in dbCursor:
                    print("{:5} {:25} {:2}".format(order, playerName, triples))
                    order += 1
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 5:
                dbCursor.execute('select playerName, homeruns from playersHitting order by homeruns DESC limit 20;')
                order = 1
                print("{:5} {:25} {:8}".format('Order', 'Name', 'Homeruns'))
                for playerName, homeruns in dbCursor:
                    print("{:5} {:25} {:2}".format(order, playerName, homeruns))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 6:
                dbCursor.execute('select playerName, rbi from playersHitting order by rbi DESC limit 20;')
                order = 1
                print("{:5} {:25} {:8}".format('Order', 'Name', 'RBIs'))
                for playerName, rbi in dbCursor:
                    print("{:5} {:25} {:2}".format(order, playerName, rbi))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 7:
                dbCursor.execute('select playerName, sb from playersHitting order by sb DESC limit 20;')
                order = 1
                print("{:5} {:25} {:12}".format('Order', 'Name', 'Stolen Bases'))
                for playerName, sb in dbCursor:
                    print("{:5} {:25} {:2}".format(order, playerName, sb))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 8:
                dbCursor.execute('select playerName, bb from playersHitting order by bb DESC limit 20;')
                order = 1
                print("{:5} {:25} {:5}".format('Order', 'Name', 'Walks'))
                for playerName, bb in dbCursor:
                    print("{:5} {:25} {:2}".format(order, playerName, bb))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 9:
                # player must have over 502 at-bats to qualify as a leader
                dbCursor.execute('select playerName, ba from playersHitting where ab >= 502 order by ba DESC limit 20;')
                order = 1
                print("{:5} {:25} {:15}".format('Order', 'Name', 'Batting Average'))
                for playerName, ba in dbCursor:
                    print("{:5} {:25} {:.3f}".format(order, playerName, ba))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 10:
                # player must have over 502 at-bats to qualify as a leader
                dbCursor.execute('select playerName, obp from playersHitting where ab >= 502 order by obp DESC limit 20;')
                order = 1
                print("{:5} {:25} {:18}".format('Order', 'Name', 'On-Base Percentage'))
                for playerName, obp in dbCursor:
                    print("{:5} {:25} {:.3f}".format(order, playerName, obp))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 11:
                # player must have over 502 at-bats to qualify as a leader
                dbCursor.execute('select playerName, slg from playersHitting where ab >= 502 order by slg DESC limit 20;')
                order = 1
                print("{:5} {:25} {:19}".format('Order', 'Name', 'Slugging Percentage'))
                for playerName, slg in dbCursor:
                    print("{:5} {:25} {:.3f}".format(order, playerName, slg))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 12:
                # player must have over 502 at-bats to qualify as a leader
                dbCursor.execute('select playerName, ops from playersHitting where ab >= 502 order by ops DESC limit 20;')
                order = 1
                print("{:5} {:25} {:32}".format('Order', 'Name', 'On-Base Plus Slugging Percentage'))
                for playerName, ops in dbCursor:
                    print("{:5} {:25} {:.3f}".format(order, playerName, ops))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------

        # catch other bad input by the user to make them retry
        except SyntaxError:
            print("\nInvalid input, try again.\n")

#-----------------------------------------------------------------------------------------------------------------------

def viewPitchingStatLeaders(dbCursor):

    """Presents user with options to view 11 different pitching statistics leaderboards
    and presents them with their desired leaderboard. The leaderboards include the top
    20 players in each category"""

    while(True):
        print()
        print("Leaderboards for Pitching Statistics")
        print("1 Wins leaderboard")
        print("2 Win-Loss Percentage leaderboard")
        print("3 ERA leaderboard")
        print("4 Games Started leaderboard")
        print("5 Complete Games leaderboard")
        print("6 Shutouts leaderboard")
        print("7 Saves leaderboard")
        print("8 Innings-Pitched leaderboard")
        print("9 Walks leaderboard")
        print("10 Strikeouts leaderboard")
        print("11 Walks-Hits per Innings Pitched (WHIP) leaderboard")
        print("12 Go back to leader's menu")
        print()

        try:
            mainOption = eval(input("Enter your choice: "))
            print()

            # user chose a number that is not an option, don't allow
            optionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            if mainOption not in optionList:
                print("\nInvalid input, try again.\n")
            #-----------------------------------------------------------------------------------------------
            # user chooses to go back to the leaderboards main menu
            elif mainOption == 12:
                return
            #-----------------------------------------------------------------------------------------------

            # for each of the 11 pitching stats leaderboards, print the player's order, name and stat for the top 20
            # DESC order to get highest results first since leaders are wanted
            # make user hit enter before continuing

            elif mainOption == 1:
                dbCursor.execute('select playerName, wins from playersPitching order by wins DESC limit 20;')
                order = 1
                print("{:5} {:25} {:8}".format('Order', 'Name', 'Wins'))
                for playerName, wins in dbCursor:
                    print("{:5} {:25} {:3}".format(order, playerName, wins))
                    order += 1
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            # pitcher must have over 150 innings pitched to qualify
            elif mainOption == 2:
                dbCursor.execute('select playerName, winLossPercent from playersPitching where ip > 150 order by winLossPercent DESC limit 20;')
                order = 1
                print("{:5} {:25} {:20}".format('Order', 'Name', 'Win-Loss Percentage'))
                for playerName, winLossPercent in dbCursor:
                    print("{:5} {:25} {:1.3f}".format(order, playerName, winLossPercent))
                    order += 1
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            # pitcher must have over 150 innings pitched to qualify
            # ASC order because want lowest ERA for a leader
            elif mainOption == 3:
                dbCursor.execute('select playerName, era from playersPitching where ip > 150 order by era limit 20;')
                order = 1
                print("{:5} {:25} {:3}".format('Order', 'Name', 'ERA'))
                for playerName, era in dbCursor:
                    print("{:5} {:25} {:1.3f}".format(order, playerName, era))
                    order += 1
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 4:
                dbCursor.execute('select playerName, gamesStarted from playersPitching order by gamesStarted DESC limit 20;')
                order = 1
                print("{:5} {:25} {:14}".format('Order', 'Name', 'Games Started'))
                for playerName, gamesStarted in dbCursor:
                    print("{:5} {:25} {:2}".format(order, playerName, gamesStarted))
                    order += 1
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 5:
                dbCursor.execute('select playerName, cg from playersPitching order by cg DESC limit 20;')
                order = 1
                print("{:5} {:25} {:15}".format('Order', 'Name', 'Complete Games'))
                for playerName, cg in dbCursor:
                    print("{:5} {:25} {:2}".format(order, playerName, cg))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 6:
                dbCursor.execute('select playerName, shutouts from playersPitching order by shutouts DESC limit 20;')
                order = 1
                print("{:5} {:25} {:10}".format('Order', 'Name', 'Shut Outs'))
                for playerName, shutouts in dbCursor:
                    print("{:5} {:25} {:2}".format(order, playerName, shutouts))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 7:
                dbCursor.execute('select playerName, saves from playersPitching order by saves DESC limit 20;')
                order = 1
                print("{:5} {:25} {:5}".format('Order', 'Name', 'Saves'))
                for playerName, saves in dbCursor:
                    print("{:5} {:25} {:2}".format(order, playerName, saves))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 8:
                dbCursor.execute('select playerName, ip from playersPitching order by ip DESC limit 20;')
                order = 1
                print("{:5} {:25} {:15}".format('Order', 'Name', 'Innings-Pitched'))
                for playerName, ip in dbCursor:
                    print("{:5} {:25} {:3.2f}".format(order, playerName, ip))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 9:
                dbCursor.execute('select playerName, walks from playersPitching order by walks DESC limit 20;')
                order = 1
                print("{:5} {:25} {:3}".format('Order', 'Name', 'Walks'))
                for playerName, walks in dbCursor:
                    print("{:5} {:25} {:3}".format(order, playerName, walks))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            elif mainOption == 10:
                dbCursor.execute('select playerName, strikeouts from playersPitching order by strikeouts DESC limit 20;')
                order = 1
                print("{:5} {:25} {:11}".format('Order', 'Name', 'Strikeouts'))
                for playerName, strikeouts in dbCursor:
                    print("{:5} {:25} {:3}".format(order, playerName, strikeouts))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------
            # pitcher must have over 150 innings pitched to qualify
            # ASC order because want lowest WHIP for a leader
            elif mainOption == 11:
                dbCursor.execute('select playerName, whip from playersPitching where ip > 150 order by whip limit 20;')
                order = 1
                print("{:5} {:25} {:4}".format('Order', 'Name', 'WHIP'))
                for playerName, whip in dbCursor:
                    print("{:5} {:25} {:1.3f}".format(order, playerName, whip))
                    order += 1
                print()
                input("Click enter to continue...")
            #-----------------------------------------------------------------------------------------------

        # catch other bad input by the user to make them retry
        except SyntaxError:
            print("\nInvalid input, try again.\n")

#-----------------------------------------------------------------------------------------------------------------------

def editMyTeam(username, dbConnection, dbCursor):

    """Presents a user with a menu that gives them options to add hitters or pitchers to their
    team they create or options to view the stats of the hitters/pitchers on their team"""

    while(True):
        print()
        print("1 Add a hitter to my team")
        print("2 Add a pitcher to my team")
        print("3 View hitters from my team")
        print("4 View pitchers from my team")
        print("5 Delete a hitter from my team")
        print("6 Delete a pitcher from my team")
        print("7 Go to main menu")
        print()

        try:
            mainOption = eval(input("Enter your choice: "))
            optionList = [1, 2, 3, 4, 5, 6, 7]

            # user chose a number not in the list, don't allow
            if mainOption not in optionList:
                print("\nInvalid input, try again.\n")
            #-----------------------------------------------------------------------------------------------------------
            # user chose to go back to main menu
            elif mainOption == 7:
                return
            #-----------------------------------------------------------------------------------------------------------
            # user chose to add hitters to their team
            elif mainOption == 1:
                addHitter(username, dbConnection, dbCursor)
            #-----------------------------------------------------------------------------------------------------------
            # user chose to add pitchers to their team
            elif mainOption == 2:
                addPitcher(username, dbConnection, dbCursor)
            #-----------------------------------------------------------------------------------------------------------
            # user chose to view the hitting stats of the hitters on their team
            elif mainOption == 3:
                viewMyHitters(username, dbCursor)
            #-----------------------------------------------------------------------------------------------------------
            # user chose to view the pitching stats of the pitchers on their team
            elif mainOption == 4:
                viewMyPitchers(username, dbCursor)
            #-----------------------------------------------------------------------------------------------------------
            # user chose to delete a hitter from their team
            elif mainOption == 5:
                deleteHitter(username, dbConnection, dbCursor)
            #-----------------------------------------------------------------------------------------------------------
            # user chose to delete a pitcher from their team
            elif mainOption == 6:
                deletePitcher(username, dbConnection, dbCursor)

        # catch other invalid input such as entering a word and don't allow
        except NameError:
            print("\nInvalid input, try again.\n")
        except SyntaxError:
            print("\nInvalid input, try again.\n")

#-----------------------------------------------------------------------------------------------------------------------

def addHitter(username, dbConnection, dbCursor):

    """User enters the name of a hitter they wish to add to their team, and this players ID
    is added along with the username to the myTeamHitters table"""

    try:
        # user enters a valid player's name spelled correctly
        playerHittingName = input("Enter player's name to add to your team of hitters: ")
        # find this player's ID
        dbCursor.execute('select playerHittingID from playersHitting where playerName=?;', (playerHittingName,))

        for playerHittingID in dbCursor:
            playerAddedID = playerHittingID[0]

        # add the username and the found player's ID to myTeamHitters table
        dbCursor.execute('insert into myTeamHitters (userID, playerHittingID) values (?,?);', (username, playerAddedID))

        # commit results to the database
        dbConnection.commit()

        print()
        print(playerHittingName,"was added to user", username, "'s team successfully!")

    except SyntaxError:
        print("\nInvalid input, try again.\n")

#-----------------------------------------------------------------------------------------------------------------------

def deleteHitter(username, dbConnection, dbCursor):

    """User enters the name of a hitter they wish to delete from their team, and this players ID
    is deleted along with the username from the myTeamHitters table"""

    try:
        # user enters a valid player's name spelled correctly
        playerHittingName = input("Enter player's name to delete from your team of hitters: ")
        # find this player's ID
        dbCursor.execute('select playerHittingID from playersHitting where playerName=?;', (playerHittingName,))

        for playerHittingID in dbCursor:
            playerAddedID = playerHittingID[0]

        # delete the username and the found player's ID from myTeamHitters table
        dbCursor.execute('delete from myTeamHitters where userID=? and playerHittingID=?;', (username, playerAddedID))

        # commit results to the database
        dbConnection.commit()

        print()
        print(playerHittingName,"was deleted from user", username, "'s team successfully!")

    except SyntaxError:
        print("\nInvalid input, try again.\n")

#-----------------------------------------------------------------------------------------------------------------------

def addPitcher(username, dbConnection, dbCursor):

    """User enters the name of a pitcher they wish to add to their team, and this players ID
    is added along with the username to the myTeamPitchers table"""

    try:
        # user enters a valid player's name spelled correctly
        playerPitchingName = input("Enter player's name to add to your team of pitchers: ")
        # find this player's ID
        dbCursor.execute('select playerPitchingID from playersPitching where playerName=?;', (playerPitchingName,))

        for playerPitchingID in dbCursor:
            playerAddedID = playerPitchingID[0]

        # add the username and the found player's ID to myTeamPitchers table
        dbCursor.execute('insert into myTeamPitchers (userID, playerPitchingID) values (?,?);', (username, playerAddedID))

        # commit results to the database
        dbConnection.commit()

        print()
        print(playerPitchingName,"was added to user", username, "'s team successfully!")

    except SyntaxError:
        print("\nInvalid input, try again.\n")

#-----------------------------------------------------------------------------------------------------------------------

def deletePitcher(username, dbConnection, dbCursor):

    """User enters the name of a pitcher they wish to delete from their team, and this players ID
    is deleted along with the username from the myTeamPitchers table"""

    try:
        # user enters a valid player's name spelled correctly
        playerPitchingName = input("Enter player's name to delete from your team of pitchers: ")
        # find this player's ID
        dbCursor.execute('select playerPitchingID from playersPitching where playerName=?;', (playerPitchingName,))

        for playerPitchingID in dbCursor:
            playerAddedID = playerPitchingID[0]

        # delete the username and the found player's ID to myTeamPitchers table
        dbCursor.execute('delete from myTeamPitchers where userID=? and playerPitchingID=?;', (username, playerAddedID))

        # commit results to the database
        dbConnection.commit()

        print()
        print(playerPitchingName,"was deleted from user", username, "'s team successfully!")

    except SyntaxError:
        print("\nInvalid input, try again.\n")

#-----------------------------------------------------------------------------------------------------------------------

def viewMyHitters(username, dbCursor):

    """Prints the hitting player's stats and names that belong to the team owned by username"""

    try:
        print()
        print(username,"'s Team of Hitters")

        # natural join playersHitting and myTeamHitters to extract the stats for each hitter on username's team
        dbCursor.execute('select playerHittingID, playerName, playerMLBTeam, gamesPlayed, ab, runs, hits, doubles, triples, homeruns, rbi, sb, bb, so, ba, obp, slg, ops from playersHitting natural join myTeamHitters where userID=?;', (username,))
        for playerHittingID, playerName, playerMLBTeam, gamesPlayed, ab, runs, hits, doubles, triples, homeruns, rbi, sb, bb, so, ba, obp, slg, ops in dbCursor:
            printHittingData(playerName, playerMLBTeam, gamesPlayed, ab, runs, hits, doubles, triples, homeruns, rbi, sb, bb, so, ba, obp, slg, ops)

        input("Click enter to continue...")

    except SyntaxError:
        print("\nInvalid input, try again.\n")

#-----------------------------------------------------------------------------------------------------------------------

def viewMyPitchers(username, dbCursor):

    """Prints the pitching player's stats and names that belong to the team owned by username"""

    try:
        print()
        print(username,"'s Team of Pitchers")

        # natural join playersPitching and myTeamPitchers to extract the stats for each pitcher on username's team
        dbCursor.execute('select playerPitchingID, playerName, playerMLBTeam, wins, losses, winLossPercent, era, gamesPlayed, gamesStarted, cg, shutouts, saves, ip, walks, strikeouts, whip from playersPitching natural join myTeamPitchers where userID=?;', (username,))
        for playerPitchingID, playerName, playerMLBTeam, wins, losses, winLossPercent, era, gamesPlayed, gamesStarted, cg, shutouts, saves, ip, walks, strikeouts, whip in dbCursor:
            printPitchingData(playerName, playerMLBTeam, wins, losses, winLossPercent, era, gamesPlayed, gamesStarted, cg, shutouts, saves, ip, walks, strikeouts, whip)

        input("Click enter to continue...")

    except SyntaxError:
        print("\nInvalid input, try again.\n")

#-----------------------------------------------------------------------------------------------------------------------

def editMyUsername(username, dbConnection, dbCursor):

    """Updates the user's username to a newly provided one and makes the change to both
    the myTeamHitters and the myTeamPitchers tables"""

    try:
        print()
        newUsername = input("What would you like to change your username to? ")

        # update the myPlayersHitting and myPlayersPitching tables with the new username
        dbCursor.execute('update myTeamHitters set userID=? where userID=?;', (newUsername, username,))
        dbCursor.execute('update myTeamPitchers set userID=? where userID=?;', (newUsername, username,))

        dbConnection.commit()

        return newUsername

    except SyntaxError:
        print("\nInvalid input, try again.\n")

#-----------------------------------------------------------------------------------------------------------------------

def main():

    print("Welcome to the 2015 MLB MyTeam Stat Tracker!\n")

    # connect to the myMLBStatTracker database and set up the cursor that will be passed to each function
    dbConnection = sqlite.connect("myMLBStatTracker.db")
    dbCursor = dbConnection.cursor()

    # immediately get the username of the user (new or returning) to be used for creating/viewing their team
    username = input("Enter a username for your team: ")

    while(True):
        # display the main menu to the user
        print()
        print("Main Menu:")
        print("1 View player statistics and team totals")
        print("2 View statistical leaderboards")
        print("3 Build or view", username, "'s team")
        print("4 Update my current username")
        print("5 Exit")
        print()

        try:
            mainOption = eval(input("Enter your choice: "))
            optionList = [1, 2, 3, 4, 5]

            # user chose a number that is not part of the list, don't allow
            if mainOption not in optionList:
                print("\nInvalid input, try again.\n")

            # user wishes to exit the program
            elif mainOption == 5:
                # close the database cursor and connection and break from the loop
                dbCursor.close()
                dbConnection.close()
                break

            # user wants to find hitting/pitching stats for players
            elif mainOption == 1:
                viewPlayerStats(dbCursor)

            # user wants to view hitting and pitching leaderboards for the 2015 MLB season
            elif mainOption == 2:
                viewStatLeaders(dbCursor)

            # user wants to create/view the player's on their team; connection must be passed in order to commit
            elif mainOption == 3:
                editMyTeam(username, dbConnection, dbCursor)

            # user wants to update their username
            elif mainOption == 4:
                newUsername = editMyUsername(username, dbConnection, dbCursor)
                # set username to the newly entered username so it appears when printed out
                username = newUsername

        # check for other bad input such as a word and don't allow
        except NameError:
            print("\nInvalid input, try again.\n")
        except SyntaxError:
            print("\nInvalid input, try again.\n")

#-----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
