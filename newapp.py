import os


def main():
     import os
     DB_NAME = os.getenv('DB_NAME')
     print(f'the database is {DB_NAME}')

if __name__ == "__main__":
     main()