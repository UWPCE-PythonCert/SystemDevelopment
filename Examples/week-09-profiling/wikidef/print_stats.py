import pstats

prof = pstats.Stats('wikidef.prof')
prof.sort_stats('cumulative')
prof.print_stats('^./[a-z]*.py:')
