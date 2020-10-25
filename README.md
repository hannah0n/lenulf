# Len's Preliminary ULF parser

This is an SBCL-ported and ASDF packaged version of Len's preliminary tree-to-ULF parser.


## Running the parser

If you would like to use this directly, without asdf or quicklisp, similar to
the original unpackaged system, you can use `init.lisp` and go into the
`lenulf` package.
```
* (load "init")
[loading messages....]
* (in-package :lenulf)

#<PACKAGE "LENULF">
* (english-to-ulf "This is a sentence")
[processing messages...]
(THIS.D~1 (IS.AUX~2 (A.D~3 SENTENCE.N~4)))
```

I would recommend making this accessible to quicklisp (by adding a symbolic
link to this directory in the quicklisp local projects directory--default is
`~/quicklisp/local-projects`). Then you can do the following.
```
* (ql:quickload :lenulf)
* (in-package :lenulf)
* (english-to-ulf "This is a sentence")
[processing messages...]
(THIS.D~1 (IS.AUX~2 (A.D~3 SENTENCE.N~4)))
```
The processing messages can be removed by setting the `*show-stages*` parameter
to `nil`.
```
* (ql:quickload :lenulf)
* (in-package :lenulf)
* (setf *show-stages* nil)
* (english-to-ulf "This is a sentence")

(THIS.D~1 (IS.AUX~2 (A.D~3 SENTENCE.N~4)))
```
If you would rather stay in your current package, the following code results in
the same input/output from your current package by using the global `*package*`
variable. NB: `intern-symbols-recursive` is from a separate utility package
[gute](https://github.com/genelkim/gute) (previously called
[cl-util](https://github.com/genelkim/cl-util)).
```
* (ql:quickload :gute)
* (ql:quickload :lenulf)
* (gute:intern-symbols-recursive ; intern output symbols to current package
    (let ((*package* (find-package :lenulf)) ; locally set *package* variable so symbols
                                             ; are interned as expected in lenulf
          (lenulf::*show-stages* nil)) ; locally turn off stage printing
      (lenulf:english-to-ulf "This is a sentence"))
    *package*) ; second argument of intern-symbols-recursive

(THIS.D~1 (IS.AUX~2 (A.D~3 SENTENCE.N~4)))
```
If your current package is locked (e.g. the `common-lisp` package in SBCL) you
may need to unlock it. This is common lisp implementation dependent. For SBCL
`(sb-ext:unlock-package *package*)` will do it.

## Original README
```
          PARSING ENGLISH INTO ULF -- PRELIMINARY VERSION
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Simplest usage: in allegro CL, do
  (load "init.lisp")
This will print out some guiding comments.

This is based on the idea that Treebank parses give pretty good POS
assignments. So along with parenteses (ignoring phrase labels), this
comes pretty close to ULF (using POS's to determine ULF atom types).

It does require quite a lot of parse-tree postprocessing (thus, tree
PRE-processing rules, before extracting a ULF), but this can be done 
very modularly with rules written in TT -- a simplification of TTT, 
using position indices in output templates to refer to pieces of an 
input (generalizing the matching in Eta). See the rules in
  "preprocessing-rules.lisp". 

After doing
  (load "init.lisp"),
the "english-to-ulf' function can be used (see "english-to-ulf.lisp" file)

The 'english-to-parse-tree' and 'parse-tree-to-ulf' functions can also
be used separately..

Initially I used sample *.cmb files from the Brown corpus for development.

I want to add quite a few more rules to "preprocessing-rules.lisp" (NB:
these also need to be added to "preprocess-tree-for-ulf", with attention
to ordering -- not all orderings work!)

I've made some adaptations so that basic BLLIP (Charniak) parses work
as well, but much checking remains to be done, ad in particular, TRACES
(empty constituents corresponding to "moved" phrases) need to be added.)

The lexical-level ULF derivation code is in 
   pos+word-to-ulf.lisp
This also requires loading of "stem.lisp" (a variant of previous versions)

The tree transduction code is in "tt.lisp". There's a documentation file
for tt, viz., "tt-documantation". It's pretty simple!

At the time of writing (Sep 20/20), ULF postprocessing remains to be done
(based on looking at lots of examples of the "raw" ULF deriven from
Brown trees). It's not always clear what should be done in proeprocessing
parse trees or postprocessing ULFs. 

It may also be quite feasible to rewrite the ULF-to-ELF rules in TT.
```
