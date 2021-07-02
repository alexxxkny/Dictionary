import click
from term import Term


@click.group()
def app():
    print('App')


@click.command()
@click.argument('term')
@click.argument('translation')
def add(term, translation):
    new_term = Term(term, translation)
    print(new_term)


@click.command()
@click.argument('term_class')
def add_class(term_class):
    print(f'{term_class}')


app.add_command(add)
app.add_command(add_class)


if __name__ == '__main__':
    app()