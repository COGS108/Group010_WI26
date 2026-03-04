import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_vs_target(df, feature_col, target_col, title, hue_col=None):
    
    #generates a scatter plot with optional regression line or color groups 
    #to analyze the relationship between a physical metric and a success metric.
    
    plt.figure(figsize=(10, 6))
    ax = plt.gca() # get current axes
    
    if hue_col and hue_col in df.columns:
        # plot with color-coding by position
        sns.scatterplot(data=df, x=feature_col, y=target_col, hue=hue_col, alpha=0.7, palette='tab10', ax=ax)
        # keep overall trendline across all data
        sns.regplot(data=df, x=feature_col, y=target_col, scatter=False, color='red', line_kws={'linestyle':'--'}, ax=ax)
        
        # capture seaborn legend handles and move them outside
        handles, labels = ax.get_legend_handles_labels()
        if handles:
            ax.legend(handles=handles, labels=labels, title=hue_col.title(), bbox_to_anchor=(1.05, 1), loc='upper left')
            
    else:
        # plot without color-coding
        sns.regplot(data=df, x=feature_col, y=target_col, scatter_kws={'alpha':0.5}, line_kws={'color':'red'}, ax=ax)
        
    plt.title(title)
    plt.xlabel(feature_col.replace('_', ' ').title())
    plt.ylabel(target_col.replace('_', ' ').title())
    
    plt.tight_layout() # makes sure that moved legend doesn't get cut off
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()