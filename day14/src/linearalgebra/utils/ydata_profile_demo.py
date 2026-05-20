# 1. Install
#pip install ydata-profiling

# 2. Import
import pandas as pd
from ydata_profiling import ProfileReport
from linearalgebra.configurations.conf import Config
# 3. Load your data
df = pd.read_csv(Config.product_path)

# 4. Generate the report
profile = ProfileReport(
    df,
    title="Customer Data Profile",
    explorative=True
)

# 5. Save as HTML (opens in browser)
profile.to_file(Config.report_path)