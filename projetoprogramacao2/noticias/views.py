from django.shortcuts import render
from bs4 import BeautifulSoup
import feedparser

def ler_projeto2():
    feed_camara = 'https://www.camara.leg.br/noticias/rss/ultimas-noticias'
    feed_ifpb = 'https://www.ifpb.edu.br/ifpb/pedrasdefogo/noticias/todas-as-noticias-do-campus-pedras-de-fogo/RSS'

    # Lê o feed RSS da câmara
    rss_camara = feedparser.parse(feed_camara)
    noticias_camara = rss_camara.entries
    noticias_camara_list = []
    for noticia in noticias_camara:
        
        html = noticia['content'][0]['value']
        soup = BeautifulSoup(html, 'html.parser')
        img_tag = soup.find('img')
        src = img_tag['src']
        alt = img_tag['alt'] if 'alt' in img_tag else ''
        descricao = "Esse rss não tem descricao"
        if 'summary_detail' in noticia:
            descricao = noticia['summary_detail']['value']
        dados_noticia = {
            'url': noticia['link'],
            'titulo': noticia['title'],
            'img_src': src,
            'img_alt': alt.upper(),
            'descricao': descricao
        }
        noticias_camara_list.append(dados_noticia)

    # Lê o outro feed RSS
    rss_ifpb = feedparser.parse(feed_ifpb)
    noticias_ifpb = rss_ifpb.entries
    noticias_ifpb_list = []
    for noticia in noticias_ifpb:
        dados_noticia = {
            'url': noticia['link'],
            'titulo': noticia['title'],
            'img_href': None,
            'img_alt': noticia['title'].upper(),
            'descricao': noticia['summary']
        }
        noticias_ifpb_list.append(dados_noticia)

    # Combine as listas de notícias em um único contexto
    context = {
        'dados': noticias_ifpb_list,
        'dados_camara': noticias_camara_list
    }
    
    return context


def projeto2(request):
    context = ler_projeto2() 

    return render(request, 'noticias/projeto2-programacao-2-matheus-e-tamires.html', context)

