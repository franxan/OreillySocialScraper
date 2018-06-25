<h1 align="center">O'Reilly Social Scraper</h1>

<div align="center">
Discover social circles and collaborations/influence among O'Reilly tech book authors.
</div>

## What to Expect
<div align="center">
<img width="400" src="/static/java_outer.png" alt="Search for Java books zoomed out"><br>
A search for Java books zoomed out<br><br>

<img width="400" src="/static/java_close.png" alt="Search for Java books zoomed in on a specific node"><br>
A search for Java books zoomed in on a specific node<br><br>

</div>
## Introduction
This is a quick weekend/semi-ongoing experiment. Feel free to contribute.<br>
#### TODO
More unit tests, more features, such as also sending node book data to Gephi.

## Initial Set Up
1. Clone this repository
```
git clone https://github.com/michaelfindlater/oreillySocial.git
```
2. Create Python 3 virtual environemnt and install requirements
```
cd oreillySocial/
virtualenv -p `which python3` virtual_environment/
. virtual_environment/bin/activate
```
## Set up Gephi
1. [Install](https://gephi.org/)
2. Update and enable the "Graph Streaming" module
3. Create a new workspace and start the server from the "Streaming" tab<br>
<div align="center">
<img width="200" src="/static/gephi_server.png" alt="Search for Java books zoomed out"><br>
Start the server, make sure you know your IP address and the configured port if not running locally.<br><br>
</div>

#### Hint
_Right click on "Master Server" and click start, the circular icon needs to be green._

## Recommended Settings for Gephi
### Layout
Force Atlas
<div align="center">
<img width="200" src="/static/gephi_force_atlas.png" alt="Search for Java books zoomed out"><br>
Give the Force Atlas layout a go, above are some settings to get started with.<br><br>
</div>

## Build your query and run
### Example
To search all Python books with a delay of 5 seconds per page:
```
python start.py -q "python"
```
#### Notes
1. This is assuming you're running Gephi on localhost:8080. If not you will need to specify the IP and port of your server. See `python start.py -h` for more information on CLI flags.
2. Quotation marks, as above, are not required unless you want to add spaces to your search query.
