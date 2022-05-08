# T5 language model demo

This is an application of the T5 language model developed by Google for translation.  

Call it directly in your code with :  

```python
import pydaisi as pyd

tranlator =  pyd.Daisi("LanguageTranslator")
result = translator.translate(text="Testing the translation", dest='french').value
```

Check also the [model doc](https://huggingface.co/docs/transformers/main/en/model_doc/t5#transformers.T5WithLMHeadModel) on Transformers.  
