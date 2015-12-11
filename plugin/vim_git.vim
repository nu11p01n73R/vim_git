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
