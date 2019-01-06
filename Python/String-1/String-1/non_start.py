#Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

def make_out_word(out, word):
  return out[:2] + word + out[2:]
