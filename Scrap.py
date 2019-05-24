from requests_html import HTML , HTMLSession
import numpy as np
import csv
import links_retrieval
csv_file1 = open('batsmen.csv','w')
csv_writer1 = csv.writer(csv_file1)
csv_writer1.writerow(['Player_Name','Runs','Balls_Faced','Team','Opposition_Team','Ground','Position','Period','Batting_Status'])
csv_file2 = open('bowlers.csv','w')
csv_writer2 = csv.writer(csv_file2)
csv_writer2.writerow(['Player_Name','Overs','Runs_Conceded','Wickets','Economy','Team','Opposition_Team','Ground','Period'])
links = links_retrieval.scorecard_links
for link in links:
	session = HTMLSession()
	r = session.get(link)
	print(r.html)
	toss = r.html.find('.sub-module.game-information.pre ' , first=True )
	print(toss)
	toss = toss.find('.match-detail--item')
	toss = toss[1]
	toss = toss.find('.match-detail--right',first=True).text
	toss = toss.split(',')
	print(toss)
	toss_winner = toss[0]
	print(toss_winner)
	if(toss_winner == "no toss" ):
			print("1")
			continue
	decision = toss[-1].split(' ')[3]
	print(decision)
	period_ground =  r.html.find(' .cscore_info-overview',first=True).text
	print(period_ground)
	match_ground =  period_ground.split(',')
	print(match_ground)
	match_ground = match_ground[1].split(' ')
	print(match_ground)
	match_ground = match_ground[-1]
	print(match_ground)
	print(period_ground)
	period = period_ground.split(',')
	print(period)
	period = period[-1]
	print(period)
	opp = r.html.find('div .cscore_details',first=True)
	team2 =  opp.find('.cscore_item--home',first=True)
	home_team_abbv =opp.find('.cscore_name--abbrev',first=True).text
	print(home_team_abbv)
	team2 = team2.find('.cscore_name--long',first=True)
	home_team = team2.text
	print(home_team)
	opp = opp.find('.cscore_item--away',first=True)
	opposition_team_abbv =opp.find('.cscore_name--abbrev',first=True).text
	print(opposition_team_abbv)
	opp = opp.find('.cscore_name--long',first=True)
	opposition_team = opp.text
	print(opposition_team)
	print(toss_winner)
	print(home_team)
	toss_winner = toss_winner.rstrip()
	set1 = toss_winner.split(' ')
	set2 = home_team.split(' ')
	print(set1)
	print(set2)
	if(set1 == set2):
    		if(decision=="field"):
        			team1 = opposition_team_abbv
        			team2 = home_team_abbv
        			print(1)
    		if(decision=="bat"):
        			team2 = opposition_team_abbv
        			team1 = home_team_abbv
        			print(2)

	else:
    		if(decision=="field"):
        			team2 = opposition_team_abbv
        			team1 = home_team_abbv
        			print(3)
    		if(decision=="bat"):
            		team1 = opposition_team_abbv
            		team2 = home_team_abbv
            		print(4)
	print()
	print(team1)
	print(team2)
	
	players = r.html.find('.sub-module.scorecard')
	i=0
	j=1
	for player in players:
            player = player.find('.scorecard-section.batsmen  ',first=True)
            if player is None:
                        		continue
            wraps = player.find('.wrap.batsmen  ')

    
            for wrap in wraps:
                    cells = wrap.find('.cell')
                    status = cells[1].text
                    print(status)
                    if(status == 'absent hurt'):
                    		print("1")
                    		continue
                    if(status == "not out"):
                    		batting_status = status
                    else:
                    		batting_status= "out"
                    batsman_name = cells[0].text
                    position=j
                    print(position)
                    j= j+1
                    print(batsman_name)
                    runs = cells[2].text
                    balls_faced = cells[3].text
                    if(i==0):
                            team=team1
                            opposition_team=team2
                    else:
                            team=team2
                            opposition_team=team1
        	
                    print(runs)
                    print(balls_faced)
                    print(team)
                    print(opposition_team)
        
                    print()
                    csv_writer1.writerow([batsman_name,runs,balls_faced,team,opposition_team,match_ground,position,period,batting_status])
            i=+1
            j=1
	
	
	players = r.html.find('.sub-module.scorecard')
	i=0

	for player in players:
            player = player.find('.scorecard-section.bowling  ',first=True)
            if player is None:
            					continue
            datas = player.find('tbody',first=True)
            datas = datas.find('tr')

            for data in datas:
                    data = data.find('td')
                    if(i==0):
                            team=team2
                            opposition_team=team1
                    else:
                            team=team1
                            opposition_team=team2
            
                    bowler_name=data[0].text
                    overs = data[2].text
                    runs_conceded = data[4].text
                    wickets = data[5].text
                    economy = data[6].text
                    csv_writer2.writerow([bowler_name,overs,runs_conceded,wickets,economy,team,opposition_team,match_ground,period])
                    print(bowler_name)
                    print(overs)
                    print(runs_conceded)
                    print(wickets)
                    print(economy)
                    print(team)
                    print(opposition_team)
                    print()
            i = +1
	

csv_file1.close()
csv_file2.close()





