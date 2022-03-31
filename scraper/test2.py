import twint
import nest_asyncio
nest_asyncio.apply()

#configuration
config = twint.Config()
config.Search = "indihome"
config.Limit = 200
config.Store_csv = True
config.Output = "indihome_200.csv"
#running search

twint.run.Search(config)