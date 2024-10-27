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
url_list = [ 'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001766&osn=8091&county=45&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001766&osn=8091&county=45&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001695&osn=8020&county=07&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001766&osn=8091&county=32&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001766&osn=8091&county=24&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001764&osn=8089&county=32&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001755&osn=8080&county=25&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001737&osn=8062&county=16&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001735&osn=8060&county=16&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001735&osn=8060&county=28&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001733&osn=8058&county=34&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001732&osn=8057&county=34&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001732&osn=8057&county=16&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001679&osn=8004&county=15&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001678&osn=8003&county=15&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001717&osn=8042&county=02&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001717&osn=8042&county=56&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001723&osn=8048&county=56&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001722&osn=8047&county=56&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001720&osn=8045&county=56&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001721&osn=8046&county=56&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001702&osn=8027&county=21&party=0',
'https://esersws.mt.gov/ResultsAjax.svc/GetMapData?type=HOUSE&category=PREC&raceID=450000000001694&osn=8019&county=07&party=0']

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
outfile_temp = open(f'2024StateHouse{datetime}.csv', 'w')
outfile_temp.write(csv_string)