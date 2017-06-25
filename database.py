import sqlite3

db = sqlite3.connect('philadelphia.db')
c = db.cursor()
query = '''SELECT nodes_tags.value, COUNT(*) as num
FROM nodes_tags
JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE key = 'shop') sub
ON sub.id = nodes_tags.id
WHERE nodes_tags.key = 'name'
GROUP BY nodes_tags.value
ORDER BY num desc
LIMIT 5;
           '''
c.execute(query)
rows = c.fetchall()

# First, what data structure did we get?
print "Row data:"
for row in rows:
  print row[0]

db.close()