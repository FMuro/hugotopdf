#!/bin/bash

# generate the list of shortcodes from two templates

mkdir shortlist_temp
while read item; do
  sed "s/title/${item}/g" block_templates/title_no_name.txt > shortlist_temp/${item}.txt
done < block_lists/no_name.txt
while read item; do
  sed "s/title/${item}/g" block_templates/title_name.txt > shortlist_temp/${item}.txt
done < block_lists/name.txt

# concatenate the shortcodes list together with a custom header and footer

cat shortlist_temp/* > shortlist_temp/shortlist.txt
cat generate/header.txt shortlist_temp/shortlist.txt generate/footer.txt > generate.py
rm -r shortlist_temp

# creating the latex root document

# conversion process

mkdir outputs
while read item; do
  python3 generate.py "${item}" # process the shortcodes to latex
  pandoc outputs/${item}.md -f markdown -t latex --mathjax -o outputs/${item}.tex # post-process the rest of the document to latex
  tail -n +2 "outputs/${item}.tex" > outputs/${item}.tmp # remove first line which contains leftovers from Hugo headers
  mv outputs/${item}.tmp outputs/${item}.tex
  sed -i "s/\\\_/_/g" outputs/${item}.tex # replace \_ with _
  sed -i "s/\\\\{/\\{/g" outputs/${item}.tex # replace \\{ with \{
  sed -i "s/\\\\}/\\}/g" outputs/${item}.tex # replace \\} with \}
  sed -i "s/−/-/g" outputs/${item}.tex # replace − with -
  sed -i "s/\\\!/\\!/g" outputs/${item}.tex # replace \\! with \!
  sed -i "s#\.\./\.\.#static#g" outputs/${item}.tex # fix images path
  sed -i "s#\.\.#static#g" outputs/${item}.tex
done < ../tree.txt

# compile with latex

cd ..
latexmk --lualatex -jobname=static/docs/latex latex.tex
cd hugotopdf
rm -r outputs

# open PDF

gio open ../static/docs/latex.pdf
