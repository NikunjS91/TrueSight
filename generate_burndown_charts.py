#!/usr/bin/env python3
"""
TrueSight Sprint 0 Burndown Chart Generator
Generates professional burndown charts in standard and enhanced versions
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

# Sprint 0 Data
dates_str = ["2026-02-04", "2026-02-05", "2026-02-06", "2026-02-07", "2026-02-08",
             "2026-02-09", "2026-02-10", "2026-02-11", "2026-02-12", "2026-02-13",
             "2026-02-14", "2026-02-15", "2026-02-16", "2026-02-17", "2026-02-18"]

actual_remaining = [4, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 0, 0, 0, 0]

# Convert dates to datetime objects
dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates_str]

# Calculate ideal burndown (linear from 4 to 0)
ideal_remaining = np.linspace(4, 0, len(dates))

# Sprint metadata
sprint_start = dates[0]
sprint_end = dates[-1]
completion_date = dates[11]  # February 15, 2026
total_tasks = 4
completed_tasks = 4
completion_rate = 100

# Calculate velocity
sprint_days = (sprint_end - sprint_start).days + 1
velocity = total_tasks / sprint_days


def create_standard_burndown():
    """Create standard burndown chart"""
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    
    # Plot ideal burndown
    ax.plot(dates, ideal_remaining, 
            color='#1f77b4', 
            marker='o', 
            markersize=8, 
            linewidth=2.5, 
            label='Ideal Burndown',
            zorder=3)
    
    # Plot actual remaining tasks
    ax.plot(dates, actual_remaining, 
            color='#ff7f0e', 
            marker='o', 
            markersize=8, 
            linewidth=2.5, 
            label='Actual Remaining Tasks',
            zorder=4)
    
    # Configure axes
    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.set_ylabel('Remaining Tasks', fontsize=12, fontweight='bold')
    ax.set_title('TrueSight Sprint 0 Burndown (04/02/2026 - 18/02/2026)', 
                 fontsize=16, fontweight='bold', pad=20)
    
    # Format x-axis
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    plt.xticks(rotation=45, ha='right')
    
    # Format y-axis
    ax.set_ylim(-0.5, 5)
    ax.set_yticks(range(0, 6))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x)}'))
    
    # Grid
    ax.grid(True, linestyle='--', alpha=0.3, color='lightgray', zorder=1)
    
    # Legend
    ax.legend(loc='upper right', fontsize=11, framealpha=0.95)
    
    # Save outputs
    plt.tight_layout()
    plt.savefig('docs/images/charts/sprint0_burndown.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('docs/images/charts/sprint0_burndown.pdf', 
                bbox_inches='tight', facecolor='white')
    plt.close()
    
    print("✅ Standard burndown chart created:")
    print("   📁 docs/images/charts/sprint0_burndown.png (300 DPI)")
    print("   📁 docs/images/charts/sprint0_burndown.pdf")


def create_enhanced_burndown():
    """Create enhanced burndown chart with completion markers and weekend shading"""
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    
    # Add weekend shading (Saturdays and Sundays)
    for i, date in enumerate(dates):
        if date.weekday() in [5, 6]:  # Saturday=5, Sunday=6
            ax.axvspan(date, date, color='gray', alpha=0.08, zorder=0)
    
    # Plot ideal burndown
    ax.plot(dates, ideal_remaining, 
            color='#1f77b4', 
            marker='o', 
            markersize=10, 
            linewidth=3, 
            label='Ideal Burndown',
            zorder=3)
    
    # Plot actual remaining tasks
    ax.plot(dates, actual_remaining, 
            color='#ff7f0e', 
            marker='o', 
            markersize=10, 
            linewidth=3, 
            label='Actual Remaining Tasks',
            zorder=4)
    
    # Add completion marker
    completion_index = 11  # February 15, 2026
    ax.plot(dates[completion_index], actual_remaining[completion_index], 
            'g*', 
            markersize=25, 
            markeredgecolor='darkgreen',
            markeredgewidth=2,
            label='Sprint Complete',
            zorder=5)
    
    # Add vertical line at completion date
    ax.axvline(x=dates[completion_index], 
               color='green', 
               linestyle='--', 
               linewidth=2, 
               alpha=0.6,
               zorder=2)
    
    # Add status info box
    status_text = "✅ Sprint Completed\n100% Complete\n4/4 Tasks Done"
    bbox_props = dict(boxstyle='round,pad=0.8', 
                     facecolor='lightgreen', 
                     alpha=0.85, 
                     edgecolor='darkgreen',
                     linewidth=2)
    ax.text(0.02, 0.98, status_text,
            transform=ax.transAxes,
            fontsize=12,
            verticalalignment='top',
            horizontalalignment='left',
            bbox=bbox_props,
            fontfamily='monospace',
            fontweight='bold',
            zorder=6)
    
    # Configure axes with velocity in title
    ax.set_xlabel('Date', fontsize=13, fontweight='bold')
    ax.set_ylabel('Remaining Tasks', fontsize=13, fontweight='bold')
    title = (f'TrueSight Sprint 0 Burndown (04/02/2026 - 18/02/2026)\n'
             f'Velocity: {velocity:.2f} tasks/day | Completed: {completed_tasks}/{total_tasks} tasks ({completion_rate}%)')
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    
    # Format x-axis (show every day for enhanced version)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.xticks(rotation=45, ha='right', fontsize=9)
    
    # Format y-axis
    ax.set_ylim(-0.5, 5)
    ax.set_yticks(range(0, 6))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x)}'))
    
    # Grid
    ax.grid(True, linestyle='--', alpha=0.3, color='lightgray', zorder=1)
    
    # Legend
    ax.legend(loc='upper right', fontsize=12, framealpha=0.95)
    
    # Save outputs
    plt.tight_layout()
    plt.savefig('docs/images/charts/sprint0_burndown_enhanced.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('docs/images/charts/sprint0_burndown_enhanced.pdf', 
                bbox_inches='tight', facecolor='white')
    plt.close()
    
    print("\n✅ Enhanced burndown chart created:")
    print("   📁 docs/images/charts/sprint0_burndown_enhanced.png (300 DPI)")
    print("   📁 docs/images/charts/sprint0_burndown_enhanced.pdf")


def main():
    """Generate both standard and enhanced burndown charts"""
    print("=" * 60)
    print("TrueSight Sprint 0 Burndown Chart Generator")
    print("=" * 60)
    print(f"\nSprint Period: {sprint_start.strftime('%B %d, %Y')} - {sprint_end.strftime('%B %d, %Y')}")
    print(f"Completion Date: {completion_date.strftime('%B %d, %Y')} (3 days early)")
    print(f"Total Tasks: {total_tasks}")
    print(f"Velocity: {velocity:.2f} tasks/day")
    print(f"Completion Rate: {completion_rate}%")
    print("\nGenerating charts...\n")
    
    # Create both versions
    create_standard_burndown()
    create_enhanced_burndown()
    
    print("\n" + "=" * 60)
    print("✨ All charts generated successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
