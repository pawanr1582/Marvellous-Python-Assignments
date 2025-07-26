import pandas as pd
import Dataframemodule

def main():

    df = Dataframemodule.getDataFrame()
    
    df.rename(columns = {"Math" : "Mathamatics"}, inplace = True)
    
    print(df)

if __name__ == "__main__":
    main()