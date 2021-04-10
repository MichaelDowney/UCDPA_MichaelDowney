# source of data set, data.csv: https://www.kaggle.com/carrie1/ecommerce-data
# Context
# Typically e-commerce datasets are proprietary and consequently hard to find among publicly available data.
# However, The UCI Machine Learning Repository has made this dataset containing actual transactions from 2010 and 2011.
# The dataset is maintained on their site, where it can be found by the title "Online Retail".
#
# Content
# "This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011
# for a UK-based and registered non-store online retail.
# The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers."
#
# Acknowledgements
# Per the UCI Machine Learning Repository, this data was made available by Dr Daqing Chen, Director:
# Public Analytics group. chend '@' lsbu.ac.uk, School of Engineering, London South Bank University, London SE1 0AA, UK.
#
# Image from stocksnap.io.

# source of data set, countrycontinent.csv: https://www.kaggle.com/statchaitya/country-to-continent?select=countryContinent.csv



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#fig,ax = plt.subplots()
#ax.plot((0,2),(5,5))
#plt.show()


sales_data = pd.read_csv("data.csv")
continent_data = pd.read_csv("countryContinent.csv")


#print(sales_data.info(), continent_data.info())
#print(sales_data.head())
#print(sales_data.shape)
#count = sales_data.isnull().sum()
#rint(count)

#type = sales_data.dtypes
#print(type)


def totalquantity():
    sum_quantity = sales_data["Quantity"].sum()
    print('{:,}'.format(sum_quantity))


def SalesTotals(group):
    sum_quantity_group = sales_data.groupby(group)['Quantity'].sum()
    #sum_quantity_group = sum_quantity_group.reset_index()
    sum_quantity_group = sum_quantity_group.sort_values(ascending=False)
    #array = np.array(sum_quantity_group)
    #sorted_array = np.sort(array)
    #reverse_array = sorted_array[::-1]
    top_five = (sum_quantity_group[0:5])
    print(sum_quantity_group)

    print(top_five)

    #print(sorted_array)
    #print(reverse_array)

   # sum_quantity_group.plot.bar()

    ypos = np.arange(len(top_five))
    plt.xticks(ypos,group)

    plt.bar(ypos,'Quantity')


    #top_five.plot.bar()

    plt.show()





SalesTotals("Country")











def display_sales_csv():
    print(sales_data.info)

#print(sales_data.head())

def shape():
    #Identifies the number of rows and columns in the data set
    print("Number of rows and columns = ")
    print(sales_data.shape)

def missing_values():
    #count the number of missing values in each column
    count_missing = sales_data.isnull().sum()
    print(count_missing)

def droprows():
   # drop rows with missing values
    droprows = sales_data.dropna()
    count_missing_droprows = droprows.isnull().sum()
    print(sales_data.shape, droprows.shape)
    print(count_missing_droprows)


def sortdata(header):
    #Sort data after dropping rows
    droprows = sales_data.dropna()
    sorted_dropped_rows = droprows.sort_values(by=[header], ascending=True)
   # print(sorted_dropped_rows.head())
   # print(droprows.shape)

def index():
    #function to sort by index
    droprows = sales_data.dropna()
    index_sort = droprows.sort_index()
    print(index_sort.head())
    print(droprows.shape)

def grouping(header):
    #function for grouping
    droprows = sales_data.dropna()
    group = droprows.groupby(header)

def Iterate():
    #Run iterrows
    for index, contents in sales_data.iterrows():
        sortdata("Country")
        grouping("CustomerID")
        print("index: {}".format(index))
        print("{} - {} - {} - {}".format(contents["StockCode"],contents["Quantity"], contents["Country"], contents["CustomerID"]))
        print()

def merge_files():
    # Merge the two datasets
    left = sales_data
    right = continent_data
    merged_data = pd.merge(left, right, on="Country", how = "inner")
    print(left.shape, right.shape)
    print(merged_data.shape)

#filenames = ["data.csv", "countryContinent.csv"]
#dataframes = []
#for f in filenames:
  #  dataframes.append(pd.read_csv(f))


def plot():
    #first plot using matplotlib
    fig,ax = plt.subplots()
    x = sales_data["InvoiceDate"].head(20)
    y1 = sales_data["Quantity"].head(20)
    ax.plot(x,y1)
    plt.show()

def highestsales():
    #highest sales
    start = sortdata("Description")
    print(start)

