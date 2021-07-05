# This file contain CLI implemented using click library

import click
import db_api
from term import Term
from set import Set
from definition import Definition
from sentence import Sentence
from term_class import TermClass
from sqlalchemy import select


@click.group()
@click.pass_context
def app(ctx):
    pass


# TODO: Multiple parameters
@click.command()
@click.option('--tables', '-t', default='terms')
@click.pass_context
def show(ctx, tables):
    tables = [table.strip().lower() for table in tables.split()]
    for table in tables:
        rows = db_api.get_table(ctx.obj['session'], table)
        if rows is not None:
            print(f'------------{table.upper()}------------')
            for row in rows:
                print(row[0])
        else:
            print(f'There is not "{table}" table')


@click.command()
@click.argument('term')
@click.argument('translation')
@click.option('--class-name', '-tc', prompt='Enter term class')
@click.option('--set-name', '-s', prompt='Enter set name')
@click.option('--add-definitions', '-def', is_flag=True)
@click.option('--add-sentences', '-sen', is_flag=True)
@click.pass_context
def add(ctx, term, translation, class_name, set_name, add_definitions, add_sentences):
    """Subcommand of CLI. It's purpose is to get info about new term and add it into DB."""
    session = ctx.obj['session']
    term_class = db_api.get_term_class(session, class_name)
    if term_class is None:
        print(f'There is not "{class_name}" term class.')
        return
    set = db_api.get_set(session, set_name)
    if set is None:
        print(f'There is not "{set_name}" set.')
        return
    definitions = []
    if add_definitions:
        while True:
            definition = input('Enter definition: ')
            if definition == '':
                break
            else:
                definitions.append(definition.strip().lower())
    sentences = []
    if add_sentences:
        while True:
            sentence = input('Enter sentence: ')
            if sentence == '':
                break
            else:
                sentences.append(sentence.strip())
    db_api.add_term(session, term, translation, term_class, set, sentences, definitions)


@click.command()
@click.argument('set_name')
@click.pass_context
def add_set(ctx, set_name):
    db_api.add_set(ctx.obj['session'], set_name)


app.add_command(add)
app.add_command(add_set)
app.add_command(show)


if __name__ == '__main__':
    app()