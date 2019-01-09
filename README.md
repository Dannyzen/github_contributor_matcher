Github Contributor Matcher
=====

Imagine you work at a company that has _a lot_ of open source committers in many many projects. And now imagine you're responsible for the happys of some users that may use some of those projects. At times you might want to answer the question: "HEY! I work at `<org>`! Maybe there's someone at `<org>` who is working on `<project>/<repository>` that I can talk to about `<repository>`!"

This script attempts to answer that question.

Setup
=====

Requirements:
---

* Python 3
* Pip
* A github account with a personal access token exported to the `GITHUB_TOKEN` environmental variable
* A sense of wonder and curiosity


Want this to work? Follow the directions below. Doesn't work? File an issue. 


Install
---

`pip install github_contributor_matcher`


Authorization:
--- 

Generate a personal access token via Github's Settings - Developer Settings - [Personal Access Token](https://github.com/settings/tokens) page. Grant the token "repo" and "user". Export the token as an environmental variable "GITHUB_TOKEN":


`export GITHUB_TOKEN=your_new_token`


Confirm the token is set by echoing its value when running `echo $GITHUB_TOKEN`.


Usage
---

`github_contributor_matcher <organization> <project> <repository>`


example: `contributor_matcher openshift kubernetes kubernetes` would print all users in the kubernetes/kubernetes project that are associated to the "openshift" organization in github. 

Contributors
=====

@dannyzen
@maxdotdotg

Thanks
=====

@sigmavirus24 & the rest of the contributors on the [github3.py](https://github.com/sigmavirus24/github3.py/graphs/contributors) project


License
=====
[Apache License, Version 2.0](LICENSE.md)
