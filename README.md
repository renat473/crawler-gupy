# crawler-gupy


![image](https://user-images.githubusercontent.com/1757167/217853912-a4caf9a0-a12a-49a9-9d76-c8d335483314.png)

## Objetivos

Extrair vagas de emprego atráves da API Gupy e persistir os dados para projeto de data science.
Registrar os dados em banco de dados NoSQL (MongoDB)


## Requisitos

* Python [3.x](https://www.python.org/downloads/) ou mais recente.
* MongoDB [6.0.3](https://www.mongodb.com/try/download/community).

## Requisitos

* requests              (https://pypi.org/project/requests/)
* pymongo               (https://pypi.org/project/pymongo/)

##### Exemplo de request vagas (parâmetros)

* name (titulo da vaga)
* badges (país de origem das vagas)
* isRemoteWork (true = vaga remota)
* publishedDate (data da publicação da vaga)
* limit (quantidade de vagas a ser listadas)

```python
import requests

url = "https://portal.api.gupy.io/api/job?name=sre&badges=Brasil&isRemoteWork=true&publishedDate=%222023-01-13%22&offset=0&limit=300"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

##### Resposta Http Request
```json
{
"data": [
        {
            "id": 4060745,
            "companyId": 12841,
            "name": "Engenheiro SRE ",
            "description": "Conquistamos mais uma vez a certificação das melhores empresas para se trabalhar no Paraná em 2021, e além disso, marcamos presença também entre as 10 Insurtech/startups que mais se destacam no setor de seguros",
            "careerPageId": 30799,
            "careerPageName": "Empresa Segfy",
            "careerPageLogo": "https://s3.amazonaws.com/gupy5/production/companies/12841/career/30799/images/2021-10-06_13-35_logo.png",
            "type": "vacancy_type_effective",
            "publishedDate": "2023-02-07T18:44:44.452Z",
            "applicationDeadline": null,
            "isRemoteWork": true,
            "city": "São José dos Pinhais",
            "state": "Paraná",
            "country": "Brasil",
            "jobUrl": "https://segfy.gupy.io/job/eyJqb2JJZCI6NDA2MDc0NSwic291cmNlIjoiZ3VweV9wb3J0YWwifQ==?jobBoardSource=gupy_portal",
            "badges": {
                "friendlyBadge": false
            },
            "careerPageUrl": "https://segfy.gupy.io/eyJzb3VyY2UiOiJndXB5X3BvcnRhbCJ9"
        }
]
}
```
