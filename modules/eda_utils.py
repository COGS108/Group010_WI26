import matplotlib.pyplot as plt
import seaborn as sns


def plot_feature_vs_target(df, feature_col, target_col, title, hue_col=None, ax=None):
    
    #generates a scatter plot with an optional regression line or hue grouping.
    #can be plotted individually or passed an 'ax' to plot inside a grid.
    
    show_plot = False
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
        show_plot = True
    
    if hue_col and hue_col in df.columns:
        # plot with color-coding
        sns.scatterplot(data=df, x=feature_col, y=target_col, hue=hue_col, alpha=0.7, palette='tab10', ax=ax)
        sns.regplot(data=df, x=feature_col, y=target_col, scatter=False, color='red', line_kws={'linestyle':'--'}, ax=ax)
        
        # legend handling
        handles, labels = ax.get_legend_handles_labels()
        if handles:
            ax.legend(handles=handles, labels=labels, title=hue_col.title(), bbox_to_anchor=(1.05, 1), loc='upper left')
            
    else:
        # plot without color-coding
        sns.regplot(data=df, x=feature_col, y=target_col, scatter_kws={'alpha':0.5}, line_kws={'color':'red'}, ax=ax)
        
    ax.set_title(title)
    ax.set_xlabel(feature_col.replace('_', ' ').title())
    ax.set_ylabel(target_col.replace('_', ' ').title())
    ax.grid(True, linestyle='--', alpha=0.7)
    
    if show_plot:
        plt.tight_layout()
        plt.show()
        
def plot_tier_comparison(df, tier_col, feature_col, title, ax=None):
    
    # generates a boxplot to compare a physical measurement across different  performance tiers.
    # can be plotted individually or passed an 'ax' to plot inside a grid.
    
    # If no axis provided, create a new standalone figure
    show_plot = False
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
        show_plot = True
        
    # draw the boxplot on the specific axis
    sns.boxplot(data=df, x=tier_col, y=feature_col, palette='Set2', ax=ax)
    
    # set the labels and titles for that specific axis
    ax.set_title(title)
    ax.set_xlabel('Career Success Tier')
    ax.set_ylabel(feature_col.replace('_', ' ').title())
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # only call plt.show() if this is standalone plot
    if show_plot:
        plt.show()