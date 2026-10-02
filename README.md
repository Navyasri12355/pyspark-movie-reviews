# PySpark Movie Reviews

Basic PySpark processing of the IMDb 50K Movie Review dataset.

## Dataset

[IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) (Kaggle). Columns: `review`, `sentiment`.
The CSV is not included in this repository. Download it and place `IMDB Dataset.csv` in the project folder.

## What the script does

`movie_reviews.py`:

1. Loads the CSV into a PySpark DataFrame
2. Prints the schema and the first 5 rows
3. Removes rows with null or empty reviews
4. Counts total reviews and positive/negative reviews
5. Adds a `review_length` column (number of characters per review)
6. Filters and displays reviews longer than 500 characters
7. Saves the cleaned and transformed DataFrame to `output/cleaned_reviews/` as CSV

## Requirements

- Python 3
- Java (JDK 8, 11, or 17)
- PySpark: `pip install pyspark`

## Run

```
python movie_reviews.py
```
