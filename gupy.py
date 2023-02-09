import requests
import csv


publishedDate  = '2023-01-13'
badges         = 'Brasil'


url = "https://portal.api.gupy.io/api/job?name=sre&badges={badges}&isRemoteWork=true&publishedDate={publishedDate}&offset=0&limit=100"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

dados = response.json()


with open('jobs.csv', 'a+', newline='', encoding='utf-8') as csvfile:

    for jobs in dados['data']:
        try:

            id = jobs['id']
            companyId = jobs['companyId']
            name = jobs['name']
            careerPageLogo = jobs['careerPageLogo']
            careerPageName = jobs['careerPageName']
            careerPageUrl = jobs['careerPageUrl']
            city = jobs['city']
            country = jobs['country']
            isRemoteWork = jobs['isRemoteWork']
            jobUrl = jobs['jobUrl']
            publishedDate = jobs['publishedDate']
            state = jobs['state']
            
            writer = csv.writer(csvfile)
            
            writer.writerow([id,companyId,name,careerPageLogo,careerPageName,careerPageUrl,city,country,isRemoteWork,jobUrl,publishedDate,state])
        except:
            print('Error ao extrair vagas')

print ('Concluído --------------------------------')               
