==========
TorSession
==========

TorSession is a library That I made for using requests html's asynchronous requests class simply for making get requests anonymously

how to use it 

Here an Example of how I use this library:

.. code-block:: python

    from TorSession import TorSession


    async def get_tor_session():

        ts = await TorSession()

        r = await ts.get("https://httpbin.org/ip")

        r.json() # -> Tor Exit Node 


The Library can also use the anti-Useragent class to spoof your useragent so that more websites can accept your requests
this also works with onionsites


You will need to have tor installed for this to work and your path will need to be setup 

Now I am a bit of a Noob with github but I'll get to your get to your guy's level eventually 

Mit Licence 
https://github.com/Dentordev/TorSession/blob/main/LICENSE

If You Would like to Support me and my projects You can donate to my Monero Wallet

.. 

    84QtScDcuiwMkdbSzWsou7XGQbfwfnMztJa51z2XDAHLVeHDAj9pg7PY2HdfjB9hxQWQm8DBvKYw4QFuzPJ5vAM91iz2HvF



