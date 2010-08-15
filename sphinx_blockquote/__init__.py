import docutils.parsers.rst.directives
import sphinx.util.compat
from docutils import nodes

class Blockquote(sphinx.util.compat.Directive):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = dict(
        cite=docutils.parsers.rst.directives.uri,
        author=str,
        )
    has_content = True

    def run(self):
        # TODO want to put options['cite'] in <blockquote cite="...">
        q = nodes.block_quote('')
        for text in self.content:
            # TODO use nested_parse to allow rst markup inside of the
            # blockquote
            q += nodes.Text(text)

        if self.options['author']:
            addr = nodes.Element()
            if self.options['cite']:
                addr += nodes.raw('', '<a href="', format='html')
                addr += nodes.Text(self.options['cite'])
                addr += nodes.raw('', '">', format='html')
            addr += nodes.Text(self.options['author'])
            if self.options['cite']:
                addr += nodes.raw('', '</a>', format='html')
            q += nodes.raw('', '<address>', format='html')
            q += addr.children
            q += nodes.raw('', '</address>', format='html')

        return [q]

def setup(Sphinx):
    Sphinx.add_directive('blockquote', Blockquote)
