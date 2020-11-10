(require :asdf)

(pushnew *default-pathname-defaults* asdf:*central-registry* :test #'equal)

(asdf:load-system :ptb2cf)
(use-package :ptb2cf)

(cf->ptb :cf "trace-parser/cf.aug" :ptb "trace-parser/ptb.mrg" :dictionary "trace-parser/ptb2cf/data/dict")