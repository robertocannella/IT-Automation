# Helpful Git Commands


## diff commands
```
    # uncommited file to HEAD
    git diff <path>

    # uncommited file to before last commit
    git diff HEAD^ -- <path>

    #last commit to before last commit
    git diff HEAD^ HEAD -- <path>

    #difference between HEAD and n-th grandparent
    git diff HEAD~n HEAD -- <path>

    #Another cool feature is whatchanged command
    git whatchanged -- <path>
```

## Rename Case Sensitive

```
    git mv casesensitive tmp
    git mv tmp CaseSensitive
```