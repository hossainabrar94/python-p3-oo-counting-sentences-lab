#!/usr/bin/env python3

class MyString:
  def __init__(self, value='', is_sentence=False):
    self.value = value

  @property
  def value(self):
    return self._value
  @value.setter
  def value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")


  def is_sentence(self):
    return self.value[-1] =='.'

  def is_question(self):
    return self.value[-1] =='?'

  def is_exclamation(self):
    return self.value[-1] =='!'

  def count_sentences(self):
    count = self.value.count('.')
    count += self.value.count('?')
    count += self.value.count('!')
    return count