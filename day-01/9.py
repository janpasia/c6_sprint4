from bs4 import BeautifulSoup
import re

def generate_html():
    return """
        <html>
            <head></head>
            <body>
                <a href="/a.html">A</a>
                <a href="/b.html">B</a>
                <a href="/c.html">C</a>
                <a href="/d.html">D</a>

                <script>
                    var hello = "yoh";
                    alert(hello);
                </script>
            </body>
        </html>
        """

def main():
    html_doc = generate_html()
    soup = BeautifulSoup(html_doc, 'html5lib')

    errors = None
    for scr in soup.find_all("script"):
        scrExtract = scr.extract()
        alert = re.findall('hello = "(.*\w)', scrExtract.text)
        if len(alert) > 0:
            errors = alert[0]

    print(errors)

if __name__ == "__main__":
    main()