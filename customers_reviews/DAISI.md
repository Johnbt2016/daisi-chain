# Daisies Orchestration

This is an example of an orchestration of 4 daisies achieving the following tasks:

1. Pulling customer reviews from Yelp for a given city/restaurant type. It uses the [`"Get Yelp Reviews"`](https://app.daisi.io/daisies/0c2f422a-1785-4c83-8a51-4a8f531dbbfd/info) Daisi
2. Analyzing the sentiment of each review using a Zero Shot Classification language model. It uses the [`"Classify Labels"`](https://app.daisi.io/daisies/6463bf95-e339-44fc-8da0-5a0ec08f695c/info) Daisi
3. Translating each review into a different language. It uses the [`"LanguageTranslator"`](https://app.daisi.io/daisies/63ed4819-2134-4cfc-87d1-eba65bdaeed2/info) Daisi
4. Computing a Wordcloud with the reviews. It uses the [`"WordCloud"`](https://app.daisi.io/daisies/023be548-c487-4dca-93b2-571c4978fc6c/info) Daisi

Call it in Python:

```python
import pydaisi as pyd
from PIL import Image
import pandas as pd

customers_reviews_etl = pyd.Daisi("laiglejm/Customers Reviews ETL")
result = customers_reviews_etl.orchestrate(term="korean", location="Houston", language="French").value

df = result[0] # A dataframe containing the Yelp reviews, sentiment analysis and translation
image = result[1] # The Wordcloud image
```
