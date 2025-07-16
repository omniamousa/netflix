import pandas as pd
df = pd.read_csv("netflix_titles.csv")

# 1- count the number of TV shows and movies separately and compare between them (which is more). .get(x)

# type_counts = df['type'].value_counts()
# print("num of movies:", type_counts.get('Movie', 0))
# print("num of tv shows:", type_counts.get('TV Show', 0))

# if type_counts['Movie'] > type_counts.get('TV Show'):
#     print("there're more movies than tv shows")
# elif type_counts['Movie'] < type_counts.get('TV Show'):
#     print("there're more tv shows than movies")
# else: 
#     print("movies and tv shows are the same num") 

# print("_" * 70)

# # 2- iterate through the rating column of the dataset and count how many times the rating is (TV-MA).

# rate = 0
# for rating in df['rating']:
#     if rating == 'TV-MA' :
#         rate += 1
# print("num of TV-MA rating:", rate)

# print("_" * 70)



# 3- filter the dataset to only include movies released after 2015.

# filtered_df = df[(df['type'] == 'Movie') & (df['release_year'] > 2015)]
# print(filtered_df.head())
# print("num of movies after 2015:", filtered_df.shape[0])

# print("_" * 70)

# 1- Create a new column called year_added from the date_added column.

# df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
# df['year_added'] = df['date_added'].dt.year
# print(df[['date_added', 'year_added']].head()) 

# # 2-For each year_added, calculate the average length of the title (character count).

# df['title_length'] = df['title'].str.len()
# avg_title_length = df.groupby('year_added')['title_length'].mean()
# print(avg_title_length)

# # 3-Plot the trend of average title length over the years Netflix added content.

# import matplotlib.pyplot as plt

# avg_title_length.plot(kind='line', marker='.', color='black')

# plt.title('Avg Title Length by year')
# plt.xlabel('Year')
# plt.ylabel('Title Length')
# plt.grid(True)
# plt.show()

##########################A##########################

#  1- Extract the month and year separately.

# df['date_added'] = pd.to_datetime(df['date_added'])
# df['month_added'] = df['date_added'].dt.month_name()
# print(df[['date_added', 'month_added']].head()) 

# print("_"*70)

# # 2-Identify which month (across all years) Netflix typically adds the most new content.

# month_counts = df['month_added'].value_counts()
# print(month_counts)
# print("Most active month:", month_counts.idxmax())

# print("_"*70)

# # 3- Plot the total number of titles added per month.

# month_counts = df['month_added'].value_counts().sort_index()

# import matplotlib.pyplot as plt

# month_counts.plot(kind='bar', color='grey')  
# plt.title('Total Titles Added per Month')
# plt.xlabel('Month')
# plt.ylabel('Num of Titles')
# plt.xticks(rotation=45)  
# plt.grid(True)
# plt.tight_layout()  
# plt.show()

# #######################################B##############################

# # 1- Identify any titles that appear more than once, regardless of country.

# # Step 1: get duplicated titles
# duplicate_titles = df[df.duplicated('title', keep=False)]

# # Step 2: show title + country + rating for duplicates
# result = duplicate_titles[['title', 'country', 'rating']].sort_values('title')
# print(result)





from collections import Counter

# 1. Remove rows with missing genres
df = df.dropna(subset=['listed_in'])

# 2. Split genres into lists
all_genres = df['listed_in'].str.split(', ')

# 3. Flatten the list using explode and count frequencies
genre_list = all_genres.explode()
genre_counts = Counter(genre_list)

# 4. Show top 10 genres
top_10_genres = genre_counts.most_common(10)

print("Top 10 Most Common Genres:")
for genre, count in top_10_genres:
    print(f"{genre}: {count}")






