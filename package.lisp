;; Len's Preliminary Treebank to ULF parser
;; Packaged on 2020-10-01

(in-package :cl-user)

(defpackage :lenulf
  (:use :cl)
  (:export english-to-ulf
           parse-tree-to-ulf))

(in-package :lenulf)
(setq *show-stages* t)

