from selenium import webdriver
from datetime import datetime
import time
from bs4 import BeautifulSoup
import json
import pandas as pd
csv_string = ""
for key in     {
      "__type": "MapData:#MontanaWebServices",
      "AreaNum": "MT",
      "AreaType": None,
      "BallotOrder": 0,
      "CandidateID": "9002",
      "CountyID": "14",
      "CountyName": "Fergus",
      "CurrentDateTime": None,
      "IsReported": False,
      "OfficeSeqNo": "99502",
      "PartyCode": "",
      "PartyName": "",
      "PrecinctName": "PREC 2",
      "PrecinctsPartial": 0,
      "PrecinctsReporting": 663,
      "RaceID": 450002128,
      "RaceName": "LEGISLATIVE REFERENDUM NO. 131",
      "RecountPercent": 0,
      "RecountVotes": 0,
      "StatePrecinctID": 2005,
      "TotalPrecincts": 663,
      "VoteFor": 1,
      "Winner": False,
      "calcCandidate": "NO",
      "calcCandidatePercentage": 0.427860696517413,
      "calcCandidateVotes": 344
    }:
    csv_string = csv_string + key + ","
csv_string = csv_string + "\n"
url_list = [ 'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=SENATE&category=PREC&raceID=450000000001661&osn=7024&county=56&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=SENATE&category=PREC&raceID=450000000001651&osn=7002&county=15&party=0']


def county_scraper(link):
    temp_string = ""
    driver = webdriver.Chrome()
    driver.get(link)
    time.sleep(0.1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    raw_data = soup.find("pre")
    json_string = raw_data.text
    dictionary = json.loads(json_string)
    for item_dict in dictionary["d"]:
        for dictionary_key in item_dict:
            temp_string = temp_string + str(item_dict[dictionary_key]) + ","
        temp_string = temp_string + "\n"
    return temp_string


for url in url_list:
    csv_string = csv_string + county_scraper(url)
now = datetime.now()
datetime = now.strftime("%Y-%m-%d %H:%M:%S")
outfile_temp = open(f'2024StateSen{datetime}.csv', 'w')
outfile_temp.write(csv_string)
