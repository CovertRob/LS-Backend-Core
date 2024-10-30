from flask import Flask, render_template, g, redirect, request

app = Flask(__name__)

@app.before_request
def load_contents():
    with open("book_viewer/data/toc.txt", "r") as file:
        g.contents = file.readlines()

@app.route("/")
def index():
    return render_template('home.html', contents=g.contents)

@app.route("/chapters/<page_num>")
def chapter(page_num):
    if page_num.isdigit() and (1 <= int(page_num) <= len(g.contents)):
        with open("book_viewer/data/toc.txt", "r") as file:
            contents = file.readlines()

        chapter_name = contents[int(page_num) - 1]
        title = f"Chapter {page_num}: {chapter_name}"

        with open(f"book_viewer/data/chp{page_num}.txt") as file:
            chapter_content = file.read()

        return render_template('chapter.html', title=title, contents=g.contents, chapter=chapter_content)
    else:
        return redirect("/")

def chapters_matching(query):
    if not query:
        return []

    results = []
    for index, name in enumerate(g.contents, start=1):
        with open(f"book_viewer/data/chp{index}.txt", "r") as file:
            chapter_content = file.read()
        if query.lower() in chapter_content.lower():
            results.append({'number': index, 'name': name})

    return results

@app.route("/search")
def search():
    query = request.args.get('query', '')
    results = chapters_matching(query) if query else []
    return render_template('search.html', query=query, results=results)
    
@app.template_filter('in_paragraphs')
def in_paragraphs(chp_content):
    paragraphs = chp_content.split("\n\n")
    print(paragraphs)
    modified_content = '<p>'
    for paragraph in paragraphs:
        modified_content += (paragraph + '</p>')
    
    return modified_content

@app.errorhandler(404)
def page_not_found(_error):
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5003)