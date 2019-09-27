import urllib2
from bs4 import BeautifulSoup
import bs4,time
import string
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import requests
from lxml import html


def player_info():
    '''
    This function web scrapes basketball-reference and extracts player's info.
    '''
    players = []
    base_url = 'http://www.basketball-reference.com/players/'

    # get player tables from alphabetical list pages
    for letter in string.lowercase:
        page_request = requests.get(base_url + letter)
        soup = BeautifulSoup(page_request.text,"lxml")
        # find table in soup
        table = soup.find('table')

        if table:
            table_body = table.find('tbody')

            # loop over list of players
            for row in table_body.findAll('tr'):

                # get name and url
                player_url = row.find('a')
                player_names = player_url.text
                player_pages = player_url['href']

                # get some player's info from table
                cells = row.findAll('td')
                active_from = int(cells[0].text)
                active_to = int(cells[1].text)
                position = cells[2].text
                height = cells[3].text
                weight = cells[4].text
                birth_date = cells[5].text
                college = cells[6].text    

                # create entry
                player_entry = {'url': player_pages,
                                'name': player_names,
                                'active_from': active_from,
                                'active_to': active_to,
                                'position': position,
                                'college': college,
                                'height': height,
                                'weight': weight,
                                'birth_date': birth_date}

                # append player dictionary
                players.append(player_entry)
                
    return pd.DataFrame(players)

## how to deal with did not play seasons (MJ)
## injured players

treeDict = {'all_per_game':[3,3,1,1,6,'odd'], 
            'all_per_minute':[13,5,"str",0,1,0,1,1,6,'all'],
            "all_per_poss":[19,5,"str",0,1,0,1,1,6,'all'],
            "all_advanced":[21,5,"str",0,1,0,1,1,6,'all'],
            "all_playoffs_per_game":[29,5,"str",0,1,0,1,1,6,'all'],
            "all_playoffs_per_minute":[33,5,"str",0,1,0,1,1,6,'all'],
            "all_playoffs_per_poss":[35,5,"str",0,1,0,1,1,6,'all'],
            "all_playoffs_advanced":[37,5,"str",0,1,0,1,1,6,'all']}

def traverseTree(obj,tr):
    if len(tr)==1:
        return obj,tr[0]
    elif type(tr[0])==str:
        converted = str(obj).replace('\n','').replace('\t','')
        return traverseTree(BeautifulSoup(converted,"html5lib"),tr[1:])
    else:
        return traverseTree(obj.contents[tr[0]],tr[1:])
    
def extractTableData(table,playerData,k,tableType):
    if len(table.contents)>1:
        if tableType=='odd':
            odds = range(1,len(table.contents),2)
            rows = []
            for o in odds:
                tableRow = table.contents[o]
                row = {}
                for i,c in enumerate(tableRow.contents):
                    try:
                        if len(c.contents)>0:
                            row[c['data-stat']] = c.contents[0]
                            ## must add stripping out contents by type
                    except:
                        continue
                rows.append(row)
            playerData[k] = rows
        elif tableType=='all':
            rows = []
            for j in range(len(table.contents))[:-1]:
                row = {}
                for i,c in enumerate(table.contents[j]):
                    try:
                        if len(c.contents)>0:
                            row[c['data-stat']] = c.contents[0]
                    except:
                        continue
                rows.append(row)
            playerData[k] = rows
    else: # deal with strings with only one year of playing time?...
        row = {}
        

def extractData(ppg):
    relevantSets = [3,13,19,21,29,33,35,37,]
    relevantSets = [r for r in relevantSets if type(ppg.body.div.contents[13].contents[r])!=bs4.element.Comment]
    playerData = {}
    #print [ppg.body.div.contents[13].contents[k]['id'] for k in relevantSets]
    for r in relevantSets:
        key = ppg.body.div.contents[13].contents[r]['id']
        if key in treeDict:
            dataTable,tableType = traverseTree(ppg.body.div.contents[13],treeDict[key])
            extractTableData(dataTable,playerData,key,tableType)
    return playerData