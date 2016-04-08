
My first step is to try to try to reproduce the problem:

::

    $ python3 define.py jfiejfin
    Traceback (most recent call last):
       File "/Users/mckim055/python/SystemDevelopment/Examples/testing/wikidef/api.py", line 26, in article
          contents = json_response['parse']['text']['*']
    KeyError: 'parse'

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
       File "define.py", line 14, in <module>
          print(Definitions.article(title).encode('utf-8'))
       File "/Users/mckim055/python/SystemDevelopment/Examples/testing/wikidef/definitions.py", line 7, in article
          return Wikipedia.article(title)
       File "/Users/mckim055/python/SystemDevelopment/Examples/testing/wikidef/api.py", line 28, in article
          raise ParseError(json_response)
    api.ParseError: {'servedby': 'mw1195', 'error': {'*': 'See https://en.wikipedia.org/w/api.php for API usage', 'info': "The page you specified doesn't exist", 'code': 'missingtitle'}}


So, one key here is 'During handling of the above exception, another exception occured:' If we look at the code that is being referenced, we see that the first exception happened during a try block. This may seem strange, because we are seeing the error that we are suppose to be excepting, KeyError, but if Python encounters an error in an exception block it will propogate both errors, so perhaps this is what happened. (This did not use to be the case, and made for difficulties debuging. It was changed in PEP_3134_).

.. _PEP_3134: https://www.python.org/dev/peps/pep-3134/ 

So, what happened? If we look at the second exception traceback, we see the second exception occured on line 28 of the same file. Sure enough, that is in the except KeyError block. And it looks like an error that is being purposely raised. So, it seems that someone thought that a KeyError was not going to be very informative, and decided it would make more sense to call it a ParseError. That does seem like a more informative error, but it gets pretty confusing with the double traceback. So, a KeyError is pretty easy to avoid. Maybe it would be more sensible to look for the 'parse' key, and then throw the error if we don't find it.

So, let's try this:

::

   if 'parse' in json_response:
       contents = json_response['parse']['text']['*']
   else:
       raise ParseError(json_response)


This gives us:

::

   $ python3 define.py jfiejfin
   Traceback (most recent call last):
     File "define.py", line 14, in <module>
        print(Definitions.article(title).encode('utf-8'))
     File "/Users/mckim055/python/SystemDevelopment/Examples/testing/wiki_solution/definitions.py", line 7, in article
        return Wikipedia.article(title)
     File "/Users/mckim055/python/SystemDevelopment/Examples/testing/wiki_solution/api.py", line 28, in article
        raise ParseError(json_response)
   api.ParseError: {'servedby': 'mw1228', 'error': {'info': "The page you specified doesn't exist", '*': 'See https://en.wikipedia.org/w/api.php for API usage', 'code': 'missingtitle'}}


That is definitely an improvement. We could probably make the error even clearer. Notice that what we are being returned a dictionary (actually json, which is similar), and the most useful information is json_response['error']['info']. Let's try using that as our error message.

::
   $ python3 define.py jfiejfin
   Traceback (most recent call last):
     File "define.py", line 14, in <module>
        print(Definitions.article(title).encode('utf-8'))
     File "/Users/mckim055/python/SystemDevelopment/Examples/testing/wiki_solution/definitions.py", line 7, in article
        return Wikipedia.article(title)
     File "/Users/mckim055/python/SystemDevelopment/Examples/testing/wiki_solution/api.py", line 28, in article
        raise ParseError(json_response['error']['info'])
   api.ParseError: The page you specified doesn't exist

That is looking much better. Now let's work on that test. In this case, I chose to figure out what was going on with the exceptions before writing the tests, because I needed the output from wikipedia to troubleshoot effectively. When debugging, it sometimes makes more sense to write a test after you have figured out what has gone wrong. But, don't forget to write the test, because these are often some of the more useful tests. Bugs have a way of returning, and best to catch them right away.

In some cases, you really don't want to call the database or network you are trying to mock at all, and have to rely on the documentation of the system you are mocking to determine how it will act. For the purposes of this exercise, however, it is probably easier to understand how mock and tests work by first testing with wikipedia and then mocking. So, I would start by uncommenting the test_missing_article_failure test to see that run. You can try running it with both a good title and a nonexistent title, just to make sure things work like you expect. Use the debugger if you want to see the progression of calls.

Now let's mock it. The first question is what exactly are we mocking. We know that if we call our api with a nonsense word, we should get back a ParseError, and we do not want to actually contact Wikipedia. In our examples we were mocking the Wikipedia classmethod article. However, that doesn't make sense for this test, because the stuff that we want to test is in the classmethod article itself. At first, I thought it would make sense to mock response (you can mock stuff you are importing as well as your own stuff). After I started down that path, I realized mocking response was relatively complicated, because it is returning a fairly complicated object (this becomes obvious when you notice that we are calling a method json on it in our code). I couldn't just use the simple setting of a return value for the mock object. I went ahead and mocked it out for fun, which you can see here:  

https://github.com/codedragon/mock_play/blob/master/test_wikidef_with_mock.py

What I then decide made more sense was to refactor my original class and create a function that I could mock. This would separate my code using requests from the code I was testing, making it shorter and more readable in the process. And that made life much easier. As was pointed out in class, with Mock sometimes the hardest part is getting the reference to the object you want to mock correct. I found a couple of good explanations here:

http://www.voidspace.org.uk/python/mock/patch.html#where-to-patch
https://www.toptal.com/python/an-introduction-to-mocking-in-python

Lastly, I would like to say that your tests should not care too much about implementation, and mock forces a bit of that. So, while mock is extremely useful in certain situations, try to use it judiciously. 
