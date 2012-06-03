#!/usr/bin/python3.2
# This file is an example of a closure (buliding dynamic functions using 
# values of outisde parameters) to iterate through a list of regular 
# expressions which match and replace endings to plurize any given noun.

import re

def build_match_and_apply_functions(pattern, search, replace):
	def matches_rule(word):
		return re.search(pattern, word)
	def apply_rule(word):
		return re.sub(search, replace, word)
	return (matches_rule, apply_rule)

patterns = \
		(
				('[sxz]$', 				'$', 	'es'),
				('[^aeioudgkprt]h$', 	'$', 	'es'),
				('(qu|[^aeiou])y$', 	'y$', 	'ies'),
				('$', 					'$', 	's')
		)
rules = [build_match_and_apply_functions(pattern, search, replace)
		for (pattern, search, replace) in patterns]
def plural(noun):
	for matches_rule, apply_rule in rules:
		if matches_rule(noun):
			return apply_rule(noun)

