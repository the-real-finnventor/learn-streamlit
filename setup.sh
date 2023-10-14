mkdir .streamlit
mkdir style
mkdir images

echo "\
[theme]\n\
primaryColor = '#E694FF'\n\
backgroundColor = '#00172B'\n\
secondaryBackgroundColor = '#0083B8'\n\
textColor = '#FFFFFF'\n\
font = "monospace"\
" > .streamlit/config.toml

echo "/
input[type=message], input[type=email], input[type=text], textarea {\n\
  width: 100%;\n\
  padding: 12px;\n\
  border: 1px solid #ccc;\n\
  border-radius: 4px;\n\
  box-sizing: border-box;\n\
  margin-top: 6px;\n\
  margin-bottom: 16px;\n\
  resize: vertical\n\
}\n\
button[type=submit] {\n\
  background-color: #04AA6D;\n\
  color: white;\n\
  padding: 12px 20px;\n\
  border: none;\n\
  border-radius: 4px;\n\
  cursor: pointer;\n\
}\n\
button[type=submit]:hover {\n\
  background-color: #45a049;\n\
}\
" > style/style.css
