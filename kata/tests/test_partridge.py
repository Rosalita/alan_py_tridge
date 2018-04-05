import pytest
from kata.partridge import partridge

def test_no_words_pierce_foot():
  words = []
  alan = partridge(words)
  assert alan == "Lynn I've pierced my foot on a spike!!"

def test_single_word_partridge_gives_a_pint():
  words = ["Partridge"]
  alan = partridge(words)
  assert alan == "Mine's a Pint!"

def test_single_word_pear_tree_gives_a_pint():
  words = ["Pear Tree"]
  alan = partridge(words)
  assert alan == "Mine's a Pint!"

def test_partridge_and_pear_tree_give_a_pint_with_two_exclamations():
  words = ["Partridge", "Pear Tree"]
  alan = partridge(words)
  assert alan == "Mine's a Pint!!"

def test_non_alan_word_pierce_foot():
  words = ["My Little Pony"]
  alan = partridge(words)
  assert alan == "Lynn I've pierced my foot on a spike!!"

def test_single_word_chat_gives_a_pint():
  words = ["Chat"]
  alan = partridge(words)
  assert alan == "Mine's a Pint!"

def test_single_word_dan_gives_a_pint():
  words = ["Dan"]
  alan = partridge(words)
  assert alan == "Mine's a Pint!"

def test_single_word_dan_gives_a_pint():
  words = ["Toblerone"]
  alan = partridge(words)
  assert alan == "Mine's a Pint!"

def test_single_word_lynn_gives_a_pint():
  words = ["Lynn"]
  alan = partridge(words)
  assert alan == "Mine's a Pint!"

def test_single_word_alphapapa_gives_a_pint():
  words = ["AlphaPapa"]
  alan = partridge(words)
  assert alan == "Mine's a Pint!"

def test_single_word_nomad_gives_a_pint():
  words = ["Nomad"]
  alan = partridge(words)
  assert alan == "Mine's a Pint!"

def test_all_the_alan_words_together():
  words = ["Partridge", "Pear Tree", "Chat", "Dan", "Toblerone", "Lynn", "AlphaPapa", "Nomad"]
  alan = partridge(words)
  assert alan == "Mine's a Pint!!!!!!!!"

def test_numbers_pierce_foot():
  words = [3,4,5]
  alan = partridge(words)
  assert alan == "Lynn I've pierced my foot on a spike!!"

def test_leading_and_trailing_space_pierce_foot():
  words = [" Dan "]
  alan = partridge(words)
  assert alan == "Lynn I've pierced my foot on a spike!!"

def test_spaces_in_alan_words_pierce_foot():
  words = ["P a r t r i d g e"]
  alan = partridge(words)
  assert alan == "Lynn I've pierced my foot on a spike!!"

def test_alan_words_in_caps_pierce_foot():
  words = ["TOBLERONE"]
  alan = partridge(words)
  assert alan == "Lynn I've pierced my foot on a spike!!"

def test_a_long_list_containing_naught_strings():
  words = ["Nomad", "😍", "Lynn", "((╯°□°）╯︵ ┻━┻)", "AlphaPapa",  "^%@/£$\^^&", "Toblerone", "<a href='test'>here</a>", " ", "False", "None", "undefined", "NULL", 1000000000000000000, "$HOME"]
  alan = partridge(words)
  assert alan == "Mine's a Pint!!!!"






