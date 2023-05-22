import pandas as pd
import graphs


def read_data_from_file(filename):
    df = pd.read_csv(filename, header=2)
    
    # transpose
    df_year = df.set_index('Country Name').T
    # clean up column headers
    df_year.columns.name = ''
    # transpose
    df_country = df_year.T
    df_country.columns.name = 'Country Name'
    # clean up
    df_year.fillna('', inplace=True)
    df_country.fillna('', inplace=True)
    # return
    return df_country, df_year

df_country, df_year = read_data_from_file('API_1_DS2_en_csv_v2_5358775.csv')

# print_data
print(df_country,df_year)


# Read_data
df = pd.read_csv('API_1_DS2_en_csv_v2_5358775.csv', skiprows=4)
# clean data
df.fillna('', inplace=True)

# Indicators_of_interest
indicators_array = ['Rural population (% of total population)', 'Agricultural nitrous oxide emissions (% of total)','Agricultural methane emissions (% of total)', 'Rural population growth (annual %)']

# Countries_of_interest
countries_array = ['China','France','India','South Africa','Romania','United Kingdom','United States']



# Subset_the_data
df_sub = df[(df['Country Name'].isin(countries_array)) & (df['Indicator Name'].isin(indicators_array))]

# Calculate statistics with describe
stats = df_sub.groupby(['Country Name', 'Indicator Name']).describe()

# Print_statistics
print(stats)

# get years colums
year = [col for col in df_sub.columns if col.isdigit()]

# graphs
graphs.bar_graph(df_sub, year, 'Rural population (% of total population)', 'Country Name', '')
graphs.bar_graph(df_sub, year, 'Agricultural methane emissions (% of total)', 'Country Name', '')
graphs.heatmap(df_sub, 'France', indicators_array,'crest')
graphs.heatmap(df_sub, 'United Kingdom', indicators_array,'BuPu')
