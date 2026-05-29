# test_merge_lists.py
import pytest
from merge_lists import merge_lists

def test_merge_lists():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    expected = [1, 2, 3, 4, 5, 6]
    assert merge_lists(list1, list2) == expected

def test_merge_lists_empty():
    list1 = []
    list2 = []
    expected = []
    assert merge_lists(list1, list2) == expected

def test_merge_lists_one_empty():
    list1 = [1, 2, 3]
    list2 = []
    expected = [1, 2, 3]
    assert merge_lists(list1, list2) == expected

def test_merge_lists_one_empty_list():
    list1 = []
    list2 = [4, 5, 6]
    expected = [4, 5, 6]
    assert merge_lists(list1, list2) == expected
```

```javascript
// mergeLists.test.js
import { mergeLists } from './mergeLists';

describe('mergeLists', () => {
  it('should merge two lists', () => {
    const list1 = [1, 2, 3];
    const list2 = [4, 5, 6];
    const expected = [1, 2, 3, 4, 5, 6];
    expect(mergeLists(list1, list2)).toEqual(expected);
  });

  it('should return empty list when both lists are empty', () => {
    const list1 = [];
    const list2 = [];
    const expected = [];
    expect(mergeLists(list1, list2)).toEqual(expected);
  });

  it('should return first list when second list is empty', () => {
    const list1 = [1, 2, 3];
    const list2 = [];
    const expected = [1, 2, 3];
    expect(mergeLists(list1, list2)).toEqual(expected);
  });

  it('should return second list when first list is empty', () => {
    const list1 = [];
    const list2 = [4, 5, 6];
    const expected = [4, 5, 6];
    expect(mergeLists(list1, list2)).toEqual(expected);
  });
});
