def main():
    import pandas as pd
    print('rizwan')

    users_list = [
        {'user_first_name': 'Scott', 'user_last_name': 'Tiger'},
        {'user_first_name': 'Donald', 'user_last_name': 'Duck'}
    ]
    # query = 'select user_first_name,user_last_name from users'
    conn = 'postgresql://riz:ubuntu@localhost:5432/retail_db'
    df = pd.DataFrame(users_list)
    df.to_sql('users',conn,if_exists='append',index=False)


if __name__=="__main__":
    main()