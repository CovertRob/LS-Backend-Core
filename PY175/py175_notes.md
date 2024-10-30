# Notes from working through PY175

- Need to review url_for() syntax

~~~HTML
<a href="{{ url_for('chapter', page_num=loop.index) }}" class="pure-menu-link">{{ chapter }}</a>
~~~

- The above `chapter` name must match the function name in the `app.py` file

- use `app.before_request()` to serve data that should be loaded globally prior to each route call

