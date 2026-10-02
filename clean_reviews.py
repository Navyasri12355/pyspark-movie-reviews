from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, trim

spark = SparkSession.builder \
    .appName("MovieReviews") \
    .master("local[*]") \
    .getOrCreate()

df = spark.read.csv("IMDB Dataset.csv", header=True, inferSchema=True, multiLine=True, quote='"', escape='"')

# Explore the data - print schema and first 5 rows
print("=== Schema ===")
df.printSchema()

print("=== First 5 rows ===")
df.show(5, truncate=80)

# Clean the data - remove rows with null/empty reviews
df_clean = df.filter(col("review").isNotNull() & (trim(col("review")) != ""))

# Analyze the data - count total, positive and negative counts of reviews
print("Total number of reviews:", df_clean.count())
positive_count = df_clean.filter(col("sentiment") == "positive").count()
negative_count = df_clean.filter(col("sentiment") == "negative").count()
print("Positive reviews:", positive_count)
print("Negative reviews:", negative_count)

# Transform the data - add column to store review length
df_final = df_clean.withColumn("review_length", length(col("review")))

# Transform the data - filter reviews longer than 500 characters
long_reviews = df_final.filter(col("review_length") > 500)
print("Reviews longer than 500 characters:", long_reviews.count())
long_reviews.select("review", "review_length").show(10, truncate=80)

# Save cleaned and transformed df
df_final.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("output/cleaned_reviews")

print("Saved to output/cleaned_reviews/")

spark.stop()