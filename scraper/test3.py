import twint
import datetime

today = datetime.datetime.now().strftime('%Y-%m-%d')
yesterday = (datetime.datetime.now() -
             datetime.timedelta(days=1)).strftime('%Y-%m-%d')

# configuration
config = twint.Config()
config.Search = "indihome"
# config.Limit = 1000
config.Store_csv = True
config.Output = "indhome_tweet6.csv"
config.Hide_output = True
config.Count = True
config.Stats = True
config.Since = '2020-03-01 10:00:00'
config.Until = '2022-03-10 10:00:00'
# config.Resume = 'resume2.txt'
# config.Year = 2021
# running search

twint.run.Search(config)
