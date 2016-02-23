userfriendly
============
userfriendly scraps userfriendly.org comic images into a rss feed.

Requirements:
-------------
* Python
* Flask
* lxml


Installation:
-------------
* clone Git repo

        git clone https://github.com/lpolasek/userfriendly.git

* satisfy dependencies

        cd userfriendly
        pip install -r requirements.txt

You can also install the dependencies using *virtualenv*.

* test userfriendly

        python wsgi/userfriendly.py

    - open http://127.0.0.1:5000 with a web browser

Live Demo:
----------

You can also try a live demo running at [http://userfriendly-lpolasek.rhcloud.com/rss.xml](http://userfriendly-lpolasek.rhcloud.com/rss.xml).
