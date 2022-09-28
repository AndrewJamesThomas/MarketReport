import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use("seaborn-dark")

INPUT_DATA = "data/program_data.csv"

df = pd.read_csv(INPUT_DATA)
df = df.replace(to_replace="Not Offered", value=0)

df = df.rename(columns={
       "Master's Degree > All Completions > 2019": "masters_all_19",
       "Master's Degree > All Completions > 2020": "masters_all_20",
       "Master's Degree > Distance Completions > 2019": "masters_distance_19",
       "Master's Degree > Distance Completions > 2020": "masters_distance_20",
       "Master's Degree > Non-Distance Completions > 2019": "masters_nondistance_19",
       "Master's Degree > Non-Distance Completions > 2020": "masters_nondistance_20"
})

df[["masters_all_19", "masters_all_20", "masters_distance_19", "masters_distance_20",
    "masters_nondistance_19", "masters_nondistance_20"]] =\
    df[["masters_all_19", "masters_all_20", "masters_distance_19", "masters_distance_20",
        "masters_nondistance_19", "masters_nondistance_20"]]\
    .astype("int")

df["yoy_change"] = (df["masters_all_20"]-df["masters_all_19"])/df["masters_all_19"]


# visualize
def viz1():
    sns.scatterplot(x="masters_all_20",
                    y='yoy_change',
                    data=df,
                    s=50,
                    alpha=0.9,
                    color="#007996")

    plt.title("Growth-Share Plot")
    plt.xlabel("Total Completions 2020")
    plt.ylabel("YOY % Change")

    plt.axvline(df["masters_all_20"].mean(), linewidth=3, color="#C0362C", zorder=-1)
    plt.axhline(0, linewidth=3, color="#C0362C", zorder=-1)

    plt.savefig("assets/plots/growth_share.png")

# histogram
def viz2():
    sns.histplot(x="masters_all_20",
                 data=df.query("masters_all_20>0"),
                 binwidth=10,
                 color="#C0362C")
    plt.xlim(0)
    plt.title("Frequency of Total 2020 Completions")
    plt.xlabel("Total Completions")
    plt.ylabel("Frequency")
    plt.savefig("assets/plots/histogram.png")

# viz1()
viz2()

# quartiles
def quantile_rep(thresh):
    print(f"Quantile {thresh}: {df['masters_all_20'].quantile(thresh)}")

quantile_rep(0.25)
quantile_rep(0.5)
quantile_rep(0.75)
quantile_rep(0.9)
