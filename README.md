# A Novel-Length Writing Prompt Generator

`perec` is a command line tool used for generating a chapter-by-chapter list of writing prompts using the infamous and mult-layered constrained writing system developed by Georges Perec for his masterpiece novel [*Life: A User's Manual*](https://en.wikipedia.org/wiki/Life:_A_User%27s_Manual).

Perec's novel uses a list elements created by the author to create unique (but not random!) writing prompts for each chapter of the book. These lists were made up of things like type of furniture, colors, clothes, types of written works, the titles of actual novels, and much much more.

The lists of elements then get processed into a list if writing prompts using the solutions two types of puzzles that help decide their combinations and order of appearance: [knight's tours](https://en.wikipedia.org/wiki/Knight%27s_tour) and [greco-latin squares](https://handwiki.org/wiki/Graeco-Latin_square).

This process is fairly complicated to explain, something I also hope to refine and make more accessible by working on this project, so I direct you to read [this Wikipedia entry](https://en.wikipedia.org/wiki/Life:_A_User's_Manual#Elements) to get a better idea of the mechanics that made up his book.

Suffice it to say, this project aims to allow a user to recreate this constrained writing system with significantly less time and headache than it took Perec to do for himself.

## What does it do?

Right now, not much. I've played with this idea on-and-off for years now and I've even made a [semi-working but oh so ugly Python script](https://github.com/OulipianSummer/Perecian) that already implements the functionality of this project, but it is brittle and impossible to maintain. In the spirit of constantly improving, I'm starting this project from scratch and trying to build it so it is easier to manage, share, and expand.

What this project *aims* to do is create a terminal program that allows you to do several things:

- Generate and solve [knight's tours](https://en.wikipedia.org/wiki/Knight%27s_tour)
- Generate and solve [latin squares](https://en.wikipedia.org/wiki/Latin_square) and [greco-latin squares](https://handwiki.org/wiki/Graeco-Latin_square)
- Manage csv files containing prompt lists
- Manage all of these objects and puzzles in such a way as to transform these disparate bits of data into an utterly unique (but not random!) list of prompts for each chapter of your novel (or stanza of your poetry, or paragraph of your thesis, I don't really care).
- Walk the user through the entire process of making and and managing a constrained writing project using this system through a tutorial and wiki that makes these somewhat abstract ideas more tangible.

## Still in development

I am actively developing this project, so be aware that this program is likely to change. A lot.

It is in early-enough stages that I am currently not accepting pull requests, but I am open to discuss features you might like to see in this tool as I'm building it! Feel free to email me directly or open a new thread in the "Discussions" tab.
