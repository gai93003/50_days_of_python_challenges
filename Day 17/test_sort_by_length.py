from sort_length import sort_length

def test_sort_by_length():
    arr = ["Peter", "Jon", "Andrew"]
    result = sort_length(arr)

    assert result == ["Jon", "Peter", "Andrew"]

