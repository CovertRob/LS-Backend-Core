# Notes from working through PY175

- Need to review url_for() syntax

~~~HTML
<a href="{{ url_for('chapter', page_num=loop.index) }}" class="pure-menu-link">{{ chapter }}</a>
~~~

- The above `chapter` name must match the function name in the `app.py` file

- use `app.before_request()` to serve data that should be loaded globally prior to each route call

- In Jinja, `#paragraph{{ index }}` is used within a URL or an anchor link to dynamically create an HTML fragment identifier based on the value of index. Here’s a breakdown of what’s happening:

- What is a Fragment Identifier?
A fragment identifier is the part of a URL that follows the # symbol. When included in a link, it allows the browser to jump directly to a specific section of a page with an id attribute matching the fragment identifier.

- How `#paragraph{{ index }}` Works
`#paragraph` is a prefix for the id attribute of a specific HTML element (like a paragraph or section).
`{{ index }}` is a Jinja variable placeholder, which will be replaced with the actual value of index when the template is rendered.
Together, `#paragraph{{ index }}` generates a unique fragment identifier, such as `#paragraph1`, `#paragraph2`, etc., for each item.

