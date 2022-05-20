def get_summary():
    text = '''
    This daisi uses the Bart language model developed by Facebook for Zero Shot classification.   
    Simply upload an Excel file with a column containing the sentences to classify and define possible labels.   
    
    Call it in your code now (see the [Daisi Zero Shot Text Classification" doc](https://app.daisi.io/daisies/237587e0-7c47-4a4f-afad-80370c8e98a4/how-to-use)):   

    ```python
    import pydaisi as pyd   

    classify =  pyd.Daisi("Zero Shot Text Classification")   
    result = classify.compute(text="Let's go the moon", candidate_labels="astronomy, travel").value  
    ```

    
    Check also the [model doc](https://huggingface.co/docs/transformers/main/en/model_doc/bart#transformers.BartForSequenceClassification) on Transformers
    '''

    return text