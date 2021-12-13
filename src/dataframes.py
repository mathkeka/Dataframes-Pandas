from loading_data import LoadingData


class DataFrameUsages:
    def __init__(self, dataframe=None) -> None:
        self.dataframe = dataframe

    def get_column(self, column):
        """Return selected column values"""
        return self.dataframe[column]

    def filter_column(self, column, value, greater_than=None, equal=None):
        """Return a new dataframe with selected filtering"""

        numbers = [int, float, complex]
        df = None

        def equal(self, column, value):
            return self.dataframe[self.dataframe[column] == value]

        if type(value) in numbers:
            if greater_than:
                df = self.dataframe[self.dataframe[column] > value]
            elif not greater_than and not equal:
                df = self.dataframe[self.dataframe[column] < value]
            else:
                df = equal(column, value)
        else:
            df = equal(column, value)

        return df

    def annotate_field(self, field, column_1, column_2):
        """Add a new field in the dataframe"""
        self.dataframe[field] = self.dataframe[column_1] + \
            self.dataframe[column_2]
        return self.dataframe


def beauty_print(statement, header=None):
    print("-"*40+"\n")
    if header:
        print(" "*20+f"{header}\n")
    print(statement)
    print("-"*40+"\n")


if __name__ == "__main__":
    df = LoadingData().read_csv('iris.csv')

    beauty_print(df.head(), 'Dataframe Head')
    beauty_print(df.tail(), 'Dataframe Tail')

    data_frame_usages = DataFrameUsages(df)

    beauty_print(data_frame_usages.get_column(
        'sepal length (cm)'), "Column: sepal length (cm)")

    beauty_print(data_frame_usages.annotate_field(
        'sepal + petal (length)', 'sepal length (cm)', 'petal length (cm)'))

    beauty_print(df.loc[5:15, ['sepal width (cm)','petal width (cm)']], 'Columns: sepal and petal width (cm)')
