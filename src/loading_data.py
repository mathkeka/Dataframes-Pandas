import pandas as pd
from sklearn import datasets


class LoadingData:
    def generate_csv(self, dataframe: pd.DataFrame) -> bool:
        try:
            file_name = "iris.csv"
            dataframe.to_csv(file_name, sep='\t', encoding='utf-8')
            return True
        except Exception as e:
            print(e)

    def generate_iris_csv(self):
        try:
            ds = datasets.load_iris()
            df = pd.DataFrame(ds.data, columns=ds.feature_names)

            done = self.generate_csv(df)

            if done:
                print("iris.csv successfully generated!")
            else:
                raise Exception("Something went wrong...")
        except Exception as e:
            print(e)

    def read_csv(self, file_name):
        try:
            return pd.read_csv(file_name)
        except Exception as e:
            print(e)

    def print_dataframe(self, dataframe):
        print(dataframe)


if __name__ == "__main__":
    LoadingData().generate_iris_csv()
