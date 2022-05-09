# Wordcloud computation

This daisi comutes and render a wordcloud.  
Simply upload an Excel file with a column containing the sentences that will be used to compute the wordcloud.  
The column needs to be labelled "title"  

Call it in your code now (see the [Daisi "WordCloud" doc](https://app.daisi.io/daisies/237587e0-7c47-4a4f-afad-80370c8e98a4/how-to-use)):  

```python
import pydaisi as pyd  
import pandas as pd  

classify =  pyd.Daisi("WordCloud")  
df = pd.read_excel(<filename>).rename(columns={'your column name': 'title'})

bytestring_image = wc.generate_wordcloud_byte(texts_path=df).value  
```
