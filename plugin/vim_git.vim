python import Git,vim
python git = Git.Git()

function! Git_status()
	python git.status()
endfunction

function! Git_add()
	python git.add()
endfunction

function! Git_commit(message)
	python git.commit(vim.eval("a:message"))
endfunction
