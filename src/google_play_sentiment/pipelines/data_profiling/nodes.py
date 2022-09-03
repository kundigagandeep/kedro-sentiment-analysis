import pandas as pd
import webbrowser
from pathlib import Path
import pathlib
from pandas_profiling import ProfileReport

def generating_report(df: pd.DataFrame):
    
    profile = ProfileReport(df, title="Pandas Profiling Report")

    profile.to_file("C:/Users/gagan/Python Projects/kedro/kedro-sentiment-analysis/data/08_reporting/first_report.html")

    url = pathlib.Path(Path.cwd()/"data/08_reporting/first_report.html").as_posix()

    return webbrowser.open(url, new=2)
