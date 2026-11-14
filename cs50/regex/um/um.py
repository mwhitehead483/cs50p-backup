import re
import sys


def main():
    print(count(input("Text: ")))

def count(s):
    #  matches all words ignoring white space and punctuation
    matches = re.findall(r"\w+", s.lower())
   # matches = re.findall(r"\bum\b", s, re.IGNORECASE)
  #  return count(matches)
    target = "um"
    return matches.count(target)

if __name__ == "__main__":
    main()
