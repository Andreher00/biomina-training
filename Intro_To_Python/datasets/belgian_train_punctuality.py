import pandas as pd
import numpy as np
import tqdm.auto as tqdm
base_url = "https://fr.ftp.opendatasoft.com/infrabel/PunctualityHistory/Data_raw_punctuality_"
year = 2025

urls = [f"{base_url}{year}{month:02d}.csv" for month in range(1, 13)]

def statistic(url):
    df = pd.read_csv(url)
    return df[["DELAY_ARR", "DATDEP"]].groupby("DATDEP").mean().to_numpy().flatten()

stats = [statistic(url) for url in tqdm.tqdm(urls)]

stats_per_day_in_minutes = np.concatenate(stats) / 60
assert len(stats_per_day_in_minutes) == 365
np.savetxt("belgian_train_punctuality.txt", stats_per_day_in_minutes)