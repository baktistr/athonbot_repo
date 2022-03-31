import datetime
import twint

twint.output.clean_lists()

# for i in range(0,60,1):
#     until = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime('%Y-%m-%d')
#     since = (datetime.datetime.now() - datetime.timedelta(days=i+1)).strftime('%Y-%m-%d')
#     file_out = "output/indihome_mentions"+"_"+ str(until) +".csv"


#     print(i,". Scrapping from",since,"until",until, "==>",file_out)

# config = twint.Config()
# config.Search = "indihome"
# # config.Limit = 1000
# config.Store_csv = True
# config.Output = file_out
# config.Hide_output = True
# config.Count = True
# config.Stats = True
# config.Since = since
# config.Until = until

# twint.run.Search(config)

# date_until = datetime.datetime(2022, 3, 20, 23, 59, 59)
# date_since = datetime.datetime(2022, 3, 20, 00, 00, 00)

# for i in range(0, 60, 1):
#     date_until -= datetime.timedelta(days=1)
#     date_since -= datetime.timedelta(days=1)
#     print(date_since, date_until)
