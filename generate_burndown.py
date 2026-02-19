#!/usr/bin/env python3
"""
TrueSight Sprint 0 Burndown Chart Generator
Generates professional burndown and velocity charts
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

# Set professional style
plt.style.use('seaborn-v0_8-darkgrid')

def create_sprint0_burndown():
    """Generate Sprint 0 burndown chart with actual TrueSight data"""
    
    # Sprint 0 actual data (February 4-18, 2026) - 15 days
    dates_str = [
        "2026-02-04", "2026-02-05", "2026-02-06", "2026-02-07",
        "2026-02-08", "2026-02-09", "2026-02-10", "2026-02-11",
        "2026-02-12", "2026-02-13", "2026-02-14", "2026-02-15",
        "2026-02-16", "2026-02-17", "2026-02-18"
    ]
    
    # Actual remaining tasks each day (from burndown chart provided)
    actual_remaining = [4, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 0, 0, 0, 0]
    
    # Convert dates to datetime objects
    dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates_str]
    
    # Create ideal burndown (linear from 4 to 0)
    ideal_burndown = np.linspace(4, 0, len(dates))
    
    # Create figure with larger size
    fig, ax = plt.subplots(figsize=(16, 9), dpi=150)
    
    # Plot ideal burndown (blue line)
    ax.plot(dates, ideal_burndown,
            marker='o',
            markersize=10,
            linewidth=3,
            color='#1f77b4',
            label='Ideal Burndown',
            alpha=0.8,
            zorder=2)
    
    # Plot actual burndown (orange line) 
    ax.plot(dates, actual_remaining,
            marker='o',
            markersize=10,
            linewidth=3,
            color='#ff7f0e',
            label='Actual Remaining Tasks',
            alpha=0.9,
            zorder=3)
    
    # Highlight sprint completion
    completion_date = dates[11]  # Feb 15 (index 11)
    ax.axvline(x=completion_date, color='green',
               linestyle='--', linewidth=2, alpha=0.7,
               label=f'Sprint Completed: 15/02/2026')
    ax.scatter([completion_date], [0], s=300, c='green',
               marker='*', zorder=5, edgecolors='black', linewidth=2)
    
    # Title
    ax.set_title('TrueSight Sprint 0 Burndown (04/02/2026 - 18/02/2026)\n' +
                 'Completed: 4/4 tasks (100%) | Finished 3 days early',
                 fontsize=20,
                 fontweight='bold',
                 pad=20)
    
    # Labels
    ax.set_xlabel('Date', fontsize=14, fontweight='bold')
    ax.set_ylabel('Remaining Tasks', fontsize=14, fontweight='bold')
    
    # Format dates
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.xticks(rotation=45, ha='right', fontsize=11)
    
    # Gridlines
    ax.grid(True, alpha=0.4, linestyle='--', linewidth=0.8)
    ax.set_axisbelow(True)
    
    # Y-axis
    ax.set_ylim(bottom=-0.3, top=4.5)
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    
    # Legend
    ax.legend(loc='upper right',
              fontsize=13,
              frameon=True,
              shadow=True,
              fancybox=True,
              framealpha=0.95)
    
    # Status info box
    textstr = '✅ Sprint Completed\n100% Complete\n4/4 Tasks Done\n3 Days Early'
    props = dict(boxstyle='round', facecolor='lightgreen', alpha=0.9)
    ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=12,
            verticalalignment='top', bbox=props, family='monospace',
            fontweight='bold')
    
    plt.tight_layout()
    
    # Save high-resolution outputs
    plt.savefig('docs/images/charts/sprint0_burndown.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('docs/images/charts/sprint0_burndown.pdf', format='pdf', bbox_inches='tight', facecolor='white')
    
    print("✅ Sprint 0 burndown chart created successfully!")
    print("   📁 docs/images/charts/sprint0_burndown.png (300 DPI)")
    print("   📁 docs/images/charts/sprint0_burndown.pdf")
    
    plt.close()


def create_velocity_chart():
    """Create velocity tracking chart"""
    
    fig, ax = plt.subplots(figsize=(12, 7), dpi=150)
    
    sprints = ['Sprint 0']
    tasks = [4]
    
    bars = ax.bar(sprints, tasks,
                  color='#2ecc71',
                  alpha=0.8,
                  edgecolor='black',
                  linewidth=2)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)} tasks\n100%',
                ha='center', va='bottom',
                fontsize=14, fontweight='bold')
    
    ax.set_title('TrueSight Team Velocity - Sprint 0',
                 fontsize=20, fontweight='bold', pad=20)
    ax.set_xlabel('Sprint', fontsize=14, fontweight='bold')
    ax.set_ylabel('Tasks Completed', fontsize=14, fontweight='bold')
    
    ax.grid(True, alpha=0.3, axis='y', linestyle='--')
    ax.set_axisbelow(True)
    ax.set_ylim(0, 5)
    
    plt.tight_layout()
    plt.savefig('docs/images/charts/velocity_sprint0.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('docs/images/charts/velocity_sprint0.pdf', format='pdf', bbox_inches='tight', facecolor='white')
    
    print("✅ Velocity chart created successfully!")
    print("   📁 docs/images/charts/velocity_sprint0.png (300 DPI)")
    print("   📁 docs/images/charts/velocity_sprint0.pdf")
    
    plt.close()


if __name__ == "__main__":
    print("=" * 70)
    print("🔍 TrueSight Sprint 0 Burndown Chart Generator")
    print("=" * 70)
    print()
    
    # Generate charts
    create_sprint0_burndown()
    print()
    create_velocity_chart()
    print()
    print("✅ All charts generated successfully!")
    print()
    print("📊 Next steps:")
    print("   1. Charts saved to: docs/images/charts/")
    print("   2. Commit to repository")
    print("   3. Charts will display in Wiki automatically")
    print()
    print("=" * 70)
