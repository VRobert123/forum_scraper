import pandas as pd
from bs4 import BeautifulSoup
import requests

class Scrapper:

    def __init__(self, link):

        self.link = link

        print('Scrapper successfully loaded with link.')


    def get_prohardver_data(self, csv_name='untitled.csv'):

        self.csv_name = csv_name

        self.df = pd.DataFrame()
        self.df['text'] = 0
        self.df['date'] = 0

        self.i = 1
        self.j = 50

        self.olddate = 0

        while True:

                self.newlink = self.link.replace('1-50', f'{self.i}-{self.j}')

                self.i += 50
                self.j += 50

                self.r = requests.get(self.newlink)

                self.soup = BeautifulSoup(self.r.content, 'html.parser')

                self.text = self.soup.find_all("div", {"class": "msg-content"})
                self.date = self.soup.find_all("span", {"class": "msg-time"})

                if self.olddate == self.date[0]:
                    print(f'Scrapping has ended. Dataframe was saved to the home library as {self.csv_name}.')
                    print(self.df)
                    self.df.to_csv(self.csv_name, sep=';')
                    break

                print(f'New link was created: {self.newlink}')

                for k in range(0, len(self.text)):
                    print(f'Comment {k} was downloaded')
                    self.df.loc[len(self.df.index)] = [self.text[k].text, self.date[k].text]

                self.olddate = self.date[0]


    def get_index_data(self, csv_name='untitled.csv'):

        self.csv_name = csv_name

        self.df = pd.DataFrame()
        self.df['text'] = 0
        self.df['date'] = 0

        self.i = 0

        while True:

            self.newlink = self.link.replace('0', f'{self.i}', 1)

            self.i += 30

            print(f'New link created {self.newlink}')

            self.r = requests.get(self.newlink)

            self.soup = BeautifulSoup(self.r.content, 'html.parser')

            self.text = self.soup.find_all("tr", {"class": "art_b"})
            self.date = self.soup.find_all("tr", {"class": "art_h"})

            if self.text == []:
                print('Scraping was successfully ended')
                print(self.df)
                self.df.to_csv(self.csv_name, sep=';')
                break


            for k in range(0, len(self.text)):
                print(f'Comment {k} was downloaded')
                self.df.loc[len(self.df.index)] = [self.text[k].text, self.date[k].text]


    def get_portfolio_data(self, csv_name='untitled.csv'):

        self.csv_name = csv_name

        self.df = pd.DataFrame()
        self.df['text'] = 0
        self.df['date'] = 0

        self.i = 1

        self.olddate = 0

        while True:

            self.newlink = self.link[:-1] + f'{self.i}'

            self.i += 1

            print(f'New link created {self.newlink}')

            self.r = requests.get(self.newlink)

            self.soup = BeautifulSoup(self.r.content, 'html.parser')

            self.text = self.soup.find_all("div", {"class": "text"})
            self.date = self.soup.find_all("span", {"class": "date pl-3"})

            if self.olddate == self.date[0]:
                print('Scraping was successfully ended')
                print(self.df)
                self.df.to_csv(self.csv_name, sep=';')
                break

            for k in range(0, len(self.text)):
                print(f'Comment {k} was downloaded')
                self.df.loc[len(self.df.index)] = [self.text[k].text, self.date[k].text]

            self.olddate = self.date[0]






