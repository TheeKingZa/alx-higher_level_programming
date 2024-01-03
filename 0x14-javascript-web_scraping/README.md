# Web Scrapping
[<](https://github.com/TheeKingZa/alx-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/README.md) 0x14 [#]()
---
# JavaScript: Introduction

```
	JavaScript is a versatile and powerful programming language that has become a cornerstone in web development.
	Its ability to run on the client side, interact with the Document Object Model (DOM),
	and seamlessly communicate with servers makes it an essential
	tool for building dynamic and interactive web applications.

	This README.md aims to highlight the amazing aspects of JavaScript programming,
	focusing on manipulating JSON data,
	utilizing the request and fetch API,
	and mastering file operations using the 'fs' module.
```

---

# Resources

* [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
* [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
* [request module](https://github.com/request/request)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

---

# NEED TO KNOW?
1. [Why JavaScript is Amazing](#why-javascript-is-amazing)
2. [Manipulating JSON Data](#manipulating-json-data)
3. [Using Request and Fetch API](#using-request-and-fetch-api)
4. [Reading and Writing Files with fs Module](#reading-and-writing-files-with-fs-module)
5. [More Info](#more-info)

---

# Why JavaScript is Amazing

JavaScript's versatility, ease of learning, and widespread use in web development contribute to its amazing nature. Here are some key points:

- **Versatility**: JavaScript can be used for both front-end and back-end development, making it a full-stack language.
- **Asynchronous Programming**: The language supports asynchronous operations, enabling efficient handling of multiple tasks simultaneously.
- **Community and Ecosystem**: A vast community and an extensive ecosystem of libraries and frameworks make JavaScript development efficient and enjoyable.

# Manipulating JSON Data

JSON (JavaScript Object Notation) is a lightweight data interchange format widely used for data storage and exchange. JavaScript provides excellent support for manipulating JSON data:

- **Parsing JSON**: Use `JSON.parse()` to convert a JSON string into a JavaScript object.
- **Stringifying Objects**: Utilize `JSON.stringify()` to convert a JavaScript object into a JSON-formatted string.

Example:

```
JavaScriptCode:

	/** 
	 * Parses a JSON string into a JavaScript object.
	 * @param {string} jsonString - The JSON string to parse.
	 * @returns {Object} - The parsed JavaScript object.
	 */
	function parseJSON(jsonString) {
	    return JSON.parse(jsonString);
	}

	/** 
	 * Converts a JavaScript object into a JSON-formatted string.
	 * @param {Object} jsonObject - The JavaScript object to stringify.
	 * @returns {string} - The JSON-formatted string.
	 */
	function stringifyJSON(jsonObject) {
	    return JSON.stringify(jsonObject);
	}
```
# Using Request and Fetch API
JavaScript facilitates making HTTP requests using the fetch API.
This allows fetching resources asynchronously and handling responses seamlessly:

Using Fetch API: Fetch resources asynchronously with the fetch function.
Handling Promises: Utilize promises to handle asynchronous operations effectively.

Example:
```
JavaScriptCode:
	
	/** 
	 * Fetches data from a specified URL using the Fetch API.
	 * @param {string} url - The URL to fetch data from.
	 * @returns {Promise} - A promise resolving to the fetched data.
	 */
	function fetchData(url) {
	    return fetch(url)
	        .then(response => response.json())
	        .catch(error => console.error('Error fetching data:', error));
	}
```
# Reading and Writing Files with fs Module
Node.js, a JavaScript runtime, provides the 'fs' module for file system operations. Reading and writing files becomes straightforward:
```
	* Reading Files: Use fs.readFile() to read the contents of a file.
	* Writing Files: Utilize fs.writeFile() to write data to a file.
```

Example:
```
JavaScriptCode:

	const fs = require('fs');

	/** 
	 * Reads the contents of a file.
	 * @param {string} filePath - The path of the file to read.
	 * @returns {Promise} - A promise resolving to the file's contents.
	 */
	function readFile(filePath) {
	    return fs.promises.readFile(filePath, 'utf8');
	}

	/** 
	 * Writes data to a file.
	 * @param {string} filePath - The path of the file to write.
	 * @param {string} data - The data to write to the file.
	 * @returns {Promise} - A promise indicating the success of the write operation.
	 */
	function writeFile(filePath, data) {
	    return fs.promises.writeFile(filePath, data, 'utf8');
	}
```
---

# More info
---
<div align="center">
<h1>Install Node 14</h1>
<p>
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</p>
<h1>Install semi-standard</h1>
<h3>Documentation</h3>
<p>
$ sudo npm install semistandard --global
</p>
<h1>Install request module and use it</h1>
<h3>Documentation</h3>
<p>
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
</p>
</div>

---

[^](#need-to-know)

---
