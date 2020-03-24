from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def scrap():
    url = 'https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("pre").find(text=True)
    x = table.split(";")
    context = {'whole_amount': x[4], 'death_amount': x[5], 'dolnoslaskie': x[7], 'dolnoslaskie_d': x[8],
               'kujawsko': x[10], 'kujawsko_d': x[11], 'lubelskie': x[13], 'lubelskie_d': x[14],
               'lubuskie': x[16], 'lubuskie_d': x[17], 'lodzkie': x[19], 'lodzkie_d': x[20],
               'malopolskie': x[22], 'malopolskie_d': x[23], 'mazowieckie': x[25], 'mazowieckie_d': x[26],
               'opolskie': x[28], 'opolskie_d': x[29], 'podkarpackie': x[31], 'podkarpackie_d': x[32],
               'podlaskie': x[34], 'podlaskie_d': x[35], 'pomorskie': x[37], 'pomorskie_d': x[38],
               'slaskie': x[40], 'slaskie_d': x[41], 'swietokrzyskie': x[43], 'swietokrzyskie_d': x[44],
               'warminsko_mazurskie': x[46], 'warminsko_mazurskie_d': x[47], 'wielkopolskie': x[49],
               'wielkopolskie_d': x[50], 'zachodniopomorskie': x[52], 'zachodniopomorskie_d': x[53]
    }
    return context


def corona(request):
    return render(request, 'corona/index.html', scrap())


def details(request):
    return render(request, 'corona/detail.html', scrap())
