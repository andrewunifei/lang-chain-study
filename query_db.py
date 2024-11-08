from embeddings import query_document

results = query_document('only retrieve with the word "double-top" in it',3, 2)
for result in results:
    print('------')
    print('')
    print(result)
    print('')