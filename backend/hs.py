import pandas as pd
import ace_tools as tools

# Re-create the literature review matrix template
data = {
    "Title": [],
    "Authors": [],
    "Year": [],
    "Sensors Used": [],
    "Features Extracted": [],
    "ML Methods Used": [],
    "Validation Setting": [],
    "Performance Metrics": [],
    "Hardware/Platform": [],
    "Limitations": [],
    "Relevance to Thesis": []
}

df_lit_matrix = pd.DataFrame(data)

# Display to user
tools.display_dataframe_to_user(name="Literature Review Matrix Template", dataframe=df_lit_matrix)
