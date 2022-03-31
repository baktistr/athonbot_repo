import datetime
import twint

twint.output.clean_lists()

until = datetime.datetime(2022, 3, 19, 17, 0, 1)
since = datetime.datetime(2022, 3, 18, 16, 59, 59)

for i in range(0, 30, 1):

    date_print = until.strftime('%Y-%m-%d')
    until_str = str(until)
    since_str = str(since)
    file_out = "output2/indihome-" + str(date_print) + ".csv"

    config = twint.Config()
    config.Search = "indihome"
    # config.Limit = 100
    config.Store_csv = True
    config.Output = file_out
    config.Hide_output = True
    config.Count = True
    config.Stats = True
    # config.Since = "2022-03-18 16:59:59"
    # config.Until = "2022-03-19 17:00:01"
    config.Since = since_str
    config.Until = until_str

    twint.run.Search(config)

    until -= datetime.timedelta(days=1)
    since -= datetime.timedelta(days=1)
