import re
import sys

  # "Orignal:  <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  #  Shorter:  <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
  #  Shortest:  https://youtu.be/xvFZjo5PgG0"

def parse(html_content):
    # Changed [^>]+ to non-greedy [^>]*? so it doesn't swallow 'src'
    match = re.search(r'<iframe\b[^>]*?\bsrc\s*=\s*["\'](https?://(?:www\.)?youtube\.com/embed/[a-zA-Z0-9_-]+)["\']', html_content, re.IGNORECASE)
    if match:
        src = match.group(1)
     # Step 2: Swap the embed base URL with the short youtu.be format
        short = re.sub(
            r'https?://(?:www\.)?youtube\.com/embed/',
            'https://youtu.be/',
            src,
            flags=re.IGNORECASE
        )
    return None

def main():
   # iframe_contents = """ <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> """
     iframe_contents = input("HTML: ")
     result = parse(iframe_contents)
     print(result) # Output: https://www.youtube.com/embed/xvFZjo5PgG0
   # print(parse(iframe_contents))


if __name__ == "__main__":
    main()
