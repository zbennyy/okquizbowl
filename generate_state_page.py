# Open state.html file
fileout = open("state.html", 'w')

# Document header
fileout.write("<!DOCTYPE html>\n")
fileout.write("<html lang=en>\n")
fileout.write("\t<head>\n")
fileout.write("\t\t<meta charset=\"UTF-8\">\n")
fileout.write("\t\t<title>NAQT Oklahoma State Championship</title>\n")
fileout.write("\t\t<link rel=\"stylesheet\" href=\"style.css\">\n")
fileout.write("\t</head>")

# Page header
fileout.write("\t<body>\n")
fileout.write("\t\t<header>\n")
fileout.write("\t\t\t<h1 style=\"display:inline\">NAQT Oklahoma State Championship</h1>\n")
fileout.write("\t\t\t<div class=\"dropdown\">\n")
fileout.write("\t\t\t\t<button class=\"drop-btn\"><img src=\"menu.png\" width=\"20\" height=\"20\"></button>\n")
fileout.write("\t\t\t\t<div class=\"dropdown-content\">\n")
fileout.write("\t\t\t\t\t<a href=\"index.html\">Homepage</a>\n")
fileout.write("\t\t\t\t\t<a href=\"schedule.html\">Tournament Schedule</a>\n")
fileout.write("\t\t\t\t\t<a href=\"results.html\">Results</a>\n")
fileout.write("\t\t\t\t\t<a href=\"state.html\">State Championship</a>\n")
fileout.write("\t\t\t\t</div>\n")
fileout.write("\t\t\t</div>\n")
fileout.write("\t\t</header>\n")

# Page Body
fileout.write("\t\t<main>\n")
fileout.write("\t\t\t<h3>About the NAQT State Championship</h3>\n")
fileout.write("\t\t\t<p>The NAQT Oklahoma State Championship is an annual tournament held to determine the state champion of pyramidal quizbowl in the state of Oklahoma. Held each year in February, the tournament uses the final NAQT Invitational Series question set of the season, a set slightly more difficult than most NAQT regular-season sets.</p>\n")
fileout.write("\t\t\t<p>Beginning in the 2023-24 season, a qualification system was implemented due to the rising number of teams wishing to enter the tournament straining the limited number of available staff and the range of viable tournament formats. The preliminary field cap is 24 teams - this may be expanded at a later date.</p>\n")

fileout.write("\t\t\t<h3>Qualification</h3>\n")
fileout.write("\t\t\t<p>Teams are required to qualify to participate in the NAQT State Championship based on their performance at prior events during the season. Qualifications can be earned in one of three ways: winning a local regular-season tournament; earning enough qualification points; or submitting an accepted wild card bid. Because the NAQT State Championship is intended to serve as the championship for all of pyramidal quizbowl, all regular-season tournaments which use pyramidal questions in the standard tossup-bonus format will be counted toward qualification, even if those tournaments do not specifically use an NAQT question set.</p>\n")

