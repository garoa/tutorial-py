# coding: utf-8

r"""
A função ``elem`` gera elementos HTML:

    >>> elem('bla')
    '<p>bla</p>'
    >>> elem('bla', tag='div')
    '<div>bla</div>'
    >>> elem(tag='span', texto='bling')
    '<span>bling</span>'
    >>> params = {'tag':'h1', 'texto':'Viva!'}
    >>> elem(**params)
    '<h1>Viva!</h1>'
    >>> params = ['Bang', 'Bong']
    >>> elem(*params, tag='h2')
    '<h2>Bang</h2>\n<h2>Bong</h2>'
    >>> elem('bla', style='bold', class_='blink', tag='a')
    '<a class="blink" style="bold">bla</a>'
    >>> print(elem('alfa', 'bravo', 'charlie'))
    <p>alfa</p>
    <p>bravo</p>
    <p>charlie</p>

"""

def elem(texto, *mais_textos, tag='p', **kwargs):
    template = '<{tag}{atribs}>{conteudo}</{tag}>'
    if kwargs:
        atribs = []
        for nome, valor in sorted(kwargs.items()):
            if nome == 'class_':
                nome = 'class'
            atribs.append('{}="{}"'.format(nome, valor))
        atribs = ' ' + ' '.join(atribs)
    else:
        atribs = ''
    textos = [texto]
    textos.extend(mais_textos)
    saida = []
    for conteudo in textos:
        saida.append(template.format(tag=tag, conteudo=conteudo, atribs=atribs))
    saida = '\n'.join(saida)
    return saida