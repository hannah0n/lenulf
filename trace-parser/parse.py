# !/usr/bin/python3
import sys
import importlib
from nltk import word_tokenize
from self_attentive_parser.src import main as cf_parser

def clean_sent(sent):
    """
    sent: a string sentence

    Rewrites the sentence in a more desirable format. Tokenizes words in the given sentence,
    removes unnecessary and uneven quotation marks (", ', `), and replace parentheses to
    LRB and RRB to follow Penn Treebank style.
    """
    # remove unnecessary quotes
    if (sent.count('``') + sent.count("''") + (sent.count('"')) == 2) != 0 and \
            sent[0] in {'"', "`", "'"} and sent[-1] in {'"', "`", "'"}:
        sent = sent.split(" ", 1)[1].rsplit(" ", 1)[0]

    # tokenize each word in the sentence and put them back together
    sent = " ".join(word_tokenize(sent))

    # for PTB style parsing, replace parentheses to LRB and RRB
    sent = sent.replace("(", "-LRB-").replace(")", "-RRB-")

    return sent

def run_cf_parser(sent):
    """
    sent: a string sentence

    Converts the given sentence into a PTB augmented tree by using
    a parsing model trained by Kitaev & Klein parser using BERT.
    """
    # Create a new file in a directory which contains the pre-trained model for converting
    # a sentence to a PTB augmented tree, and write the sentence to the file
    with open('trace-parser/sent.txt', 'w') as f:
        f.write(sent)

    cf_parser.main(['parse', '--model-path-base', 'trace-parser/ptb2cf/data/model-BERT_dev=94.81.pt', '--input-path', 'trace-parser/sent.txt', '--output-path', 'trace-parser/cf.aug'])

def main():
    # This program takes one argument (one sentence)
    sent = clean_sent(sys.argv[1])
    run_cf_parser(sent)

if __name__ == "__main__":
    # execute only if run as a script
    main()