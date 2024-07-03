import matplotlib.pyplot as plt
import matplotlib.patches as patches


def create_diagram():
    fig, ax = plt.subplots(figsize=(14, 10))

    box_width = 0.0002  # Adjusted width
    box_height = 0.0001  # Adjusted height

    # Coordinates for the boxes
    coordinates = [
        (0.1, 0.8),  # Step 1: Initialization
        (0.1, 0.6),  # Step 2: Stimulation Parameters
        (0.1, 0.4),  # Step 3: Phosphene Characteristics
        (0.5, 0.8),  # Step 4: Rendering Phosphenes
        (0.5, 0.6),  # Step 5: Summing Renderings
        (0.5, 0.4),  # Step 6: Temporal Dynamics
        (0.8, 0.6),  # Step 7: Modular Design
        (0.8, 0.4),  # Step 8: Validation and Application
    ]

    # Box colors
    colors = [
        "skyblue",
        "lightgreen",
        "lightcoral",
        "gold",
        "violet",
        "orange",
        "lightpink",
        "lightgray",
    ]

    # Box labels
    labels = [
        "Initialization",
        "Stimulation\nParameters",
        "Phosphene\nCharacteristics",
        "Rendering\nPhosphenes",
        "Summing\nRenderings",
        "Temporal\nDynamics",
        "Modular and\nOpen-Source Design",
        "Validation and\nApplication",
    ]

    boxes = []

    for i, (x, y) in enumerate(coordinates):
        rect = patches.FancyBboxPatch(
            (x, y),
            box_width,
            box_height,
            boxstyle="round,pad=0.1",
            ec="black",
            fc=colors[i],
        )
        ax.add_patch(rect)
        ax.text(
            x + box_width / 2,
            y + box_height / 2,
            labels[i],
            ha="center",
            va="center",
            fontsize=10,
            weight="bold",
        )
        boxes.append(rect)

    # Arrows
    arrowprops = dict(facecolor="black", arrowstyle="->")
    arrow_coordinates = [
        (0.1 + box_width / 2, 0.8, 0.1 + box_width / 2, 0.6 + box_height),  # 1 to 2
        (0.1 + box_width / 2, 0.6, 0.1 + box_width / 2, 0.4 + box_height),  # 2 to 3
        (0.1 + box_width / 2, 0.4, 0.5 + box_width / 2, 0.8 + box_height),  # 3 to 4
        (0.5 + box_width / 2, 0.8, 0.5 + box_width / 2, 0.6 + box_height),  # 4 to 5
        (0.5 + box_width / 2, 0.6, 0.5 + box_width / 2, 0.4 + box_height),  # 5 to 6
        (0.5 + box_width / 2, 0.4, 0.8 + box_width / 2, 0.6 + box_height),  # 6 to 7
        (0.8 + box_width / 2, 0.6, 0.8 + box_width / 2, 0.4 + box_height),  # 7 to 8
    ]

    for x1, y1, x2, y2 in arrow_coordinates:
        ax.annotate("", xy=(x1, y1), xytext=(x2, y2), arrowprops=arrowprops)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    plt.title("Visual Cortical Prostheses Simulation Steps", fontsize=16, weight="bold")
    plt.show()


create_diagram()
