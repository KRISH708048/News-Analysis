from gnews import GNews
import datetime
import pandas as pd
import json
import csv
google_news = GNews(country='IN', language='en')
# nl = google_news.get_news_by_site("newslaundry.com")

start_date = datetime.datetime(2024, 1, 1)
end_date = datetime.datetime(2024, 1, 15)

sites = ['newslaundry.com', 'theprint.in', 'opindia.com', 'republicworld.com', 'indianexpress.com']

for site in sites:      # creates emply file
    file_path = './initial/' + site.replace('www.', '').replace('.in', '').replace('.com', '') + '.csv'
    # file_path = './result/' + site + '.csv'
    open(file_path, 'w')

for site in sites:
    file_path = './initial/' + site.replace('www.', '').replace('.in', '').replace('.com', '') + '.csv'
    # file_path = './result/' + site + '.csv'
    while start_date < end_date:
        # Set the date and period
        google_news.start_date = (start_date.year, start_date.month, start_date.day)
        google_news.period = '1d'  # Period of 1 day

        # Get the news results
        results = google_news.get_news_by_site(site)
        print(results)
        df = pd.json_normalize(results)
        # df = pd.DataFrame(results)
        df.to_csv(file_path, mode='a', encoding='utf-8', index=True, header=False)

        # Increment the start date by 1 day
        start_date += datetime.timedelta(days=1)
    
    start_date = datetime.datetime(2024, 1, 1)



    # file_path = "gnews-res.json"
    # with open(file_path, 'r') as json_file:
    #     print(json_file.length)




# print (nl)
