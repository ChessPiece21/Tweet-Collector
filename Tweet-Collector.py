# Install and Configure Twarc

!pip install twarc
!pip install plotly

!twarc2 configure
# Happy twarcing!

# Get Tweets and Metadata
# To collect tweets and associated metadata, we can use the command twarc2 search and insert a query. 
# If you have an Academic Research account, you can collect tweets from the entire archive with the flag --archive.
!twarc2 search "(\"the adam friedland show\")" --archive --limit 30 --tweet-fields "text"

# Save Tweets to a CSV file.
!twarc2 search "(\"the adam friedland show\")" --archive > tafs_tweets.csv

# Save to Google
from google.colab import drive
drive.mount('/content/drive')

