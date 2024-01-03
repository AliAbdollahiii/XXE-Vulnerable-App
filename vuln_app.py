from lxml import etree
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        xml_data = request.get_data()
        result = parse_xml(xml_data)
        return render_template('index.html', result=result)
    else:
        return render_template('index.html', result=None)

def parse_xml(xml_data):
    try:
        parser = etree.XMLParser(resolve_entities=True)  # Use resolve_entities=True
        root = etree.fromstring(xml_data, parser)
        return f'Successfully parsed XML:\n\n{etree.tostring(root, pretty_print=True).decode("utf-8")}'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
