# Network 1
[<](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master/0x10-python-network_0/README.md) 0x11 [>](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master/0x12-javascript-warm_up/README.md)
---
# Fetching Internet Resources with Python
    Read or watch:
* [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
* [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/)
* [Requests package](https://pypi.org/project/requests/)
---

# NEED TO KNOW?
* [How to fetch internet resources with the Python package urllib](#how-to-fetch-internet-resources)
* [How to decode urllib body response](#how-to-decode-urllib-body-response)
* [How to use the Python package requests](#how-to-use-the-requests-package) #requestsiswaysimplerthanurllib
* [How to make HTTP GET request](#how-to-make-http-get-request)
* [How to make HTTP POST/PUT/etc. request](#how-to-make-http-post-put-etc-request)
* [How to fetch JSON resources?](#how-to-fetch-json-resources)
* [How to manipulate data from an external service?](#how-to-manipulate-data-from-an-external-service)

---

# urllib

### How to Fetch Internet Resources

To fetch internet resources with `urllib`, you can use the `urllib.request` module. Here's a basic example:

    python
        #!/usr/bin/python3
        import urllib.request

        url = "https://example.com"
        response = urllib.request.urlopen(url)
        data = response.read()

# Now 'data' contains the content of the URL
### How to Decode urllib Body Response
    The body response from urllib can be decoded using the decode method. For example:

      pyCode
          decoded_data = data.decode('utf-8')

[^](#need-to-know)

# requests
### How to Use the requests Package
    The requests package simplifies the process of making HTTP requests. Install it using:

      bashCode
          pip install requests

[^](#need-to-know)

# How to Make HTTP GET Request
    Here's an example of making a GET request using requests:

    pyCode
        #!/usr/bin/python3
        import requests

        url = "https://example.com"
        response = requests.get(url)
        data = response.text

        # Now 'data' contains the content of the URL

[^](#need-to-know)

# How to Make HTTP POST/PUT/etc. Request
    Using requests, you can make various HTTP requests. For example, a POST request:

      pyCode
          data = {'key': 'value'}
          response = requests.post(url, data=data)

[^](#need-to-know)

# How to Fetch JSON Resources
    requests makes it easy to work with JSON resources:

      pyCode
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        json_data = response.json()

[^](#need-to-know)

# How to Manipulate Data from an External Service
    Once you have the data, you can manipulate it according to your needs. For instance:

      pyCode
        title = json_data['title']
        print(f"Title: {title}")

[^](#need-to-know)

Remember to check the official documentation for more details on each package:

* [urllib documentation](https://docs.python.org/3/library/urllib.html)
* [requests documentation](https://docs.python-requests.org/en/latest/)

[^](#network-1)


