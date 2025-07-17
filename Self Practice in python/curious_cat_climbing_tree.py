def simulate_cat_climb(tree_height, climb_speed):
    cat_position = 0
    progress = []

    while cat_position < tree_height:
        cat_position += climb_speed

        if cat_position > tree_height:
            cat_position = tree_height

        spaces = ' ' * (cat_position - 1)
        if cat_position == tree_height:
            progress.append(f"Height: {cat_position}|{spaces}^ω^ Meow! Top reached!")
        else:
            progress.append(f"Height: {cat_position}|{spaces}^ω^")

    return "\n".join(progress)

print(simulate_cat_climb(30, 2))