sphinx-cook
===========

Make sphinx easier for end users.

Requirements
------------

Sphinx-cook based on sphinx (python documentation generator).

Following repository is fork from official sphinx and contains improvements (clean themes and mobi support, etc...).

* https://bitbucket.org/lyhcode/sphinx

Install sphinx-cook
-------------------

	wget https://github.com/contpub/sphinx-cook/raw/master/bin/sphinx-cook
	sudo mv sphinx-cook /usr/bin
	sudo chmod a+x /usr/bin/sphinx-cook

Using sphinx-cook
-----------------

Clone BookTemplate into path-of-your-ebook.

    git clone git://github.com/contpub/BookTemplate.git path-of-your-ebook

And, cook it:

	cd path-of-your-ebook
	sphinx-cook .

Sphinx-cook will create a "cook" sub-folder in your ebook folder.
It contains following outputs:

* *.epub
* *.mobi
* *.pdf

