def calMean(df, clmn):
    if clmn not in df.columns:
        raise ValueError("ValueError. Input column not in input DataFrame.")
    try:
        return df[clmn].mean()
    except Exception as e:
        raise ValueError("ValueError. Check if input column is of datatype int or float.") from e
    

def calMedian(df, clmn):
    if clmn not in df.columns:
        raise ValueError("ValueError. Input column not in input DataFrame.")
    try:
        return df[clmn].median()
    except Exception as e:
        raise ValueError("ValueError. Check if input column is of datatype int or float.") from e

def countItemOcc(df, clmn, example):
    if clmn not in df.columns:
        raise ValueError("ValueError. Input column not in input DataFrame.")
    return df[df[clmn]==example].shape[0]

def calItemRate(df, clmn, example):
    if clmn not in df.columns:
        raise ValueError("ValueError. Input column not in input DataFrame.")
    return (df[df[clmn]==example].shape[0])/(df.dropna(subset=[clmn]).shape[0])

def printNumClmnStats(df, clmn):
    clmnMean = round(calMean(df, clmn), 2)
    clmnMedian = round(calMedian(df, clmn), 2)
    print('The mean is {}. The median is {}.'.format(str(clmnMean),str(clmnMedian)))
    return None
          
def printCatClmnStats(df, clmn, example):
    ItemOcc = countItemOcc(df, clmn, example)
    ItemOccPercent = calItemRate(df, clmn, example)
    print('The number of occurance is {}, or {}% of total samples.'.format(ItemOcc,str(round(ItemOccPercent, 2))))
    return None