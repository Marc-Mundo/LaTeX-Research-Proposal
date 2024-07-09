import os
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties
import textwrap

tasks = {
    "Year 1: Preparation and Initial Research": [
        (
            "Literature Review, Training, and Participant Recruitment",
            [
                "Conduct literature review on prosthetic vision, AI algorithms, and edge computing.",
                "Identify research gaps and formulate research questions.",
                "Undertake initial training on necessary software and hardware.",
                "Begin participant recruitment process.",
            ],
            1,
            4,
        ),
        (
            "Prototype Development and Setup",
            [
                "Develop initial prototypes of AI algorithms (CNNs, GANs).",
                "Set up experimental infrastructure (VR headsets, obstacle courses).",
            ],
            5,
            3,
        ),
        (
            "Preliminary Experiments and Data Collection",
            [
                "Conduct preliminary experiments with basic AI models.",
                "Collect data and perform initial performance evaluation.",
            ],
            8,
            3,
        ),
        (
            "Model Refinement and Reporting",
            [
                "Refine AI models based on preliminary results.",
                "Prepare and submit first-year review and progress report.",
            ],
            11,
            3,
        ),
    ],
    "Year 2: Advanced AI and Pilot Testing": [
        (
            "Advanced Algorithm Development",
            [
                "Implement advanced AI algorithms and adaptive systems.",
                "Continue participant recruitment for pilot testing.",
            ],
            14,
            3,
        ),
        (
            "Data Analysis and Optimization",
            [
                "Analyze pilot test data.",
                "Optimize AI models and integrate edge computing for real-time processing.",
            ],
            17,
            3,
        ),
        (
            "Neurophysiological Studies and Protocol Refinement",
            [
                "Conduct neurophysiological studies (VEPs, fNIRS) on the pilot group.",
                "Refine experimental protocols based on feedback.",
            ],
            20,
            3,
        ),
        (
            "Expanded Pilot Testing and Reporting",
            [
                "Expand pilot testing to include more diverse environments and tasks.",
                "Submit annual review and progress report.",
            ],
            23,
            3,
        ),
    ],
    "Year 3: Full-scale Experiments and Data Analysis": [
        (
            "Behavioral Experiments and Data Collection",
            [
                "Conduct full-scale behavioral experiments with larger participant groups.",
                "Collect extensive performance data.",
            ],
            26,
            3,
        ),
        (
            "Neurophysiological Analysis and Model Tuning",
            [
                "Continue full-scale neurophysiological studies.",
                "Analyze neurophysiological data for patterns and insights.",
            ],
            29,
            3,
        ),
        (
            "Model Optimization and Final Experiments",
            [
                "Fine-tune AI models and adaptive algorithms based on experimental data.",
                "Implement optimization strategies for stimulation parameters.",
            ],
            32,
            3,
        ),
        (
            "Comprehensive Data Analysis and Reporting",
            [
                "Conduct final round of experiments to validate improvements.",
                "Compile and analyze comprehensive dataset.",
                "Prepare and submit third-year review and progress report.",
            ],
            35,
            3,
        ),
    ],
    "Year 4: Final Analysis and Thesis Writing": [
        (
            "In-depth Data Analysis and Findings",
            [
                "Perform in-depth statistical analysis of all collected data.",
                "Draw conclusions and formulate findings.",
            ],
            38,
            3,
        ),
        (
            "Dissertation Writing",
            [
                "Begin writing the dissertation.",
                "Draft chapters on literature review, methodology, and initial results.",
            ],
            41,
            3,
        ),
        (
            "Results Compilation and Defense Preparation",
            [
                "Complete writing of results and discussion chapters.",
                "Prepare for thesis defense and any required revisions.",
            ],
            44,
            3,
        ),
        (
            "Dissertation Finalization and Presentation",
            [
                "Finalize the dissertation.",
                "Submit the dissertation and prepare for the defense.",
                "Present findings at conferences and submit papers to journals.",
            ],
            47,
            3,
        ),
    ],
}

# Path to Helvetica font file
helvetica_path = r"C:\USERS\MARC_\APPDATA\LOCAL\MICROSOFT\WINDOWS\FONTS\HELVETICA.TTF"

# Use Helvetica font
font_helvetica = FontProperties(fname=helvetica_path)
rcParams["font.family"] = font_helvetica.get_name()

# Colors for each phase
colors = ["#d3d3d3", "#87CEFA", "#90EE90", "#FFB6C1"]
phase_labels = ["Phase 1", "Phase 2", "Phase 3", "Phase 4"]

fig, ax = plt.subplots(figsize=(16, 10))

yticks = []
yticklabels = []

for i, (year, activities) in enumerate(tasks.items()):
    color = colors[i % len(colors)]  # Cycle through colors if more than 4 years
    for j, (activity_name, subtasks, start, duration) in enumerate(activities):
        # Flatten the subtasks into a single task for simplicity in the Gantt chart
        combined_task = f"{activity_name}: {', '.join(subtasks)}"
        ax.broken_barh(
            [(start, duration)],
            (i * 10 + j * 2, 1.5),
            facecolors=color,
            edgecolor="none",
        )
        yticks.append(i * 10 + j * 2 + 0.75)
        wrapped_label = "\n".join(textwrap.wrap(activity_name, width=40))
        yticklabels.append(wrapped_label)

# Add vertical lines for year cutoffs
for i in range(1, len(phase_labels)):
    ax.axvline(x=i * 12, color="black", linestyle="-", linewidth=1)

# Add legend for the phases using proxy artists
legend_handles = [
    plt.Line2D([0], [0], color=colors[i], lw=4, label=phase)
    for i, phase in enumerate(phase_labels)
]
ax.legend(handles=legend_handles, loc="lower right", frameon=False, fontsize=14)
# Set labels and ticks
ax.set_xlabel("Months", fontsize=14, fontweight="bold", fontproperties=font_helvetica)
ax.set_xticks(range(1, 49))  # Set x-ticks from 1 to 48
ax.set_xlim(1, 48)  # Set the x-axis limit to ensure it covers 1 to 48
ax.set_yticks(yticks)
ax.set_yticklabels(yticklabels, fontsize=14, fontproperties=font_helvetica)
ax.grid(True, linestyle="--", alpha=0.6)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(0.5)
ax.spines["bottom"].set_linewidth(0.5)

# plt.title("Gantt Chart of the 4-Year Project")

# Adjust layout to prevent clipping
plt.tight_layout()

# CD to Gannt_chart folder
os.chdir("Gannt_chart")

# Define save path
save_path = "timetable.png"

# Save the figure as an image file with bounding box tight to prevent clipping
fig.savefig("timetable.png", dpi=300, bbox_inches="tight")

plt.show()
