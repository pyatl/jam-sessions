Unit testing in Python
======================

Unit testing has many purposes, including verifying the correctness of code,
documentation, and guarding against bug regression.

The simplest and most straightforward way to do unit testing in Python is to
use the unittest module built into the standard library.
http://docs.python.org/library/unittest.html

This allows you to set up simple classes called Test Cases which are usually
intended to test a single Python module or class, and add several methods to
the test case to represent variations or parameters for testing.  For example,
if testing a simple mathmatical calculation, test methods might be created to
test calculations with positive numbers, negative numbers, zero, floating point
values, and so on, to ensure the correctness of each of these varities of
calculations.

If we go one step further and write our tests *before* writing our code, we are
then taking advantage of the technique of TDD (Test Driven Development/Design).
With TDD, when we write tests before we write our code, it can help us design
the implemenation of the code, since we write implementation simply to pass
tests, and therefore avoid cluttering up our classes with a bunch of methods or
properties we may never actually use.

As an example, test code has been provided.  In this example, we will assume
we're trying to build a simple string-manipulation class which has the ability
to "URL-ify" a particular domain name.  If we input 'jrrickerson' we should
expect to receive 'www.jrrickerson.com' as output.  This is obviously a
contrived example, but serves the purpose of demonstrating unit testing and the
TDD technique.

Here are the basic steps to writing a simple test with unittest using the TDD
technique:

Step 1 - Create a test module (fixture)
---------------------------------------
Create a new Python module for your test case, and import unittest
    import unittest
     

Step 2 - Create your test case
------------------------------
Create a new class that inherits from the TestCase class in the unittest module.
    import unittest

    class WebTest(unittest.TestCase):

Step 3 - Add a test method
--------------------------
Add a test method.  You want to try to focus a test method on a particular
behavior.  For this example we're going to cover the "happy case" or normal usage
of our "URL-ifying" class.  Note that test method names should start with the
word "test."
    import unittest

    class WebTest(unittest.TestCase):
        def test_create_url(self):
            domain = 'jrrickerson'
            expected_url = 'www.jrrickerson.com'

            maker = UrlMaker()
            result = maker.make(domain)

            self.assertEquals(result, expected_url)
Note that we have a variable for the domain we want to input, the url-like
string we expect to get, and the actual result that comes from out of our
implementation.  This is the core of unit testing.  Each test should have some
form of well-known input, well-known expected output, and be able to verify
that the result from the implementation matches the expected output.  After all,
if your inputs or your expected results are not well-known, or you have no
means of comparing the result to the expected output, how will you know when
your test passes or fails?

Step 4 - Run the Test
---------------------
Run the test and watch it fail.  Keep in mind that since we wrote the test
first, and there isn't any implementation yet, we *expect* the test to fail.
If we started with a passing test, we couldn't be sure if it was working properly,
or if the test was passing and giving us a false sense of confidence.
You can run the test from the command line, using the -m switch on python, like so:
    python -m unittest test
or you can simply add the following to the bottom of your test module and run it
like you would run any other script:
    if __name__ == 'main':
        unittest.main()
When the test fails, you should get an error that says something about
"global name UrlMaker not defined."  This is somewhat obvious, since if we
haven't written the UrlMaker class yet, of course it won't be defined.

Step 5 - Begin implementation
-----------------------------
Begin implementation of your UrlMaker class.  We'll simply put it into a new
module called urlmaker.py and declare our new class.
    class UrlMaker(object):
        pass
Next we want to make this new class visible to our test class, we'll need to
import it.  The top of your test module should now look like this:
    import unittest
    from urlmaker import UrlMaker
We'll start with an empty class to keep things simple, and here's where another
part of the TDD technique comes in.  Once you've written a basic test or two,
start your implementation, but do it fairly incrementally, and run the tests
often as you go.  Unit tests should by and large run very quickly, and this will
let you be sure you're only writing enough code to pass the test, and no more.
This time when you run your tests, you should get a new error.  It should say
something about UrlMaker not having an attribute "make."  So now we have to
actually write the method we wanted to test.

Step 6 - Pass the test
----------------------
Now we finish writing our implementation for the purpose of passing the test.
If desired, you can add an empty method, rerun the test, begin adding lines of
code to the method, rerun the test, and so on, until it passes.  To skip ahead
a bit, here's an implmentation that will hopefully pass.
    class UrlMaker(object):
        def make(self, domain):
            return 'www.{0}.com'.format(domain)
Of course this is a simple implementation and probably prone to a good number
of errors if we were to use it in a production environment, but one point of
TDD is to help us ensure we don't end up writing too much code, so a simple
implementation is a great start.  After this we should write more tests, which
serve to *prove* that we need further implementation, and we can organically
grow the implementation to meet the needs of all the tests we write.

After finishing this implemenation method, we should run our tests again, and
see that this time they pass. Now we have proof that in this specific case, our
implementation produces the correct results. We also have an automated test
that can be run again very quickly in case we want to re-verify this correctness
after we change the code.  With this foundation of confidence we can move forward
to write additional tests to cover addtional cases, and slowly adjust our
implementation to make sure all of those tests pass.  Once we pass all the tests
we think we should reasonbly write, our implemenation is done!
