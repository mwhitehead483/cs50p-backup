import re
import sys

  # "Orignal:  <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  #  Shorter:  <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
  #  Shortest:  https://youtu.be/xvFZjo5PgG0"


def parse(html_content):
    # Looser Step 1: Just grabs anything inside the src quotes of an iframe
    match = re.search(r'<iframe[^>]+src=["\']([^"\']+)["\']', html_content, re.IGNORECASE)

    if match:
        src = match.group(1)
        # Step 2: Replace embed with youtu.be, handling http/https and optional www
        return re.sub(r'https?:\/\/(?:www\.)?youtube\.com\/embed\/', 'https://youtu.be/', src, flags=re.IGNORECASE)

    return None

def main():
   # iframe_contents = """ <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> """
     iframe_contents = input("HTML: ")
     result = parse(iframe_contents)
     print(result) # Output: https://www.youtube.com/embed/xvFZjo5PgG0
   # print(parse(iframe_contents))


if __name__ == "__main__":
    main()
