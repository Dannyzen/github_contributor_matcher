Github Contributor Matcher
=====

Imagine you work at a company that has _a lot_ of open source committers in many many projects. And now imagine you're responsible for the happys of some users that may use some of those projects. At times you might want to answer the question: "HEY! I work at `<org>`! Maybe there's someone at `<org>` who is working on `<project>/<repository>` that I can talk to about `<repository>`!"

This script attempts to answer that question.

Usings
=====

usage: `contributor_matcher <organization> <project> <repository>`


example: `contributor_matcher openshift kubernetes kubernetes` would print all users in the kubernetes/kubernetes project that are associated to the "openshift" organization in github. 

Contributors
====

@dannyzen
@maxdotdotg

Thanks
=====

@sigmavirus24 & the rest of the contributors on the [github3.py](https://github.com/sigmavirus24/github3.py/graphs/contributors) project
