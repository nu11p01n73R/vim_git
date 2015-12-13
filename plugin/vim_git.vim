python import Git
python import vim
python git = Git.Git()

function! Git_status()
	python git.status()
endfunction

function! Git_add()
	python git.add([vim.current.buffer.name])
endfunction

function! Git_commit(message)
	python git.commit(vim.eval("a:message"))
endfunction

function! Git_pull(...)
	if a:0
		python 		git.pull(vim.eval("a:1"))
	else
		python 		git.pull()
	endif
endfunction

function! Git_push(branch)
	python git.push(vim.eval('a:branch')
endfunction

