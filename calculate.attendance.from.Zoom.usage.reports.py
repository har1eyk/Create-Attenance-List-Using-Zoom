import pandas as pd
import datetime
from os import listdir
from os.path import isfile, join

# folder in which .csv attendance files can be found
# relative
directory = "Test_Data/"
# windows
# directory = "C:/Users/harley/Dropbox/Fall2020_BSCI414/Attendance/Test_Data/"
# mac
#directory = '/Users/harleyk/Dropbox/Fall2020_BSCI414/Attendance/Test_Data/'

all_csv_files =[]
all_files = listdir(directory)
for csv in all_files:
    if csv.endswith('.csv'):
        all_csv_files.append(csv)
    else:
        pass
# # finds all csv files in folder (works on windows, not on mac)
# all_csv_files = [f for f in listdir(directory) if isfile(join(directory, f).endswith(".csv"))]
print (all_csv_files)
print ("Pulling Data from:", len(all_csv_files), " attendance files.")

# create empty df
df = pd.DataFrame(columns=['Name','Email'])
# record = '20200915_lecture_participants_94758381041.csv'
# df_temp = pd.read_csv(directory+record, skiprows=2, engine='python', encoding='utf-8')
# df_temp = df_temp[['Name (Original Name)', 'User Email', 'Duration (Minutes)']]
# display (df_temp)

# loop through all attendance records in directory; append to df
for record in all_csv_files:
    # skip header and first 2 rows. 
    df_temp = pd.read_csv(directory+record, skiprows=2, engine='python', encoding='utf-8')
    # sometimes more than 3 columns; sometimes 'total' omitted
    if (len(df_temp.columns) ==3):
        df_temp = df_temp[['Name (Original Name)', 'User Email', 'Total Duration (Minutes)']]
    else:
        df_temp = df_temp[['Name (Original Name)', 'User Email', 'Duration (Minutes)']]
    # need to get date as it becomes col name
    dfdate = pd.read_csv(directory+record, skiprows=1, nrows=0, engine='python', encoding='utf-8')
    dfdate_cols = dfdate.columns
    col_date= (dfdate_cols[2]) # e.g. 09/04/2020 12:30:59 PM
    mtg_date = datetime.datetime.strptime(col_date, '%m/%d/%Y %H:%M:%S %p')
    # print('Date:', mtg_date.date())
    # rename columns
    df_temp.columns=['Name', 'Email', mtg_date.date()]
    # print (mtg_date.date())
    # display (df_temp)
    # df = df.merge(df_temp.drop(columns=['Email']), how='outer', on='Name', sort=True)
    df = df.merge(df_temp, how='outer', on=['Name', 'Email'], sort=True)
# print (df)

# need to reorder columns by date; have to remove "Name" and "Email" to sort by date
my_headers = df.columns.tolist() # makes list
sorted_headers = sorted(my_headers[2::]) # slices list, removing "Name", "Email"
# print (sorted_headers)
# add back in "Name and Email"
sorted_headers.insert(0, 'Name') # adds to sorted list
sorted_headers.insert(1, 'Email')

df_sort = df.reindex(columns=sorted_headers)
print (df_sort)

# fill NaN to be NR, "no record"
df_sort.fillna('NR', inplace=True)
# output df to txt file
file_out = "Class.attendance.up.to."+str(sorted_headers[-1])+".txt"
df_sort.to_csv(directory+file_out, sep='\t')