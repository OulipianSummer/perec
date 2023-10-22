# What is this directory? 

This is a best-attempt to import parts and pieces of the [pattern](https://github.com/clips/pattern/tree/master) package by The University of Antwerp, Belgium.

This package is designed to act as an advanced web miner and content scraper for training Machine Learning programs.

It also happens to be a fantastic tool for parsing natural language input, which is what we're interested in.

The original package is pretty large, too large for our purposes here, and it has a long dependency chain including tools we simply will not use. As a result, it seems best to only import the parts we want as a sort of polyfill library, at least until we can figure something else out.

The functions we're interested in are found in the `inflect.py` file: `singularize` and `pluralize`.

It isn't clear whether or not there are more functions or tools we may want to import later, but as of last writing these two functions are tested to work and are good enough for now.