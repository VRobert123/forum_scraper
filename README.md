# forum_scraper v1
 
An easy software to scrap some hungarian forums. You can get the comments and the date of comments in a csv file and you can use that for text mining and other stuff. 

# These forums are included in the software:

Prohardver

Mobilarena

It Café

GamePod

Portfolio

Index Fórum


# How to use this software?

Run Scrapper_v1.py. In the GUI you have to give the link for the forum topic and you have to give a filename (with a.csv extension, for example filename.csv).

If you want to scrap Prohardver, Mobilarena, It Café, GamePod or Index, you only have to copy the link of the first page. 

For example: https://prohardver.hu/tema/jovedelem/hsz_1-50.html

Index fórum link must looks like this:

https://forum.index.hu/Article/showArticle?na_start=0&na_step=30&t=9024233&na_order=

If you want to scrap Portfolio, you have to link the last page.

For example: https://forum.portfolio.hu/topics/lakasingatlan-arak-topik/20340?oldal=1


# dependencies

pandas, requests, BeautifulSoup, tkinter, customtkinter, threading

