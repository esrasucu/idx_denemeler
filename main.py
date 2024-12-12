from flask import Flask, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__) 



@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/sozluk")
def sozluk():
    dictionary = {"elma": "apple", "armut": "pear", "muz": "banana"}
    return render_template("sozluk.html", data=dictionary)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()


@app.route("/katalog")
def katalog():
    
    tree = ET.parse('katalog.xml')
    root = tree.getroot()

    catalog = []
    for cd in root.findall('CD'):
        cd_dict = {}
        for child in cd:
            cd_dict[child.tag] = child.text
        catalog.append(cd_dict)

    return render_template("katalog.html", data=catalog)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()


@app.route("/test")
def test_route():
    data = {
        "data1": "Open Resource Portal",
        "data2": "openresource.net"
    }
    return render_template("test.html", data=data)


@app.route("/tarifler")
def tarifler():
    
    tree = ET.parse('tarifler.xml')
    root = tree.getroot()

    tarifler = []
    for cd in root.findall('CD'):
        cd_dict = {}
        for child in cd:
            cd_dict[child.tag] = child.text
        tarifler.append(cd_dict)

    return render_template("tarifler.html", data=tarifler)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()

