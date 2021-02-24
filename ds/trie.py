def create_trie(list_of_words):
    root = dict()
    for word in list_of_words:
        level = root
        for letter in word:
            pre = level
            if letter not in level:
                level[ letter ] = dict()
            level = level[ letter ]
        pre[ letter ] = '*'
    return root

def add_word( root, word ):
  level = root
  for letter in word:
      pre = level
      if letter not in level:
          level[letter] = dict()
      level = level[letter]
  pre[letter] = '*'

def is_word( root , word ):
    level = root
    for letter in word:
        if letter not in level:
            return False
        level = level[letter]
    if '*' in level:
        return True

# Testing:

words = ['glass','girl','gloss','a']

t = create_trie( words )
add_word(t,'guernica')
print(t)
print(is_word(t , 'glossa'))
print(is_word(t, 'gloss'))
