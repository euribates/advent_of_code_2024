#!/usr/bin/env python3

import core


def defrag(directory, trace=False):
    directory.remove_adjacent_gaps()
    files_to_nodes = {}
    for node in directory.nodes:
        if node.is_file():
            files_to_nodes[node.id_file] = node
    for id_file, node in reversed(files_to_nodes.items()):
        if trace:
            print(
                f'Searching free space to hold {node.num_blocks} bloks'
                f' (file {id_file})',
                end='',
                )
        first_hole = None
        for _index, n in enumerate(directory.nodes):
            if n.is_file():
                if n.id_file == node.id_file:
                    break
            else:
                if n.num_blocks >= node.num_blocks:
                    first_hole = n
                    break
        if first_hole:
            if trace:
                print(f' [ok Found enough space at {first_hole}] _index is {_index}')
                print(' - ', directory.signature())
            gap = first_hole.num_blocks - node.num_blocks
            if gap:
                if directory.nodes[_index + 1].is_free():
                    directory.nodes[_index + 1].num_blocks += gap
                else:
                    directory.nodes.insert(_index + 1, core.Node(gap))
            first_hole.id_file = node.id_file
            first_hole.num_blocks = node.num_blocks
            node.id_file = None
            if trace:
                print(' - ', directory.signature())
        else:
            if trace:
                print(f'[No adjacent space available]')
        directory.remove_adjacent_gaps()
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
