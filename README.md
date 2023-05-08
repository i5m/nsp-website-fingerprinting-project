# nsp-website-fingerprinting-project

# NSP Website Fingerprinting Attack Analysis

The dataset is available at: [https://myuva-my.sharepoint.com/:f:/g/personal/efk7cz_virginia_edu/Er2YC7JRnClDmr3cz7h5nygBV_-BvT_rvt9Gji6Pkz2HAw?e=8zcp66](https://myuva-my.sharepoint.com/:f:/g/personal/efk7cz_virginia_edu/Er2YC7JRnClDmr3cz7h5nygBV_-BvT_rvt9Gji6Pkz2HAw?e=8zcp66)

### Collection
Execute the **pcaps/bulk.sh** file. It'll run torsocks and tcpdump in parellel to visit the websites and capture all the network packets

### Training and Testing
There are two Python Notebook that you can run.
1. **RF_kNN.ipynb**: To train and test the data on Random Forest and k-Nearest-Neighbours.
2. **kFP.ipynb**: To train and test the data on k-fingerprinting technique.

There are multiple important variables which you can change in notebooks, such as:
```
[ENUM] config_file - "config - monitored.json", "config - unmonitored.json"
[ENUM] data_folder - "data", "data_eduroam"
[INT] num_features - 1-45
[FLOAT] test_size = 0-1 ratio of train vs test from dataset
```

### Feature Plot
Use the **graph.py** python file to create a 3D visual plot of all the features.
