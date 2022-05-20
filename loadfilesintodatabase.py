def main():
    import pandas as pd
    print('rizwan')
    # GET BASE DIRECTORY AND TABLE NAME
    BASE_DIR = '/home/riz/retail_db_json'
    TABLE_NAME = 'departments'

    # GET FILE NAMES
    import os

    FILE_NAME = os.listdir(f'{BASE_DIR}/{TABLE_NAME}')[0]

    #CONCATENATE ALL TO GET FILE PATH
    fp = f'{BASE_DIR}/{TABLE_NAME}/{FILE_NAME}'

    #CREATE A DATAFRAME
    df = pd.read_json(fp, lines=True)


    #CREATE A CONNNECTION TO TARGET POSTGRES DATABASE
    conn = 'postgresql://riz:ubuntu@localhost:5432/retail_db'

    df.to_sql(TABLE_NAME,conn,if_exists='append',index=False)


if __name__=="__main__":
    main()