import sys
import simhash

with open('../data.csv', 'rb') as f:
    companies = [c.strip() for c in f]

hashes = [simhash.hash(x) for x in companies]
d = {h: c for h, c in zip(hashes, companies)}

corpus = simhash.Corpus(32, 16)
corpus.insert_bulk(hashes)

matches = corpus.find_all_bulk(hashes)

results = filter(lambda e: len(set(e)) > 1, matches)

print >> sys.stderr, 'There are %d candidates duplicates' % len(results)

seen = set()

for l in results:
    s = set(l)
    for m in s:
        if m not in seen:
            print d[m]
            seen.add(m)
    print '----'
