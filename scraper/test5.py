import datetime
import twint

twint.output.clean_lists()

until = datetime.datetime(2022, 3, 19)
since = datetime.datetime(2022, 3, 10)
date_print = until.strftime('%Y-%m-%d')
until_str = until.strftime("%Y-%m-%d")
since_str = until.strftime("%Y-%m-%d")
file_out = "indihome-" + str(date_print) + ".csv"

config = twint.Config()
config.Search = "indihome"
config.Limit = 100
config.Store_csv = True
config.Output = "indihome_8.csv"
# config.Hide_output = True
config.Count = True
config.Stats = True
# config.Since = since_str
config.Until = until_str

twint.run.Search(config)


# for i in range(0, 5, 1):
#     until -= datetime.timedelta(days=1)
#     since -= datetime.timedelta(days=1)
#     date_print = until.strftime('%Y-%m-%d')
#     file_out = "output/indihome-" + str(date_print) + ".csv"

#     print(i, "Scrapping tweet on", date_print, "==>", file_out)

#     config = twint.Config()
#     config.Search = "indihome"
#     # config.Limit = 1000
#     config.Store_csv = True
#     config.Output = file_out
#     config.Hide_output = True
#     config.Count = True
#     config.Stats = True
#     config.Since = since
#     config.Until = until

#     twint.run.Search(config)
