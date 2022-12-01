def most_op_elf_on_the_block(calories):
    return max(([elf, sum(elf_cal)] for elf, elf_cal in enumerate(calories)), key=lambda sublist: sublist[0])
