import pandas as pd

DATA_DEV = './data/snli_1.0_dev.txt'
DATA_TEST = './data/snli_1.0_test.txt'
DATA_TRAIN = './data/snli_1.0_train.txt'


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path, sep='\t')


def data_preprocessing(data: pd.DataFrame) -> pd.DataFrame:
    data = data.copy()
    data = data[['gold_label', 'sentence1', 'sentence2']]
    data = data[data['gold_label'] != '-']
    data.dropna(inplace=True)

    return data


def main():
    data_raw_dev = load_data(DATA_DEV)
    data_raw_test = load_data(DATA_TEST)
    data_raw_train = load_data(DATA_TRAIN)

    data_dev = data_preprocessing(data_raw_dev)
    data_test = data_preprocessing(data_raw_test)
    data_train = data_preprocessing(data_raw_train)

if __name__ == "__main__":
    main()
