# see below for information on the license of this script
header = """[Adblock Plus 2.0]
! Title: ThioJoe YouTube Spam List - unofficial filterlist
! Homepage: https://github.com/iam-py-test/thiojoe_yt_lists/tree/main
! Data source: https://github.com/ThioJoe/YT-Spam-Lists
! Expires: 1 day
! the script was written by iam-py-test and is copyleft
! the data used is maintained by ThioJoe and other contributors, and is licensed under MIT. See the below license:
! MIT License
! Copyright (c) 2021 ThioJoe
! Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
! The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
! THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import requests

data_content = requests.get("https://raw.githubusercontent.com/ThioJoe/YT-Spam-Lists/main/SpamDomainsList.txt").text
data_lines = data_content.replace('\r', '').split("\n")
filter_lines = []
for line in data_lines:
  if line == "" or line.startswith("#"):
    continue
  elif "." in line:
    domain = line
    filter_lines.append(f"||{domain}^$all")
  elif len(line) == 11:
    url_filter = f"||youtube.com/watch?v={line}^$document"
    filter_lines.append(url_filter)
filter_file = open('filter.txt', 'w', encoding='UTF-8')
filter_file.write(header + '\n'.join(filter_lines))
filter_file.close()
