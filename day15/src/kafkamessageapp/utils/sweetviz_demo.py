# Install first
# pip install sweetviz

import pandas as pd
import sweetviz as sv
from linearalgebra.configurations.conf import Config
from sklearn.model_selection import train_test_split

# ── 1. Load data ──────────────────────────────────────────
df = pd.read_csv(Config.customer_data_path)

# ── 2. Basic report with target feature highlighted ───────
report = sv.analyze(df, target_feat="churned")
report.show_html("sweetviz_report.html")      # opens in browser automatically

# ── 3. Train / test comparison ────────────────────────────
train, test = train_test_split(df, test_size=0.2, random_state=42)

compare = sv.compare(
    [train, "Train"],
    [test,  "Test"],
    target_feat="churned"
)
compare.show_html("train_vs_test.html")

# ── 4. Segment comparison (churned vs retained) ───────────
churned  = df[df["churned"] == True]
retained = df[df["churned"] == False]

seg = sv.compare(
    [retained, "Retained"],
    [churned,  "Churned"]
)
seg.show_html("segment_compare.html")

# ── 5. Jupyter — render inline instead of browser tab ─────
# report.show_notebook()