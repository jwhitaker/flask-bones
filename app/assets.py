from flask_assets import Bundle, Environment, Filter

# fixes missing semicolon in last statement of jquery.pjax.js
class ConcatFilter(Filter):
    def concat(self, out, hunks, **kw):
        out.write(';'.join([h.data() for h, info in hunks]))

js = Bundle(
    'node_modules/jquery/dist/jquery.js',
    'node_modules/jquery-pjax/jquery.pjax.js',
    'node_modules/bootbox/bootbox.js',
    'node_modules/bootstrap/dist/js/bootstrap.min.js',
    'js/application.js',
    filters=(ConcatFilter, 'jsmin'),
    output='gen/packed.js'
)

css = Bundle(
    'node_modules/bootstrap/dist/css/bootstrap.css',
    'node_modules/font-awesome/css/font-awesome.css',
    'css/style.css',
    filters=('cssmin','cssrewrite'),
    output='gen/packed.css'
)

assets = Environment()
assets.register('js_all', js)
assets.register('css_all', css)
