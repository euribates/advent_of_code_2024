#!/usr/bin/env python3

import core


def defrag(directory, trace=False):
    files_to_nodes = {}
    for node in directory.nodes:
        if node.is_file():
            files_to_nodes[node.id_file] = node

    for id_file, node in reversed(files_to_nodes.items()):
        assert directory.no_adjacent_gaps()
        print(
            f'Buscando hueco para acomodar {node.num_blocks}'
            f' (file {id_file})',
            end='',
            )
        _index, first_hole = directory.first(
            lambda b: b.num_blocks >= node.num_blocks
                      and b.is_free()
            )
        if first_hole and _index <= id_file:
            print(f' [ok Encontrado hueco en {first_hole}]')
            print(' - ', directory.signature())
            gap = first_hole.num_blocks - node.num_blocks
            if gap:
                if directory.nodes[_index + 1].is_free():
                    print('Fusion!')
                    directory.nodes[_index + 1].num_blocks += gap
                else:
                    directory.nodes.insert(_index + 1, core.Node(gap))
                    print('Insert!')
            first_hole.id_file = node.id_file
            first_hole.num_blocks = node.num_blocks
            node.id_file = None
            print(' - ', directory.signature())
        else:
            print(f'[No encuntro hueco]')
    return False


def main(options):
    dd = core.Directory()
    for (id_file, num_blocks, empty) in core.load_input(options.filename):
        dd.add_file(id_file, num_blocks)
        if empty is not None:
            dd.add_free(empty)
    flag = defrag(dd, options.trace)
    while flag:
        if options.trace:
            print(dd.signature())
        flag = defrag(dd, options.trace)
    if options.trace:
        print(dd.signature())
        print('Terminada defragmentacion')
    return dd.checksum()


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 9] Sol. part two is: {sol}')
