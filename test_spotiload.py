import pytest
from spotiload import search, extract_meta

def test_search():
    # Test the search function with a known input
    result = search('Test Song')
    assert result.startswith('/watch?v='), "The search function should return a YouTube URL suffix starting with '/watch?v='"

def test_extract_meta():
    # Test the extract_meta function with a known input
    result = extract_meta('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    assert 'title' in result, "The extract_meta function should return a dictionary with a 'title' key"