
def main():
    import pandas as pd
    print('rizwan')
    query = 'select user_first_name,user_last_name from users'
    conn = 'postgresql://riz:ubuntu@localhost:5432/retail_db'
    df = pd.read_sql(query,conn)
    print(df)
    print(f'The total records are {df.count()}')
    print(f'the shape is {df.shape[0]}')
if __name__=="__main__":
    main()