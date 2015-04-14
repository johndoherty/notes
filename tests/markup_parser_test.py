import markup_parser

result = markup_parser.parse('<html><head><title>Test</title></head>'
    '<body><h1>Parse me!</h1><p>Reminders:</p><ul><li>Do this</li><li>And this</li></ul></body></html>')

assert "Reminders" in result, "No reminders" 
assert len(result["Reminders"]) == 2, "Incorrect number of reminders" 
print "Passed all tests!"