fileout.write("\t\t\t<ul>\n")
fileout.write("\t\t\t\t<li><p><b>Tier 1: Winning a Tournament</b></p>\n")
fileout.write("\t\t\t\t<p>Any team that wins a local, regular-season tournament using pyramidal tossup-bonus questions will be awarded an automatic qualification to the NAQT State Championship. This only includes tournaments held in the state of Oklahoma - winning a tournament in another state or winning an online national tournament does not count toward qualification.</p></li>\n")
fileout.write("\t\t\t\t<li><p><b>Tier 2: Qualification Points</b></p>\n")
fileout.write("\t\t\t\t<p>All teams that participate in qualifying events will be awarded points based on the percentile of their finishing position. For example, in a field of 20 teams the winning team will be awarded 100 points (and an automatic qualification), the second place team will receive 95 points, the third place team will receive 90 points, and so on. The number of points a team receives at a given tournament can be computed from the formula, 100 * (1 - <sup>p-1</sup>&frasl;<sub>n</sub>) where <i>p</i> is the team's finishing position and <i>n</i> is the number of teams at the event.</p></li>\n")
fileout.write("\t\t\t\t<li><p><b>Tier 3: Wildcard Bids</b></p>\n")
fileout.write("\t\t\t\t<p>Any team that is unable to qualify through one of the above methods may submit an application for a wildcard bid. Teams will be required to submit their prospective roster for the state championship, as well as links to stats which show why their application should be accepted. The application for the 2025 State Championship will be opened near the end of the first semester of the competition year.</p>\n")
fileout.write("\t\t\t\t<p>Acceptable justifications for a wildcard bid include: </p>\n")
fileout.write("\t\t\t\t<ul>\n")
fileout.write("\t\t\t\t\t<li>Your team was not able to attend sufficient tournaments due to scheduling conflicts, but performed well at the tournaments they did attend</li>\n")
fileout.write("\t\t\t\t\t<li>Your team was not able to compete with its best roster at most tournaments, but would reasonably be expected to perform at a higher level with the proposed roster for state</li>\n")
fileout.write("\t\t\t\t\t<li>Your team performed well enough at a non-qualifying tournament (such as an out-of-state or online tournament) that you believe it to warrant an automatic qualification</li>\n")
fileout.write("\t\t\t\t</ul></li>\n")
fileout.write("\t\t\t</ul>\n")
fileout.write("\t\t\t<h3>Current Qualification Standings</h3>\n")
fileout.write("\t\t\t<p>Green indicates Tier 1 qualification, Blue indicates Tier 2 qualification</p>")

standings_file = open("2025 NAQT State Standings.csv", 'r')

# Variables for Tracking Points Qualifications
num_total_tournaments = 8

# Begin Table
fileout.write("\t\t\t<table id=\"state_standings\">\n")
fileout.write("\t\t\t\t<tr>\n")

# Add Header Row of Table
header_row = standings_file.readline().split(',')
fileout.write("\t\t\t\t\t<th class=\"rank_col\">" + str(header_row[0]).strip('\n') + "</th>\n")
fileout.write("\t\t\t\t\t<th class=\"name_col\">" + str(header_row[1]).strip('\n') + "</th>\n")
x = 2
while x != len(header_row) - 1:
    fileout.write("\t\t\t\t\t<th class=\"tourn_col\">" + str(header_row[x]).strip('\n') + "</th>\n")
    x += 1
fileout.write("\t\t\t\t\t<th class=\"total_col\">" + str(header_row[-1]).strip('\n') + "</th>\n")
fileout.write("\t\t\t\t</tr>\n")

# Account for Rank, Team, and Total Columns
team_row = standings_file.readline().split(',')
while len(team_row) > 1:
    tier = 0
    rank = team_row[0]
    name = team_row[1]
    total = team_row[-1]
    for item in team_row:
        if item == str(100):
            tier = 1
    if (tier == 0 and int(team_row[-1]) >= 250): 
        tier = 2
    fileout.write("\t\t\t\t<tr class=\"tier_" + str(tier) + "\">\n")
    fileout.write("\t\t\t\t\t<td><b>" + str(rank) + "</b></td>\n")
    fileout.write("\t\t\t\t\t<td><b>" + str(name) + "</b></td>\n")

    i = 2
    while i != num_total_tournaments + 2:
        if i > len(team_row):
            fileout.write("\t\t\t\t\t<td></td>\n")
        else:
            if str(team_row[i]) == str(100):
                fileout.write("\t\t\t\t\t<td><b>" + str(team_row[i]) + "</b></td>\n")
            else:
                fileout.write("\t\t\t\t\t<td>" + str(team_row[i]) + "</td>\n")
        i += 1
    fileout.write("\t\t\t\t\t<td><b>" + str(team_row[-1]).strip('\n') + "</b></td>\n")
    fileout.write("\t\t\t\t</tr>\n")

    team_row = standings_file.readline().split(',')

# Close table, page body, and document
fileout.write("\t\t\t</table>\n")
fileout.write("\t\t</main>\n")
fileout.write("\t</body>\n")
fileout.write("</html>\n")
