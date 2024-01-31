import sys
import requests
from pymongo import MongoClient
from crud import insert, update

conn = MongoClient('mongodb://localhost:27017')
db = conn.gupy
coll = db.vagas

def jobRequest(jobName, badges, publishedDate, offset, limit):
    url = f'https://portal.api.gupy.io/api/job?name={jobName}&badges={badges}&isRemoteWork=true&publishedDate={publishedDate}&offset={offset}&limit={limit}'
    return requests.request("GET", url).json()

def setData(dc, ri={}):
    dc['_id'] = dc['id']
    del dc['id']
    ri['_id'] = dc['_id']
    return dc, ri

def closingSession():
    print("Concluído")

def main(offset=0, jobName='rpa'):
    publishedDate = '2024-01-01'
    badges = 'Brasil'
    limit = 10

    dados = {}
    dados = jobRequest(jobName, badges, publishedDate, offset, limit)

    for jobs in dados['data']:
        jobs,jobId = setData(jobs)
        insertResult = insert(coll, jobs)
        if insertResult == 1:
            update(coll, jobs, jobId)

if __name__ == '__main__':
    param = len(sys.argv)
    try:
        for page in range(int(sys.argv[-1])):
            main(page," ".join(sys.argv[1:param -1]))
        closingSession()
    except ValueError:
        main(0," ".join(sys.argv[1:]))
        closingSession()
