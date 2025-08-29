"""
Task: Sports Analysis Dashboard (Premier League)

Goal:
- Analyze simulated match data from the English Premier League (APL)
- Compute key metrics and statistics:
    1. Average goals per match
    2. Top 5 scorers
    3. Team performance (Wins/Draws/Losses)
- Visualizations:
    a) Line plot: total goals per match over time
    b) Bar plot: Top 5 scorers
    c) Heatmap: goals per team per month
    d) Pie chart: percentage of goals per team
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load Data ---
df = pd.read_csv("apl_matches.csv", parse_dates=["date"])

# --- Add useful columns ---
df["total_goals"] = df["home_score"] + df["away_score"]
df["Month"] = df["date"].dt.to_period("M")

# --- 1. Basic Metrics ---
avg_goals_per_match = df["total_goals"].mean()
print(f"Average goals per match: {avg_goals_per_match:.2f}\n")

# --- 2. Top 5 Scorers ---
top_scorers = df.groupby("top_scorer")["top_scorer_goals"].sum().sort_values(ascending=False).head(5)
print("Top 5 Scorers:")
print(top_scorers, "\n")

# --- 3. Team Results ---
teams = pd.concat([
    df[["home_team","home_score","away_score"]].rename(columns={"home_team":"team","home_score":"goals_for","away_score":"goals_against"}),
    df[["away_team","away_score","home_score"]].rename(columns={"away_team":"team","away_score":"goals_for","home_score":"goals_against"})
])
teams["result"] = teams.apply(lambda row: "Win" if row["goals_for"] > row["goals_against"] 
                              else ("Draw" if row["goals_for"]==row["goals_against"] else "Loss"), axis=1)
team_summary = teams.groupby(["team","result"]).size().unstack(fill_value=0)
print("Team Results:")
print(team_summary, "\n")

# --- 4. Visualization ---

# a) Goals per match over time
plt.figure(figsize=(10,5))
sns.lineplot(data=df, x="date", y="total_goals", marker="o")
plt.title("Goals per Match Over Time")
plt.ylabel("Total Goals")
plt.xlabel("Date")
plt.grid(True)
plt.tight_layout()
plt.show()

# b) Top 5 scorers
plt.figure(figsize=(8,5))
sns.barplot(x=top_scorers.index, y=top_scorers.values, palette="Oranges_r")
plt.title("Top 5 Scorers")
plt.ylabel("Goals")
plt.xlabel("Player")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# c) Heatmap: team × month (sum of goals)
pivot_home = df.pivot_table(index="home_team", columns="Month", values="home_score", aggfunc="sum").fillna(0)
pivot_away = df.pivot_table(index="away_team", columns="Month", values="away_score", aggfunc="sum").fillna(0)
heatmap_data = pivot_home.add(pivot_away, fill_value=0)

plt.figure(figsize=(10,6))
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="YlGnBu", cbar_kws={'label':'Goals'})
plt.title("Goals per Team per Month")
plt.ylabel("Team")
plt.xlabel("Month")
plt.tight_layout()
plt.show()

# d) Pie chart: % goals per team
team_goals = df.groupby("home_team")["home_score"].sum() + df.groupby("away_team")["away_score"].sum()
plt.figure(figsize=(7,7))
team_goals.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=sns.color_palette("Set3"))
plt.title("Percentage of Goals by Team")
plt.ylabel("")
plt.tight_layout()
plt.show()
