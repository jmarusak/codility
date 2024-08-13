import pandas as pd

def merge():
    df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3']})
    df2 = pd.DataFrame({'A': ['A0', 'B1', 'B2', 'B3']})

    df = pd.merge(df1, df2, on='A', how='inner') 
    print(df)


if __name__ == '__main__':
    merge() 