# Network 0
[<](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master/0x0F-python-object_relational_mapping/README.md) 0x10 [>](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master/0x12-javascript-warm_up/README.md)
---

Resources
Read or watch:
   * [HTTPS(hyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html) (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)
   * [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)


# NEED TO KNOW?
  * [What is a URL?](#what-is-a-url)
  * [What is HTTP?](#what-is-http)
  * [How to read a URL?](#how-to-read-a-url)
  * [The scheme for a HTTP URL](#scheme-for-an-http-url)
  * [What a domain name is](#domain-name)
  * [What a sub-domain is](#sub-domain)
  * [How to define a port number in a URL](#port-number)
  * [What a query string is](#query-string)
  * [What an HTTP request is](#http-request)
  * [What an HTTP response is](#http-response)
  * [What HTTP headers are](#http-headers)
  * [What the HTTP message body is](#http-message-body)
  * [What an HTTP request method is](#http-request-method)
  * [What an HTTP response status code is](#http-response-status-code)
  * [What an HTTP Cookie is](#http-cookie)
  * [How to make a request with cURL](#making-requests-with-curl)
  * [What happens when you type google.com in your browser](#browser-behavior) (Application level)

# What is a URL?
A URL (Uniform Resource Locator) is a reference or address used to access resources on the internet. It consists of various components that specify how to locate and retrieve a resource.

[^](#need-to-know)

# What is HTTP?
HTTP (Hypertext Transfer Protocol) is the foundation of data communication on the World Wide Web. It is an application protocol for distributed, collaborative, and hypermedia information systems.

[^](#need-to-know)

# How to Read a URL
A URL is typically composed of a scheme, domain, sub-domain, port number, path, and query string. Understanding each part is crucial for navigating the web effectively.

[^](#need-to-know)

# Scheme for an HTTP URL
The scheme indicates the protocol used, such as HTTP or HTTPS, determining how the resource should be accessed.

[^](#need-to-know)

## Components of a URL

# Domain Name
The domain name identifies the server hosting the resource. For example, in "www.google.com," "google.com" is the domain.

[^](#need-to-know)

# Sub-Domain
A sub-domain is a subdivision of the domain. In "api.google.com," "api" is the sub-domain.

[^](#need-to-know)

# Port Number
A port number, if specified, indicates the communication endpoint on the server. For instance, in "www.google.com:8080," "8080" is the port.

[^](#need-to-know)

# Query String
The query string follows a "?" in the URL and contains parameters for the resource. In "example.com/search?q=term," "q" is a parameter with the value "term."

[^](#need-to-know)

## Understanding HTTP

# HTTP Request
An HTTP request is a message sent by a client to request a resource from a server. It includes information like the request method, headers, and sometimes a message body.

[^](#need-to-know)

# HTTP Response
An HTTP response is a message from a server to a client containing the requested resource along with metadata. It includes a status code indicating the success or failure of the request.

[^](#need-to-know)

# HTTP Headers
HTTP headers provide additional information about the resource or request. They include details like content type, length, and encoding.

[^](#need-to-know)

# HTTP Message Body
The HTTP message body contains the data being sent in the request or response.

[^](#need-to-know)

# HTTP Request Method
The request method specifies the desired action to be performed on a resource. Common methods include GET, POST, and PUT.

[^](#need-to-know)

# HTTP Response Status Code
The status code indicates the outcome of the request. For example, "200 OK" means success, while "404 Not Found" signifies the requested resource wasn't found.

[^](#need-to-know)

# HTTP Cookie
An HTTP cookie is a small piece of data stored on the user's device, allowing servers to recognize and remember users.

[^](#need-to-know)

# Making Requests with cURL
cURL is a command-line tool for making HTTP requests. You can use it to interact with web services and APIs from the terminal.

[^](#need-to-know)

# Browser Behavior
    (Application Level)
When you type "google.com" in your browser, it initiates an application-level process. The browser resolves the domain, establishes a connection, sends an HTTP request, receives an HTTP response, and renders the content for you to interact with. Understanding these processes enhances your overall web literacy.

[^](#need-to-know)

