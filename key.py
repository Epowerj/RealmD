import os

#you can replace the environment variable calls with normal strings
apikey = str(os.environ["TGKEY"])

table_name = str(os.environ.get("APPNAME")).replace("-", "")
