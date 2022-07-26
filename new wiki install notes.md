# new wiki install notes

Notes on attempting to start up a new MW using the starter-repo

2022-07-25:

1. used the `git clone --recurse-submodules ...` command to establish the starter wiki vault
	- n.b.: massivewikibuilder submodule is installed at v1.7.1
	- need to upgrade it to v1.9.0 with `git submodule update --remote` command next (DONE)
	- get your Python on

- breakdown: themes and static directory
- `git submodule update --recursive --remote


test case. here is my plan:

1.  clone a starter wiki using the clone with remote submodules
2.  add content; insure that MWB works
3.  update the MWB submodule code by copying the 2.0 files
4.  insure that MWB works
5.  then update my copy of MWB main branch
6.  check in those changes
7.  clone another starter wiki including submodules
8.  add content; insure MWB works