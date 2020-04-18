" Change the color scheme from a list of color scheme names.
" Version 2010-09-12 from http://vim.wikia.com/wiki/VimTip341
" Press key:
"   F8                next scheme
"   Shift-F8          previous scheme
"   Alt-F8            random scheme
" Set the list of color schemes used by the above (default is 'all'):
"   :SetColors all              (all $VIMRUNTIME/colors/*.vim)
"   :SetColors my               (names built into script)
"   :SetColors blue slate ron   (these schemes)
"   :SetColors                  (display current scheme names)
" Set the current color scheme based on time of day:
"   :SetColors now
if v:version < 700 || exists('loaded_setcolors') || &cp
  finish
endif

let loaded_setcolors = 1
" 'slate', 'torte', 'darkblue', 'delek', 'murphy', 'elflord', 'pablo', 'koehler'
let s:mycolors = ['gruvbox', 'PaperColor', 'colorsbox-stbright', 'rupza', 'smyck', 'turtles']  " colorscheme names that we use to set color

function! GetColorschemes()
    " Get a list of all the runtime directories by taking the value of that
    " option and splitting it using a comma as the separator.
    let rtps = split(&runtimepath, ",")
    " This will be the list of colorschemes that the function returns
    let listcolorschemes = []

    " Loop through each individual item in the list of runtime paths
    for rtp in rtps
        let colors_dir = rtp . "/colors"
        " Check to see if there is a colorscheme directory in this runtimepath.
        if (isdirectory(colors_dir))
            " Loop through each vimscript file in the colorscheme directory
            for color_scheme in split(glob(colors_dir . "/*.vim"), "\n")
                " Add this file to the colorscheme list with its everything
                " except its name removed.
                call add(listcolorschemes, fnamemodify(color_scheme, ":t:r"))
		"echo color_scheme
            endfor
        endif
    endfor

    " This removes any duplicates and returns the resulting list.
    return uniq(sort(listcolorschemes))
endfunction

" Set list of color scheme names that we will use, except
" argument 'now' actually changes the current color scheme.
function! s:SetColors(args)
  if len(a:args) == 0
    echo 'Current color scheme names:'
    let i = 0
    while i < len(s:mycolors)
      echo '  '.join(map(s:mycolors[i : i+4], 'printf("%-14s", v:val)'))
      let i += 5
    endwhile
  elseif a:args == 'all'
    let paths = split(globpath(&runtimepath, 'colors/*.vim'), "\n")
    let s:mycolors = uniq(sort(map(paths, 'fnamemodify(v:val, ":t:r")')))
    echo 'List of colors set from all installed color schemes'
  elseif a:args == 'sysall'
    let s:mycolors = GetColorschemes()
    echo 'List of colors set from all installed color schemes'
  elseif a:args == 'my'
    let c1 = 'default elflord peachpuff desert256 breeze morning'
    let c2 = 'darkblue gothic aqua earth black_angus relaxedgreen'
    let c3 = 'darkblack freya motus impact less chocolateliquor'
    let s:mycolors = split(c1.' '.c2.' '.c3)
    echo 'List of colors set from built-in names'
  elseif a:args == 'now'
    call s:HourColor()
  else
    let s:mycolors = split(a:args)
    echo 'List of colors set from argument (space-separated names)'
  endif
endfunction

command! -nargs=* SetColors call s:SetColors('<args>')

" Set next/previous/random (how = 1/-1/0) color from our list of colors.
" The 'random' index is actually set from the current time in seconds.
" Global (no 's:') so can easily call from command line.
function! NextColor(how)
  call s:NextColor(a:how, 1)
endfunction

" Helper function for NextColor(), allows echoing of the color name to be
" disabled.
function! s:NextColor(how, echo_color)
  if len(s:mycolors) == 0
    call s:SetColors('sysall')
  endif
  if exists('g:colors_name')
    echo g:colors_name
    let old_color_name = g:colors_name
    let current = index(s:mycolors, g:colors_name)
  else
    let old_color_name = ""
    let current = -1
  endif
  let missing = []
  let how = a:how
  let alen = len(s:mycolors)
  if how>0
	  let s:mycolors = uniq(s:mycolors[how:-1] + s:mycolors[0:how])
	  let blen = len(s:mycolors)
  else
	  let s:mycolors = uniq(s:mycolors[how-1:-1] + s:mycolors[0:how-1])
	  let blen = len(s:mycolors)
  endif

  try
	  execute 'colorscheme '.s:mycolors[0]
	  "break
	  "catch /E121:/
	  "  echo "Catched E121"
	  "  call add(missing, s:mycolors[current])
	  "  g:colors_name = old_color_name
	  "  call s:NextColor(how>0 : how+1 : how-1, echo_color)
  catch /E185:/
	  call add(missing, s:mycolors[0])
  endtry
  redraw
  "echo g:colors_name + ' ' + s:mycolors[0] + ' ' + alen + ' -> ' + blen + ' ' + s:mycolors[-1]

  return
  for i in range(len(s:mycolors))
    if how == 0
      let current = localtime() % len(s:mycolors)
      let how = 1  " in case random color does not exist
    else
      let current += how
      if !(0 <= current && current < len(s:mycolors))
        let current = (how>0 ? 0 : len(s:mycolors)-1)
      endif
    endif
    try
      execute 'colorscheme '.s:mycolors[current]
      break
    "catch /E121:/
	  "  echo "Catched E121"
    "  call add(missing, s:mycolors[current])
    "  g:colors_name = old_color_name
    "  call s:NextColor(how>0 : how+1 : how-1, echo_color)
    catch /E185:/
      call add(missing, s:mycolors[current])
    endtry
  endfor
  redraw
  if len(missing) > 0
    echo 'Error: colorscheme not found:' join(missing)
  endif
  if (a:echo_color)
    "echo g:colors_name
  endif
endfunction

nnoremap <F8> :call NextColor(1)<CR>
nnoremap <S-F8> :call NextColor(-1)<CR>
"nnoremap <A-F8> :call NextColor(0)<CR>

" Set color scheme according to current time of day.
function! s:HourColor()
  let hr = str2nr(strftime('%H'))
  if hr <= 3
    let i = 0
  elseif hr <= 7
    let i = 1
  elseif hr <= 14
    let i = 2
  elseif hr <= 18
    let i = 3
  else
    let i = 4
  endif
  let nowcolors = 'elflord morning desert evening pablo'
  execute 'colorscheme '.split(nowcolors)[i]
  redraw
  echo g:colors_name
endfunction