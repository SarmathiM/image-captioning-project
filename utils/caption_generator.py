import numpy as np
import random

def generate_caption(features):
    captions = [
        "A person is walking in a beautiful outdoor area",
        "A group of people are enjoying a sunny day",
        "A scenic view of nature with trees and sky",
        "A person standing in front of a building",
        "An outdoor environment with natural scenery",
        "A close-up image showing important details",
        "A calm and peaceful landscape view"
    ]

    return random.choice(captions)