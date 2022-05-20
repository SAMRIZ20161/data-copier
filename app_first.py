def main():
    import pandas as pd
    print('rizwan')
    fp='/home/riz/retail_db_json/order_items/part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e'
    df=pd.read_json(fp,lines=True)
    print(f'The total records are {df.count()}')
    print(f'the shape is {df.shape}')
if __name__=="__main__":
    main()