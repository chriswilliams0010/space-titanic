from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
competition = 'spaceship-titanic'
datasets = ['train.csv', 'test.csv']

api.authenticate()

for i in range(len(datasets)):
	api.competition_download_file(competition, datasets[i])
