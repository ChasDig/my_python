from patterns.behavioral.iterator import WordsCollectionIterable


def test_iterator():
    words_collection_iterable = WordsCollectionIterable(collection=["first", "second", "third"])
    words_ = ", ".join(words_collection_iterable).strip()
    result_ = f"Result: {words_}"

    assert result_ == "Result: first, second, third"