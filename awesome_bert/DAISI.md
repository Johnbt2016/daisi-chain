### Question Answering with BERT

Bert is a transformers-based language model developed by Google.
Call it programmatically !

```python
import pydaisi as pyd

ask_bert = pyd.Daisi("erichare/Ask BERT")
answer = ask_bert.compute(query = "What is a potato", context = "A potato is a starchy vegetable").value
```
