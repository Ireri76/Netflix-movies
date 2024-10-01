# Load necessary libraries
library(ggplot2)
library(dplyr)
library(readr)

# Load the cleaned data
netflix_show_movies <- read_csv("C:/Users/user/OneDrive/NEXFORD UNIVERSITY/MSDA COURSE UNITS/BAN6420 PROGRAMMING IN R AND PYTHON/BAN6420-MODULE 4/Submitted Files/netflix_show_movies.csv")
View(netflix_show_movies)

# Graph 1: 'Recoded_release_year' and 'type'
ggplot(netflix_show_movies, aes(x = Recoded_release_year, fill = type)) +
  geom_bar(position = "dodge") +
  labs(title = "Figure 1: Distribution of Types by Release Year") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

# Graph 2: 'type' and 'rating'
ggplot(netflix_show_movies, aes(x = type, fill = rating)) +
  geom_bar(position = "dodge") +
  labs(title = "Figure 2: Distribution of Ratings by Type") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

# Graph 3: 'type' and 'Recoded_duration'
ggplot(netflix_show_movies, aes(x = type, fill = Recoded_duration)) +
  geom_bar(position = "dodge") +
  labs(title = "Figure 3: Distribution of Duration by Type") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))
