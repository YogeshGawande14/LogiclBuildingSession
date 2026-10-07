# 🐍 Python Algorithms & Data Structures Toolkit
**MES's Institute of Management & Career Courses (IMCC)**

A comprehensive, pure-Python implementation of foundational algorithms and data structures. This repository is designed as a learning resource, coding interview prep guide, and quick reference library for common computational problems.

---

## 📂 Project Structure

The codebase is organized into five core modules:

1. **String Manipulation** (`#1`) - Common string processing and transformation algorithms.
2. **Searching Algorithms** (`#2`) - Linear and binary search variations.
3. **Sorting Algorithms** (`#3`) - Iterative and divide-and-conquer sorting techniques.
4. **Recursion & Backtracking** (`#3` continued) - Classic recursive problem-solving functions.
5. **Linked List Data Structure** (`#4`) - Singly linked list implementation with advanced pointer operations.

---

## 🛠️ Function & Method Reference

### 1. String Manipulation
| Function | Description |
| :--- | :--- |
| `reverse_string(s)` | Reverses a string iteratively. |
| `is_palindrome(s)` | Checks if a string reads the same forwards and backwards (Two-pointer approach). |
| `count_vowels_consonants(s)` | Counts vowels and consonants, ignoring non-alphabetic characters. |
| `find_duplicates(s)` | Identifies characters appearing more than once. |
| `remove_spaces(s)` | Strips all spaces from a string. |
| `substring_occurrence(s, sub)` | Counts non-overlapping occurrences of a substring. |
| `is_anagram(a, b)` | Validates if two strings are anagrams using frequency maps. |
| `to_uppercase(s)` | Converts lowercase letters to uppercase via ASCII manipulation. |
| `longest_word(sentence)` | Finds the longest word in a sentence. |
| `replace_char(s, old, new)` | Replaces specific characters in a string. |

### 2. Searching Algorithms
| Function | Description | Time Complexity |
| :--- | :--- | :--- |
| `linear_search(arr, target)` | Sequentially checks each element. | $O(n)$ |
| `binary_search_iterative(arr, target)` | Efficiently searches sorted arrays iteratively. | $O(\log n)$ |
| `binary_search_recursive(arr, l, r, target)` | Recursive variant of binary search. | $O(\log n)$ |
| `first_occurrence(arr, target)` | Locates the first index of a repeated target. | $O(\log n)$ |
| `last_occurrence(arr, target)` | Locates the last index of a repeated target. | $O(\log n)$ |

### 3. Sorting Algorithms
| Function | Description | Average Time | Worst Time |
| :--- | :--- | :--- | :--- |
| `bubble_sort(arr)` | Repeatedly swaps adjacent out-of-order elements. | $O(n^2)$ | $O(n^2)$ |
| `selection_sort(arr)` | Selects the minimum element and shifts it left. | $O(n^2)$ | $O(n^2)$ |
| `insertion_sort(arr)` | Builds a sorted list element by element. | $O(n^2)$ | $O(n^2)$ |
| `merge_sort(arr)` | Divide-and-conquer sorting algorithm. | $O(n \log n)$ | $O(n \log n)$ |
| `quick_sort(arr)` | Partition-based sorting using a pivot element. | $O(n \log n)$ | $O(n^2)$ |

### 4. Recursion & Classic Problems
* **`factorial(n)`**: Computes $n!$.
* **`fibonacci(n)`**: Computes the $n$-th Fibonacci number.
* **`sum_digits(n)`**: Recursively calculates the sum of an integer's digits.
* **`reverse_string_rec(s)`**: Reverses a string using recursive slicing.
* **`print_1_to_n(n)` & `print_n_to_1(n)`**: Prints number sequences recursively.
* **`power(x, n)`**: Computes base $x$ raised to exponent $n$.
* **`gcd(a, b)`**: Finds the Greatest Common Divisor using the Euclidean algorithm.
* **`is_palindrome_rec(s)`**: Recursive palindrome validator.
* **`tower_of_hanoi(...)`**: Solves the Tower of Hanoi puzzle for $n$ disks.

### 5. Linked List (`Node` & `LinkedList`)
* **Insertion**: `insert_begin(value)`, `insert_end(value)`
* **Deletion**: `delete_first()`, `delete_last()`
* **Traversal & Search**: `traverse()`, `search(key)`, `count_nodes()`
* **Reversal**: `reverse_iterative()`, `reverse_recursive(node)`
* **Advanced Operations**: 
  * `detect_cycle()`: Detects loops using Floyd's Cycle-Finding Algorithm (Tortoise and Hare).
  * `merge_sorted(other)`: Merges two pre-sorted linked lists into a single sorted list.

---

## 🚀 Getting Started

1. **Clone or Download** the script into your local environment.
2. Ensure you have **Python 3.x** installed.
3. Run the script directly to see the built-in test outputs printed to your console:

```bash
python solution.py
