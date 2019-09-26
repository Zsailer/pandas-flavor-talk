from pandas_flavor import register_dataframe_accessor


@register_dataframe_accessor('zach')
class MyFlavorAccessor:
    
    def __init__(self, df):
        self._df = df

    def func1(self):
        # The original DataFrame is availabe through self._df
        print("Hello, everyone!\n")
        return self._df

    def func2(self):
        print("Check out my flavor of Pandas")
        return self._df