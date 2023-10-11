from .models import Item
import ast
import pandas as pd
import io
import requests
def upload_csv():
    df=pd.read_csv("MobInsight/description/phones.csv")
    for idx,row in df.iterrows():
        name = row['Phone Name']
        image1 = str(row['Image Link 1'])
        image2 = str(row['Image Link 2'])
        price = int(row['Price'])
        comment = row['Expert Comment']
        performance = row['Performance']
        display = row['Display']
        camera = row['Camera']
        battery = row['Battery']
        Item.objects.create(
            name = name,
            comment = comment,
            price = price,
            performance = performance,
            display =display,
            camera = camera,
            battery = battery,
            image1 = "https://"+image1,
            image2 = "https://"+image2
        )
    print("Done Uploading...")
        