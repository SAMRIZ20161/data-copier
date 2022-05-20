def main():
    import pandas as pd
    print('rizwan')
    # GET BASE DIRECTORY AND TABLE NAME
    BASE_DIR = '/home/riz/retail_db_json'
    TABLE_NAME = 'orders'

    # GET FILE NAMES
    import os

    FILE_NAME = os.listdir(f'{BASE_DIR}/{TABLE_NAME}')[0]

    #CONCATENATE ALL TO GET FILE PATH
    fp = f'{BASE_DIR}/{TABLE_NAME}/{FILE_NAME}'

    #CREATE A JSON READER USING CHUNKSIZE
    json_reader = pd.read_json(fp, lines=True, chunksize=1000)


    #CREATE A CONNNECTION TO TARGET POSTGRES DATABASE
    conn = 'postgresql://riz:ubuntu@localhost:5432/retail_db'

    # EACH CHUNK IS LOADED AS A DATAFRAME, SO YOU CAN PERFORM MIN MAX ETC ON DATAFRAME AND LOAD
    for df in json_reader:
        min_key = df['order_id'].min()
        max_key = df['order_id'].max()

        df.to_sql(TABLE_NAME,conn,if_exists='append',index=False)
        print(f'Processed {TABLE_NAME} with in the range of {min_key} and {max_key}')


if __name__=="__main__":
    main()