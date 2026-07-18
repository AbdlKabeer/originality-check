from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from difflib import SequenceMatcher
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import cv2
from deepface import DeepFace


@api_view()
def say_hellow(request):
    # Declaring string variables
    string1 = 'I am geek ijbh hibber fehebhbfe fewhefwhfewf wefwhjewf'
    string2 = 'I am geeks'
    match = SequenceMatcher(None,string1, string2)

    result = match.ratio() * 100
    print(int(result), "%")

    
    """

    # with open('doc1.txt') as first_file, open('doc2.txt') as second_file:
    #     file1 = first_file.read()    
    #     file2 = second_file.read()

    #     ab = SequenceMatcher(None, file1, file2).ratio()

    #     result = int(ab*100)
        
    #     print(f"{result}% Plagiarized Content")
    """
    
    # Sample documents
    # documents = [
    #         "This is the first document.",
    #         "This document is the second document.",
    #         "And this is the third one.",
    #         "Is this the first document?"
    #     ]

    # # Initialize TF-IDF vectorizer
    # vectorizer = TfidfVectorizer()

    # # Compute TF-IDF matrix
    # tfidf_matrix = vectorizer.fit_transform(documents)

    # # Calculate cosine similarity between documents
    # similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # # Set a similarity threshold (adjust as needed)
    # threshold = 0.7

    # # Find potential plagiarism cases
    # plagiarism_cases = []
    # for i in range(len(similarities)):
    #     for j in range(i + 1, len(similarities)):
    #         if similarities[i][j] > threshold:
    #             plagiarism_cases.append((i, j, similarities[i][j]))

    # # Print plagiarism cases
    # for case in plagiarism_cases:
    #     doc1, doc2, similarity = case
    #     print(f"Documents {doc1} and {doc2} are similar with a similarity score of {similarity:.2f}")



    return Response(f"{result}")




