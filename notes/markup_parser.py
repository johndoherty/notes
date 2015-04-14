from HTMLParser import HTMLParser

tracked_tags = {"reminders": "list"}

class GeneratedHTMLParser(HTMLParser):
    parse_dict = {}
    parsing_tracked_tag = None
    parsing_tag = None

    def get_parsed(self):
        return self.parse_dict

    def handle_starttag(self, tag, attrs):
        self.parsing_tag = tag

    def handle_endtag(self, tag):
        self.parsing_tag = None

    def handle_data(self, data):
        if self.parsing_tracked_tag is None:
            tag = data.strip().lower()
            if tag[-1] == ':':
                tag = tag[:-1]

            if tag in tracked_tags:
                self.parsing_tracked_tag = tag
        else:
            if tracked_tags[self.parsing_tracked_tag] == "list" and self.parsing_tag == "li":
                if self.parsing_tracked_tag not in self.parse_dict:
                    self.parse_dict[self.parsing_tracked_tag] = []
                self.parse_dict[self.parsing_tracked_tag].append(data.strip())


def parse(html_string):
    parser = GeneratedHTMLParser()
    parser.feed(html_string)
    return parser.get_parsed()

