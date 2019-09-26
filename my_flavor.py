from pandas_flavor import register_dataframe_method


@register_dataframe_method
def zach_func1(df):
    print("Hello, everyone!\n")
    return df


@register_dataframe_method
def zach_func2(df):
    print("Check out my flavor of Pandas")
    return df