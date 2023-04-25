library(academictwitteR)

bearer_token <- "XXXXX"

tweets <- get_all_tweets(
  "from:elonmusk",
  "2021-01-01T00:00:00Z",
  "2021-06-14T00:00:00Z",
  bearer_token
)

View(tweets$text)
