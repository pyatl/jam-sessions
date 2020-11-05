# Sorting 101

PyATL Jam Session, November 5th 2020

[Sorting] is arguably among the fundamental problems in Computer Science.
Thankfully we rarely need to think about it too much. Like other languages,
Python includes built-in sorting routines that use fast and efficient
(and [complex][Timsort]) algorithms. Sorted collections are always just one
`sorted()` call away!

While not essential to all programming tasks, understanding how sorting works
is useful. While the concept of sorting is very simple, the techniques used to
achieve it can be very complex. Sorting problems are also very common in job
interview questions, so it never hurts to be prepared.

## Instructions

First, connect to the Cyber Dojo session using the code shared separately.
For more details, you can read our wiki:  
<https://github.com/pyatl/jam-sessions/wiki/Cyber-Dojo-Instructions>

You will need to write your code in `sorting.py`. The `list_to_sort` variable
will hold a list of integers, and your code needs to sort it! Using any of the
built-in `sorted` or `list.sort` calls is not allowed.

You are free to use any sorting algorithm you want. If you have never done this
before, the next section will explain an easy sorting method.

## Guide: Insertion Sort

One of the easiest sorting strategies to implement is the [insertion sort].
The general idea is to progress through the list item by item while maintaining
the part of the list behind you always sorted.

Here is an example: lets try to sort `[4, 1, 5, 0, 3, 2]`.

In the illustrations below:

* the `|` symbol will indicate our progress through the list (therefore
  the elements to its left are the ones we've sorted),
* the `^` symbol marks our progress when moving an item to its position,
* and `-` will show which pair of numbers was just swapped.

Let's go through this process step-by-step.

 1. We start at the first position, with no elements behind us:

        4 1 5 0 3 2
        |
    
    Because we are just starting, 4 is already at its correct position in the
    sorted part of the list. So there is nothing to do.
 
 2. At the next position we find the number 1:
 
        4 1 5 0 3 2
          |
 
    1 is not in its correct position, so we swap it with 4 to keep the sort:
 
        1-4 5 0 3 2
          |
 
 3. The number 5 being greater than 4, it is in its correct position and there
    is nothing to do:

        1 4 5 0 3 2
            |
 
 4. In the fourth position, zero is clearly not in its place. We can fix that
    by swapping pairs until that is fixed. Step by step:

        1 4 5 0 3 2     Swap 0 and 5
              |
        1 4 0-5 3 2     Swap 0 and 4
            ^ |
        1 0-4 5 3 2     Swap 0 and 1
          ^   |
        0-1 4 5 3 2     Done
        ^     |
 
 5. Repeat that process with the next item:

        0 1 4 5 3 2    
                |
        0 1 4 3-5 2
              ^ |
        0 1 3-4 5 2
            ^   |
    We have now reached a position where 3 is preceded by a smaller number, so
    we know that it's in the correct place.
    
 6. Finally, let's bring the last item in its correct position.

        0 1 3 4 2-5
                ^ |
        0 1 3 2-4 5
              ^   |
        0 1 2-3 4 5
            ^     |
 
There are many great videos on YouTube about this technique or a variant of it:

* <https://youtu.be/JU767SDMDvA>
* <https://youtu.be/pcJHkWwjNl4>
 
Rosetta Code has many examples of implementations, though I strongly recommend
trying it yourself before looking at solutions:  
<http://www.rosettacode.org/wiki/Sorting_algorithms/Insertion_sort>
 
## Extra Challenges

Can you implement other sorting algorithms? Here are some you can try:

* [Library sort]
* [Quicksort]
* [Radix sort]


[Sorting]: https://en.wikipedia.org/wiki/Sorting_algorithm
[Timsort]: https://en.wikipedia.org/wiki/Timsort
[Insertion sort]: https://en.wikipedia.org/wiki/Insertion_sort
[Library sort]: https://en.wikipedia.org/wiki/Library_sort
[Quicksort]: https://en.wikipedia.org/wiki/Quicksort
[Radix sort]: https://en.wikipedia.org/wiki/Radix_sort
