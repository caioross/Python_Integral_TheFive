from requests import get
from bs4 import BeautifulSoup
from warnings import warn
from time import sleep
from random import randint
import numpy as np, pandas as pd
import seaborn as sns

pages = np.arange(1, 5, 50)
headers = {'Accept-Language': 'pt-BR, pt;q=0.8'}
titles = []
years = []
genres = []
runtimes = []
imdb_ratings = []
imdb_ratings_standardized = []
votes = []
page = 1

for page in pages:
  response = get("https://www.imdb.com/search/title?genres=sci-fi&" + "start=" + str(page) + "&explore=title_type,genres&ref_=adv_prv", headers=headers)
  sleep(randint(8,15))
  if response.status_code !=200:
    warn('Muito erradinho: {}; Statu code: {}' .format(requests, response.status_code))
  page_html = BeautifulSoup(response.text, 'html.parser')

  movie_containers = page_html.find_all ('div', class_ = 'lister-item mode-advanced')
  for container in movie_containers:
    if container.find('div', class_ = 'ratings-metascore') is not None:
      title = container.h3.a.text
      title.append(title)

      if container.h3.find('span', class_= 'lister-item-year text-muted unbold') is not None:
        year = container.h3.find('span', class_= 'lister-item-year text-muted unbold').text
        years.append(year)

      else:
        years.append(None)
      if container.p.find('span', class_ = 'certificate') is not None:
        rating = container.p.find('span', class_= 'certifcate').text
        ratings.append(rating)

      else:
        ratings.append("")

      if container.p.find('span', class_= 'genre') is not None:
        genre = container.p.find ('span', class_ = 'genre').text.replace('\n', "").rstrip().split(',')
        genres.append(genre)

      else:
          genres.append("")

      if container.p.find('span', class_= 'runtime') is not None:
        time = int(container.p.find ('span', class_ = 'runtime').text.replace(" min",""))
        runtimes.append(time)

      else:
        runtimes.append(None)

      if container.strong.text is not None:
        imdb = float(container.strong.text.replace(",","."))
        imdb_ratings.append(imdb)

      else:
        imdb_ratings.append(None)

      if container.find('span', attrs = {'name':'nv'})['data-value'] is not None:
        vote = int(container.find('span', attrs = {'name':'nv'})['data value'])
        votes.append(vote)

      else:
        votes.append(None)
        
        sci_fi_df = pd.DataFrame({'Filme': titles,
                          'ano': years,
                          'genero': genres,
                          'tempo': runtimes,
                          'imdb': imdb_ratings,
                          'votos': votes}
                          )
sci_fi_df.loc[:, 'ano'] = sci_fi_df['ano'].str[-5:-1]
sci_fi_df['nota_imdb'] = sci_fi_df['imdb'] * 10
final_df = sci_fi_df.loc[sci_fi_df['ano'] !='Movie']
final_df.loc[:, 'ano'] = pd.to_numeric(final_df['ano'])
