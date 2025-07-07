# # from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# # # Load the FLAN-T5-base model and tokenizer
# # model_name = "google/flan-t5-base"
# # tokenizer = AutoTokenizer.from_pretrained(model_name)
# # model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# # def query_model(context, query):
# #     """
# #     Handle queries based on context to fetch specific information.
# #     """
# #     input_text = f"""
# #     You are an assistant that answers questions strictly based on the given context. 
    
# #     Context:
# #     {context}

# #     Query:
# #     {query}
# #     """
# #     # Tokenize input
# #     inputs = tokenizer(input_text.strip(), return_tensors="pt")

# #     # Generate response with constraints
# #     outputs = model.generate(
# #         **inputs,
# #         max_length=256,
# #         num_return_sequences=1,
# #         no_repeat_ngram_size=2,  # Avoid repetitive n-grams
# #         early_stopping=True,    # Stop when output looks complete
# #         temperature=0.7,        # Lower temperature for less randomness
# #     )

# #     # Decode and return
# #     return tokenizer.decode(outputs[0], skip_special_tokens=True)


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the FLAN-T5-base model and tokenizer
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


predefined_queries = [
    "What is the intent of the email?",
]

def query_model(context):
    """
    Handle predefined queries based on the given context (email).
    """
    responses = {}
    for query in predefined_queries:
        input_text = f"""
        You are an assistant that answers questions strictly based on the given context. 
        
        Context:
        {context}

        Query:
        {query}
        """
        # Tokenize input
        inputs = tokenizer(input_text.strip(), return_tensors="pt")

        # Generate response with constraints
        outputs = model.generate(
            **inputs,
            max_length=256,
            num_return_sequences=1,
            no_repeat_ngram_size=2,  # Avoid repetitive n-grams
            early_stopping=True,    # Stop when output looks complete
            temperature=0.7,        # Lower temperature for less randomness
        )

        # Decode and store the response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        responses[query] = response + "\n"

    return responses


# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# # Load the FLAN-T5-large model and tokenizer
# model_name = "google/flan-t5-large"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# # Predefined queries
# predefined_queries = [
# "summarize the email in short"
# ]

# def query_model(context):
#     """
#     Handle predefined queries based on the given context (email).
#     """
#     responses = {}
#     for query in predefined_queries:
#         input_text = f"""
#         You are an assistant that answers questions strictly based on the given context. 
        
#         Context:
#         {context}

#         Query:
#         {query}
#         """
#         # Tokenize input
#         inputs = tokenizer(input_text.strip(), return_tensors="pt")

#         # Generate response with constraints
#         outputs = model.generate(
#             **inputs,
#             max_length=256,
#             num_return_sequences=1,
#             no_repeat_ngram_size=2,  # Avoid repetitive n-grams
#             early_stopping=True,    # Stop when output looks complete
#             temperature=0.7,        # Lower temperature for less randomness
#         )

#         # Decode and store the response
#         response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#         responses[query] = response

#     return responses

