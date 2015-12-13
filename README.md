
Vim plugin to call git commands

**Installation**

If you are using [pathogen](https://github.com/tpope/vim-pathogen), clone this repo into the `bundles` folder.

```
cd .vim/bundle/
git clone https://github.com/nu11p01n73R/vim_git.git
```
And you are good to go.

**Configurations**

If you wish to add custom commands to call the functions, then add these lines to your `.vimrc`

```
command GitStatus call Git_status()
command GitAdd call Git_add()
command -nargs=1 GitCommit call Git_commit(<f-args>)
command -nargs=* GitPull call Git_pull(<f-args>)
command -nargs=1 GitPush call Git_push(<f-args>)
```

Also, add the `plugins` folder to your `PYTHONPATH`

```
export PYTHONPATH=${PYTHONPATH}:~/.vim/bundle/vim_git/plugin
```

**Usage**

- To view status,
```
:GitStatus
```

- To add the current file. 
```
:GitAdd
```

- To commit the files
```
:GitCommit "Some commit message"
```

- To pull the current origin branch
```
:GitPull
```

- To pull any origin branch
```
:GitPull master
```
  This will pull the origin master to the current branch
  
- To push changes to origin
```
:GitPush master
```

