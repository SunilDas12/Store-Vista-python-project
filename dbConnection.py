import pyrebase
import pandas as pd
 
#https://firebase.google.com/docs/web/setup#available-libraries
 
def retriveData():  
  firebaseConfig = {
    "apiKey": "AIzaSyDKYGw-MTMAAdFdFNprEMMRDystI84BvcA",
    "authDomain": "sales-a39e2.firebaseapp.com",
    "databaseURL": "https://sales-a39e2-default-rtdb.firebaseio.com",
    "projectId": "sales-a39e2",
    "storageBucket": "sales-a39e2.appspot.com",
    "messagingSenderId": "478820009418",
    "appId": "1:478820009418:web:ee4c5c0fbf23681d373b33",
    "measurementId": "G-CB8Q07VG15"
  }
  firebase=pyrebase.initialize_app(firebaseConfig)
  db=firebase.database()
  data=db.child("1xDNcARfYi3Ajnj3PGnwnUgGKavlNFl7wEPTG53PiuRk").child("Sheet1").get()
  data_list = []
  for dt in data.each():
        val = dt.val()
        if isinstance(val, dict):
          data_list.append(val)
      #data_list.append(dt.val())

  df = pd.DataFrame(data_list)

  if 'Order Date' in df.columns:
    try:
        # Convert to datetime and strip time component
        df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%y', errors='coerce')
        print("Converted 'Order Date' to the desired format.")
    except Exception as e:
        print(f"Error converting 'Order Date' to datetime: {e}")
  else:
      print("The 'Order Date' column is missing from the DataFrame.")

  df = df.convert_dtypes()


    #print("DataFrame after converting types:\n", df.dtypes)

# Optionally, save the DataFrame to a CSV to inspect the data manually
  df.to_csv('output.csv', index=False)
  return df

df=retriveData()

# # Print the columns to check if 'Order Date' exists
# print("DataFrame Columns:", df.columns)

# # Print data types of the DataFrame
# print("DataFrame Data Types:\n", df.dtypes)

# # Print a sample of the DataFrame to see the data
# print("DataFrame Sample:\n", df.head())

# # Convert 'Order Date' to datetime if it exists
# if 'Order Date' in df.columns:
#     try:
#         df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
#         print("Converted 'Order Date' to datetime.")
#     except Exception as e:
#         print(f"Error converting 'Order Date' to datetime: {e}")
# else:
#     print("The 'Order Date' column is missing from the DataFrame.")

# Ensure all columns are of appropriate types for serialization
# df = df.convert_dtypes()
# print("DataFrame after converting types:\n", df.dtypes)

# # Optionally, save the DataFrame to a CSV to inspect the data manually
# df.to_csv('output.csv', index=False)

# # Display the DataFrame
# print("Final DataFrame:\n", df)
 



 
 