import twint
import nest_asyncio
nest_asyncio.apply()

config = twint.Config()
config.Search = "indihome"
config.Limit = 10
config.Store_csv = True
config.Output = "indihome_7.csv"
# config.Since = '2022-03-19 00:00:00'
# config.Hide_output = True

twint.run.Search(config)
