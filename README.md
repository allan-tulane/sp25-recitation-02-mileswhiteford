# CMPS 2200  Recitation 02

**Name (Team Member 1):**Miles Whiteford 

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

If f(n) is 1 and a=1 and b=2, W(n) is O(logn). 
Examples:
n = 1, W(n) = 1
n = 10, W(n) = 4
n = 100, W(n) = 7
n = 1000, W(n) = 10
These values grow at a rate of log(n), increasing at the same rate as n is increased exponentially

If f(n) = logn and a = 1 and b=2, W(n) will be O(logn) because it will be root dominated.
Examples:
n = 1, W(n) = 1
n = 10, W(n) = 5.605
n = 100, W(n) = 18.111
n = 1000, W(n) = 37.786
n = 10000, W(n) = 66.154
These values grow at a rate of log(n), increasing at the same rate as n is increased exponentially

If f(n) = n, a=1, b=2, then W(n) will be O(n) since it will be root dominated
Examples:
n=1, W(n)=1
n=10, W(n)=18
n=100 W(n)=197
n=1000, W(n)=1994
n=10000, W(n)=19995
These values grow at a rate of n because both n and W(n) grow at the same rate. 

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer.
- [ ] 
In the order (n, W_1(n), W_2(n), W_3(n))
(10, 1068, 132, 108), (20, 8944, 664, 472), (50, 104780, 4228, 3076), (100, 848240, 17816, 12304), (1000, 509190592, 1898080, 1275296), (5000, 143543110592, 49110112, 32077640), (10000, 1148444884736, 197392832, 128431968)

These results match the predicted outputs. W_1 is root dominated which should have to do the most worka nd the data shows that it easily grows the fastest. W_3 is leaf dominated which should do the least amount of work, and the data shows us that it grows much slower than W1 and slower than W2. W2 is balanced, meaning recursion and work at each level contribute equally, and as we see from the data it has an intermediate level of growth as expected

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

(10, 4, 4.605170185988092, 18), (20, 5, 7.600902459542082, 38), (50, 6, 12.506177237980513, 97), (100, 7, 17.111347423968603, 197), (1000, 10, 36.78583226092475, 1994), (5000, 13, 55.94412444836603, 9995), (10000, 14, 65.15446482034221, 19995)

These values line up with what is predicted from these different runtimes. As mentioned earlier, with a=1, b=2, f(1) and f(logn) are both root dominant which makes them O(logn) and the data shows both of those functions growing at a rate of logn. Similarly, f(n) should grow at a rate of O(n) and as we can see, the values for F_3 grow at a linear rate.  
