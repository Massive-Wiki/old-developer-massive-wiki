# new wiki install notes

Notes on attempting to start up a new MW using the starter-repo

2022-07-25:

1. used the `git clone --recurse-submodules ...` command to establish the starter wiki vault
	- n.b.: massivewikibuilder submodule is installed at v1.7.1
	- need to upgrade it to v1.9.0 with `git submodule update --remote` command next (DONE)
	- get your Python on

- breakdown: themes and static directory
- `git submodule update --recursive --remote


test case. here is Bill's plan:

1.  clone a starter wiki using the clone with remote submodules
2.  add content; insure that MWB works
3.  update the MWB submodule code by copying the 2.0 files
4.  insure that MWB works
5.  then update my copy of MWB main branch
6.  check in those changes
7.  clone another starter wiki including submodules
8.  add content; insure MWB works

## Pete, 2022-07-26

### Work steps

- copy search code over from developer wiki into the MWB repo, create a [v2.0.0 release candidate branch and pull request](https://github.com/peterkaminski/massivewikibuilder/pull/38)
- create a release candidate branch in the MWT repo, that is v1.9/v2.0 compliant
- start Bill's test case above, with the RC branches
- ...
- when ready, merge RC branches to main and make new MWB and MWT releases
- convert developer wiki to have v1.9/v2.0 directory structure (including MWB and MWT as submodules)
- update starter wiki repo

### Today I Learned: Submodule update vs. init

this is the "update" incantation:

```shell
git submodule update --recursive --remote
```

but if you're setting up submodules for the first time, you need to do this, to turn the submodules references into Git folders:

```shell
git submodule update --init --recursive
```