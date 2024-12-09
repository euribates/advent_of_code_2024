#!/usr/bin/env python3

import core


def defrag(directory, trace=False):
    idx_hole, first_hole = directory.first(condition=lambda b: b.is_free())
    if trace:
        print(f'First hole is {first_hole} at index {idx_hole}')
    idx_file, last_file = directory.last(condition=lambda b: b.is_file())
    if trace:
        print(f'Last file is {last_file} at index {idx_file}')
    if idx_hole > idx_file:
        return False
    if first_hole.num_blocks > last_file.num_blocks:
        remain = first_hole.num_blocks - last_file.num_blocks
        if trace:
            print(f'Hole is bigger or equal than file by {remain}')
        first_hole.id_file = last_file.id_file
        first_hole.num_blocks = last_file.num_blocks
        if remain > 0:
            if directory.nodes[idx_hole + 1].is_free():
                directory.nodes[idx_hole + 1].num_blocks += remain
                directory.nodes[idx_hole + 1].id_file = None
            else:
                directory.nodes.insert(idx_hole + 1, core.Node(remain))
                directory.total_blocks += 1
        if trace:
            print('Free file space')
        last_file.id_file = None
    else:
        remain = last_file.num_blocks - first_hole.num_blocks
        moved = first_hole.num_blocks
        if trace:
            print(
                f'Hole [{first_hole.num_blocks}]'
                f' is smaller than file [{last_file.num_blocks}]'
                f' by {remain}, moved: {moved}'
                )
        first_hole.id_file = last_file.id_file
        last_file.num_blocks = remain
        if directory.nodes[-1].is_free():
            directory.nodes[-1].num_blocks += moved
        else:
            directory.add_free(moved)

    index = len(directory.nodes) - 1
    while (
        len(directory.nodes) > 1
        and directory.nodes[index].is_free()
        and directory.nodes[index-1].is_free()
            ):
        removed_node = directory.nodes.pop()
        directory.nodes[-1].num_blocks += removed_node.num_blocks
        directory.total_blocks -= 1
        index -= 1
    return True


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
        print(dd.dump())
    return dd.checksum()


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 9] Sol. part one is: {sol}')
