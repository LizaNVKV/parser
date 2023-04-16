from icrawler.builtin import GoogleImageCrawler

path = GoogleImageCrawler(storage={'root_dir': 'C:/Users/Lisa/Desktop/parser'})

print('Сколько фото?')
quabtity = int(input())

print('Ваш запрос?')
name = str(input())

path.crawl(keyword=name, max_num=quabtity)