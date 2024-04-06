import pandas as pd
import os
import yaml

def prepare(path):
    cols_for_target = ['DATE','MonthlyMinimumTemperature','MonthlyDepartureFromNormalAverageTemperature','MonthlyMeanTemperature','MonthlyMaximumTemperature']
    os.mkdir("/home/clifford/clifford/clifflearns/insti/CS5830/a04/Ground_truth")
    save_dir = "/home/clifford/clifford/clifflearns/insti/CS5830/a04/Ground_truth/"
    csv_files=[]
    for file in os.listdir(path):
        if file.endswith('.csv'):
            csv_files.append(file)

    for file in csv_files:
        full_path = os.path.join(path,file)
        data = pd.read_csv(full_path)
        data = data.assign(DATE=data['DATE'].str[5:7])[cols_for_target]
        data = data.set_index('DATE')
        target_data = data.dropna()
        if(len(target_data)<10):
            print("Inadequate data so deleting the file.")
            os.remove(full_path)
        else:
            target_data.to_csv(os.path.join(save_dir,f'{file[:-4]}_GT.csv'))

if __name__ =="__main__":
    params = yaml.safe_load(open("params.yaml"))["prepare"]
    data_path = params["path"]
    prepare(data_path)


            